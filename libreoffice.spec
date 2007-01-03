# NOTE:
#	- normal build with java requires about 24GB of disk space
#		$BUILD_ROOT	 7.1 GB
#		BUILD		15.7 GB
#		SRPMS		 0.3 GB
#		RPMS		 1.2 GB
# TODO:
#	- problems with gcc-4.2.0 (I guess): oowriter is useless (invisble text till refresh)
#	- fix help files (broken links)
#	- LFS support is disabled (no_lfs_hack.patch for xml2cmp crash) because it need LFS-ready STLport
#	- bcond with_xt is broken (xt in PLD is too old or broken)
#       - bcond with_mono is broken (cli_types.dll not found, and can't be made)
#	- build on 64-bit architectures
#       - adapt help-support.diff to PLD
# MAYBE TODO:
#	- drop requirement on nas-devel
#	- --with-system-myspell + myspell package as in Debian
#	- in gtk version menu highlight has almost the same colour as menu text
#	- 6 user/config/*.so? files shared between -i18n-en and -i18n-sl
#	- add ooglobal symlink and it's ooo-wrapper entry (among calc|draw|impress|math|web|writer)
#	- add %{_libdir}/%{name}/share/autocorr/acor_(ll)-(LL).dat files to package (marked with %lang)
#	- fix locale names and other locale related things
#       - can't be just i18n-{be,gu,hi,kn,pa,ta} instead of *-{be_BY,*_IN}?
#	- add option to build with {not} all lanquages
#	- REMOVE USE of Xvfb from build-galleries script (ooo-build-2.0.1.2/bin/build-galleries line 84)
#   - more system libs todo:
#	$ grep SYSTEM ooo-build-ooe680-m6/build/ooe680-m6/config_office/config.log |grep NO
#	SYSTEM_AGG='NO'
#	SYSTEM_HSQLDB='NO'
#	SYSTEM_HUNSPELL='NO'
#	SYSTEM_HYPH='NO'
#	SYSTEM_LIBXSLT='NO'
#	SYSTEM_MYSPELL='NO'
#	SYSTEM_MYTHES='NO'
#	SYSTEM_STDLIBS='NO'
#	SYSTEM_XALAN='NO'
#	SYSTEM_XERCES='NO'
#	SYSTEM_XML_APIS='NO'
#	SYSTEM_XT='NO'
#

# Conditional build:
%bcond_without	gnomevfs	# GNOME VFS and Evolution 2 support
%bcond_without	java		# without Java support (disables help support)
%bcond_without	kde		# KDE L&F packages
%bcond_with	mono		# enable compilation of mono bindings
%bcond_without	mozilla		# without mozilla
%bcond_with	seamonkey	# use seamonkey instead of firefox

%bcond_without	system_db		# with internal berkeley db
%bcond_without	system_mdbtools
%bcond_with	system_xt
%bcond_without	system_beanshell
%bcond_without	system_libhnj		# with internal ALTLinuxhyph

%define		ver		2.1.0
%define		_rel		0.4
%define		subver		680
%define		snap		OOE680
%define		snap2		SRC680
%define		bver		m6
%define		bbver		m6
%define		bugfix		%{nil}
%define		ooobver		ooe680-%{bbver}
%define		ssnap		ooe680-%{bver}

%define		specflags	-fno-strict-aliasing

Summary:	OpenOffice.org - powerful office suite
Summary(pl):	OpenOffice.org - potê¿ny pakiet biurowy
Name:		openoffice.org
Version:	%{ver}%{bugfix}
Release:	0.%{bver}%{?without_gnomevfs:.novfs}.%{_rel}
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
#Source0:	http://go-ooo.org/packages/%{snap}/ooo-build-%{ooobver}.tar.gz
Source0:	ooo-build-%{ooobver}.tar.gz
# Source0-md5:	797f04099223b549ed1b4939dfc2a335
Source1:	http://go-ooo.org/packages/%{snap}/%{ssnap}-core.tar.bz2
# Source1-md5:	7dbf5f7ea4f469bb6c8b1d6037567431
Source2:	http://go-ooo.org/packages/%{snap}/%{ssnap}-system.tar.bz2
# Source2-md5:	7f645231043a776c07a22300c0a10848
Source3:	http://go-ooo.org/packages/%{snap}/%{ssnap}-binfilter.tar.bz2
# Source3-md5:	22acf75656a2186d8a969ee5069ef193
Source4:	http://go-ooo.org/packages/%{snap}/%{ssnap}-lang.tar.bz2
# Source4-md5:	9b1a1d5dafbde7cbc90da8b903e6b0bf
Source10:	http://go-ooo.org/packages/%{snap2}/ooo_custom_images-13.tar.bz2
# Source10-md5:	2480af7f890c8175c7f9e183a1b39ed2
Source11:	http://go-ooo.org/packages/%{snap2}/ooo_crystal_images-6.tar.bz2
# Source11-md5:	586d0f26b3f79d89bbb5b25b874e3df6
Source12:	http://go-ooo.org/packages/%{snap2}/extras-2.tar.bz2
# Source12-md5:	733051ebeffae5232a2eb760162da020
Source15:	http://go-ooo.org/packages/xt/xt-20051206-src-only.zip
# Source15-md5:	0395e6e7da27c1cea7e1852286f6ccf9
Source16:	http://go-ooo.org/packages/%{snap2}/lp_solve_5.5.tar.gz
# Source16-md5:	2ff7b4c52f9c3937ebe3002798fbc479
Source17:	http://go-ooo.org/packages/%{snap2}/biblio.tar.bz2
# Source17-md5:	1948e39a68f12bfa0b7eb309c14d940c
Source50:	openabout_pld.png
Source51:	openintro_pld.bmp
# patches applied in prep section
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-vendorname.patch
Patch2:		%{name}-stl5_fix.patch
Patch3:		%{name}-mdbtools_fix.diff
Patch4:		%{name}-nolfs_hack.patch
Patch5:		%{name}-no_fonts_dir_buildfix.patch
Patch6:		%{name}-java16.patch
# patches applied by ooo-patching-system
Patch100:	%{name}-STL-lib64.diff
Patch101:	%{name}-64bit-inline.diff
Patch102:	%{name}-build-pld-splash.diff
Patch104:	%{name}-portaudio_v19.diff
Patch105:	%{name}-firefox.diff
Patch106:	%{name}-seamonkey.diff
URL:		http://www.openoffice.org/
BuildRequires:	ImageMagick
BuildRequires:	STLport-devel >= 2:5.0.0
BuildRequires:	autoconf >= 2.51
BuildRequires:	automake >= 1:1.9
%{?with_system_beanshell:BuildRequires:	beanshell}
BuildRequires:	bison >= 1.875-4
BuildRequires:	boost-devel
BuildRequires:	boost-mem_fn-devel
BuildRequires:	boost-spirit-devel
BuildRequires:	cairo-devel >= 0.5.2
BuildRequires:	cups-devel
BuildRequires:	curl-devel >= 7.9.8
%if %{with system_db}
BuildRequires:	db-cxx-devel
BuildRequires:	db-devel
%endif
BuildRequires:	/usr/bin/getopt
%if %{with gnomevfs}
BuildRequires:	gnome-vfs2-devel
%endif
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	gstreamer-devel >= 0.10.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	gtk+2-devel
BuildRequires:	icu
%if %{with kde}
BuildRequires:	kdelibs-devel
%endif
BuildRequires:	libart_lgpl-devel
%if %{with system_libhnj}
BuildRequires:	libhnj-devel
%endif
BuildRequires:	libbonobo-devel >= 2.0
BuildRequires:	libicu-devel >= 3.4
BuildRequires:	libjpeg-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel >= 5:3.2.1
BuildRequires:	libwpd-devel >= 0.8.6
BuildRequires:	libxml2-devel >= 2.0
%if %{with system_mdbtools}
BuildRequires:	mdbtools-devel >= 0.6
%endif
BuildRequires:	nspr-devel >= 1:4.6-0.20041030.3
BuildRequires:	nss-devel >= 1:3.10
%if %{with mono}
BuildRequires:	mono-csharp >= 1.1.8
BuildRequires:	mono-devel >= 1.1.8
%endif
BuildRequires:	nas-devel >= 1.7-1
BuildRequires:	neon-devel
BuildRequires:	openclipart-png >= 0:0.16
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel
BuildRequires:	python >= 2.2
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sablotron-devel
BuildRequires:	sane-backends-devel
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	tcsh
BuildRequires:	unixODBC-devel
BuildRequires:	unzip
BuildRequires:	xmlsec1-nss-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-xserver-Xvfb
%{?with_system_xt:BuildRequires:	xt}
BuildRequires:	zip
BuildRequires:	zlib-devel
%if %{with java}
BuildRequires:	ant
BuildRequires:	db-java >= 4.2.52-4
BuildRequires:	jar
BuildRequires:	jdk >= 1.4.0_00
%else
BuildRequires:	libxslt-progs
%endif
%if %{with seamonkey}
BuildRequires:	seamonkey-devel
%else
BuildRequires:	mozilla-firefox-devel
%endif
BuildConflicts:	STLport4
BuildConflicts:	java-sun = 1.4.2
Requires(post,postun):	fontpostinst
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
# libcups.so.2 is dlopened (in cupsmgr.cxx); maybe Suggests instead?
Requires:	cups-lib
Requires:	libstdc++ >= 5:3.2.1
Requires:	mktemp
Requires:	sed
Obsoletes:	openoffice
#Suggests:	chkfontpath
ExclusiveArch:	%{ix86} %{x8664} ppc sparc sparcv9
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

%package libs
Summary:	OpenOffice.org shared libraries
Summary(pl):	Biblioteki dzielone OpenOffice.org
Group:		X11/Libraries
Obsoletes:	openoffice-libs

%description libs
OpenOffice.org productivity suite - shared libraries.

%description libs -l pl
Pakiet biurowy OpenOffice.org - biblioteki.

%package libs-kde
Summary:	OpenOffice.org KDE Interface
Summary(pl):	Interfejs KDE dla OpenOffice.org
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en-kde
Obsoletes:	openoffice-libs-kde

%description libs-kde
OpenOffice.org productivity suite - KDE Interface.

%description libs-kde -l pl
Pakiet biurowy OpenOffice.org - Interfejs KDE.

%package libs-gtk
Summary:	OpenOffice.org GTK+ Interface
Summary(pl):	Interfejs GTK+ dla OpenOffice.org
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en-gtk
Obsoletes:	openoffice-libs-gtk

%description libs-gtk
OpenOffice.org productivity suite - GTK+ Interface.

%description libs-gtk -l pl
Pakiet biurowy OpenOffice.org - Interfejs GTK+.

%package i18n-af
Summary:	OpenOffice.org - interface in Afrikaans language
Summary(pl):	OpenOffice.org - interfejs w jêzyku afrykanerskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-af
Obsoletes:	openoffice-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af-kde

%description i18n-af
This package provides resources containing menus and dialogs in
Afrikaans language.

%description i18n-af -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
afrykanerskim.

%package i18n-ar
Summary:	OpenOffice.org - interface in Arabic language
Summary(pl):	OpenOffice.org - interfejs w jêzyku arabskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ar
Obsoletes:	openoffice-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar-kde

%description i18n-ar
This package provides resources containing menus and dialogs in Arabic
language.

%description i18n-ar -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
arabskim.

%package i18n-as_IN
Summary:	OpenOffice.org - interface in Assamese language for India
Summary(pl):	OpenOffice.org - interfejs w jêzyku asamskim dla Indii
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-as_IN
This package provides resources containing menus and dialogs in
Assamese language for India.

%description i18n-as_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
asamskim dla Indii.

%package i18n-be_BY
Summary:	OpenOffice.org - interface in Belarusian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku bia³oruskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-be_BY
This package provides resources containing menus and dialogs in
Belarusian language.

%description i18n-be_BY -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
bia³oruskim.

%package i18n-bg
Summary:	OpenOffice.org - interface in Bulgarian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku bu³garskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-bg
Obsoletes:	openoffice-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg-kde

%description i18n-bg
This package provides resources containing menus and dialogs in
Bulgarian language.

%description i18n-bg -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
bu³garskim.

%package i18n-bn
Summary:	OpenOffice.org - interface in Bangla language
Summary(pl):	OpenOffice.org - interfejs w jêzyku bengalskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-bn
This package provides resources containing menus and dialogs in Bangla
language.

%description i18n-bn -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
bengalskim.

%package i18n-bn_BD
Summary:	OpenOffice.org - interface in Bangla language for Bangladesh
Summary(pl):	OpenOffice.org - interfejs w jêzyku bengalskim dla Bangladeszu
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-bn_BD
This package provides resources containing menus and dialogs in Bangla
language for Bangladesh.

%description i18n-bn_BD -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
bengalskim dla Bangladeszu.

%package i18n-bn_IN
Summary:	OpenOffice.org - interface in Bangla language for India
Summary(pl):	OpenOffice.org - interfejs w jêzyku bengalskim dla Indii
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-bn_IN
This package provides resources containing menus and dialogs in Bangla
language for India.

%description i18n-bn_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
bengalskim dla Indii.

%package i18n-br
Summary:	OpenOffice.org - interface in Breton language
Summary(pl):	OpenOffice.org - interfejs w jêzyku bretoñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-br
This package provides resources containing menus and dialogs in Breton
language.

%description i18n-br -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
bretoñskim.

%package i18n-bs
Summary:	OpenOffice.org - interface in Bosnian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku bo¶niañskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-bs
This package provides resources containing menus and dialogs in
Bosnian language.

%description i18n-bs -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
bo¶niañskim

%package i18n-ca
Summary:	OpenOffice.org - interface in Catalan language
Summary(pl):	OpenOffice.org - interfejs w jêzyku kataloñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ca
Obsoletes:	openoffice-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca-kde

%description i18n-ca
This package provides resources containing menus and dialogs in
Catalan language.

%description i18n-ca -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
kataloñskim.


%package i18n-cs
Summary:	OpenOffice.org - interface in Czech language
Summary(pl):	OpenOffice.org - interfejs w jêzyku czeskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-cs
Obsoletes:	openoffice-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs-kde

%description i18n-cs
This package provides resources containing menus and dialogs in Czech
language.

%description i18n-cs -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
czeskim.

%package i18n-cy
Summary:	OpenOffice.org - interface in Cymraeg language
Summary(pl):	OpenOffice.org - interfejs w jêzyku walijskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-cy
Obsoletes:	openoffice-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy-kde

%description i18n-cy
This package provides resources containing menus and dialogs in
Cymraeg language.

%description i18n-cy -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
walijskim.

%package i18n-da
Summary:	OpenOffice.org - interface in Danish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku duñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-da
Obsoletes:	openoffice-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da-kde

%description i18n-da
This package provides resources containing menus and dialogs in Danish
language.

%description i18n-da -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
duñskim.

%package i18n-de
Summary:	OpenOffice.org - interface in German language
Summary(pl):	OpenOffice.org - interfejs w jêzyku niemieckim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-de
Obsoletes:	openoffice-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de-kde

%description i18n-de
This package provides resources containing menus and dialogs in German
language.

%description i18n-de -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
niemieckim.

%package i18n-el
Summary:	OpenOffice.org - interface in Greek language
Summary(pl):	OpenOffice.org - interfejs w jêzyku greckim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-el
Obsoletes:	openoffice-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el-kde

%description i18n-el
This package provides resources containing menus and dialogs in Greek
language.

%description i18n-el -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
greckim.

%package i18n-en_GB
Summary:	OpenOffice.org - interface in English language for United Kingdom
Summary(pl):	OpenOffice.org - interfejs w jêzyku anglieskim dla Wielkiej Brytanii
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-en_GB
This package provides resources containing menus and dialogs in
English language for United Kingdom.

%description i18n-en_GB -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
anglieskim dla Wielkiej Brytanii.

%package i18n-en_ZA
Summary:	OpenOffice.org - interface in English language for South Africa
Summary(pl):	OpenOffice.org - interfejs w jêzyku anglieskim dla Po³udniowej Afryki
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-en_ZA
This package provides resources containing menus and dialogs in
English language for South Africa.

%description i18n-en_ZA -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
anglieskim dla Po³udniowej Afryki.

%package i18n-eo
Summary:	OpenOffice.org - interface in Esperanto language
Summary(pl):	OpenOffice.org - interfejs w jêzyku esperanto
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-eo
This package provides resources containing menus and dialogs in
Esperanto language.

%description i18n-eo -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
esperanto.

%package i18n-es
Summary:	OpenOffice.org - interface in Spanish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hiszpañskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-es
Obsoletes:	openoffice-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es-kde

%description i18n-es
This package provides resources containing menus and dialogs in
Spanish language.

%description i18n-es -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hiszpañskim.

%package i18n-et
Summary:	OpenOffice.org - interface in Estonian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku estoñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-et
Obsoletes:	openoffice-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et-kde

%description i18n-et
This package provides resources containing menus and dialogs in
Estonian language.

%description i18n-et -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
estoñskim.

%package i18n-eu
Summary:	OpenOffice.org - interface in Basque (Euskara) language
Summary(pl):	OpenOffice.org - interfejs w jêzyku baskijskim (euskera)
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-eu
Obsoletes:	openoffice-i18n-eu-gtk
Obsoletes:	openoffice-i18n-eu-kde

%description i18n-eu
This package provides resources containing menus and dialogs in Basque
(Euskara) language.

%description i18n-eu -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
baskijskim (euskera).

%package i18n-fa
Summary:	OpenOffice.org - interface in Persian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku perskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fa
Obsoletes:	openoffice-i18n-fa-gtk
Obsoletes:	openoffice-i18n-fa-kde

%description i18n-fa
This package provides resources containing menus and dialogs in
Persian language.

%description i18n-eu -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
perskim.

%package i18n-fi
Summary:	OpenOffice.org - interface in Finnish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku fiñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fi
Obsoletes:	openoffice-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi-kde

%description i18n-fi
This package provides resources containing menus and dialogs in
Finnish language.

%description i18n-fi -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
fiñskim.

%package i18n-fo
Summary:	OpenOffice.org - interface in Faroese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku farerskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fo
Obsoletes:	openoffice-i18n-fo-gtk
Obsoletes:	openoffice.org-i18n-fo-gtk
Obsoletes:	openoffice.org-i18n-fo-kde

%description i18n-fo
This package provides resources containing menus and dialogs in
Faroese language.

%description i18n-fo -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
farerskim.

%package i18n-fr
Summary:	OpenOffice.org - interface in French language
Summary(pl):	OpenOffice.org - interfejs w jêzyku francuskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fr
Obsoletes:	openoffice-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr-kde

%description i18n-fr
This package provides resources containing menus and dialogs in French
language.

%description i18n-fr -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
francuskim.

%package i18n-ga
Summary:	OpenOffice.org - interface in Irish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku irlandzkim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ga
Obsoletes:	openoffice-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga-kde

%description i18n-ga
This package provides resources containing menus and dialogs in Irish
language.

%description i18n-ga -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
irlandzkim.

%package i18n-gl
Summary:	OpenOffice.org - interface in Galician language
Summary(pl):	OpenOffice.org - interfejs w jêzyku galicyjskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-gl
Obsoletes:	openoffice-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl-kde

%description i18n-gl
This package provides resources containing menus and dialogs in
Galician language.

%description i18n-gl -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
galicyjskim.

%package i18n-gu_IN
Summary:	OpenOffice.org - interface in Gujarati language
Summary(pl):	OpenOffice.org - interfejs w jêzyku gud¼arati
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-gu_IN
This package provides resources containing menus and dialogs in
Gujarati language.

%description i18n-gu_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
gud¼arati.

%package i18n-he
Summary:	OpenOffice.org - interface in Hebrew language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hebrajskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-he
Obsoletes:	openoffice-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he-kde

%description i18n-he
This package provides resources containing menus and dialogs in Hebrew
language.

%description i18n-he -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hebrajskim.

%package i18n-hi_IN
Summary:	OpenOffice.org - interface in Hindi language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hindi
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hi
Obsoletes:	openoffice-i18n-hi-gtk
Obsoletes:	openoffice.org-i18n-hi-gtk
Obsoletes:	openoffice.org-i18n-hi-kde

%description i18n-hi_IN
This package provides resources containing menus and dialogs in Hindi
language.

%description i18n-hi_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hindi.

%package i18n-hr
Summary:	OpenOffice.org - interface in Croatian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku chorwackim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hr
Obsoletes:	openoffice-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr-kde

%description i18n-hr
This package provides resources containing menus and dialogs in
Croatian language.

%description i18n-hr -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chorwackim.

%package i18n-hu
Summary:	OpenOffice.org - interface in Hungarian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku wêgierskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hu
Obsoletes:	openoffice-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu-kde

%description i18n-hu
This package provides resources containing menus and dialogs in
Hungarian language.

%description i18n-hu -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
wêgierskim.

%package i18n-ia
Summary:	OpenOffice.org - interface in Interlingua language
Summary(pl):	OpenOffice.org - interfejs w jêzyku interlingua
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ia
Obsoletes:	openoffice-i18n-ia-gtk
Obsoletes:	openoffice.org-i18n-ia-gtk
Obsoletes:	openoffice.org-i18n-ia-kde

%description i18n-ia
This package provides resources containing menus and dialogs in
Interlingua language.

%description i18n-ia -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
interlingua.

%package i18n-id
Summary:	OpenOffice.org - interface in Indonesian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku indonezyjskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-id
Obsoletes:	openoffice-i18n-id-gtk
Obsoletes:	openoffice.org-i18n-id-gtk
Obsoletes:	openoffice.org-i18n-id-kde

%description i18n-id
This package provides resources containing menus and dialogs in
Indonesian language.

%description i18n-id -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
indonezyjskim.

%package i18n-it
Summary:	OpenOffice.org - interface in Italian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku w³oskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-it
ObsoleteS:	openoffice-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it-kde

%description i18n-it
This package provides resources containing menus and dialogs in
Italian language.

%description i18n-it -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
w³oskim.

%package i18n-ja
Summary:	OpenOffice.org - interface in Japan language
Summary(pl):	OpenOffice.org - interfejs w jêzyku japoñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ja
Obsoletes:	openoffice-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja-kde

%description i18n-ja
This package provides resources containing menus and dialogs in Japan
language.

%description i18n-ja -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
japoñskim.

%package i18n-km
Summary:	OpenOffice.org - interface in Khmer language
Summary(pl):	OpenOffice.org - interfejs w jêzyku khmerskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-km
This package provides resources containing menus and dialogs in Khmer
language.

%description i18n-km -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
khmerskim.

%package i18n-kn_IN
Summary:	OpenOffice.org - interface in Kannada language
Summary(pl):	OpenOffice.org - interfejs w jêzyku kannara
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-kn
Obsoletes:	openoffice-i18n-kn-gtk
Obsoletes:	openoffice-i18n-kn-kde

%description i18n-kn_IN
This package provides resources containing menus and dialogs in
Kannada language.

%description i18n-kn_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
kannara.

%package i18n-ko
Summary:	OpenOffice.org - interface in Korean language
Summary(pl):	OpenOffice.org - interfejs w jêzyku koreañskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ko
Obsoletes:	openoffice-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko-kde

%description i18n-ko
This package provides resources containing menus and dialogs in Korean
language.

%description i18n-ko -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
koreañskim.

%package i18n-ku
Summary:	OpenOffice.org - interface in Kurdish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku kurdyjskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ku
This package provides resources containing menus and dialogs in
Kurdish language.

%description i18n-ku -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
kurdyjskim.

%package i18n-la
Summary:	OpenOffice.org - interface in Latin language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ³aciñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-la
Obsoletes:	openoffice-i18n-la-gtk
Obsoletes:	openoffice.org-i18n-la-gtk
Obsoletes:	openoffice.org-i18n-la-kde

%description i18n-la
This package provides resources containing menus and dialogs in Latin
language.

%description i18n-la -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
³aciñskim.

%package i18n-lo
Summary:	OpenOffice.org - interface in Lao language
Summary(pl):	OpenOffice.org - interfejs w jêzyku laotañskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-lo
This package provides resources containing menus and dialogs in Lao
language.

%description i18n-lo -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
laotañskim.

%package i18n-lt
Summary:	OpenOffice.org - interface in Lithuanian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku litewskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-lt
Obsoletes:	openoffice-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt-kde

%description i18n-lt
This package provides resources containing menus and dialogs in
Lithuanian language.

%description i18n-lt -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
litewskim.

%package i18n-lv
Summary:	OpenOffice.org - interface in Latvian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ³otewskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-lv
This package provides resources containing menus and dialogs in
Latvian language.

%description i18n-lv -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
³otewskim.

%package i18n-med
Summary:	OpenOffice.org - interface in Melpa language
Summary(pl):	OpenOffice.org - interfejs w jêzyku melpa
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-med
Obsoletes:	openoffice-i18n-med-gtk
Obsoletes:	openoffice.org-i18n-med-gtk
Obsoletes:	openoffice.org-i18n-med-kde

%description i18n-med
This package provides resources containing menus and dialogs in Melpa
language.

%description i18n-med -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
melpa.

%package i18n-mi
Summary:	OpenOffice.org - interface in Maori language
Summary(pl):	OpenOffice.org - interfejs w jêzyku maoryjskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-mi
Obsoletes:	openoffice-i18n-mi-gtk
Obsoletes:	openoffice.org-i18n-mi-gtk
Obsoletes:	openoffice.org-i18n-mi-kde

%description i18n-mi
This package provides resources containing menus and dialogs in Maori
language.

%description i18n-mi -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
maoryjskim.

%package i18n-mk
Summary:	OpenOffice.org - interface in Macedonian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku macedoñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-mk
This package provides resources containing menus and dialogs in
Macedonian language.

%description i18n-mk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
macedoñskim.

%package i18n-ml_IN
Summary:	OpenOffice.org - interface in Malayalam language for India
Summary(pl):	OpenOffice.org - interfejs w jêzyku malajalamskim dla Indii
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ml_IN
This package provides resources containing menus and dialogs in
Malayalam language for India.

%description i18n-ml_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
malajalamskim dla Indii.

%package i18n-mr_IN
Summary:	OpenOffice.org - interface in Marathi language for India
Summary(pl):	OpenOffice.org - interfejs w jêzyku marathi dla Indii
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-mr_IN
This package provides resources containing menus and dialogs in
Marathi language for India.

%description i18n-mr_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
marathi dla Indii.

%package i18n-ms
Summary:	OpenOffice.org - interface in Malay language
Summary(pl):	OpenOffice.org - interfejs w jêzyku malajskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ms
Obsoletes:	openoffice-i18n-ms-gtk
Obsoletes:	openoffice.org-i18n-ms-gtk
Obsoletes:	openoffice.org-i18n-ms-kde

%description i18n-ms
This package provides resources containing menus and dialogs in Malay
language.

%description i18n-ms -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
malajskim.

%package i18n-nb
Summary:	OpenOffice.org - interface in Norwegian Bokmaal language
Summary(pl):	OpenOffice.org - interfejs w jêzyku norweskim (odmiana Bokmaal)
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nb
Obsoletes:	openoffice-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb-kde

%description i18n-nb
This package provides resources containing menus and dialogs in
Norwegian Bokmaal language.

%description i18n-nb -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
norweskim w odmianie Bokmaal.

%package i18n-ne
Summary:	OpenOffice.org - interface in Nepali language
Summary(pl):	OpenOffice.org - interfejs w jêzyku nepalskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ne
This package provides resources containing menus and dialogs in Nepali
language.

%description i18n-ne -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
nepalskim.

%package i18n-nl
Summary:	OpenOffice.org - interface in Dutch language
Summary(pl):	OpenOffice.org - interfejs w jêzyku holenderskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nl
Obsoletes:	openoffice-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl-kde

%description i18n-nl
This package provides resources containing menus and dialogs in Dutch
language.

%description i18n-nl -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
holenderskim.

%package i18n-nn
Summary:	OpenOffice.org - interface in Norwegian Nynorsk language
Summary(pl):	OpenOffice.org - interfejs w jêzyku norweskim (odmiana Nynorsk)
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nn
Obsoletes:	openoffice-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn-kde

%description i18n-nn
This package provides resources containing menus and dialogs in
Norwegian Nynorsk language.

%description i18n-nn -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
norweskim w odmianie Nynorsk.

%package i18n-nr
Summary:	OpenOffice.org - interface in South Ndebele language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ndebele (po³udniowym)
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-nr
This package provides resources containing menus and dialogs in South
Ndebele language.

%description i18n-nr -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
ndebele (po³udniowym).

%package i18n-nso
Summary:	OpenOffice.org - interface in Northern Sotho language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ludu Soto
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nso
Obsoletes:	openoffice-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso-kde

%description i18n-nso
This package provides resources containing menus and dialogs in
Northern Sotho language.

%description i18n-nso -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
ludu Soto.

%package i18n-or_IN
Summary:	OpenOffice.org - interface in Oriya language for India
Summary(pl):	OpenOffice.org - interfejs w jêzyku orija dla Indii
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-or_IN
This package provides resources containing menus and dialogs in Oriya
language for India.

%description i18n-or_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
orija dla Indii.

%package i18n-pa_IN
Summary:	OpenOffice.org - interface in Punjabi language
Summary(pl):	OpenOffice.org - interfejs w jêzyku pend¿abskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-pa_IN
This package provides resources containing menus and dialogs in
Punjabi language.

%description i18n-pa_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
pend¿abskim.

%package i18n-pl
Summary:	OpenOffice.org - interface in Polish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku polskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pl
Obsoletes:	openoffice-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl-kde

%description i18n-pl
This package provides resources containing menus and dialogs in Polish
language.

%description i18n-pl -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
polskim.

%package i18n-pt
Summary:	OpenOffice.org - interface in Portuguese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku portugalskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pt
Obsoletes:	openoffice-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt-kde

%description i18n-pt
This package provides resources containing menus and dialogs in
Portuguese language.

%description i18n-pt -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
portugalskim.

%package i18n-pt_BR
Summary:	OpenOffice.org - interface in Brazilian Portuguese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku portugalskim dla Brazylii
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pt_BR
Obsoletes:	openoffice-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR-kde

%description i18n-pt_BR
This package provides resources containing menus and dialogs in
Brazilian Portuguese language.

%description i18n-pt_BR -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
portugalskim dla Brazylii.

%package i18n-ro
Summary:	OpenOffice.org - interface in Romanian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku rumuñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ro
Obsoletes:	openoffice-i18n-ro-gtk
Obsoletes:	openoffice.org-i18n-ro-gtk
Obsoletes:	openoffice.org-i18n-ro-kde

%description i18n-ro
This package provides resources containing menus and dialogs in
Romanian language.

%description i18n-ro -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
rumuñskim.

%package i18n-ru
Summary:	OpenOffice.org - interface in Russian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku rosyjskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ru
Obsoletes:	openoffice-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru-kde

%description i18n-ru
This package provides resources containing menus and dialogs in
Russian language.

%description i18n-ru -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
rosyjskim.

%package i18n-rw
Summary:	OpenOffice.org - interface in Kinarwanda language
Summary(pl):	OpenOffice.org - interfejs w jêzyku kinya-ruanda
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-rw
This package provides resources containing menus and dialogs in
Kinarwanda language.

%description i18n-rw -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
kinya-ruanda.

%package i18n-sh
Summary:	OpenOffice.org - interface in Serbo-Croatian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku serbsko-chorwackim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-sh
This package provides resources containing menus and dialogs in
Serbo-Croatian language.

%description i18n-sh -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
serbsko-chorwackim.

%package i18n-sk
Summary:	OpenOffice.org - interface in Slovak language
Summary(pl):	OpenOffice.org - interfejs w jêzyku s³owackim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sk
Obsoletes:	openoffice-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk-kde

%description i18n-sk
This package provides resources containing menus and dialogs in Slovak
language.

%description i18n-sk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
s³owackim.

%package i18n-sl
Summary:	OpenOffice.org - interface in Slovenian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku s³oweñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sl
Obsoletes:	openoffice-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl-kde

%description i18n-sl
This package provides resources containing menus and dialogs in
Slovenian language.

%description i18n-sl -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
s³oweñskim.

%package i18n-sr
Summary:	OpenOffice.org - interface in Serbian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku serbskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-sr
This package provides resources containing menus and dialogs in
Serbian language.

%description i18n-sr -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
serbskim.

%package i18n-ss
Summary:	OpenOffice.org - interface in Siswant language
Summary(pl):	OpenOffice.org - interfejs w jêzyku siswati
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ss
This package provides resources containing menus and dialogs in
Siswant language.

%description i18n-ss -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
siswati.

%package i18n-st
Summary:	OpenOffice.org - interface in Southern Sotho language
Summary(pl):	OpenOffice.org - interfejs w jêzyku po³udniowym sotho
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-st
This package provides resources containing menus and dialogs in
Southern Sotho language.

%description i18n-st -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
po³udniowym sotho.

%package i18n-sv
Summary:	OpenOffice.org - interface in Swedish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku szwedzkim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sv
Obsoletes:	openoffice-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv-kde

%description i18n-sv
This package provides resources containing menus and dialogs in
Swedish language.

%description i18n-sv -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
szwedzkim.

%package i18n-sw
Summary:	OpenOffice.org - interface in Swahili language
Summary(pl):	OpenOffice.org - interfejs w jêzyku suahili
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-sw
This package provides resources containing menus and dialogs in
Swahili language.

%description i18n-sw -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
suahili.

%package i18n-sw_TZ
Summary:	OpenOffice.org - interface in Swahili language for Tanzania
Summary(pl):	OpenOffice.org - interfejs w jêzyku suahili dla Tanzanii
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-sw_TZ
This package provides resources containing menus and dialogs in
Swahili language for Tanzania.

%description i18n-sw_TZ -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
suahili dla Tanzanii.

%package i18n-sx
Summary:	OpenOffice.org - interface in Sutu language
Summary(pl):	OpenOffice.org - interfejs w jêzyku sutu
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-sx
This package provides resources containing menus and dialogs in Sutu
language.

%description i18n-sx -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
sutu.

%package i18n-ta_IN
Summary:	OpenOffice.org - interface in Tamil language
Summary(pl):	OpenOffice.org - interfejs w jêzyku tamiskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ta_IN
This package provides resources containing menus and dialogs in Tamil
language.

%description i18n-ta_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tamilskim.

%package i18n-te_IN
Summary:	OpenOffice.org - interface in Telugu language for India
Summary(pl):	OpenOffice.org - interfejs w jêzyku telugu dla Indii
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-te_IN
This package provides resources containing menus and dialogs in Telugu
language for India.

%description i18n-te_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
telugu dla Indii.

%package i18n-tg
Summary:	OpenOffice.org - interface in Tajik language
Summary(pl):	OpenOffice.org - interfejs w jêzyku tad¿yckim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-tg
This package provides resources containing menus and dialogs in Tajik
language.

%description i18n-tg -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tad¿yckim.

%package i18n-th
Summary:	OpenOffice.org - interface in Thai language
Summary(pl):	OpenOffice.org - interfejs w jêzyku tajskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-th
Obsoletes:	openoffice-i18n-th-gtk
Obsoletes:	openoffice-i18n-th-kde

%description i18n-th
This package provides resources containing menus and dialogs in Thai
language.

%description i18n-th -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tajskim.

%package i18n-ti_ER
Summary:	OpenOffice.org - interface in Tigrigna language for Eritrea
Summary(pl):	OpenOffice.org - interfejs w jêzyku tigrinia dla Erytrei
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ti_ER
This package provides resources containing menus and dialogs in
Tigrigna language for Eritrea.

%description i18n-ti_ER -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tigrinia dla Erytrei.

%package i18n-tn
Summary:	OpenOffice.org - interface in Tswana language
Summary(pl):	OpenOffice.org - interfejs w jêzyku tswana
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-tn
Obsoletes:	openoffice-i18n-tn-gtk
Obsoletes:	openoffice-i18n-tn-kde

%description i18n-tn
This package provides resources containing menus and dialogs in Tswana
language.

%description i18n-tn -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tswana.

%package i18n-tr
Summary:	OpenOffice.org - interface in Turkish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku tureckim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-tr
Obsoletes:	openoffice-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr-kde

%description i18n-tr
This package provides resources containing menus and dialogs in
Turkish language.

%description i18n-tr -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tureckim.

%package i18n-ts
Summary:	OpenOffice.org - interface in Tsonga language
Summary(pl):	OpenOffice.org - interfejs w jêzyku tsonga
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ts
This package provides resources containing menus and dialogs in Tsonga
language.

%description i18n-ts -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tsonga.

%package i18n-uk
Summary:	OpenOffice.org - interface in Ukrainian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ukraiñskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-uk
Obsoletes:	openoffice-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk-kde

%description i18n-uk
This package provides resources containing menus and dialogs in
Ukrainian language.

%description i18n-uk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
ukraiñskim.

%package i18n-ur_IN
Summary:	OpenOffice.org - interface in Urdu language for India
Summary(pl):	OpenOffice.org - interfejs w jêzyku urdu dla Indii
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ur_IN
This package provides resources containing menus and dialogs in Urdu
language for India.

%description i18n-ur_IN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
urdu dla Indii.

%package i18n-ve
Summary:	OpenOffice.org - interface in Venda language
Summary(pl):	OpenOffice.org - interfejs w jêzyku venda
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ve
This package provides resources containing menus and dialogs in Venda
language.

%description i18n-ve -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
venda.

%package i18n-vi
Summary:	OpenOffice.org - interface in Vietnamese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku wietnamskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-vi
This package provides resources containing menus and dialogs in
Vietnamese language.

%description i18n-vi -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
wietnamskim.

%package i18n-xh
Summary:	OpenOffice.org - interface in Xhosa language
Summary(pl):	OpenOffice.org - interfejs w jêzyku khosa
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-xh
This package provides resources containing menus and dialogs in Xhosa
language.

%description i18n-xh -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
khosa.

%package i18n-zh_CN
Summary:	OpenOffice.org - interface in Chinese language for China
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim dla Chin
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_CN
Obsoletes:	openoffice-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN-kde

%description i18n-zh_CN
This package provides resources containing menus and dialogs in
Chinese language for China.

%description i18n-zh_CN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim dla Chin.

%package i18n-zh_TW
Summary:	OpenOffice.org - interface in Chinese language for Taiwan
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim dla Tajwanu
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_TW
Obsoletes:	openoffice-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW-kde

%description i18n-zh_TW
This package provides resources containing menus and dialogs in
Chinese language for Taiwan.

%description i18n-zh_TW -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim dla Tajwanu.

%package i18n-zu
Summary:	OpenOffice.org - interface in Zulu language
Summary(pl):	OpenOffice.org - interfejs w jêzyku zuluskim
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zu
Obsoletes:	openoffice-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu-kde

%description i18n-zu
This package provides resources containing menus and dialogs in Zulu
language.

%description i18n-zu -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
zuluskim.

%package -n bash-completion-openoffice
Summary:	bash-completion for OpenOffice.org
Summary(pl):	bashowe uzupe³nianie nazw dla OpenOffice.org
Group:		Applications/Shells
Requires:	%{name}
Requires:	bash-completion

%description -n bash-completion-openoffice
bash-completion for OpenOffice.org.

%description -n bash-completion-openoffice -l pl
bashowe uzupe³nianie nazw dla Openoffice.org.

%prep
%setup -q -n ooo-build-%{ooobver}

install -d src
cp %{SOURCE50} %{SOURCE51} src

# sources, icons, KDE_icons
ln -sf %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
	%{SOURCE10} %{SOURCE11} %{SOURCE12} \
	%{SOURCE15} %{SOURCE16} %{SOURCE17} src

# fixes for the patch subsystem
%patch0 -p1

# teach configure.in about PLD
%patch1 -p1

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# 64 bit related patches (not applied now)
install %{PATCH100} patches/64bit
install %{PATCH101} patches/64bit/64bit-inline.diff

echo "[ PLDOnly ]" >> patches/src680/apply
# patches applied by ooo (extension .diff is required)
for P in %{PATCH102} %{PATCH104} %{PATCH105} %{PATCH106} ; do
	PATCHNAME=`basename $P | sed "s/%{name}-//; s/.patch$/.diff/"`
	install $P patches/src680/$PATCHNAME
	echo $PATCHNAME >> patches/src680/apply
done

%build
# Make sure we have /proc mounted - otherwise idlc will fail later.
if [ ! -r /proc/cpuinfo ]; then
	echo "You need to have /proc mounted in order to build this package!"
	exit 1
fi

%{__aclocal}
%{__autoconf}

%ifarch %{x8664} sparc64 ppc64 alpha
DISTRO="PLD64"
%else
DISTRO="PLD"
%endif

export CC="%{__cc}"
export CXX="%{__cxx}"
export ENVCFLAGS="%{rpmcflags}"
# disable STLport 5.1 containers extension, doesn't work with map indexed by enum
export ENVCFLAGSCXX="%{rpmcflags} -fpermissive -D_STLP_NO_CONTAINERS_EXTENSION"
export DESTDIR=$RPM_BUILD_ROOT
export IGNORE_MANIFEST_CHANGES=1
export QTINC="%{_includedir}/qt"
export QTLIB="%{_libdir}"

%if %{with java}
export JAVA_HOME=%{java_home}
export DB_JAR="%{_javadir}/db.jar"
export ANT_HOME=%{_prefix}
%endif

export DEFAULT_TO_ENGLISH_FOR_PACKING=1

RPM_BUILD_NR_THREADS="%(echo "%{__make}" | sed -e 's#.*-j\([[:space:]]*[0-9]\+\)#\1#g')"
[ "$RPM_BUILD_NR_THREADS" = "%{__make}" ] && RPM_BUILD_NR_THREADS=1
RPM_BUILD_NR_THREADS=$(echo $RPM_BUILD_NR_THREADS)

CONFOPTS=" \
%ifarch %{ix86} \
	--with-arch=x86 \
%endif
%ifarch ppc
	--with-arch=ppc \
%endif
%ifarch sparc sparcv9
	--with-arch=sparc \
%endif
%ifarch %{x8664}
	--with-arch=x86_64 \
%endif
	--disable-odk \
	--with-ccache-allowed \
	--with-system-gcc \
	--with-system-zlib \
	--with-system-jpeg \
	--with-system-libxml \
	--with-system-python \
	--with-system-sane-header \
	--with-system-x11-extensions-headers \
	--with-system-odbc-headers \
	--with-system-stdlibs \
%if %{with system_db}
	--with-system-db \
%endif
	--with-system-curl \
	--with-system-freetype \
	--with-system-nas \
	--with-system-xrender \
	--with-system-xrender-headers=yes \
	--with-system-expat \
	--with-system-sablot \
	--with-system-boost \
	--with-system-icu \
	--with-system-libwpd \
%if %{with system_mdbtools}
	--with-system-mdbtools \
%endif
	--with-system-neon \
	--with-system-portaudio \
	--with-system-sndfile \
%if %{with system_xt}
	--with-system-xt \
	--with-xt-jar=/usr/share/java/classes/ \
%endif
%if %{with system_beanshell}
	--with-system-beanshell \
%endif
	--with-system-xmlsec \
%if %{with mozilla}
	--with-system-mozilla \
%if %{with seamonkey}
	--with-seamonkey \
%else
	--with-firefox \
%endif
%else
	--disable-mozilla \
%endif
	--with-system-cairo \
	--with-dynamic-xinerama \
	--with-intro-bitmaps="\$SRCDIR/openintro_pld.bmp" \
	--with-about-bitmaps="\$SRCDIR/openabout_pld.png" \
	--with-distro="${DISTRO}" \
	--enable-gtk \
%if %{with kde}
	--enable-kde \
%else
	--disable-kde \
%endif
	--without-binsuffix \
	--with-installed-ooo-dirname=%{name} \
	--with-lang=ALL \
%if %{with java}
	--with-java \
	--with-jdk-home=$JAVA_HOME \
%else
	--without-java \
%endif
%if %{with gnomevfs}
	--enable-gnome-vfs \
%else
	--disable-gnome-vfs \
%endif
	--with-docdir=%{_docdir}/%{name}-%{version} \
	--with-python=%{__python} \
	--with-openclipart=%{_datadir}/openclipart \
	--with-stlport=/usr \
	--with-x \
	--without-fonts \
	--without-gpc \
	--disable-epm \
	--disable-fontooo \
	--enable-access \
	--enable-cairo \
	--enable-crypt-link \
	%{?with_mono:--enable-mono} %{!?with_mono:--disable-mono} \
	--enable-pam-link \
	--enable-openldap \
	--enable-cups \
	--enable-fontconfig \
	--enable-libsn \
	--enable-libart \
	--disable-rpath \
%if 0%{?debug:1}
	--enable-debug \
	--enable-crashdump=yes \
	--enable-symbols=FULL \
%else
	--enable-crashdump=no \
	--disable-symbols \
%endif
	--with-num-cpus=$RPM_BUILD_NR_THREADS
	--with-tag=%{ssnap}
"

# build-ooo script will pickup these
export CONFIGURE_OPTIONS="$CONFOPTS"

:> distro-configs/Common.conf
:> distro-configs/Common.conf.in
echo "$CONFOPTS" > distro-configs/PLD.conf.in

# for cvs snaps
[ -x ./autogen.sh ] && ./autogen.sh $CONFOPTS

# main build
%configure \
	$CONFOPTS

# this limits processing some files but doesn't limit parallel build
# processes of main OOo build (since OOo uses it's own build system)
%{__make} -j1

# hack for parallel build
if [ $RPM_BUILD_NR_THREADS -gt 1 ]; then
	doit=1
	while [ "$doit" -eq 1 ]; do
		echo "Waiting one more time..."
		FCH=$(nice -n 20 find . -type f ! -mmin +3 -print 2> /dev/null | wc -l)
		[ "$FCH" -eq 0 ] && doit=0 || sleep 30
	done
fi

%install
rm -rf $RPM_BUILD_ROOT

# limit to single process installation, it's safe at least
%{__sed} -i -e 's#^BUILD_NCPUS=.*#BUILD_NCPUS=1#g' bin/setup

export DESTDIR=$RPM_BUILD_ROOT
export TMP="%{tmpdir}"
export TEMP="%{tmpdir}"
export DEFAULT_TO_ENGLISH_FOR_PACKING=1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

# Add in the regcomp tool since some people need it for 3rd party add-ons
cp -f build/%{ssnap}/solver/%{subver}/unxlng*.pro/bin/regcomp $RPM_BUILD_ROOT%{_libdir}/%{name}/program

# fix python
sed -i -e 's|#!/bin/python|#!%{_bindir}/python|g' $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*.py

# Really needed?
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/kde
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/cde
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/gnome
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/icons
rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome

# Remove dictionaries (in separate pkg)
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo/*
touch $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo/dictionary.lst

# OOo should not install the Vera fonts, they are Required: now
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/fonts/truetype/*

# Copy fixed OpenSymbol to correct location
install -d $RPM_BUILD_ROOT%{_fontsdir}/TTF
install build/%{ssnap}/extras/source/truetype/symbol/opens___.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

# We don't need spadmin (gtk) or the setup application
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/setup
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/crash_report.bin
rm -f $RPM_BUILD_ROOT%{_desktopdir}/openoffice-setup.desktop
rm -f $RPM_BUILD_ROOT%{_desktopdir}/openoffice-printeradmin.desktop

#rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/gnomeint

# some libs creep in somehow
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libstl*.so*
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libsndfile*

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/sopatchlevel.sh
perl -pi -e 's/^[       ]*LD_LIBRARY_PATH/# LD_LIBRARY_PATH/;s/export LD_LIBRARY_PATH/# export LD_LIBRARY_PATH/' \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/program/setup

# Remove setup log
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/setup.log

# Remove copied system libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libgcc_s.so* \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/program/libstdc++*so*

# Find out locales
rm -f *.lang*
langlist="`ls build/lang_*_list.txt|sed -e 's=build/lang_\(.*\)_list.txt=\1=g'`"

for lang in $langlist; do
	echo "%%defattr(644,root,root,755)" > ${lang}.lang

	# help files
	if [ -f build/help_${lang}_list.txt ]; then
		cat build/help_${lang}_list.txt >> ${lang}.lang
	fi

	lfile="build/lang_${lang}_list.txt"
	if [ -f ${lfile} ]; then
		lprefix="`bin/openoffice-xlate-lang -p ${lang} 2>/dev/null || echo ""`"
		longlang="`bin/openoffice-xlate-lang -l ${lang} 2>/dev/null || echo ""`"
		# share/*/${longlang}
		if [ "x${longlang}" != "x" ] ; then
			grep "^%%dir.*/${longlang}/\$" ${lfile} > tmp.lang || :
		fi
		# share/registry/res/${lang} (but en-US for en)
		grep "^%%dir.*/res/${lang}[^/]*/\$" ${lfile} >> tmp.lang || :
		# ... translate %dir into whole tree, handle special wordbook/english case
		sed -e 's,^%%dir ,,;s,\(wordbook/english/\)$,\1soffice.dic,;s,/$,,' tmp.lang >> ${lang}.lang || :
		# share/autocorr/acor${somecodes}.dat (if exist)
		grep '/autocorr/acor.*dat$' ${lfile} >> ${lang}.lang || :
		# user/config/* (if exist, without parent directory)
		grep '/user/config/..*' ${lfile} >> ${lang}.lang || :
		grep "/licenses/LICENSE_${lang}" ${lfile} >> ${lang}.lang || :
		grep "/readmes/README_${lang}" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/presers/config/*.so[cdegh]
		grep "/presets/config/.*_${lang}\.so[cdegh]$" ${lfile} >> ${lang}.lang || :
		if [ "x${lprefix}" != "x" ] ; then
			grep "/presets/config/${lprefix}.*\.so[cdegh]$" ${lfile} >> ${lang}.lang || :
		fi
		# lib/openoffice.org/program/resource/*.res
		grep "/program/resource/.*${lang}.res$" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/share/autocorr/*.dat
		grep "/share/autocorr/.*${lang}.dat$" ${lfile} >> ${lang}.lang || :
		grep -i "/share/autocorr/.*${lang}-${lang}.dat$" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/share/autotext/$lang
		grep "/share/autotext/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/autotext/${lang}/" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/share/registry/res/$lang
		grep "/share/registry/res/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/registry/res/${lang}/" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/share/template/$lang
		grep "/share/template/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/template/${lang}/" ${lfile} >> ${lang}.lang || :
		# lib/openoffice.org/share/template/wizard/letter/lang
		grep "/share/template/wizard/letter/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/template/wizard/letter/${lang}$" build/common_list.txt >> ${lang}.lang || :
		grep "/share/template/wizard/letter/${lang}/" ${lfile} >> ${lang}.lang || :
		grep "/share/template/wizard/letter/${lang}/" build/common_list.txt >> ${lang}.lang || :
		# lib/openoffice.org/share/wordbook/$lang
		grep "/share/wordbook/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/wordbook/${lang}/" ${lfile} >> ${lang}.lang || :
		%if %{with java}
		grep "/help/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/help/${lang}/" ${lfile} >> ${lang}.lang || :
		%endif
	fi
done

find $RPM_BUILD_ROOT -type f -name '*.so' -exec chmod 755 "{}" ";"
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/xdg
rm -rf $RPM_BUILD_ROOT/opt/gnome
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/cde-open-url

%if %{without java}
# Java-releated bits
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/program/hid.lst
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/program/java-set-classpath
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/program/jvmfwk3rc
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/Scripts/beanshell
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/Scripts/javascript
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/xslt
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:
[ ! -x /usr/bin/update-mime-database ] || /usr/bin/update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
[ ! -x /usr/bin/update-mime-database ] || /usr/bin/update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:

%post libs
fontpostinst TTF

%postun libs
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc %{_libdir}/%{name}/LICENSE*
%doc %{_libdir}/%{name}/*README*

%dir %{_sysconfdir}/openoffice.org

%attr(755,root,root) %{_libdir}/%{name}/install-dict

%{_libdir}/%{name}/program/*.rdb
%{_libdir}/%{name}/program/*.bmp
#%{_libdir}/%{name}/program/user_registry.xsl
%{_libdir}/%{name}/program/sofficerc
%{_libdir}/%{name}/program/unorc
%{_libdir}/%{name}/program/bootstraprc
%{_libdir}/%{name}/program/configmgrrc
#%{_libdir}/%{name}/program/instdb.ins
%dir %{_libdir}/%{name}/program/resource
%dir %{_libdir}/%{name}/licenses
%dir %{_libdir}/%{name}/readmes

#%dir %{_libdir}/%{name}/help
#%{_libdir}/%{name}/help/en
#%{_libdir}/%{name}/help/main_transform.xsl

%dir %{_libdir}/%{name}/share
%dir %{_libdir}/%{name}/share/autocorr
%dir %{_libdir}/%{name}/share/autotext
%{_libdir}/%{name}/share/basic
#%dir %{_libdir}/%{name}/share/bookmark
%dir %{_libdir}/%{name}/share/config
%{_libdir}/%{name}/share/config/symbol
%{_libdir}/%{name}/share/config/webcast
%{_libdir}/%{name}/share/config/*.xpm
%{_libdir}/%{name}/share/config/images.zip
%{_libdir}/%{name}/share/config/images_crystal.zip
%{_libdir}/%{name}/share/config/images_industrial.zip
%{_libdir}/%{name}/share/config/images_hicontrast.zip
%{_libdir}/%{name}/share/config/soffice.cfg
%{_libdir}/%{name}/share/config/wizard
#%dir %{_libdir}/%{name}/share/database
%dir %{_libdir}/%{name}/share/dict
%dir %{_libdir}/%{name}/share/dict/ooo
%{_libdir}/%{name}/share/dtd
%{_libdir}/%{name}/share/fonts
%{_libdir}/%{name}/share/gallery
%{_libdir}/%{name}/share/psprint
%dir %{_libdir}/%{name}/share/samples
%dir %{_libdir}/%{name}/share/template
%dir %{_libdir}/%{name}/share/template/wizard
%dir %{_libdir}/%{name}/share/template/wizard/letter
%dir %{_libdir}/%{name}/share/wordbook
#%dir %{_libdir}/%{name}/share/wordbook/english
#%{_libdir}/%{name}/share/wordbook/english/sun.dic
%{_libdir}/%{name}/share/readme

%dir %{_libdir}/%{name}/share/registry
%dir %{_libdir}/%{name}/share/registry/res
%{_libdir}/%{name}/share/registry/data
%{_libdir}/%{name}/share/registry/schema
%{_libdir}/%{name}/share/registry/ldap
# split ?
%{_libdir}/%{name}/share/registry/modules

#%{_libdir}/%{name}/share/autotext/english
# XXX: in ooo-build only template/english/wizard/bitmaps is in main?
#%{_libdir}/%{name}/share/template/english
%ghost %{_libdir}/%{name}/share/dict/ooo/dictionary.lst

%dir %{_libdir}/%{name}/presets
%dir %{_libdir}/%{name}/presets/autotext
%{_libdir}/%{name}/presets/autotext/mytexts.bau
%{_libdir}/%{name}/presets/basic
%dir %{_libdir}/%{name}/presets/config
%{_libdir}/%{name}/presets/config/autotbl.fmt
%{_libdir}/%{name}/presets/config/cmyk.soc
%{_libdir}/%{name}/presets/config/gallery.soc
%{_libdir}/%{name}/presets/config/html.soc
%{_libdir}/%{name}/presets/config/standard.so?
%{_libdir}/%{name}/presets/config/sun-color.soc
%{_libdir}/%{name}/presets/config/web.soc

%{_libdir}/%{name}/presets/database
%{_libdir}/%{name}/presets/gallery
%{_libdir}/%{name}/presets/psprint

#%{_libdir}/%{name}/presets/autotext/english

# Programs
%attr(755,root,root) %{_bindir}/oo*
#%attr(755,root,root) %{_sbindir}/oopadmin
#%attr(755,root,root) %{_libdir}/%{name}/spadmin
%attr(755,root,root) %{_libdir}/%{name}/program/configimport.bin
%attr(755,root,root) %{_libdir}/%{name}/program/gengal.bin
%attr(755,root,root) %{_libdir}/%{name}/program/pkgchk.bin
%attr(755,root,root) %{_libdir}/%{name}/program/pluginapp.bin
%attr(755,root,root) %{_libdir}/%{name}/program/setofficelang.bin
%attr(755,root,root) %{_libdir}/%{name}/program/soffice.bin
%attr(755,root,root) %{_libdir}/%{name}/program/spadmin.bin
%attr(755,root,root) %{_libdir}/%{name}/program/testtool.bin
%{_libdir}/%{name}/program/testtoolrc
%attr(755,root,root) %{_libdir}/%{name}/program/uno.bin
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg.bin
#%attr(755,root,root) %{_libdir}/%{name}/program/fromtemplate
#%attr(755,root,root) %{_libdir}/%{name}/program/mozwrapper
#%attr(755,root,root) %{_libdir}/%{name}/program/nswrapper
#%attr(755,root,root) %{_libdir}/%{name}/program/ooovirg
%attr(755,root,root) %{_libdir}/%{name}/program/ooqstart
%attr(755,root,root) %{_libdir}/%{name}/program/pagein*
#%attr(755,root,root) %{_libdir}/%{name}/program/python.sh
%{_libdir}/%{name}/program/pythonloader.unorc
#%attr(755,root,root) %{_libdir}/%{name}/program/pyunorc
%attr(755,root,root) %{_libdir}/%{name}/program/regcomp
#%attr(755,root,root) %{_libdir}/%{name}/program/sagenda
%attr(755,root,root) %{_libdir}/%{name}/program/scalc
%attr(755,root,root) %{_libdir}/%{name}/program/sdraw
#%attr(755,root,root) %{_libdir}/%{name}/program/setup
%{_libdir}/%{name}/program/setuprc
#%attr(755,root,root) %{_libdir}/%{name}/program/sfax
%attr(755,root,root) %{_libdir}/%{name}/program/simpress
#%attr(755,root,root) %{_libdir}/%{name}/program/slabel
#%attr(755,root,root) %{_libdir}/%{name}/program/sletter
#%attr(755,root,root) %{_libdir}/%{name}/program/smaster
%attr(755,root,root) %{_libdir}/%{name}/program/smath
#%attr(755,root,root) %{_libdir}/%{name}/program/smemo
%attr(755,root,root) %{_libdir}/%{name}/program/soffice
%attr(755,root,root) %{_libdir}/%{name}/program/spadmin
#%attr(755,root,root) %{_libdir}/%{name}/program/svcard
#%attr(755,root,root) %{_libdir}/%{name}/program/sweb
%attr(755,root,root) %{_libdir}/%{name}/program/swriter
%attr(755,root,root) %{_libdir}/%{name}/program/open-url
%if %{with mozilla}
%attr(755,root,root) %{_libdir}/%{name}/program/nsplugin
%endif
%attr(755,root,root) %{_libdir}/%{name}/program/gengal
%attr(755,root,root) %{_libdir}/%{name}/program/configimport
%attr(755,root,root) %{_libdir}/%{name}/program/sbase
%attr(755,root,root) %{_libdir}/%{name}/program/senddoc
%attr(755,root,root) %{_libdir}/%{name}/program/setofficelang
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg
%attr(755,root,root) %{_libdir}/%{name}/program/uri-encode
%attr(755,root,root) %{_libdir}/%{name}/program/viewdoc
%attr(755,root,root) %{_libdir}/%{name}/program/*.py
# exclusive arch x86_64 ?
#%attr(755,root,root) %{_libdir}/%{name}/program/pyunorc-update64
%{_libdir}/%{name}/program/versionrc

%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/program/javaldx
%attr(755,root,root) %{_libdir}/%{name}/program/java-set-classpath
%{_libdir}/%{name}/program/jvmfwk3rc
%{_libdir}/%{name}/program/JREProperties.class
%dir %{_libdir}/%{name}/help
%{_libdir}/%{name}/help/en
%{_libdir}/%{name}/help/main_transform.xsl
%{_libdir}/%{name}/program/hid.lst
%{_libdir}/%{name}/program/classes
%{_libdir}/%{name}/share/Scripts/beanshell
%{_libdir}/%{name}/share/Scripts/javascript
%{_libdir}/%{name}/share/Scripts/java
%{_libdir}/%{name}/share/xslt
%{_libdir}/%{name}/share/config/javavendors.xml
%endif

%dir %{_libdir}/%{name}/share/Scripts
%{_libdir}/%{name}/share/Scripts/python

%{_datadir}/mime/packages/openoffice.xml
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/o*.1*

# en-US
%{_libdir}/%{name}/presets/config/*_en-US.so*
%{_libdir}/%{name}/share/autocorr/acor_*.dat
%{_libdir}/%{name}/share/autotext/en-US
%{_libdir}/%{name}/share/registry/res/en-US
%{_libdir}/%{name}/share/template/en-US
%dir %{_libdir}/%{name}/share/template/wizard/letter/en-US
%{_libdir}/%{name}/share/template/wizard/letter/en-US/*.ott
%{_libdir}/%{name}/share/wordbook/en-US
%{_libdir}/%{name}/program/resource/*en-US.res
%{_libdir}/%{name}/licenses/LICENSE_en-US
%{_libdir}/%{name}/licenses/LICENSE_en-US.html
%{_libdir}/%{name}/readmes/README_en-US
%{_libdir}/%{name}/readmes/README_en-US.html

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/program
#%dir %{_libdir}/%{name}/program/filter
#%attr(755,root,root) %{_libdir}/%{name}/program/filter/*.so

%attr(755,root,root) %{_libdir}/%{name}/program/acceptor.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/basprov680*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/behelper.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/bridgefac.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/cairocanvas.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/canvasfactory.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/cmdmail.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/configmgr2.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/connector.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/deployment680*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/deploymentgui680*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/desktopbe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/dlgprov680*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/fpicker.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/fps_office.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/fsstorage.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/hatchwindowfactory.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/i18npool.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/i18nsearch.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/implreg.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/introspection.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/invocadapt.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/invocation.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/ldapbe2.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libabp680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libadabas2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libagg680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libanalysis680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libanimcore.so
%attr(755,root,root) %{_libdir}/%{name}/program/libavmedia680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libavmediagst.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasctl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasegfx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_frm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_lng680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_migratefilter680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_ofa680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_sc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_sch680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_sd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_sm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_svx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_sw680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_wrapper680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_xo680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbib680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbindet680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcached1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcalc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcanvastools680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcollator_data.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcommuni680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcomphelp4gcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcppcanvas680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libctl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdate680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdba680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbacfg680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbase680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbaxml680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbp680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbpool2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbtools680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbu680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdict_ja.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdict_zh.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdtransX11680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libeggtray680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libegi680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libembobj.so
%attr(755,root,root) %{_libdir}/%{name}/program/libemboleobj.so
%attr(755,root,root) %{_libdir}/%{name}/program/libeme680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libemp680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libepb680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libepg680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libepp680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libeps680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libept680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libera680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libeti680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libevoab1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libevoab2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libevtatt.so
%attr(755,root,root) %{_libdir}/%{name}/program/libexlink680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libexp680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfile680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfileacc.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfilterconfig1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libflash680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libflat680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfrm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwe680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwi680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwk680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libgcc3_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libgo680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libhunspell.so
%attr(755,root,root) %{_libdir}/%{name}/program/libhwp.so
%attr(755,root,root) %{_libdir}/%{name}/program/libhyphen680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libi18nisolang1gcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libi18nregexpgcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libi18nutilgcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libicd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libicg680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libidx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libime680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libindex_data.so
%attr(755,root,root) %{_libdir}/%{name}/program/libipb680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libipd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libips680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libipt680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libipx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libira680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libitg680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libiti680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libj680li_g.so
%attr(755,root,root) %{_libdir}/%{name}/program/libkab1.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblegacy_binfilters680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblng680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblnth680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_en.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_es.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_euro.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_others.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblwpft680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmcnttype.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmdb680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmdbimpl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmysql2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libnpsoplugin.so
%attr(755,root,root) %{_libdir}/%{name}/program/libodbc2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libodbcbase2.so
%attr(755,root,root) %{_libdir}/%{name}/program/liboffacc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpackage2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpcr680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpdffilter680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpk680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libplacewareli.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpreload680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libprotocolhandler680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpsp680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpyuno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libqstart_gtk680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/librecentfile.so
%attr(755,root,root) %{_libdir}/%{name}/program/libres680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsb680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsch680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libschd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscn680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscriptframe.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdbc2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdbt680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsfx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsimplecm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsmd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libso680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsot680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspa680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspell680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspl_unx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsrtrs1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsts680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvgfilter680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvt680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsw680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextconv_dict.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextconversiondlgs680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtfu680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtk680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtvhlp1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucb1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucbhelper3gcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpchelp1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpdav1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpfile1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpftp1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucphier1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucppkg1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libunoxml680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libupdchk680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/liburp_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libutl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libuui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvcl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_gen680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvos3gcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwpft680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxcr680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlfa680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlfd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlsecurity.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxo680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxof680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsec_fw.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsec_xmlsec.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsltdlg680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsltfilter680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxstor.so
%attr(755,root,root) %{_libdir}/%{name}/program/localebe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/migrationoo2.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/namingservice.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/nestedreg.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/passwordcontainer.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/productregistration.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/proxyfac.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/pythonloader.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/pyuno.so
%attr(755,root,root) %{_libdir}/%{name}/program/reflection.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/regtypeprov.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/remotebridge.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/sax.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/security.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/servicemgr.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/shlibloader.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/simplereg.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/slideshow.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/streams.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/svtmisc.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/sysmgr1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/syssh.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/textinstream.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/textoutstream.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/typeconverter.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/typemgr.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/ucpexpand1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/ucptdoc1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/uriproc.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/uuresolver.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/vbaevents680*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/vclcanvas.uno.so

# versioned libraries and their symlinks
%attr(755,root,root) %{_libdir}/%{name}/program/*.so.*
%attr(755,root,root) %{_libdir}/%{name}/program/libcppu.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcppuhelper3gcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcppuhelpergcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libreg.so
%attr(755,root,root) %{_libdir}/%{name}/program/librmcxt.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsal.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsalhelper3gcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsalhelpergcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libstore.so
%attr(755,root,root) %{_libdir}/%{name}/program/libuno_cppu.so
%attr(755,root,root) %{_libdir}/%{name}/program/libuno_cppuhelpergcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libuno_sal.so
%attr(755,root,root) %{_libdir}/%{name}/program/libuno_salhelpergcc3.so

%{_fontsdir}/TTF/*.ttf

%if %{with kde}
%files libs-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/kde-open-url
%attr(755,root,root) %{_libdir}/%{name}/program/kdebe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/kdefilepicker
%attr(755,root,root) %{_libdir}/%{name}/program/libfps_kde.so
%attr(755,root,root) %{_libdir}/%{name}/program/libkabdrv1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_kde*.so
#%dir %{_libdir}/%{name}/program/resource.kde
%endif

%files libs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/fps_gnome.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/gconfbe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/gnome-open-url
%attr(755,root,root) %{_libdir}/%{name}/program/gnome-open-url.bin
%attr(755,root,root) %{_libdir}/%{name}/program/gnome-set-default-application
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_gtk*.so
%attr(755,root,root) %{_libdir}/%{name}/program/ucpgvfs1.uno.so
#%dir %{_libdir}/%{name}/program/resource.gnome

%files i18n-af -f af.lang
%defattr(644,root,root,755)

%files i18n-ar -f ar.lang
%defattr(644,root,root,755)

%files i18n-as_IN -f as-IN.lang
%defattr(644,root,root,755)

%files i18n-be_BY -f be-BY.lang
%defattr(644,root,root,755)

%files i18n-bg -f bg.lang
%defattr(644,root,root,755)

%files i18n-bn -f bn.lang
%defattr(644,root,root,755)

%files i18n-bn_BD -f bn-BD.lang
%defattr(644,root,root,755)

%files i18n-bn_IN -f bn-IN.lang
%defattr(644,root,root,755)

%files i18n-br -f br.lang
%defattr(644,root,root,755)

%files i18n-bs -f bs.lang
%defattr(644,root,root,755)

%files i18n-ca -f ca.lang
%defattr(644,root,root,755)

%files i18n-cs -f cs.lang
%defattr(644,root,root,755)

%files i18n-cy -f cy.lang
%defattr(644,root,root,755)

%files i18n-da -f da.lang
%defattr(644,root,root,755)

%files i18n-de -f de.lang
%defattr(644,root,root,755)

%files i18n-el -f el.lang
%defattr(644,root,root,755)

%files i18n-en_GB -f en-GB.lang
%defattr(644,root,root,755)

%files i18n-en_ZA -f en-ZA.lang
%defattr(644,root,root,755)

%files i18n-eo -f eo.lang
%defattr(644,root,root,755)

%files i18n-es -f es.lang
%defattr(644,root,root,755)

%files i18n-et -f et.lang
%defattr(644,root,root,755)

%files i18n-eu -f eu.lang
%defattr(644,root,root,755)

%files i18n-fa -f fa.lang
%defattr(644,root,root,755)

%files i18n-fi -f fi.lang
%defattr(644,root,root,755)

#%files i18n-fo -f fo.lang
#%defattr(644,root,root,755)

%files i18n-fr -f fr.lang
%defattr(644,root,root,755)

%files i18n-ga -f ga.lang
%defattr(644,root,root,755)

%files i18n-gl -f gl.lang
%defattr(644,root,root,755)

%files i18n-gu_IN -f gu-IN.lang
%defattr(644,root,root,755)

%files i18n-he -f he.lang
%defattr(644,root,root,755)

%files i18n-hi_IN -f hi-IN.lang
%defattr(644,root,root,755)

%files i18n-hr -f hr.lang
%defattr(644,root,root,755)

%files i18n-hu -f hu.lang
%defattr(644,root,root,755)

#%files i18n-ia -f ia.lang
#%defattr(644,root,root,755)

#%files i18n-id -f id.lang
#%defattr(644,root,root,755)

%files i18n-it -f it.lang
%defattr(644,root,root,755)

%files i18n-ja -f ja.lang
%defattr(644,root,root,755)

%files i18n-km -f km.lang
%defattr(644,root,root,755)

%files i18n-kn_IN -f kn-IN.lang
%defattr(644,root,root,755)

%files i18n-ko -f ko.lang
%defattr(644,root,root,755)

%files i18n-ku -f ku.lang
%defattr(644,root,root,755)

#%files i18n-la -f la.lang
#%defattr(644,root,root,755)

%files i18n-lo -f lo.lang
%defattr(644,root,root,755)

%files i18n-lt -f lt.lang
%defattr(644,root,root,755)

%files i18n-lv -f lv.lang
%defattr(644,root,root,755)

#%files i18n-med -f med.lang
#%defattr(644,root,root,755)

#%files i18n-mi -f mi.lang
#%defattr(644,root,root,755)

%files i18n-mk -f mk.lang
%defattr(644,root,root,755)

%files i18n-ml_IN -f ml-IN.lang
%defattr(644,root,root,755)

%files i18n-mr_IN -f mr-IN.lang
%defattr(644,root,root,755)

%files i18n-ms -f ms.lang
%defattr(644,root,root,755)

%files i18n-nb -f nb.lang
%defattr(644,root,root,755)

%files i18n-ne -f ne.lang
%defattr(644,root,root,755)

%files i18n-nl -f nl.lang
%defattr(644,root,root,755)

%files i18n-nn -f nn.lang
%defattr(644,root,root,755)

%files i18n-nr -f nr.lang
%defattr(644,root,root,755)

%files i18n-nso -f ns.lang
%defattr(644,root,root,755)

%files i18n-or_IN -f or-IN.lang
%defattr(644,root,root,755)

%files i18n-pa_IN -f pa-IN.lang
%defattr(644,root,root,755)

%files i18n-pl -f pl.lang
%defattr(644,root,root,755)

%files i18n-pt -f pt.lang
%defattr(644,root,root,755)

%files i18n-pt_BR -f pt-BR.lang
%defattr(644,root,root,755)

#%files i18n-ro -f ro.lang
#%defattr(644,root,root,755)

%files i18n-ru -f ru.lang
%defattr(644,root,root,755)

%files i18n-rw -f rw.lang
%defattr(644,root,root,755)

%files i18n-sh -f sh-YU.lang
%defattr(644,root,root,755)

%files i18n-sk -f sk.lang
%defattr(644,root,root,755)

%files i18n-sl -f sl.lang
%defattr(644,root,root,755)

%files i18n-sr -f sr-CS.lang
%defattr(644,root,root,755)

%files i18n-ss -f ss.lang
%defattr(644,root,root,755)

%files i18n-st -f st.lang
%defattr(644,root,root,755)

%files i18n-sv -f sv.lang
%defattr(644,root,root,755)

%files i18n-sw -f sw.lang
%defattr(644,root,root,755)

%files i18n-sw_TZ -f sw-TZ.lang
%defattr(644,root,root,755)

%files i18n-sx -f sx.lang
%defattr(644,root,root,755)

%files i18n-ta_IN -f ta-IN.lang
%defattr(644,root,root,755)

%files i18n-te_IN -f te-IN.lang
%defattr(644,root,root,755)

%files i18n-tg -f tg.lang
%defattr(644,root,root,755)

%files i18n-th -f th.lang
%defattr(644,root,root,755)

%files i18n-ti_ER -f ti-ER.lang
%defattr(644,root,root,755)

%files i18n-tn -f tn.lang
%defattr(644,root,root,755)

%files i18n-tr -f tr.lang
%defattr(644,root,root,755)

%files i18n-ts -f ts.lang
%defattr(644,root,root,755)

%files i18n-uk -f uk.lang
%defattr(644,root,root,755)

%files i18n-ur_IN -f ur-IN.lang
%defattr(644,root,root,755)

%files i18n-ve -f ve.lang
%defattr(644,root,root,755)

%files i18n-vi -f vi.lang
%defattr(644,root,root,755)

%files i18n-xh -f xh.lang
%defattr(644,root,root,755)

%files i18n-zh_CN -f zh-CN.lang
%defattr(644,root,root,755)

%files i18n-zh_TW -f zh-TW.lang
%defattr(644,root,root,755)

%files i18n-zu -f zu.lang
%defattr(644,root,root,755)

%files -n bash-completion-openoffice
%defattr(644,root,root,755)
/etc/bash_completion.d/*
