#! /usr/bin/perl

use strict;

#- Define full path to unzip command
my $UnzipCommand = "/usr/bin/unzip";

#- Define the default setup file
my $SetupConf = "setup.ins";

#- Define the zipfiles dir (will be the same as of setup.ins)
my $SetupDir = "."; 

#- Define destination directory
my $DestDir = "/usr/lib/openoffice";

#- Define to extract help files
my $ExtractHelp = 0;

sub dirname { local $_ = shift; s|[^/]*/*\s*$||; s|(.)/*$|$1|; $_ || '.' }
sub cat_ { local *F; open F, $_[0] or return; my @l = <F>; wantarray() ? @l : join '', @l }

sub mkdir_p {
  my ($dir) = @_;
  if (-d $dir) {
    # nothing to do
  } elsif (-e $dir) {
    die "mkdir: error creating directory $dir: $dir is a file and i won't delete it\n";
  } else {
    mkdir_p(dirname($dir));
    mkdir($dir, 0755) or die "mkdir: error creating directory $dir: $!\n";
  }
  1;
}

while ( $ARGV[0] =~ /^-/ ) {
	$_ = shift;
	if (m/^-d=(\S+)/) {
		$DestDir=$1;
	}
	elsif (m/^-z=(\S+)/) {
		$UnzipCommand=$1;
	}
	elsif (m/^-i=(\S+)/) {
		$SetupConf=$1;
		$SetupDir=dirname $SetupConf;
	}
	elsif (m/^-h/) {
		$ExtractHelp = 1;
	}
	else {
		print STDERR "$0: Unknown option $_";
	}
}

# Parse enough of <setup.ins> to get correct Directory and File sections.
sub ReadSetup($) {
	my ($file) = @_;
    my $e;
    my %entries;
    foreach (cat_("$file")) {
		if (/^([_A-Za-z]+)\s*([_A-Za-z0-9]+)/) {
			$entries{$1}{$2} = $e = { };
		}
		elsif (/\s*([_A-Za-z]+)\s*=\s*\"?([^;\"]+)\"?;/) {
			$e->{$1} = $2;
		}
    }
	
	# Expand predefined dirs to de $DestDir variable
	$entries{Directory}{$_} = { HostName => "$DestDir" } foreach
		qw( PREDEFINED_HOMEDIR  PREDEFINED_PROGDIR PREDEFINED_CONFIGDIR );
			
    \%entries;
}

sub DumpEntries(\%$) {
    my $entries = shift;
    my ($basename) = @_;
    my $sections = $entries->{$basename} if $entries->{$basename};
    while (my ($key, $value) = each(%$sections)) {
	print "$basename $key\n";
	$value->{$_} and print "\t$_\t= \"$value->{$_}\";\n"
	    foreach qw(Bitmap Date DefaultDestPath DefaultLanguage
		       Description FadeType FileName fontsDirFile
		       fontsDirGlobalFile fontspath HostName ID Key
		       Languages Name PackedName Path ProcName
		       ProductName ProductVersion Section Text Time
		       Value VendorBitmap);
	$value->{$_} and print "\t$_\t= $value->{$_};\n"
	    foreach qw(ArchiveFiles ArchiveSize BitmapPosX BitmapPoxY
		       Carrier Default Dir DiskNo FileID FontSize
		       Minimal ModuleID NetDir Order ParentID
		       ProfileID RegistryID ScriptVersion Size
		       TextHeight TextWidth UnixRights);
	print "End\n\n";
    }
}

sub GetFullPath {
    my $dirs = shift;
    my ($id) = @_;
	return ( $dirs->{$id}->{ParentID} ? GetFullPath($dirs, $dirs->{$id}->{ParentID}) . "/" : "" )
		   . $dirs->{$id}->{HostName};
}

# Parse the file and get all entries
die "$0: Can't open $SetupConf\n" if ( ! -r $SetupConf );
my $setup = ReadSetup($SetupConf);
#DumpEntries %$setup, "Directory";
#DumpEntries %$setup, "File";

die "$UnzipCommand not found, please set the full path to the unzip command\n" if
    ( ! -x "$UnzipCommand" );

while (my ($key, $value) = each (%{$setup->{File}})) {
    if ($value->{PackedName}) {
		my $zipfile = "$SetupDir/$value->{PackedName}";
		die "$0: zip file $zipfile not accessible" if
			( ! -r "$zipfile" );
		
		# Find language-specific candidates
		if ($key =~ /_Lang$/ || $value->{Name} =~ /\.res$/
			|| ($ExtractHelp && $key =~ /File_Help/ && $value->{Dir} =~ /gid_Dir_Help_Isolanguage/)) {
			print "Unpacking $zipfile... ";
			# Prefer NetDir path over simple Dir
			my $outpath = GetFullPath \%{$setup->{Directory}}, $value->{NetDir} ? $value->{NetDir} : $value->{Dir};
			-d $outpath or mkdir_p($outpath);
			system("$UnzipCommand $zipfile -d $outpath");
		}
    }
}

