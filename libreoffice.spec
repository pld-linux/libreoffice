Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	6.13
Release:	1
License:	GPL/LGPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://a1388.g.akamai.net/7/1388/2064/OpenOffice613/anoncvs.openoffice.org/download/OpenOffice613/oo_613_src.tar.bz2
URL:		http://www.openoffice.org/
BuildPreReq:	STLport-devel
BuildPreReq:	tcsh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenOffice is powerful office suite based on StarOffice.

%description -l pl
OpenOffice jest potê¿nym pakietem biurowym wywodz±cym siê ze StarOffice.

%prep
%setup -q

%build
cd config-office
%configure \
	--with-stlport4-home=%{_prefix}

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
