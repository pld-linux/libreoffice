Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	619
Release:	1
Epoch:          1
License:	GPL/LGPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://a1652.g.akamai.net/7/1652/2064/OpenOffice619/anoncvs.openoffice.org/download/OpenOffice619/oo_%{version}_src.tar.bz2
URL:		http://www.openoffice.org/
BuildRequires:	STLport-devel
#BuildRequires:	STLport-static
#BuildRequires:	jdk
BuildRequires:	flex
BuildRequires:	tcsh
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenOffice is powerful office suite based on StarOffice.

%description -l pl
OpenOffice jest potê¿nym pakietem biurowym wywodz±cym siê ze StarOffice.

%prep
%setup -q -n oo_%{version}_src

%build
cd config_office
%configure \
	--with-stlport4-home=%{_prefix} \
	--with-jdk-home=/usr/local/lib/jdk \
	--enable-xprint

cd ..

./bootstrap

cat <<EOF > compile
#!/bin/csh
source LinuxIntelEnv.Set
dmake
EOF

chmod u+rx compile
./compile

%install
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
