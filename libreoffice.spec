%define		oo_ver	641d
Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	0.641d
Release:	1
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://sf1.mirror.openoffice.org/%{oo_ver}/oo_%{oo_ver}_src.tar.bz2
Source1:	ftp://ftp.cs.man.ac.uk/pub/toby/gpc/gpc231.tar.Z
Source2:	%{name}-db3.jar
Patch0:		%{name}-gcc.patch
Patch1:		%{name}-db3.patch
URL:		http://www.openoffice.org/
BuildRequires:	STLport-static
BuildRequires:	XFree86-devel
BuildRequires:	db3-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
%{?!_with_ibm_java:BuildRequires: jdk = 1.3.1_01}
%{?_with_ibm_java:BuildRequires: ibm-java-sdk}
BuildRequires:	perl
BuildRequires:	tcsh
BuildRequires:	unzip
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
 - Downloadable source code,
 - CVS control, and
 - Infrastructure for community involvement, including guidelines and
   discussion groups.

%description -l pl
OpenOffice.org jest projektem open-source sponsorowanym przez Sun
Microsystems i przechowywanym przez CollabNet. W pa¼dzierniku 2000
roku Sun udostêpni³ kod ¼ród³owy popularnego pakietu biurowego
StarOfficeTM na zasadach licencji open-source. G³ównym celem
OpenOffice.org jest stworzenie sieciowego pakietu biurowego nastêpnej
generacji, wykorzystuj±c open-source'owe metody pracy.

Do zalet OpenOffice.org mo¿na zaliczyæ:
 - dostêpny ca³y czas kod ¼ród³owy,
 - kontrola CVS,
 - infrastruktura s³u¿±ca do komunikowania siê w ramach projektu.

%prep
%setup -q -n oo_%{oo_ver}_src
%patch0 -p1
%patch1 -p1
install %{SOURCE1} external
cd external; tar fxz %{SOURCE1}; cp -fr gpc231/* gpc
install -d solver/641/unxlngi3.pro/bin
install %{SOURCE2} solver/641/unxlngi3.pro/bin/db.jar

%build
cd config_office
autoconf

%{?!_with_ibm_java:JAVA_HOME="/usr/lib/jdk1.3.1_01"}
%{?_with_ibm_java:JAVA_HOME="/usr/lib/IBMJava2-13"}
%configure \
	--with-jdk-home=$JAVA_HOME \
	--with-stlport4-home=/usr \
	--with-lang=ALL \
	--with-x

cd ..
cat <<EOF > compile
#!/bin/tcsh
./bootstrap
# you must have a valid & working X DISPLAY setting on the build machine,
# see http://tools.openoffice.org/troubleshoot.html
#Xvfb :15 &
#setenv DISPLAY	:15
source LinuxIntelEnv.Set
dmake -p -v
EOF

chmod u+rx compile
./compile

%install
rm -rf $RPM_BUILD_ROOT

cat <<EOF > install
#!/bin/csh
source LinuxIntelEnv.Set
dmake install
EOF

chmod u+rx install
./install

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/%{name}}

install solver/%{version}/unxlngi3.pro/bin/*.{bin,exe}		$RPM_BUILD_ROOT%{_bindir}
install solver/%{version}/unxlngi3.pro/lib/*.so		 	$RPM_BUILD_ROOT%{_libdir}
cp -fr solver/%{version}/unxlngi3.pro/{par,pck,rdb,res,xml}	$RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_datadir}/%{name}
