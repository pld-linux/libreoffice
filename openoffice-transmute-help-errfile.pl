#!/usr/bin/perl

use strict;
use XML::Twig;

my ($Language, $XMLFile) = (shift, shift);
die "Invalid arguments" if (!$Language || !$XMLFile);

#- Define localized help package name
my $HelpPackage = "OpenOffice.org-help-$Language";

my $t = XML::Twig->new(twig_roots => { "li" => \&handle_li },
                       twig_print_outside_roots => 1,
                       keep_encoding => 1,
                       pretty_print => "indented"
                       );

$t->parsefile($XMLFile);
{
    my $num_li = 0;
    sub handle_li {
        my ($t, $li) = @_;
        ++$num_li;
        # Only print the first item, aka "Help module is not installed"
        if ($num_li == 1) {
            # Implant OpenOffice.org help package name
            my @p = $t->descendants("p");
            (my $text = $p[1]->text()) =~ s/^([^.]+)/\1 (e.g. <b>${HelpPackage}<\/b>)/;
            $p[1]->set_text($text);
            # Don't print the help link
            foreach (@p) { $_->delete if ($_->descendants("help:link")) }
            $li->print;
        }
    }
}

# Local variables:
# tab-width: 4
# indent-tabs-mode: nil
# End:
