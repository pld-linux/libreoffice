#! /usr/bin/perl

use strict;

#- Define full path to unzip command
my $UnzipCommand = "/usr/bin/unzip";

#- Define the default setup file
my $SetupConf = "setup.ins";

#- Define the generated instdb.ins file
my $InstDb = "instdb.ins";

#- Define destination directory
my $DestDir = "/usr/lib/openoffice";

#- Define the zipfiles dir (will be the same as of setup.ins)
my $SetupDir = "."; 

#- Define Product Version and Name
my ($ProductName, $ProductVersion) = ("OpenOffice.org", "1.0.1");

sub dirname { local $_ = shift; s|[^/]*/*\s*$||; s|(.)/*$|$1|; $_ || '.' }
sub cat_ { local *F; open F, $_[0] or return; my @l = <F>; wantarray() ? @l : join '', @l }
sub member { my $e = shift; foreach (@_) { $e eq $_ and return 1 } 0 }
sub output { my $f = shift; local *F; open F, ">$f" or die "output in file $f failed: $!\n"; print F foreach @_; 1 }

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
	if (m/^-d(=(\S+))?/) {
		$DestDir = $2 || shift;
	}
	elsif (m/^-z(=(\S+))?/) {
		$UnzipCommand = $2 || shift;
	}
	elsif (m/^-i(=(\S+))?/) {
		$SetupConf = $2 || shift;
		$SetupDir = dirname $SetupConf;
	}
	elsif (m/^-o(=(\S+))?/) {
		$InstDb = $2 || shift;
	}
	elsif (m/^-pn(=(\S+))?/) {
		$ProductName = $2 || shift;
	}
	elsif (m/^-pv(=(\S+))?/) {
		$ProductVersion = $2 || shift;
	}
	else {
		die "$0: Unknown option $_\n";
	}
}

die "$0: Can't open $SetupConf\n"
	if ( ! -r $SetupConf );

die "$UnzipCommand not found, please set the full path to the unzip command\n"
	if ( ! -x "$UnzipCommand" );

my @exclude_modules = ( "GID_MODULE_OPTIONAL_GNOME",
						"gid_Module_Optional_Kde",
						"gid_Module_Optional_Cde" );

my ($zipfile, $instdb);
my $is_archive = 0;
foreach (cat_("$SetupConf"), "EndOfFile\n") {
	if (/^\s*Installation/ ... /^\s*End/) {
		if (/^\s*ScriptVersion/) {
			$instdb .= "\tDestPath\t = \"$DestDir\";\n";
			$instdb .= "\tSourcePath\t = \"$DestDir/program\";\n";
			$instdb .= "\tMode\t\t = NETWORK;\n";
			$instdb .= "\tInstallFromNet = NO;\n";
		}
	}
	elsif (/^\s*Module\s+(\w+)\s*/ ... /^\s*End/) {
		my $module = $1;
		if (/^\s*Files/ || /^\s*Styles.+HIDDEN_ROOT/) {
			my $state = member($module, @exclude_modules) ? "NO" : "YES";
			$instdb .= "\tInstalled\t = $state;\n";
		}
	}
	elsif (/^\s*File/ ... /^\s*End/) {
		if (/^\s*End/) {
			if ($is_archive) {
				my @filelist;
				foreach (cat_("$UnzipCommand -l $zipfile |")) {
					push @filelist, { size => $1, name => $2 }
					if (/^\s+([0-9]+)\s+[-0-9]+\s+[:0-9]+\s+(.+)\s+/);
				}
				$instdb .= "\tContains\t = (";
				my $n = 0;
				foreach my $e (@filelist) {
					if (++$n > 10) {
						$instdb .= ",\n\t\t\t\t\t";
						$n = 1;
					}
					elsif ($n > 1) {
						$instdb .= ", ";
					}
					$instdb .= "\"$e->{name}:$e->{size}\"";
				}
				$instdb .= ");\n";
				$is_archive = 0;
			}
		}
		elsif (/^\s*Styles\s*=\s*.*ARCHIVE/) {
			$is_archive = 1;
		}
		elsif (/^\s*PackedName\s*=\s*"(\w+)"/) {
			$zipfile = "$SetupDir/$1";
			die "$0: zip file $zipfile not accessible"
				if ( ! -r "$zipfile" );
		}
	}
	$instdb .= $_ if !/^EndOfFile/;
}

# Implant Product Name and Version
$instdb =~ s/%PRODUCTNAME/$ProductName/g;
$instdb =~ s/%PRODUCTVERSION/$ProductVersion/g;
$instdb =~ s/"<productkey>"/"$ProductName $ProductVersion"/g;
$instdb =~ s/"<installmode>"/"NETWORK"/g;

output $InstDb, $instdb;
