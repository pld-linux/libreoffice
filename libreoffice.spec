Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	619
Release:	0.1
Epoch:          1
License:	GPL/LGPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://a1652.g.akamai.net/7/1652/2064/OpenOffice619/anoncvs.openoffice.org/download/OpenOffice619/oo_%{version}_src.tar.bz2
URL:		http://www.openoffice.org/
BuildRequires:	XFree86-devel
BuildRequires:	STLport-devel
BuildRequires:	STLport-static
#BuildRequires:	jdk
BuildRequires:	flex
BuildRequires:	tcsh
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenOffice.org is an open-source project sponsored by Sun Microsystems 
and hosted by CollabNet. In October of 2000, Sun released the source 
code of its popular StarOfficeTM productivity suite under open-source
licenses. The aim of the OpenOffice.org project is to create, using 
open-source methods, the next generation of open-network productivity 
services, including the establishment of open, XML-based standards for 
office productivity file formats and language-independent bindings to 
component APIs.

Features of OpenOffice.org include:
 * Downloadable source code,
 * CVS control, and
 * Infrastructure for community involvement,
   including guidelines and discussion groups.

%description -l pl
OpenOffice.org jest projektem open-source sponsorowanym przez Sun 
Microsystems i przechowywanym przez CollabNet. W pa¼dzierniku 2000
roku Sun udostêpni³ kod ¼ród³owy popularnego pakietu biurowego 
StarOfficeTM na zasadach licencji open-source. G³ównym celem 
OpenOffice.org jest stworzenie sieciowego pakietu biurowego nastêpnej 
generacji, wykorzystuj±c open-source'owe metody pracy.

Do zalet OpenOffice.org mo¿na zaliczyæ:
 * dostêpny ca³y czas kod ¼ród³owy,
 * kontrola CVS,
 * infrastruktura s³u¿±ca do komunikowania siê w ramach projektu.

%prep
%setup -q -n oo_%{version}_src

%build
cd config_office
# configure script is buggy, you have to put path to jdk manually
%configure \
	--with-stlport4-home=%{_prefix} \
	--with-jdk-home=/opt/jdk1.3 \
	--with-xprint

cd ..

./bootstrap

cat <<EOF > compile
#!/bin/csh
source LinuxIntelEnv.Set

# you must have a valid & working X DISPLAY setting on the build machine,
# see http://tools.openoffice.org/troubleshoot.html
setenv DISPLAY :0
dmake

# workaround, there seem to be a missing step in the bootstrap
cd tools/bootstrp/addexes2
dmake
cd ../../..
cp -p tools/unxlngi3.pro/bin/javadep solenv/unxlngi3/bin/
dmake
EOF

chmod u+rx compile
./compile

%install
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
