
# Conditional build:
# _with_ibm_java	- uses IBM java instead SUN java
# _with_nest		- build for nest envinronment

# _with_us		- 01 US translation
# _with_pl		- 48 PL translation
# _with_de		- 49 DE translation

#%define		oo_ver	1.0
Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	1.0.0
Release:	0.4
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
#Source0:	http://sf1.mirror.openoffice.org/%{version}/oo_%{version}_source.tar.bz2
Source0:	http://sf1.mirror.openoffice.org/%{version}/OOo_%{version}_source.tar.bz2
Source1:	ftp://ftp.cs.man.ac.uk/pub/toby/gpc/gpc231.tar.Z
Source2:	%{name}-db3.jar
Source3:	%{name}-rsfile.txt
Patch0:		%{name}-gcc.patch
Patch1:		%{name}-db3.patch
Patch2:		%{name}-mozilla.patch
Patch3:		%{name}-nest.patch
Patch4:		%{name}-perl.patch
Patch5:		%{name}-system-freetype.patch
Patch6:		%{name}-system-getopt.patch
Patch7:		%{name}-freetype-2.1.patch
URL:		http://www.openoffice.org/
BuildRequires:	STLport-static
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-fonts-PEX
BuildRequires:	XFree86-Xvfb
BuildRequires:	db3-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  bison
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.1
%{?!_with_nest:BuildRequires:	gcc <= 3.0.0}
%{?_with_nest:BuildRequires:	gcc2}
%{?!_with_nest:BuildRequires:	gcc-c++ <= 3.0.0}
%{?_with_nest:BuildRequires:	gcc2-c++}
%{?_with_ibm_java:BuildRequires:	ibm-java-sdk}
%{?!_with_ibm_java:BuildRequires:	jdk = 1.3.1_03}
%{?!_with_nest:BuildRequires:	libstdc++-devel <= 3.0.0}
%{?_with_nest:BuildRequires:	libstdc++2-devel}
BuildRequires:	pam-devel
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
%setup -q -n oo_1.0_src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if%{?_with_nest:1}%{!?_with_nest:0}
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1


install %{SOURCE1} external
cd external; tar fxz %{SOURCE1}; cp -fr gpc231/* gpc

%build
cd config_office
#autoconf


%{?!_with_ibm_java:JAVA_HOME="/usr/lib/jdk1.3.1_03"}
%{?_with_ibm_java:JAVA_HOME="/usr/lib/IBMJava2-13"}
%configure2_13 \
	--with-jdk-home=$JAVA_HOME \
	--with-stlport4-home=/usr \
	--with-lang=ALL \
	--with-x

cd ..

cat <<EOF > prep
#!/bin/tcsh
./bootstrap
EOF
chmod u+rx prep
./prep

install -d solver/641/unxlngi3.pro/bin
install %{SOURCE2} solver/641/unxlngi3.pro/bin/db.jar

cat <<EOF > compile
#!/bin/tcsh
source LinuxIntelEnv.Set
dmake -p -v
EOF
chmod u+rx compile
./compile

%install
rm -rf $RPM_BUILD_ROOT

cat <<EOF > install
#!/bin/tcsh
source LinuxIntelEnv.Set
dmake install
EOF

chmod u+rx install
./install

# starting Xvfb
i=0
while [ -f /tmp/.X$i-lock ]; do
	i=$(($i+1))
done

/usr/X11R6/bin/Xvfb :$i & 
PID=$!
sleep 5

# preparing to start installator
cp -f %{SOURCE3} $RPM_BUILD_DIR/oo_%{oo_ver}_src/install.rs.in
sed -e "s,@DESTDIR@,$RPM_BUILD_ROOT/usr/X11R6/lib/openoffice," \
	-e "s,@LOGFILE@,$RPM_BUILD_DIR/oo_%{oo_ver}_src/install.log," \
	install.rs.in > install.rs

# starting installator
%{?_with_us:DISPLAY=":$i" instsetoo/unxlngi3.pro/01/normal/setup -R:$RPM_BUILD_DIR/oo_%{oo_ver}_src/install.rs}
%{?_with_pl:DISPLAY=":$i" instsetoo/unxlngi3.pro/48/normal/setup -R:$RPM_BUILD_DIR/oo_%{oo_ver}_src/install.rs}
%{?_with_de:DISPLAY=":$i" instsetoo/unxlngi3.pro/49/normal/setup -R:$RPM_BUILD_DIR/oo_%{oo_ver}_src/install.rs}

# stopping Xvfb
#kill $PID

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
