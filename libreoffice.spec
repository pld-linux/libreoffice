# NOTE:
#	- normal build (athlon) requires about 25 GB of disk space:
#		$BUILD_ROOT	7.0 GB
#		BUILD	       16.2 GB
#		RPMS		1.2 GB
#		SRPMS		0.3 GB
#
#
# TODO:
#   - ON PPC help FILES ARE NOT BUILT DUE TO SOME REASON (is missing java the reason?)
#   - --with mono wants static mono
#	- without system_db will not work (w/ java) as it will use db4.2 which is too old (see r1.650)
#	- LFS support is disabled (no_lfs_hack.patch for xml2cmp crash) because it need LFS-ready STLport
#	- maybe it could be build with gcc-java
#   - adapt help-support.diff to PLD
#	- configure --without-ppds --without afms
#	- fix locale names and other locale related things
#   - can't be just i18n-{be,gu,hi,kn,pa,ta} instead of *-{be_BY,*_IN}?
#   - more system libs todo:
#	- (SYSTEM_HYPH) bcond system_libhnj doesn't work - needs Debian-patched version of libhnj
#	- --with-system-mythes + mythes package (http://lingucomponent.openoffice.org/thesaurus.html)
#   - --with-system-mspack - use libmspack already installed on system
#	- bcond system_xt doesn't work - xt in PLD is too old or broken
#   - package (english) help files into subpackage
#   - if compiled with java-sun, libgcj not compatible:
#     error: libjawt.so(SUNWprivate_1.1)(64bit) is required by installed openoffice.org-core-2.4.1.7-ooh680_m17.6.x86_64, give up
#
#	$ grep SYSTEM ooo-build-ooe-m6/build/ooe-m6/config_office/config.log |grep NO
#
# MAYBE TODO:
#	- drop requirement on nas-devel
#	- 6 user/config/*.so? files shared between -i18n-en and -i18n-sl
#	- add ooglobal symlink and it's ooo-wrapper entry (among calc|draw|impress|math|web|writer)
#

# Conditional build:
%bcond_without	gnomevfs	# GNOME VFS and Evolution 2 support
%bcond_without	java		# without Java support (disables help support)
%bcond_without	kde		# KDE L&F packages
%bcond_with	mono		# enable compilation of mono bindings
%bcond_without	mozilla		# without mozilla components
%bcond_without	i18n		# do not create i18n packages
%bcond_with	ccache		# use ccache to speed up builds
%bcond_with	icecream	# use icecream to speed up builds
%bcond_with	msaccess	# with ms access import pieces

%bcond_without	system_beanshell
%bcond_without	system_db		# without system (i.e. with internal) Berkeley DB
%bcond_with	system_libhnj		# with system ALTLinuxhyph (NFY)
%bcond_without	system_mdbtools		# with system mdbtools
%bcond_without	system_xalan
%bcond_without	system_xerces
%bcond_without	system_xml_apis
%bcond_without	system_hsqldb
%bcond_with	system_agg		# with system agg
%bcond_without	system_hunspell
%bcond_without	system_myspell
%bcond_with	system_xt

# this list is same as java-sun
%ifnarch i586 i686 pentium3 pentium4 athlon %{x8664}
%undefine	with_java
%endif

%if %{without java}
%undefine	with_system_beanshell
%undefine	with_system_xalan
%undefine	with_system_xerces
%undefine	with_system_xml_apis
%undefine	with_system_xt
%undefine	with_system_hsqldb
%endif

%define		upd			300
%define		mws			OOO%{upd}
%define		tag			%(echo %{mws} | tr A-Z a-z)-%{milestone}
%define		milestone	m15
%define		_tag		%(echo %{tag} | tr - _)
%define		_rel		9

Summary:	OpenOffice.org - powerful office suite
Summary(pl.UTF-8):	OpenOffice.org - potężny pakiet biurowy
Name:		openoffice.org
Version:	3.0.1.3
Release:	%{_tag}.%{_rel}
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
# we use git because released tarballs are buggy too often
# git clone git://anongit.freedesktop.org/git/ooo-build/ooo-build
# cd ooo-build
# git checkout -b ooo-build-3-0-1 origin/ooo-build-3-0-1
Source0:	ooo-build-20090727.tar.bz2
# Source0-md5:	3fd9197e22fa801e2c2df408df462a22
Source1:	http://download.go-oo.org/DEV300/ooo-cli-prebuilt-3.0.tar.bz2
# Source1-md5:	8b3979cd7fd99b7e9722fd8f690e69a9
Source2:	http://download.go-oo.org/%{mws}/%{tag}-base.tar.bz2
# Source2-md5:	c2eb3afafe7305be70c46f0bbc82ccff
Source3:	http://download.go-oo.org/%{mws}/%{tag}-calc.tar.bz2
# Source3-md5:	78bf10d9a15f5cb801999dc6be0144d1
Source4:	http://download.go-oo.org/%{mws}/%{tag}-l10n.tar.bz2
# Source4-md5:	02b20bd978e342de45ef84d3232e3f94
Source5:	http://download.go-oo.org/%{mws}/%{tag}-ure.tar.bz2
# Source5-md5:	65565feb49307361209b610249e45dc7
Source6:	http://download.go-oo.org/%{mws}/%{tag}-writer.tar.bz2
# Source6-md5:	04f68dfb9a34b5c0766a65e6ff48b841
Source7:	http://download.go-oo.org/%{mws}/%{tag}-impress.tar.bz2
# Source7-md5:	00a1646d1913989bc432073f8954c92b
Source8:	http://download.go-oo.org/%{mws}/%{tag}-artwork.tar.bz2
# Source8-md5:	cc928a9c348121d82fb80c43dbf3901f
Source9:	http://download.go-oo.org/%{mws}/%{tag}-filters.tar.bz2
# Source9-md5:	729550f40870eeaa94b2ae493e038848
Source10:	http://download.go-oo.org/%{mws}/%{tag}-testing.tar.bz2
# Source10-md5:	406087778a00ad68cc4e94aa5a677086
Source11:	http://download.go-oo.org/%{mws}/%{tag}-bootstrap.tar.bz2
# Source11-md5:	6d680f8bfe532bb8833a0e6bb6d19cc9
Source12:	http://download.go-oo.org/%{mws}/%{tag}-libs_gui.tar.bz2
# Source12-md5:	e23ba759d82041c665a24ea4ef3d8b9b
Source13:	http://download.go-oo.org/%{mws}/%{tag}-libs_core.tar.bz2
# Source13-md5:	bdd173a94ece251126ae0e4120cbb661
Source14:	http://download.go-oo.org/%{mws}/%{tag}-libs_extern.tar.bz2
# Source14-md5:	2582ddfe11a64cca9190a046e9a159df
Source15:	http://download.go-oo.org/%{mws}/%{tag}-components.tar.bz2
# Source15-md5:	d29035a293298c6e69d5d8a3acbab75f
Source16:	http://download.go-oo.org/%{mws}/%{tag}-libs_extern_sys.tar.bz2
# Source16-md5:	8016fc38320ebd4ab7720df7eb4e4df0
Source17:	http://download.go-oo.org/%{mws}/%{tag}-extensions.tar.bz2
# Source17-md5:	f307de1b92d488484a53fa8ce45a7b3b
Source18:	http://download.go-oo.org/%{mws}/%{tag}-sdk.tar.bz2
# Source18-md5:	f298e95232efdd4182345c095a497799
Source19:	http://download.go-oo.org/%{mws}/%{tag}-postprocess.tar.bz2
# Source19-md5:	73b6c538639310c2ad242d6cb5045c52
Source50:	http://download.go-oo.org//DEV300/scsolver.2008-10-30.tar.bz2
# Source50-md5:	04181e5ef82973eb349d3122a19d2274
Source51:	http://download.go-oo.org/SRC/biblio.tar.bz2
# Source51-md5:	1948e39a68f12bfa0b7eb309c14d940c
Source52:	http://download.go-oo.org/SRC/extras-3.tar.bz2
# Source52-md5:	36f323a55ee83e9dc968e1b92569b62a
Source53:	%{name}-splash.bmp
Source54:	%{name}-about.bmp
# patches applied in prep section
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-gcc-Wextra.patch
# patch50/51 need review
Patch50:	%{name}-mdbtools_fix.diff
Patch51:	%{name}-nodictinst.patch
# patches applied by ooo-patching-system
Patch100:	%{name}-lang.patch
#Patch101:	%{name}-java6.patch
Patch103:	%{name}-missing-includes.diff
Patch104:	%{name}-xulrunner.patch
# patches 1000+ need review
Patch1001:	%{name}-64bit-inline.diff
Patch1002:	%{name}-build-pld-splash.diff
Patch1003:	%{name}-portaudio_v19.diff
Patch1004:	%{name}-agg25.patch
Patch1005:	%{name}-nsplugin-path.diff
Patch1006:	%{name}-perl-nodiag.patch
Patch1007:	%{name}-gcc42-swregion.diff

Patch2001:	%{name}-kde3support.patch
Patch2002:	%{name}-gcc44.patch
Patch2003:	%{name}-hotfix-glibc210.patch
Patch2004:	%{name}-hotfix-xulrunner.patch
URL:		http://www.openoffice.org/
BuildRequires:	/usr/bin/getopt
BuildRequires:	GConf2-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
%{?with_system_agg:BuildRequires:	agg-devel}
BuildRequires:	atk-devel >= 1:1.9.0
BuildRequires:	autoconf >= 2.51
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison >= 1.875-4
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	cairo-devel >= 1.2.0
%{?with_ccache:BuildRequires:	ccache}
BuildRequires:	cups-devel
BuildRequires:	curl-devel >= 7.9.8
%{?with_system_db:BuildRequires:	db-cxx-devel}
%{?with_system_db:BuildRequires:	db-devel}
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	glib2-devel >= 2.13.5
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel}
BuildRequires:	gperf
BuildRequires:	gstreamer-devel >= 0.10.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	gtk+2-devel >= 2:2.10
%{?with_system_hsqldb:BuildRequires:	hsqldb >= 1.8.0.9}
%{?with_system_hunspell:BuildRequires:	hunspell-devel >=1.2.2}
%{?with_icecream:BuildRequires:	icecream}
BuildRequires:	icu
%{?with_system_beanshell:BuildRequires:	java-beanshell}
%if %{with kde}
BuildRequires:	kde4-kde3support-devel
BuildConflicts:	kde4-kdelibs-devel
BuildConflicts:	kde4-kdepimlibs-devel
%endif
BuildRequires:	libart_lgpl-devel
BuildRequires:	libbonobo-devel >= 2.0
%{?with_system_libhnj:BuildRequires:	libhnj-devel}
BuildRequires:	libicu-devel >= 3.4
BuildRequires:	libjpeg-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel >= 5:3.2.1
BuildRequires:	libsvg-devel >= 0.1.4
BuildRequires:	libwpd-devel >= 0.8.6
BuildRequires:	libwpg-devel >= 0.1.0
BuildRequires:	libwps-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel
BuildRequires:	libxslt-progs
%{?with_access:%{?with_system_mdbtools:BuildRequires:	mdbtools-devel >= 0.6}}
%{?with_mono:BuildRequires:	mono-csharp >= 1.2.3}
%{?with_mono:BuildRequires:	mono-static >= 1.2.3}
%{?with_system_myspell:BuildRequires:	myspell-devel}
BuildRequires:	nas-devel >= 1.7-1
BuildRequires:	neon-devel
BuildRequires:	nspr-devel >= 1:4.6-0.20041030.3
BuildRequires:	nss-devel >= 1:3.10
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	pango-devel >= 1:1.17.3
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	poppler-devel >= 0.8.0
BuildRequires:	portaudio-devel
BuildRequires:	python >= 2.2
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
BuildRequires:	redland-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	sablotron-devel
BuildRequires:	sane-backends-devel
BuildRequires:	saxon
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	tcsh
BuildRequires:	unixODBC-devel >= 2.2.12-2
BuildRequires:	unzip
BuildRequires:	vigra-devel
%{?with_system_xalan:BuildRequires:	xalan-j}
%{?with_system_xerces:BuildRequires:	xerces-j}
%{?with_system_xml_apis:BuildRequires:	xml-commons}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXtst-devel
%{?with_system_xt:BuildRequires:	xt}
BuildRequires:	zip
BuildRequires:	zlib-devel
%if %{with java}
BuildRequires:	ant
%{?with_system_db:BuildRequires:	db-java >= 4.3}
BuildRequires:	java-sun >= 1.4.0_00
BuildRequires:	java-sun-jre-X11
BuildRequires:	java-sun-tools
%endif
BuildRequires:	xulrunner-devel
BuildConflicts:	xmlsec1-devel
# contains (dlopened) *.so libs
BuildConflicts:	xmlsec1-nss
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-calc = %{epoch}:%{version}-%{release}
Requires:	%{name}-draw = %{epoch}:%{version}-%{release}
Requires:	%{name}-emailmerge = %{epoch}:%{version}-%{release}
Requires:	%{name}-graphicfilter = %{epoch}:%{version}-%{release}
Requires:	%{name}-impress = %{epoch}:%{version}-%{release}
%{?with_java:Requires:	%{name}-javafilter = %{epoch}:%{version}-%{release}}
Requires:	%{name}-math = %{epoch}:%{version}-%{release}
Requires:	%{name}-pyuno = %{epoch}:%{version}-%{release}
Requires:	%{name}-testtools = %{epoch}:%{version}-%{release}
Requires:	%{name}-web = %{epoch}:%{version}-%{release}
Requires:	%{name}-writer = %{epoch}:%{version}-%{release}
Requires:	%{name}-xsltfilter = %{epoch}:%{version}-%{release}
ExclusiveArch:	%{ix86} %{x8664} ppc sparc sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing -O2

# No ELF objects there to strip/chrpath, skips processing:
# - share/ - 17000 files of 415M
# - help/ - 6500 files of 1.4G
# - program/resource/ - 5610 files of 216M
%define		_noautostrip	.*\\(%{_datadir}\\|%{_libdir}/%{name}/basis*/program/resource\\)/.*
%define		_noautochrpath	.*\\(%{_datadir}\\|%{_libdir}/%{name}/basis*/program/resource\\)/.*

%define		ooobasisdir	%{_libdir}/%{name}/basis3.0

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

%description -l pl.UTF-8
OpenOffice.org jest projektem open-source sponsorowanym przez Sun
Microsystems i przechowywanym przez CollabNet. W październiku 2000
roku Sun udostępnił kod źródłowy popularnego pakietu biurowego
StarOfficeTM na zasadach licencji open-source. Głównym celem
OpenOffice.org jest stworzenie sieciowego pakietu biurowego następnej
generacji, wykorzystując open-source'owe metody pracy.

Do zalet OpenOffice.org można zaliczyć:
 - dostępny cały czas kod źródłowy,
 - kontrola CVS,
 - infrastruktura służąca do komunikowania się w ramach projektu.

%package libs-kde
Summary:	OpenOffice.org KDE Interface
Summary(pl.UTF-8):	Interfejs KDE dla OpenOffice.org
Group:		X11/Libraries
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en-kde
Obsoletes:	openoffice-libs-kde

%description libs-kde
OpenOffice.org productivity suite - KDE Interface.

%description libs-kde -l pl.UTF-8
Pakiet biurowy OpenOffice.org - Interfejs KDE.

%package libs-gtk
Summary:	OpenOffice.org GTK+ Interface
Summary(pl.UTF-8):	Interfejs GTK+ dla OpenOffice.org
Group:		X11/Libraries
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en-gtk
Obsoletes:	openoffice-libs-gtk

%description libs-gtk
OpenOffice.org productivity suite - GTK+ Interface.

%description libs-gtk -l pl.UTF-8
Pakiet biurowy OpenOffice.org - Interfejs GTK+.

%package core
Summary:	Core modules for OpenOffice.org
Summary(pl.UTF-8):	Podstawowe moduły dla OpenOffice.org
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires:	%{name}-ure = %{epoch}:%{version}-%{release}
# libcups.so.2 is dlopened (in cupsmgr.cxx); maybe Suggests instead?
Requires:	cups-lib
Requires:	fonts-TTF-OpenSymbol
%{?with_system_hsqldb:Requires:	hsqldb >= 1.8.0}
%{?with_system_beanshell:Requires:	java-beanshell}
Requires:	libstdc++ >= 5:3.2.1
Requires:	mktemp
Requires:	saxon
Requires:	sed
%{?with_system_xalan:Requires:	xalan-j}
%{?with_system_xerces:Requires:	xerces-j}
%{?with_system_xml_apis:Requires:	xml-commons}
%{?with_system_xt:Requires:	xt}
#Suggests:	chkfontpath
Obsoletes:	oooqs
Obsoletes:	openoffice
Obsoletes:	openoffice-i18n-fo
Obsoletes:	openoffice-i18n-fo-gtk
Obsoletes:	openoffice-i18n-ia
Obsoletes:	openoffice-i18n-ia-gtk
Obsoletes:	openoffice-i18n-id
Obsoletes:	openoffice-i18n-id-gtk
Obsoletes:	openoffice-i18n-la
Obsoletes:	openoffice-i18n-la-gtk
Obsoletes:	openoffice-i18n-med
Obsoletes:	openoffice-i18n-med-gtk
Obsoletes:	openoffice-i18n-mi
Obsoletes:	openoffice-i18n-mi-gtk
Obsoletes:	openoffice-i18n-ro
Obsoletes:	openoffice-i18n-ro-gtk
Obsoletes:	openoffice-libs
Obsoletes:	openoffice.org-dirs
Obsoletes:	openoffice.org-i18n-fo
Obsoletes:	openoffice.org-i18n-fo-gtk
Obsoletes:	openoffice.org-i18n-fo-kde
Obsoletes:	openoffice.org-i18n-ia
Obsoletes:	openoffice.org-i18n-ia-gtk
Obsoletes:	openoffice.org-i18n-ia-kde
Obsoletes:	openoffice.org-i18n-id
Obsoletes:	openoffice.org-i18n-id-gtk
Obsoletes:	openoffice.org-i18n-id-kde
Obsoletes:	openoffice.org-i18n-la
Obsoletes:	openoffice.org-i18n-la-gtk
Obsoletes:	openoffice.org-i18n-la-kde
Obsoletes:	openoffice.org-i18n-med
Obsoletes:	openoffice.org-i18n-med-gtk
Obsoletes:	openoffice.org-i18n-med-kde
Obsoletes:	openoffice.org-i18n-mi
Obsoletes:	openoffice.org-i18n-mi-gtk
Obsoletes:	openoffice.org-i18n-mi-kde
Obsoletes:	openoffice.org-i18n-ro
Obsoletes:	openoffice.org-i18n-ro-gtk
Obsoletes:	openoffice.org-i18n-ro-kde
Obsoletes:	openoffice.org-i18n-sx
Obsoletes:	openoffice.org-libs < 1:2.1.0-0.m6.0.11

%description core
Core libraries and support files for OpenOffice.org.

%description core -l pl.UTF-8
Podstawowe moduły dla OpenOffice.org.

%package pyuno
Summary:	Python bindings for OpenOffice.org
Summary(pl.UTF-8):	Wiązania Pythona dla OpenOffice.org
Group:		Libraries
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	python

%description pyuno
Cool Python bindings for the OpenOffice.org UNO component model.
Allows scripts both external to OpenOffice.org and within the internal
OpenOffice.org scripting module to be written in Python.

%description pyuno -l pl.UTF-8
Wiązania Pythona dla modelu komponentów UNO OpenOffice.org. Pozwala na
oskryptowanie zarówno na zewnątrz OpenOffice.org, jak i na używanie
skryptów w Pythonie w wewnętrznym module skryptów OpenOffice.org.

%package base
Summary:	Database frontend for OpenOffice.org
Summary(pl.UTF-8):	Frontend do baz danych dla OpenOffice.org
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description base
GUI database frontend for OpenOffice.org. Allows creation and
management of databases through a GUI.

%description base -l pl.UTF-8
Graficzny frontend do baz danych dla OpenOffice.org. Pozwala na
tworzenie i zarządzanie bazami poprzez graficzny interfejs
użytkownika.

%package web
Summary:	Web module for OpenOffice.org
Summary(pl.UTF-8):	Moduł Web dla OpenOffice.org
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	%{name}-writer = %{epoch}:%{version}-%{release}

%description web
Web publishing application of OpenOffice.org.

%description web -l pl.UTF-8
Aplikacja do tworzenia stron WWW z OpenOffice.org.

%package writer
Summary:	Writer module for OpenOffice.org
Summary(pl.UTF-8):	Moduł Writer dla OpenOffice.org
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description writer
Wordprocessor application of OpenOffice.org.

%description writer -l pl.UTF-8
Procesor tekstu z OpenOffice.org.

%package emailmerge
Summary:	email mail merge component for OpenOffice.org
Summary(pl.UTF-8):	Kompolent email mail merge dla OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-pyuno = %{epoch}:%{version}-%{release}
Requires:	%{name}-writer = %{epoch}:%{version}-%{release}

%description emailmerge
Enables OpenOffice.org Writer module to enable mail merge to email.

%description emailmerge -l pl.UTF-8
Komponent umożliwiający modułowi Writer włączanie poczty do poczty
elektronicznej.

%package calc
Summary:	Calc module for OpenOffice.org
Summary(pl.UTF-8):	Moduł Calc dla OpenOffice.org
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description calc
Spreadsheet application of OpenOffice.org.

%description calc -l pl.UTF-8
Arkusz kalkulacyjny z OpenOffice.org.

%package draw
Summary:	Draw module for OpenOffice.org
Summary(pl.UTF-8):	Moduł Draw dla OpenOffice.org
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description draw
Drawing application of OpenOffice.org.

%description draw -l pl.UTF-8
Aplikacja rysunkowa z OpenOffice.org.

%package impress
Summary:	Impress module for OpenOffice.org
Summary(pl.UTF-8):	Moduł Impress dla OpenOffice.org
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description impress
Presentation application of OpenOffice.org.

%description impress -l pl.UTF-8
Aplikacja do tworzenia prezentacji z OpenOffice.org.

%package math
Summary:	Math module for OpenOffice.org
Summary(pl.UTF-8):	Moduł Math dla OpenOffice.org
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description math
Math editor of OpenOffice.org.

%description math -l pl.UTF-8
Edytor równań matematycznych z OpenOffice.org.

%package graphicfilter
Summary:	Extra graphicfilter module for OpenOffice.org
Summary(pl.UTF-8):	Dodatkowy moduł graphicfilter dla OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description graphicfilter
Graphicfilter module for OpenOffice.org, provides additional SVG and
Flash export filters.

%description graphicfilter -l pl.UTF-8
Moduł graphicfilter dla OpenOffice.org, udostępnia dodatkowe filtry
eksportu SVG i Flash.

%package xsltfilter
Summary:	Extra xsltfilter module for OpenOffice.org
Summary(pl.UTF-8):	Dodatkowy moduł xsltfilter dla OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description xsltfilter
xsltfilter module for OpenOffice.org, provides additional docbook and
xhtml export transforms. Install this to enable docbook export.

%description xsltfilter -l pl.UTF-8
Moduł xsltfilter dla OpenOffice.org, udostępnia dodatkowe
przekształcenia wyjściowe dla formatów docbook i xhtml. Jest potrzebny
do eksportu do docbooka.

%package javafilter
Summary:	Extra javafilter module for OpenOffice.org
Summary(pl.UTF-8):	Dodatkowy moduł javafilter dla OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description javafilter
javafilter module for OpenOffice.org, provides additional aportisdoc,
Pocket Excel and Pocket Word import filters.

%description javafilter -l pl.UTF-8
Moduł javafilter dla OpenOffice.org, udostępnia dodatkowe filtry
importu aportisdoc, Pocket Excel i Pocket Word.

%package testtools
Summary:	testtools for OpenOffice.org
Summary(pl.UTF-8):	Narzędzia testowe dla OpenOffice.org
Group:		Development/Libraries
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description testtools
QA tools for OpenOffice.org, enables automated testing.

%description testtools -l pl.UTF-8
Narzędzia QA dla OpenOffice.org, pozwalają na automatyczne testowanie.

# FIXME
%package ure
Summary:	UNO Runtime Environment
Group:		Libraries

%description ure
UNO is the component model of OpenOffice.org. UNO offers
interoperability between programming languages, other components
models and hardware architectures, either in process or over process
boundaries, in the Intranet as well as in the Internet. UNO components
may be implemented in and accessed from any programming language for
which a UNO implementation (AKA language binding) and an appropriate
bridge or adapter exists.

%package -n browser-plugin-%{name}
Summary:	OpenOffice.org plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczka OpenOffice.org dla przeglądarek WWW
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})

%description -n browser-plugin-%{name}
OpenOffice.org plugin for WWW browsers.

This plugin allows browsers to display OOo documents inline.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka OpenOffice.org dla przeglądarek WWW.

Ta wtyczka umożliwia wyświetlanie dokumentów OOo wewnątrz stron.

%package i18n-af
Summary:	OpenOffice.org - interface in Afrikaans language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku afrykanerskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-af
Obsoletes:	openoffice-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af-kde

%description i18n-af
This package provides resources containing menus and dialogs in
Afrikaans language.

%description i18n-af -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
afrykanerskim.

%package i18n-ar
Summary:	OpenOffice.org - interface in Arabic language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku arabskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ar
Obsoletes:	openoffice-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar-kde

%description i18n-ar
This package provides resources containing menus and dialogs in Arabic
language.

%description i18n-ar -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
arabskim.

%package i18n-as_IN
Summary:	OpenOffice.org - interface in Assamese language for India
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku asamskim dla Indii
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-as_IN
This package provides resources containing menus and dialogs in
Assamese language for India.

%description i18n-as_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
asamskim dla Indii.

%package i18n-be_BY
Summary:	OpenOffice.org - interface in Belarusian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku białoruskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-be_BY
This package provides resources containing menus and dialogs in
Belarusian language.

%description i18n-be_BY -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
białoruskim.

%package i18n-bg
Summary:	OpenOffice.org - interface in Bulgarian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku bułgarskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-bg
Obsoletes:	openoffice-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg-kde

%description i18n-bg
This package provides resources containing menus and dialogs in
Bulgarian language.

%description i18n-bg -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bułgarskim.

%package i18n-bn
Summary:	OpenOffice.org - interface in Bangla language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku bengalskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-bn
This package provides resources containing menus and dialogs in Bangla
language.

%description i18n-bn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bengalskim.

%package i18n-bn_BD
Summary:	OpenOffice.org - interface in Bangla language for Bangladesh
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku bengalskim dla Bangladeszu
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-bn_BD
This package provides resources containing menus and dialogs in Bangla
language for Bangladesh.

%description i18n-bn_BD -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bengalskim dla Bangladeszu.

%package i18n-bn_IN
Summary:	OpenOffice.org - interface in Bangla language for India
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku bengalskim dla Indii
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-bn_IN
This package provides resources containing menus and dialogs in Bangla
language for India.

%description i18n-bn_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bengalskim dla Indii.

%package i18n-br
Summary:	OpenOffice.org - interface in Breton language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku bretońskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-br
This package provides resources containing menus and dialogs in Breton
language.

%description i18n-br -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bretońskim.

%package i18n-bs
Summary:	OpenOffice.org - interface in Bosnian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku bośniackim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-bs
This package provides resources containing menus and dialogs in
Bosnian language.

%description i18n-bs -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bośniackim.

# FIXME
%package i18n-by
Summary:	OpenOffice.org - interface in ... language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku ...
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-by
This package provides resources containing menus and dialogs in
... language.

%description i18n-by -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
...

%package i18n-ca
Summary:	OpenOffice.org - interface in Catalan language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku katalońskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ca
Obsoletes:	openoffice-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca-kde

%description i18n-ca
This package provides resources containing menus and dialogs in
Catalan language.

%description i18n-ca -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
katalońskim.

%package i18n-cs
Summary:	OpenOffice.org - interface in Czech language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku czeskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-cs
Obsoletes:	openoffice-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs-kde

%description i18n-cs
This package provides resources containing menus and dialogs in Czech
language.

%description i18n-cs -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
czeskim.

%package i18n-cy
Summary:	OpenOffice.org - interface in Cymraeg language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku walijskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-cy
Obsoletes:	openoffice-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy-kde

%description i18n-cy
This package provides resources containing menus and dialogs in
Cymraeg language.

%description i18n-cy -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
walijskim.

%package i18n-da
Summary:	OpenOffice.org - interface in Danish language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku duńskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-da
Obsoletes:	openoffice-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da-kde

%description i18n-da
This package provides resources containing menus and dialogs in Danish
language.

%description i18n-da -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
duńskim.

%package i18n-de
Summary:	OpenOffice.org - interface in German language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku niemieckim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-de
Obsoletes:	openoffice-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de-kde

%description i18n-de
This package provides resources containing menus and dialogs in German
language.

%description i18n-de -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
niemieckim.

%package i18n-dz
Summary:	OpenOffice.org - interface in Dzongkha language
Summary(pl.UTF-8):	Openoffice.org - interfejs w języku dżongkha
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-dz
This package provides resources containing menus and dialogs in
Dzongkha language.

%description i18n-dz -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
dżongkha.

%package i18n-el
Summary:	OpenOffice.org - interface in Greek language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku greckim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-el
Obsoletes:	openoffice-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el-kde

%description i18n-el
This package provides resources containing menus and dialogs in Greek
language.

%description i18n-el -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
greckim.

%package i18n-en_GB
Summary:	OpenOffice.org - interface in English language for United Kingdom
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku anglieskim dla Wielkiej Brytanii
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-en_GB
This package provides resources containing menus and dialogs in
English language for United Kingdom.

%description i18n-en_GB -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
anglieskim dla Wielkiej Brytanii.

%package i18n-en_ZA
Summary:	OpenOffice.org - interface in English language for South Africa
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku anglieskim dla Południowej Afryki
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-en_ZA
This package provides resources containing menus and dialogs in
English language for South Africa.

%description i18n-en_ZA -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
anglieskim dla Południowej Afryki.

%package i18n-eo
Summary:	OpenOffice.org - interface in Esperanto language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku esperanto
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-eo
This package provides resources containing menus and dialogs in
Esperanto language.

%description i18n-eo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
esperanto.

%package i18n-es
Summary:	OpenOffice.org - interface in Spanish language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku hiszpańskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-es
Obsoletes:	openoffice-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es-kde

%description i18n-es
This package provides resources containing menus and dialogs in
Spanish language.

%description i18n-es -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
hiszpańskim.

%package i18n-et
Summary:	OpenOffice.org - interface in Estonian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku estońskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-et
Obsoletes:	openoffice-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et-kde

%description i18n-et
This package provides resources containing menus and dialogs in
Estonian language.

%description i18n-et -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
estońskim.

%package i18n-eu
Summary:	OpenOffice.org - interface in Basque (Euskara) language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku baskijskim (euskera)
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-eu
Obsoletes:	openoffice-i18n-eu-gtk
Obsoletes:	openoffice-i18n-eu-kde

%description i18n-eu
This package provides resources containing menus and dialogs in Basque
(Euskara) language.

%description i18n-eu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
baskijskim (euskera).

%package i18n-fa
Summary:	OpenOffice.org - interface in Persian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku perskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fa
Obsoletes:	openoffice-i18n-fa-gtk
Obsoletes:	openoffice-i18n-fa-kde

%description i18n-fa
This package provides resources containing menus and dialogs in
Persian language.

%description i18n-eu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
perskim.

%package i18n-fi
Summary:	OpenOffice.org - interface in Finnish language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku fińskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fi
Obsoletes:	openoffice-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi-kde

%description i18n-fi
This package provides resources containing menus and dialogs in
Finnish language.

%description i18n-fi -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
fińskim.

%package i18n-fr
Summary:	OpenOffice.org - interface in French language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku francuskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fr
Obsoletes:	openoffice-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr-kde

%description i18n-fr
This package provides resources containing menus and dialogs in French
language.

%description i18n-fr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
francuskim.

%package i18n-ga
Summary:	OpenOffice.org - interface in Irish language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku irlandzkim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ga
Obsoletes:	openoffice-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga-kde

%description i18n-ga
This package provides resources containing menus and dialogs in Irish
language.

%description i18n-ga -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
irlandzkim.

%package i18n-gd
Summary:	OpenOffice.org - interface in Scottish Gaelic language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku gaelickim szkockim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-gd
This package provides resources containing menus and dialogs in
Scottish Gaelic language.

%description i18n-gd -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gaelickim szkockim.

%package i18n-gl
Summary:	OpenOffice.org - interface in Galician language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku galicyjskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-gl
Obsoletes:	openoffice-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl-kde

%description i18n-gl
This package provides resources containing menus and dialogs in
Galician language.

%description i18n-gl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
galicyjskim.

%package i18n-gu_IN
Summary:	OpenOffice.org - interface in Gujarati language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku gudźarati
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-gu_IN
This package provides resources containing menus and dialogs in
Gujarati language.

%description i18n-gu_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gudźarati.

%package i18n-gu
Summary:	OpenOffice.org - interface in Gujarati language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku gudźarati
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-gu
This package provides resources containing menus and dialogs in
Gujarati language.

%description i18n-gu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gudźarati.

%package i18n-he
Summary:	OpenOffice.org - interface in Hebrew language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku hebrajskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-he
Obsoletes:	openoffice-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he-kde

%description i18n-he
This package provides resources containing menus and dialogs in Hebrew
language.

%description i18n-he -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
hebrajskim.

%package i18n-hi_IN
Summary:	OpenOffice.org - interface in Hindi language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku hindi
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hi
Obsoletes:	openoffice-i18n-hi-gtk
Obsoletes:	openoffice.org-i18n-hi-gtk
Obsoletes:	openoffice.org-i18n-hi-kde

%description i18n-hi_IN
This package provides resources containing menus and dialogs in Hindi
language.

%description i18n-hi_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
hindi.

%package i18n-hr
Summary:	OpenOffice.org - interface in Croatian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku chorwackim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hr
Obsoletes:	openoffice-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr-kde

%description i18n-hr
This package provides resources containing menus and dialogs in
Croatian language.

%description i18n-hr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
chorwackim.

%package i18n-hu
Summary:	OpenOffice.org - interface in Hungarian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku węgierskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hu
Obsoletes:	openoffice-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu-kde

%description i18n-hu
This package provides resources containing menus and dialogs in
Hungarian language.

%description i18n-hu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
węgierskim.

%package i18n-it
Summary:	OpenOffice.org - interface in Italian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku włoskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-it
ObsoleteS:	openoffice-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it-kde

%description i18n-it
This package provides resources containing menus and dialogs in
Italian language.

%description i18n-it -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
włoskim.

%package i18n-ja
Summary:	OpenOffice.org - interface in Japan language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku japońskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ja
Obsoletes:	openoffice-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja-kde

%description i18n-ja
This package provides resources containing menus and dialogs in Japan
language.

%description i18n-ja -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
japońskim.

%package i18n-ka
Summary:	OpenOffice.org - interface in Georgian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku gruzińskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ka
This package provides resources containing menus and dialogs in
Georgian language.

%description i18n-ka -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gruzińskim.

%package i18n-km
Summary:	OpenOffice.org - interface in Khmer language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku khmerskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-km
This package provides resources containing menus and dialogs in Khmer
language.

%description i18n-km -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
khmerskim.

%package i18n-kn_IN
Summary:	OpenOffice.org - interface in Kannada language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku kannara
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-kn
Obsoletes:	openoffice-i18n-kn-gtk
Obsoletes:	openoffice-i18n-kn-kde

%description i18n-kn_IN
This package provides resources containing menus and dialogs in
Kannada language.

%description i18n-kn_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kannara.

%package i18n-ko
Summary:	OpenOffice.org - interface in Korean language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku koreańskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ko
Obsoletes:	openoffice-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko-kde

%description i18n-ko
This package provides resources containing menus and dialogs in Korean
language.

%description i18n-ko -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
koreańskim.

%package i18n-ku
Summary:	OpenOffice.org - interface in Kurdish language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku kurdyjskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ku
This package provides resources containing menus and dialogs in
Kurdish language.

%description i18n-ku -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kurdyjskim.

%package i18n-lo
Summary:	OpenOffice.org - interface in Lao language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku laotańskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-lo
This package provides resources containing menus and dialogs in Lao
language.

%description i18n-lo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
laotańskim.

%package i18n-lt
Summary:	OpenOffice.org - interface in Lithuanian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku litewskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-lt
Obsoletes:	openoffice-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt-kde

%description i18n-lt
This package provides resources containing menus and dialogs in
Lithuanian language.

%description i18n-lt -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
litewskim.

%package i18n-lv
Summary:	OpenOffice.org - interface in Latvian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku łotewskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-lv
This package provides resources containing menus and dialogs in
Latvian language.

%description i18n-lv -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
łotewskim.

%package i18n-mk
Summary:	OpenOffice.org - interface in Macedonian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku macedońskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-mk
This package provides resources containing menus and dialogs in
Macedonian language.

%description i18n-mk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
macedońskim.

%package i18n-ml_IN
Summary:	OpenOffice.org - interface in Malayalam language for India
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku malajalamskim dla Indii
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ml_IN
This package provides resources containing menus and dialogs in
Malayalam language for India.

%description i18n-ml_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
malajalamskim dla Indii.

%package i18n-mr_IN
Summary:	OpenOffice.org - interface in Marathi language for India
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku marathi dla Indii
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-mr_IN
This package provides resources containing menus and dialogs in
Marathi language for India.

%description i18n-mr_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
marathi dla Indii.

%package i18n-mn
Summary:	OpenOffice.org - interface in Mongolian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku mongolskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-mn
This package provides resources containing menus and dialogs in
Mongolian language.

%description i18n-mn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
mongolskim.

%package i18n-ms
Summary:	OpenOffice.org - interface in Malay language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku malajskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ms
Obsoletes:	openoffice-i18n-ms-gtk
Obsoletes:	openoffice.org-i18n-ms-gtk
Obsoletes:	openoffice.org-i18n-ms-kde

%description i18n-ms
This package provides resources containing menus and dialogs in Malay
language.

%description i18n-ms -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
malajskim.

%package i18n-my
Summary:	OpenOffice.org - interface in Burmese language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku birmańskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-my
This package provides resources containing menus and dialogs in
Burmese language.

%description i18n-my -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
birmańskim.

%package i18n-nb
Summary:	OpenOffice.org - interface in Norwegian Bokmaal language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku norweskim (odmiana Bokmaal)
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nb
Obsoletes:	openoffice-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb-kde

%description i18n-nb
This package provides resources containing menus and dialogs in
Norwegian Bokmaal language.

%description i18n-nb -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
norweskim w odmianie Bokmaal.

%package i18n-ne
Summary:	OpenOffice.org - interface in Nepali language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku nepalskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ne
This package provides resources containing menus and dialogs in Nepali
language.

%description i18n-ne -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
nepalskim.

%package i18n-nl
Summary:	OpenOffice.org - interface in Dutch language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku holenderskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nl
Obsoletes:	openoffice-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl-kde

%description i18n-nl
This package provides resources containing menus and dialogs in Dutch
language.

%description i18n-nl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
holenderskim.

%package i18n-nn
Summary:	OpenOffice.org - interface in Norwegian Nynorsk language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku norweskim (odmiana Nynorsk)
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nn
Obsoletes:	openoffice-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn-kde

%description i18n-nn
This package provides resources containing menus and dialogs in
Norwegian Nynorsk language.

%description i18n-nn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
norweskim w odmianie Nynorsk.

%package i18n-nr
Summary:	OpenOffice.org - interface in South Ndebele language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku ndebele (południowym)
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-nr
This package provides resources containing menus and dialogs in South
Ndebele language.

%description i18n-nr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ndebele (południowym).

%package i18n-nso
Summary:	OpenOffice.org - interface in Northern Sotho language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku ludu Soto
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nso
Obsoletes:	openoffice-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso-kde

%description i18n-nso
This package provides resources containing menus and dialogs in
Northern Sotho language.

%description i18n-nso -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ludu Soto.

%package i18n-oc
Summary:	OpenOffice.org - interface in Occitan language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku oksytańskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-oc
This package provides resources containing menus and dialogs in
Occitan language.

%description i18n-oc -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
oksytańskim.

%package i18n-or_IN
Summary:	OpenOffice.org - interface in Oriya language for India
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku orija dla Indii
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-or_IN
This package provides resources containing menus and dialogs in Oriya
language for India.

%description i18n-or_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
orija dla Indii.

%package i18n-pa_IN
Summary:	OpenOffice.org - interface in Punjabi language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku pendżabskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-pa_IN
This package provides resources containing menus and dialogs in
Punjabi language.

%description i18n-pa_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
pendżabskim.

%package i18n-pl
Summary:	OpenOffice.org - interface in Polish language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku polskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pl
Obsoletes:	openoffice-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl-kde

%description i18n-pl
This package provides resources containing menus and dialogs in Polish
language.

%description i18n-pl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
polskim.

%package i18n-pt
Summary:	OpenOffice.org - interface in Portuguese language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku portugalskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pt
Obsoletes:	openoffice-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt-kde

%description i18n-pt
This package provides resources containing menus and dialogs in
Portuguese language.

%description i18n-pt -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
portugalskim.

%package i18n-pt_BR
Summary:	OpenOffice.org - interface in Brazilian Portuguese language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku portugalskim dla Brazylii
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pt_BR
Obsoletes:	openoffice-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR-kde

%description i18n-pt_BR
This package provides resources containing menus and dialogs in
Brazilian Portuguese language.

%description i18n-pt_BR -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
portugalskim dla Brazylii.

%package i18n-ru
Summary:	OpenOffice.org - interface in Russian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku rosyjskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ru
Obsoletes:	openoffice-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru-kde

%description i18n-ru
This package provides resources containing menus and dialogs in
Russian language.

%description i18n-ru -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
rosyjskim.

%package i18n-rw
Summary:	OpenOffice.org - interface in Kinarwanda language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku kinya-ruanda
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-rw
This package provides resources containing menus and dialogs in
Kinarwanda language.

%description i18n-rw -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kinya-ruanda.

%package i18n-sh
Summary:	OpenOffice.org - interface in Serbo-Croatian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku serbsko-chorwackim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-sh
This package provides resources containing menus and dialogs in
Serbo-Croatian language.

%description i18n-sh -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
serbsko-chorwackim.

%package i18n-sk
Summary:	OpenOffice.org - interface in Slovak language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku słowackim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sk
Obsoletes:	openoffice-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk-kde

%description i18n-sk
This package provides resources containing menus and dialogs in Slovak
language.

%description i18n-sk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
słowackim.

%package i18n-sl
Summary:	OpenOffice.org - interface in Slovenian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku słoweńskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sl
Obsoletes:	openoffice-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl-kde

%description i18n-sl
This package provides resources containing menus and dialogs in
Slovenian language.

%description i18n-sl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
słoweńskim.

%package i18n-sr
Summary:	OpenOffice.org - interface in Serbian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku serbskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-sr
This package provides resources containing menus and dialogs in
Serbian language.

%description i18n-sr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
serbskim.

%package i18n-ss
Summary:	OpenOffice.org - interface in Swati language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku suazi (siswati)
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ss
This package provides resources containing menus and dialogs in Swati
language.

%description i18n-ss -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
suazi (siswati).

%package i18n-st
Summary:	OpenOffice.org - interface in Southern Sotho language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku południowym sotho
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-st
This package provides resources containing menus and dialogs in
Southern Sotho language.

%description i18n-st -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
południowym sotho.

%package i18n-sv
Summary:	OpenOffice.org - interface in Swedish language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku szwedzkim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sv
Obsoletes:	openoffice-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv-kde

%description i18n-sv
This package provides resources containing menus and dialogs in
Swedish language.

%description i18n-sv -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
szwedzkim.

%package i18n-sw
Summary:	OpenOffice.org - interface in Swahili language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku suahili
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-sw
This package provides resources containing menus and dialogs in
Swahili language.

%description i18n-sw -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
suahili.

%package i18n-sw_TZ
Summary:	OpenOffice.org - interface in Swahili language for Tanzania
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku suahili dla Tanzanii
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-sw_TZ
This package provides resources containing menus and dialogs in
Swahili language for Tanzania.

%description i18n-sw_TZ -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
suahili dla Tanzanii.

%package i18n-ta_IN
Summary:	OpenOffice.org - interface in Tamil language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku tamiskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ta_IN
This package provides resources containing menus and dialogs in Tamil
language.

%description i18n-ta_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tamilskim.

%package i18n-te_IN
Summary:	OpenOffice.org - interface in Telugu language for India
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku telugu dla Indii
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-te_IN
This package provides resources containing menus and dialogs in Telugu
language for India.

%description i18n-te_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
telugu dla Indii.

%package i18n-tg
Summary:	OpenOffice.org - interface in Tajik language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku tadżyckim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-tg
This package provides resources containing menus and dialogs in Tajik
language.

%description i18n-tg -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tadżyckim.

%package i18n-th
Summary:	OpenOffice.org - interface in Thai language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku tajskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-th
Obsoletes:	openoffice-i18n-th-gtk
Obsoletes:	openoffice-i18n-th-kde

%description i18n-th
This package provides resources containing menus and dialogs in Thai
language.

%description i18n-th -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tajskim.

%package i18n-ti_ER
Summary:	OpenOffice.org - interface in Tigrigna language for Eritrea
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku tigrinia dla Erytrei
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ti_ER
This package provides resources containing menus and dialogs in
Tigrigna language for Eritrea.

%description i18n-ti_ER -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tigrinia dla Erytrei.

%package i18n-tn
Summary:	OpenOffice.org - interface in Tswana language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku tswana
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-tn
Obsoletes:	openoffice-i18n-tn-gtk
Obsoletes:	openoffice-i18n-tn-kde

%description i18n-tn
This package provides resources containing menus and dialogs in Tswana
language.

%description i18n-tn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tswana.

%package i18n-tr
Summary:	OpenOffice.org - interface in Turkish language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku tureckim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-tr
Obsoletes:	openoffice-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr-kde

%description i18n-tr
This package provides resources containing menus and dialogs in
Turkish language.

%description i18n-tr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tureckim.

%package i18n-ts
Summary:	OpenOffice.org - interface in Tsonga language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku tsonga
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ts
This package provides resources containing menus and dialogs in Tsonga
language.

%description i18n-ts -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tsonga.

%package i18n-uk
Summary:	OpenOffice.org - interface in Ukrainian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku ukraińskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-uk
Obsoletes:	openoffice-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk-kde

%description i18n-uk
This package provides resources containing menus and dialogs in
Ukrainian language.

%description i18n-uk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ukraińskim.

%package i18n-ur_IN
Summary:	OpenOffice.org - interface in Urdu language for India
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku urdu dla Indii
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ur_IN
This package provides resources containing menus and dialogs in Urdu
language for India.

%description i18n-ur_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
urdu dla Indii.

%package i18n-uz
Summary:	OpenOffice.org - interface in Uzbek language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku uzbeckim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-uz
This package provides resources containing menus and dialogs in Uzbek.

%description i18n-uz -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
uzbeckim.

%package i18n-ve
Summary:	OpenOffice.org - interface in Venda language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku venda
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ve
This package provides resources containing menus and dialogs in Venda
language.

%description i18n-ve -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
venda.

%package i18n-vi
Summary:	OpenOffice.org - interface in Vietnamese language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku wietnamskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-vi
This package provides resources containing menus and dialogs in
Vietnamese language.

%description i18n-vi -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
wietnamskim.

%package i18n-xh
Summary:	OpenOffice.org - interface in Xhosa language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku khosa
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-xh
This package provides resources containing menus and dialogs in Xhosa
language.

%description i18n-xh -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
khosa.

%package i18n-zh_CN
Summary:	OpenOffice.org - interface in Chinese language for China
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku chińskim dla Chin
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_CN
Obsoletes:	openoffice-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN-kde

%description i18n-zh_CN
This package provides resources containing menus and dialogs in
Chinese language for China.

%description i18n-zh_CN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
chińskim dla Chin.

%package i18n-zh_TW
Summary:	OpenOffice.org - interface in Chinese language for Taiwan
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku chińskim dla Tajwanu
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_TW
Obsoletes:	openoffice-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW-kde

%description i18n-zh_TW
This package provides resources containing menus and dialogs in
Chinese language for Taiwan.

%description i18n-zh_TW -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
chińskim dla Tajwanu.

%package i18n-zu
Summary:	OpenOffice.org - interface in Zulu language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku zuluskim
Group:		I18n
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zu
Obsoletes:	openoffice-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu-kde

%description i18n-zu
This package provides resources containing menus and dialogs in Zulu
language.

%description i18n-zu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
zuluskim.

%package -n bash-completion-openoffice
Summary:	bash-completion for OpenOffice.org
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla OpenOffice.org
Group:		Applications/Shells
Requires:	%{name}
Requires:	bash-completion

%description -n bash-completion-openoffice
bash-completion for OpenOffice.org.

%description -n bash-completion-openoffice -l pl.UTF-8
bashowe uzupełnianie nazw dla Openoffice.org.

%prep
%setup -q -n ooo-build
install -d src

# sources, icons, KDE_icons. You can verify that all needed sources
# are here by running ./download script manually after rpmbuild -bp
ln -sf %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
	%{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} \
	%{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
	%{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} \
	%{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE50} \
	%{SOURCE51} %{SOURCE52} \
	src

%patch2001 -p1

# fixes
ln -s %{PATCH104} patches/hotfixes/%{basename:%{PATCH104}}.diff
ln -s %{PATCH2002} patches/hotfixes/%{basename:%{PATCH2002}}.diff
ln -s %{PATCH2003} patches/hotfixes/%{basename:%{PATCH2003}}.diff
ln -s %{PATCH2004} patches/hotfixes/%{basename:%{PATCH2004}}.diff

%build
# Make sure we have /proc mounted - otherwise idlc will fail later.
if [ ! -f /proc/cpuinfo ]; then
	echo "You need to have /proc mounted in order to build this package!"
	exit 1
fi

# Skip optimization. It overwrites some OOo own hacks with -O0
SAFE_CFLAGS=""
for i in %{rpmcflags}; do
	case "$i" in
	-O?)
		;;
	*)
		SAFE_CFLAGS="$SAFE_CFLAGS $i"
		;;
	esac
done

export CC="%{__cc}"
export CXX="%{__cxx}"
export CPP="%{__cpp}"

%{__aclocal}
%{__autoconf}

%ifarch %{x8664} sparc64 ppc64 alpha
DISTRO="PLD64"
%else
DISTRO="PLD"
%endif

export DESTDIR=$RPM_BUILD_ROOT
export IGNORE_MANIFEST_CHANGES=1
export QTINC="%{_includedir}/qt"
export QTLIB="%{_libdir}"

%if %{with java}
export JAVA_HOME="%{java_home}"
export DB_JAR="%{_javadir}/db.jar"
export ANT_HOME="%{_datadir}/ant"
%endif

%if %{with ccache}
if [ "$CCACHE_DIR" = "" ] ; then
	export CCACHE_DIR=$HOME/.ccache/
fi
%endif

export DEFAULT_TO_ENGLISH_FOR_PACKING=1

RPM_BUILD_NR_THREADS="%(echo "%{__make}" | sed -e 's#.*-j\([[:space:]]*[0-9]\+\)#\1#g')"
[ "$RPM_BUILD_NR_THREADS" = "%{__make}" ] && RPM_BUILD_NR_THREADS=1
RPM_BUILD_NR_THREADS=$(echo $RPM_BUILD_NR_THREADS)

if [ -f %{_javadir}/serializer.jar ];then
	serializer_jar=%{_javadir}/serializer.jar
else
	serializer_jar=%{_javadir}/xalan.jar
fi

CONFOPTS="\
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
	%{?with_ccache:--with-gcc-speedup=ccache} \
	%{?with_icecream:--with-gcc-speedup=icecream} \
	%{?with_system_agg:--with-system-agg} \
	%{?with_system_beanshell:--with-system-beanshell} \
	%{?with_system_db:--with-system-db} \
	%{?with_system_hsqldb:--with-system-hsqldb} \
	%{?with_system_hunspell:--with-system-hunspell --without-myspell-dicts} \
	%{?with_system_libhnj:--with-system-altlinuxhyphen} \
	%{?with_msaccess:%{?with_system_mdbtools:--with-system-mdbtools}} \
	%{?with_system_myspell:--with-system-myspell} \
	%{?with_system_xalan:--with-system-xalan --with-xalan-jar=%{_javadir}/xalan.jar --with-serializer-jar=$serializer_jar} \
	%{?with_system_xerces:--with-system-xerces} \
	%{?with_system_xml_apis:--with-system-xml-apis} \
	%{?with_system_xt:--with-system-xt --with-xt-jar=%{_javadir}/classes} \
	--with-system-boost \
	--with-system-cairo \
	--with-system-curl \
	--with-system-dicts \
	--with-external-dict-dir=/usr/share/myspell \
	--with-system-expat \
	--with-system-freetype \
	--with-system-gcc \
	--with-system-icu \
	--with-system-jpeg \
	--with-system-libsvg \
	--with-system-libwpd \
	--with-system-libwpg \
	--with-system-libwps \
	--with-system-libxml \
	--with-system-libxslt \
	--with-system-nas \
	--with-system-neon \
	--with-system-odbc-headers \
	--with-system-openssl \
	--with-system-poppler \
	--with-system-portaudio \
	--with-system-python \
	--with-system-redland \
	--with-system-sablot \
	--with-system-sane-header \
	--with-system-saxon \
	--with-system-sndfile \
	--with-system-stdlibs \
	--with-system-vigra \
	--with-system-x11-extensions-headers \
	--with-system-xrender \
	--with-system-xrender-headers=yes \
	--with-system-zlib \
%if %{with mozilla}
	--with-system-mozilla=xulrunner \
%else
	--disable-mozilla \
%endif
	--with-dynamic-xinerama \
	--with-intro-bitmaps="\$SRCDIR/openintro_pld.bmp" \
	--with-about-bitmaps="\$SRCDIR/openabout_pld.bmp" \
	--with-distro="${DISTRO}" \
	--enable-gtk \
	--%{!?with_kde:dis}%{?with_kde:en}able-kde \
	--without-binsuffix \
	--with-installed-ooo-dirname=%{name} \
	--with-lang=%{?with_i18n:ALL} \
%if %{with java}
	--with-java \
	--with-jdk-home=$JAVA_HOME \
	--with-ant-home=$ANT_HOME \
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
	--without-stlport \
	--with-x \
	--without-fonts \
	--without-gpc \
	--disable-epm \
	--disable-fontooo \
	--disable-strip \
	--enable-openxml \
	--enable-atkbridge \
	--%{?with_msaccess:en}%{!?with_msaccess:dis}able-access \
	--enable-cairo \
	--enable-crypt-link \
	--enable-dbus \
	--%{?with_mono:en}%{!?with_mono:dis}able-mono \
	--enable-pam-link \
	--enable-opengl \
	--enable-openldap \
	--enable-openxml \
	--enable-cups \
	--enable-fontconfig \
	--enable-libsn \
	--enable-libart \
	--enable-lockdown \
	--enable-sdext \
	--disable-rpath \
%if 0%{?debug:1}
	--enable-debug \
	--enable-crashdump=yes \
	--enable-symbols=FULL \
%else
	--enable-crashdump=no \
	--disable-symbols \
%endif
	--disable-strip \
	--with-num-cpus=$RPM_BUILD_NR_THREADS \
	--with-build-version=%{version}-%{release} \
	--with-tag=%{tag} \
	--with-drink=coffee \
	--enable-split-app-modules \
	--enable-split-opt-features \
	--disable-access \
	--enable-minimizer \
	--enable-presenter-console \
	--enable-pdfimport
"

# build-ooo script will pickup these
export CONFIGURE_OPTIONS="$CONFOPTS"

:> distro-configs/Common.conf
:> distro-configs/Common.conf.in
echo -n "$CONFOPTS" > distro-configs/PLD.conf
echo -n "$CONFOPTS" > distro-configs/PLD64.conf
if [ $(cat distro-configs/PLD.conf | wc -l) -gt 1 ]; then
	: 'newline(s) found in distro-configs. some of the options might be lost'
	exit 1
fi

# for cvs snaps
[ -x ./autogen.sh ] && ./autogen.sh $CONFOPTS

# main build
# don't use %%configure here. We don't want cflags/ldflags to be set that way since
# it breaks things (like preventing NOOPTFILES from working)
./configure \
		CC="$CC" \
		CXX="$CXX" \
		CPP="$CPP" \
		--host=%{_target_platform} \
		--build=%{_target_platform} \
		--prefix=%{_prefix} \
		--exec-prefix=%{_exec_prefix} \
		--bindir=%{_bindir} \
		--sbindir=%{_sbindir} \
		--sysconfdir=%{_sysconfdir} \
		--datadir=%{_datadir} \
		--includedir=%{_includedir} \
		--libdir=%{_libdir} \
		--libexecdir=%{_libexecdir} \
		--localstatedir=%{_localstatedir} \
		--sharedstatedir=%{_sharedstatedir} \
		--mandir=%{_mandir} \
		--infodir=%{_infodir} \
		--x-libraries=%{?_x_libraries}%{!?_x_libraries:%{_libdir}} \
		%{?configure_cache:--cache-file=%{configure_cache_file}} \
		--with-vendor="PLD/Linux Team" \
		$CONFOPTS

# this limits processing some files but doesn't limit parallel build
# processes of main OOo build (since OOo uses it's own build system)
%{__make} -j1 \
	ARCH_FLAGS="$SAFE_CFLAGS -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CC="$SAFE_CFLAGS -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CXX="$SAFE_CFLAGS -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden" \
	ARCH_FLAGS_OPT="$SAFE_CFLAGS"

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
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	# clean file listings
	rm -f build/*_list.txt

	# limit to single process installation, it's safe at least
	%{__sed} -i -e 's#^BUILD_NCPUS=.*#BUILD_NCPUS=1#g' bin/setup

	export DESTDIR=$RPM_BUILD_ROOT
	export TMP="%{tmpdir}"
	export TMPDIR="%{tmpdir}"
	export TEMP="%{tmpdir}"
	export DEFAULT_TO_ENGLISH_FOR_PACKING=1

	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT

	# save orignal install layout
	find $RPM_BUILD_ROOT -ls > ls.txt
	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	chmod -Rf a+rX,u+w,g-w,o-w $RPM_BUILD_ROOT

	# do we need those? large comparing to png
	rm -r $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/*.svg

	# is below comment true?
	# OOo should not install the Vera fonts, they are Required: now
	#rm $RPM_BUILD_ROOT%{_libdir}/%{name}/share/fonts/truetype/*

	# some libs creep in somehow
	#rm $RPM_BUILD_ROOT%{ooobasisdir}/program/libstl*.so*
	#rm $RPM_BUILD_ROOT%{ooobasisdir}/program/libsndfile*
	#rm $RPM_BUILD_ROOT%{ooobasisdir}/program/libgcc3_uno.so*
	#rm $RPM_BUILD_ROOT%{ooobasisdir}/program/libstdc++*so*

	#rm $RPM_BUILD_ROOT%{ooobasisdir}/program/sopatchlevel.sh

	# Remove setup log
	#rm $RPM_BUILD_ROOT%{ooobasisdir}/program/setup.log

	rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/share/xdg
	#rm $RPM_BUILD_ROOT%{ooobasisdir}/program/cde-open-url

	%if %{without java}
	# Java-releated bits
	#rm -r $RPM_BUILD_ROOT%{ooobasisdir}/program/hid.lst
	#rm -r $RPM_BUILD_ROOT%{ooobasisdir}/program/java-set-classpath
	#rm -r $RPM_BUILD_ROOT%{ooobasisdir}/program/jvmfwk3rc
	#rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/share/Scripts/beanshell
	#rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/share/Scripts/javascript
	#rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/share/xslt
	%endif

	%if %{with mono}
	rm $RPM_BUILD_ROOT%{_libdir}/pkgconfig/mono-ooo-2.1.pc
	%endif

	# Remove dictionaries (in separate pkg)
	#rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo/*
	%if %{with system_myspell}
	#rmdir $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo
	#ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo
	%else
	#touch $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo/dictionary.lst
	%endif

	%if %{with mozilla}
	install -d $RPM_BUILD_ROOT%{_browserpluginsdir}
	ln -s %{ooobasisdir}/program/libnpsoplugin.so $RPM_BUILD_ROOT%{_browserpluginsdir}
	%endif

	# FIXME: OOo doesn't start when sofficerc is a symlink:
	#        "Missing vcl resource. This indicates that files vital to localization are missing. You might have a corrupt installation."
	# configs
	#install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
	#mv $RPM_BUILD_ROOT{%{_libdir}/%{name}/program,%{_sysconfdir}/%{name}}/sofficerc
	#ln -s %{_sysconfdir}/%{name}/sofficerc $RPM_BUILD_ROOT%{_libdir}/%{name}/program

	# FIXME: do we really need it?
	# This breaks apps: The application cannot be started. The component manager is not available.
	# Probably due to relative paths in unorc.
	# mv $RPM_BUILD_ROOT{%{_libdir}/%{name}/program,%{_sysconfdir}/%{name}}/unorc
	# ln -s %{_sysconfdir}/%{name}/unorc $RPM_BUILD_ROOT%{_libdir}/%{name}/program
	# Use this instead:
	#ln -s %{ooobasisdir}/program/unorc $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/unorc

	perl -pi -e 's/^[       ]*LD_LIBRARY_PATH/# LD_LIBRARY_PATH/;s/export LD_LIBRARY_PATH/# export LD_LIBRARY_PATH/' \
		$RPM_BUILD_ROOT%{ooobasisdir}/program/setup

	chmod +x $RPM_BUILD_ROOT%{ooobasisdir}/program/*.so

	install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
	# put share to %{_datadir} so we're able to produce noarch packages
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/share $RPM_BUILD_ROOT%{_datadir}/%{name}
	ln -s ../../share/%{name}/share $RPM_BUILD_ROOT%{_libdir}/%{name}/share
	# more non-archidecture dependant nature data
	#mv $RPM_BUILD_ROOT%{_libdir}/%{name}/help $RPM_BUILD_ROOT%{_datadir}/%{name}
	#ln -s ../../share/%{name}/help $RPM_BUILD_ROOT%{_libdir}/%{name}/help
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/licenses $RPM_BUILD_ROOT%{_datadir}/%{name}
	ln -s ../../share/%{name}/licenses $RPM_BUILD_ROOT%{_libdir}/%{name}/licenses
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/readmes $RPM_BUILD_ROOT%{_datadir}/%{name}
	ln -s ../../share/%{name}/readmes $RPM_BUILD_ROOT%{_libdir}/%{name}/readmes

	# fix python
	#sed -i -e 's|#!/bin/python|#!%{_bindir}/python|g' $RPM_BUILD_ROOT%{ooobasisdir}/program/*.py

	# Add in the regcomp tool since some people need it for 3rd party add-ons
	cp -a build/%{tag}/solver/%{upd}/unxlng*.pro/bin/regcomp{,.bin} $RPM_BUILD_ROOT%{ooobasisdir}/program/

	# Rename .desktop files to avoid conflicts with other applications .desktops
	# TODO: make patch instead.
	for a in $RPM_BUILD_ROOT%{_desktopdir}/*.desktop; do
		d=$(dirname "$a")
		f=$(basename "$a")
		mv $a $d/oo$f
	done

	install %{SOURCE53} $RPM_BUILD_ROOT%{_libdir}/%{name}/program/openintro_pld.bmp
	install %{SOURCE54} $RPM_BUILD_ROOT%{_libdir}/%{name}/program/openabout_pld.bmp

	touch installed.stamp
fi

# Find out locales
find_lang() {
	local lang=$(echo $1 | sed -e 's/_/-/')
	local langfn="$1"
	echo "%%defattr(644,root,root,755)" > ${langfn}.lang

	# help files
	if [ -f build/help_${langfn}_list.txt ]; then
		cat build/help_${langfn}_list.txt >> ${langfn}.lang
	fi

	lfile="build/lang_${langfn}_list.txt"
	if [ -f ${lfile} ]; then
		lprefix=$(bin/openoffice-xlate-lang -p ${lang} 2>/dev/null || :)
		longlang=$(bin/openoffice-xlate-lang -l ${lang} 2>/dev/null || :)
		# share/*/${longlang}
		if [ "x${longlang}" != "x" ] ; then
			grep "^%%dir.*/${longlang}/\$" ${lfile} > tmp.lang || :
		fi
		# share/registry/res/${lang} (but en-US for en)
		grep "^%%dir.*/res/${lang}[^/]*/\$" ${lfile} >> tmp.lang || :
		# ... translate %dir into whole tree, handle special wordbook/english case
		sed -e 's,^%%dir ,,;s,\(wordbook/english/\)$,\1soffice.dic,;s,/$,,' tmp.lang >> ${langfn}.lang || :
		# share/autocorr/acor${somecodes}.dat (if exist)
		grep '/autocorr/acor.*dat$' ${lfile} >> ${langfn}.lang || :
		# user/config/* (if exist, without parent directory)
		grep '/user/config/..*' ${lfile} >> ${langfn}.lang || :
		grep "/licenses/LICENSE_${lang}" ${lfile} >> ${langfn}.lang || :
		grep "/readmes/README_${lang}" ${lfile} >> ${langfn}.lang || :
		grep "share/readme/LICENSE_${lang}" ${lfile} >> ${langfn}.lang || :
		grep "share/readme/README_${lang}" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/presers/config/*.so[cdegh]
		grep "/presets/config/.*_${lang}\.so[cdegh]$" ${lfile} >> ${langfn}.lang || :
		if [ "x${lprefix}" != "x" ] ; then
			grep "/presets/config/${lprefix}.*\.so[cdegh]$" ${lfile} >> ${langfn}.lang || :
		fi
		# lib/openoffice.org/program/resource/*.res
		grep "/program/resource/.*${lang}.res$" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/autocorr/*.dat
		grep "/share/autocorr/.*${lang}.dat$" ${lfile} >> ${langfn}.lang || :
		grep -i "/share/autocorr/.*${lang}-${lang}.dat$" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/autotext/$lang
		grep "/share/autotext/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/autotext/${lang}/" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/registry/modules/org/openoffice/Office/Common/Common-cjk_$lang.xcu
		grep "/share/registry/modules/org/openoffice/Office/Common/Common-cjk_${lang}.xcu$" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/registry/modules/org/openoffice/Office/Common/Common-ctl_$lang.xcu
		grep "/share/registry/modules/org/openoffice/Office/Common/Common-ctl_${lang}.xcu$" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/registry/modules/org/openoffice/Office/Writer/Writer-cjk_$lang.xcu
		grep "/share/registry/modules/org/openoffice/Office/Writer/Writer-cjk_${lang}.xcu" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/registry/modules/org/openoffice/Setup/Langpack-$lang.xcu
		grep "/share/registry/modules/org/openoffice/Setup/Langpack-${lang}.xcu$" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/registry/res/$lang
		grep "/share/registry/res/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/registry/res/${lang}/" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/template/$lang
		grep "/share/template/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/${lang}/" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/template/wizard/letter/lang
		grep "/share/template/wizard/letter/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}/" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		# lib/openoffice.org/share/wordbook/$lang
		grep "/share/wordbook/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/wordbook/${lang}/" ${lfile} >> ${langfn}.lang || :
		# lib/openoffice.org/share/samples/$lang
		grep "/share/samples/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/samples/${lang}/" ${lfile} >> ${langfn}.lang || :
		grep "/help/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/help/${lang}/" ${lfile} >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/dbapp/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/dbapp/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/dbbrowser/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/dbbrowser/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/dbquery/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/dbquery/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/dbreport/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/dbreport/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/dbtdata/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/dbtdata/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/scalc/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/scalc/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/sdraw/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/sdraw/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/sglobal/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/sglobal/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/simpress/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/simpress/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/sweb/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/sweb/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/swform/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/swform/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/swreport/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/swreport/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/swriter/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/swriter/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/swxform/accelerator/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/config/soffice.cfg/modules/swxform/accelerator/${lang}/" build/common_list.txt >> ${langfn}.lang || :
	fi
}

rm -f *.lang*
langlist=$(ls build/lang_*_list.txt | sed -e 's=build/lang_\(.*\)_list.txt=\1=g')

for lang in $langlist; do
	find_lang $lang
done

%{__sed} -i -e '
	s,%{_libdir}/%{name}/help,%{ooobasisdir}/help,;
	s,%{_libdir}/%{name}/licenses,%{_datadir}/%{name}/licenses,;
	s,%{_libdir}/%{name}/readmes,%{_datadir}/%{name}/readmes,;
	s,%{_libdir}/%{name}/share,%{_datadir}/%{name}/share,;
' *.lang

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans core
%if %{with system_myspell}
# we symlink the dir, unless smb wishes to patch OOo to use system dir directly
if [ -d %{_libdir}/%{name}/share/dict/ooo ] && [ ! -L %{_libdir}/%{name}/share/dict/ooo ]; then
	rmdir %{_libdir}/%{name}/share/dict/ooo 2>/dev/null || mv -v %{_libdir}/%{name}/share/dict/ooo{,.rpmsave} || :
fi
%endif
for d in share %{?with_java:help} readmes licenses; do
	if [ -d %{_libdir}/%{name}/$d ] && [ ! -L %{_libdir}/%{name}/$d ]; then
		install -d %{_datadir}/%{name}
		mv %{_libdir}/%{name}/$d %{_datadir}/%{name}/$d || mv %{_libdir}/%{name}/$d{,.rpmsave}
	fi
done
if [ -L %{ooobasisdir}/presets ]; then
	rm -f %{ooobasisdir}/presets
fi

%post core
%update_mime_database
%update_desktop_database_post

%postun core
%update_desktop_database_postun
%update_mime_database

%post base
%update_desktop_database_post

%postun base
%update_desktop_database_postun

%post web
%update_desktop_database_post

%postun web
%update_desktop_database_postun

%post writer
%update_desktop_database_post

%postun writer
%update_desktop_database_postun

%post calc
%update_desktop_database_post

%postun calc
%update_desktop_database_postun

%post draw
%update_desktop_database_post

%postun draw
%update_desktop_database_postun

%post impress
%update_desktop_database_post

%postun impress
%update_desktop_database_postun

%post math
%update_desktop_database_post

%postun math
%update_desktop_database_postun

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

# NOTE:
# you may find build/*_list.txt useful to help you package files to packages

%files
%defattr(644,root,root,755)

%files core
%defattr(644,root,root,755)
%doc %{_libdir}/%{name}/LICENSE*
%doc %{_libdir}/%{name}/*README*

%attr(755,root,root) %{_bindir}/ooconfig
%attr(755,root,root) %{_bindir}/ooffice
%attr(755,root,root) %{_bindir}/oofromtemplate
%attr(755,root,root) %{_bindir}/ootool
%attr(755,root,root) %{_bindir}/soffice
%attr(755,root,root) %{_bindir}/unopkg

%dir %{ooobasisdir}
%dir %{ooobasisdir}/help
%{ooobasisdir}/help/*.xsl
%dir %{ooobasisdir}/help/en
%{ooobasisdir}/help/en/*.html
%{ooobasisdir}/help/en/*.css
%{ooobasisdir}/help/en/sbasic.*
%{ooobasisdir}/help/en/schart.*
%{ooobasisdir}/help/en/shared.*

%dir %{ooobasisdir}/presets
%dir %{ooobasisdir}/presets/autotext
%{ooobasisdir}/presets/autotext/mytexts.bau
%{ooobasisdir}/presets/basic
%dir %{ooobasisdir}/presets/config
%{ooobasisdir}/presets/config/*_en-US.so*
%{ooobasisdir}/presets/config/autotbl.fmt
%{ooobasisdir}/presets/config/cmyk.soc
%{ooobasisdir}/presets/config/gallery.soc
%{ooobasisdir}/presets/config/html.soc
%{ooobasisdir}/presets/config/standard.so?
%{ooobasisdir}/presets/config/sun-color.soc
%{ooobasisdir}/presets/config/web.soc
%{ooobasisdir}/presets/database
%{ooobasisdir}/presets/gallery
%{ooobasisdir}/presets/psprint

%dir %{ooobasisdir}/program
%attr(755,root,root) %{ooobasisdir}/program/OGLTrans.uno.so
%attr(755,root,root) %{ooobasisdir}/program/basprov*.uno.so
%attr(755,root,root) %{ooobasisdir}/program/behelper.uno.so
%attr(755,root,root) %{ooobasisdir}/program/cairocanvas.uno.so
%attr(755,root,root) %{ooobasisdir}/program/canvasfactory.uno.so
%attr(755,root,root) %{ooobasisdir}/program/cde-open-url
%attr(755,root,root) %{ooobasisdir}/program/cmdmail.uno.so
%attr(755,root,root) %{ooobasisdir}/program/configmgr2.uno.so
%attr(755,root,root) %{ooobasisdir}/program/deployment*.uno.so
%attr(755,root,root) %{ooobasisdir}/program/desktopbe1.uno.so
%attr(755,root,root) %{ooobasisdir}/program/dlgprov*.uno.so
%attr(755,root,root) %{ooobasisdir}/program/fastsax.uno.so
%attr(755,root,root) %{ooobasisdir}/program/fpicker.uno.so
%attr(755,root,root) %{ooobasisdir}/program/fps_office.uno.so
%attr(755,root,root) %{ooobasisdir}/program/fsstorage.uno.so
%attr(755,root,root) %{ooobasisdir}/program/gengal
%attr(755,root,root) %{ooobasisdir}/program/gengal.bin
%attr(755,root,root) %{ooobasisdir}/program/hatchwindowfactory.uno.so
%attr(755,root,root) %{ooobasisdir}/program/i18npool.uno.so
%attr(755,root,root) %{ooobasisdir}/program/i18nsearch.uno.so
%attr(755,root,root) %{ooobasisdir}/program/java-set-classpath
%attr(755,root,root) %{ooobasisdir}/program/ldapbe2.uno.so
%attr(755,root,root) %{ooobasisdir}/program/libaccl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libadabasl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libaggl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libavmediagst.so
%attr(755,root,root) %{ooobasisdir}/program/libavmedial[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbasctll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbasebmpl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbasegfxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_frml[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_gol[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_migratefilterl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_ofal[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_sbl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_schl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_scl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_sdl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_sml[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_sol[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_swl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_svtl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_svxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_wrapperl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbf_xol[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbibl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libbindetl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libcached1.so
%attr(755,root,root) %{ooobasisdir}/program/libcanvastoolsl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libchartcontrollerl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libchartmodell[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libcharttoolsl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libchartviewl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libcollator_data.so
%attr(755,root,root) %{ooobasisdir}/program/libcomphelp4gcc3.so
%attr(755,root,root) %{ooobasisdir}/program/libcppcanvasl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libctll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libcuil[ipx].so
%{!?with_system_db:%attr(755,root,root) %{ooobasisdir}/program/libdb-4.2.so}
%attr(755,root,root) %{ooobasisdir}/program/libdbacfgl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdbal[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdbasel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdbaxmll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdbmml[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdbpool2.so
%attr(755,root,root) %{ooobasisdir}/program/libdbtoolsl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdbul[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdeploymentmiscl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdict_ja.so
%attr(755,root,root) %{ooobasisdir}/program/libdict_zh.so
%attr(755,root,root) %{ooobasisdir}/program/libdtransX11l[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libeggtrayl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libegil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libembobj.so
%attr(755,root,root) %{ooobasisdir}/program/libemboleobj.so
%attr(755,root,root) %{ooobasisdir}/program/libemel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libempl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libepbl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libepgl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libeppl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libepsl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libeptl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/liberal[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libetil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libevoab1.so
%attr(755,root,root) %{ooobasisdir}/program/libevtatt.so
%attr(755,root,root) %{ooobasisdir}/program/libexlinkl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libexpl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfileacc.so
%attr(755,root,root) %{ooobasisdir}/program/libfilel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfilterconfig1.so
%attr(755,root,root) %{ooobasisdir}/program/libflatl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfrml[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfwel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfwil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfwkl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfwll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfwml[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libgol[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libguesslangl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libhelplinkerl[ipx].so
%{!?with_system_hunspell:%attr(755,root,root) %{ooobasisdir}/program/libhunspell.so}
%attr(755,root,root) %{ooobasisdir}/program/libhyphenl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libi18nisolang1gcc3.so
%attr(755,root,root) %{ooobasisdir}/program/libi18nregexpgcc3.so
%attr(755,root,root) %{ooobasisdir}/program/libi18nutilgcc3.so
%attr(755,root,root) %{ooobasisdir}/program/libicdl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libicgl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libidxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libindex_data.so
%attr(755,root,root) %{ooobasisdir}/program/libimel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libipbl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libipdl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libipsl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libiptl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libipxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libiral[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libitgl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libitil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libjl*_g.so
%attr(755,root,root) %{ooobasisdir}/program/liblegacy_binfiltersl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/liblngl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/liblnthl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/liblocaledata_en.so
%attr(755,root,root) %{ooobasisdir}/program/liblocaledata_es.so
%attr(755,root,root) %{ooobasisdir}/program/liblocaledata_euro.so
%attr(755,root,root) %{ooobasisdir}/program/liblocaledata_others.so
%attr(755,root,root) %{ooobasisdir}/program/liblogl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libmcnttype.so
%attr(755,root,root) %{ooobasisdir}/program/libmozbootstrap.so
%attr(755,root,root) %{ooobasisdir}/program/libmysql2.so
%attr(755,root,root) %{ooobasisdir}/program/libodbc2.so
%attr(755,root,root) %{ooobasisdir}/program/libodbcbase2.so
%attr(755,root,root) %{ooobasisdir}/program/liboffaccl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/liboooimprovecorel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libooxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libpackage2.so
%attr(755,root,root) %{ooobasisdir}/program/libpcrl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libpdffilterl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libpll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libpreloadl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libprotocolhandlerl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libpspl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libqstart_gtkl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/librecentfile.so
%attr(755,root,root) %{ooobasisdir}/program/libresl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsaxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsbl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libscnl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libscriptframe.so
%attr(755,root,root) %{ooobasisdir}/program/libsdbc2.so
%attr(755,root,root) %{ooobasisdir}/program/libsdbtl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsddl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsdl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsduil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsfxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsofficeapp.so
%attr(755,root,root) %{ooobasisdir}/program/libsotl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libspal[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libspelll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libspl_unxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libspll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsrtrs1.so
%attr(755,root,root) %{ooobasisdir}/program/libstsl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsvll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsvtl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsvxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libswl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libtextcat.so
%attr(755,root,root) %{ooobasisdir}/program/libtextconv_dict.so
%attr(755,root,root) %{ooobasisdir}/program/libtextconversiondlgsl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libtful[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libtkl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libtll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libtvhlp1.so
%attr(755,root,root) %{ooobasisdir}/program/libucb1.so
%attr(755,root,root) %{ooobasisdir}/program/libucbhelper4gcc3.so
%attr(755,root,root) %{ooobasisdir}/program/libucpchelp1.so
%attr(755,root,root) %{ooobasisdir}/program/libucpdav1.so
%attr(755,root,root) %{ooobasisdir}/program/libucpfile1.so
%attr(755,root,root) %{ooobasisdir}/program/libucpftp1.so
%attr(755,root,root) %{ooobasisdir}/program/libucphier1.so
%attr(755,root,root) %{ooobasisdir}/program/libucppkg1.so
%attr(755,root,root) %{ooobasisdir}/program/libunopkgapp.so
%attr(755,root,root) %{ooobasisdir}/program/libunordfl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libunoxmll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libupdchkl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libutll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libuuil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libvcll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libvclplug_genl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libvclplug_svpl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libvos3gcc3.so
%attr(755,root,root) %{ooobasisdir}/program/libxcrl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libxmlfal[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libxmlfdl[ipx].so
## maybe external is possible?
# - external broken in 3.0.1
%attr(755,root,root) %{ooobasisdir}/program/libxmlsec1*.so
##
%attr(755,root,root) %{ooobasisdir}/program/libxmlsecurity.so
%attr(755,root,root) %{ooobasisdir}/program/libxmxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libxofl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libxol[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libxsec_fw.so
%attr(755,root,root) %{ooobasisdir}/program/libxsec_xmlsec.so
%attr(755,root,root) %{ooobasisdir}/program/libxsltdlgl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libxsltfilterl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libxstor.so
%attr(755,root,root) %{ooobasisdir}/program/localebe1.uno.so
%attr(755,root,root) %{ooobasisdir}/program/migrationoo2.uno.so
%attr(755,root,root) %{ooobasisdir}/program/open-url
%attr(755,root,root) %{ooobasisdir}/program/pagein*
%attr(755,root,root) %{ooobasisdir}/program/passwordcontainer.uno.so
%attr(755,root,root) %{ooobasisdir}/program/pluginapp.bin
%attr(755,root,root) %{ooobasisdir}/program/productregistration.uno.so
## seems to be exactly the same as in -ure
%attr(755,root,root) %{ooobasisdir}/program/regcomp
%attr(755,root,root) %{ooobasisdir}/program/regcomp.bin
##
%attr(755,root,root) %{ooobasisdir}/program/sax.uno.so
%attr(755,root,root) %{ooobasisdir}/program/senddoc
%attr(755,root,root) %{ooobasisdir}/program/setofficelang
%attr(755,root,root) %{ooobasisdir}/program/setofficelang.bin
%attr(755,root,root) %{ooobasisdir}/program/simplecanvas.uno.so
%attr(755,root,root) %{ooobasisdir}/program/slideshow.uno.so
%attr(755,root,root) %{ooobasisdir}/program/spadmin.bin
%attr(755,root,root) %{ooobasisdir}/program/stocservices.uno.so
%attr(755,root,root) %{ooobasisdir}/program/stringresource*.uno.so
%attr(755,root,root) %{ooobasisdir}/program/svtmisc.uno.so
%attr(755,root,root) %{ooobasisdir}/program/sysmgr1.uno.so
%attr(755,root,root) %{ooobasisdir}/program/syssh.uno.so
%attr(755,root,root) %{ooobasisdir}/program/ucpexpand1.uno.so
%attr(755,root,root) %{ooobasisdir}/program/ucptdoc1.uno.so
%attr(755,root,root) %{ooobasisdir}/program/updatefeed.uno.so
%attr(755,root,root) %{ooobasisdir}/program/uri-encode
%attr(755,root,root) %{ooobasisdir}/program/vbaevents*.uno.so
%attr(755,root,root) %{ooobasisdir}/program/vclcanvas.uno.so
# versioned libraries and their symlinks
%attr(755,root,root) %{ooobasisdir}/program/*.so.*

%if %{with java}
%attr(755,root,root) %{ooobasisdir}/program/libhsqldb2.so
%attr(755,root,root) %{ooobasisdir}/program/libjdbc2.so
%attr(755,root,root) %{ooobasisdir}/program/libofficebean.so
%endif

%if %{with mono}
%attr(755,root,root) %{ooobasisdir}/program/libcli_uno.so
%attr(755,root,root) %{ooobasisdir}/program/libcli_uno_glue.so
%{ooobasisdir}/program/cli_basetypes.dll
%{ooobasisdir}/program/cli_cppuhelper.dll
%{ooobasisdir}/program/cli_types.dll
%{ooobasisdir}/program/cli_uno_bridge.dll
%{ooobasisdir}/program/cli_ure.dll
%endif

%{ooobasisdir}/program/configmgrrc
%{ooobasisdir}/program/fundamentalbasisrc
%{ooobasisdir}/program/gengalrc
%{ooobasisdir}/program/legacy_binfilters.rdb
%{ooobasisdir}/program/offapi.rdb
%{ooobasisdir}/program/oovbaapi.rdb
%{ooobasisdir}/program/root3.dat
%{ooobasisdir}/program/root4.dat
%{ooobasisdir}/program/root5.dat
%{ooobasisdir}/program/services.rdb
%config(noreplace) %verify(not md5 mtime size) %{ooobasisdir}/program/unorc
%{ooobasisdir}/program/versionrc

%if %{with java}
%dir %{ooobasisdir}/program/classes
%{ooobasisdir}/program/classes/LuceneHelpWrapper.jar
%{ooobasisdir}/program/classes/ScriptFramework.jar
%{ooobasisdir}/program/classes/ScriptProviderForBeanShell.jar
%{ooobasisdir}/program/classes/ScriptProviderForJava.jar
%{ooobasisdir}/program/classes/ScriptProviderForJavaScript.jar
%{ooobasisdir}/program/classes/XMergeBridge.jar
%{ooobasisdir}/program/classes/XSLTFilter.jar
%{ooobasisdir}/program/classes/XSLTValidate.jar
%{ooobasisdir}/program/classes/agenda.jar
%{ooobasisdir}/program/classes/classes.jar
%{ooobasisdir}/program/classes/commonwizards.jar
%{ooobasisdir}/program/classes/fax.jar
%{ooobasisdir}/program/classes/form.jar
%{!?with_system_hsqldb:%{ooobasisdir}/program/classes/hsqldb.jar}
%{ooobasisdir}/program/classes/js.jar
%{ooobasisdir}/program/classes/jut.jar
%{ooobasisdir}/program/classes/letter.jar
%{ooobasisdir}/program/classes/lucene-analyzers-2.3.jar
%{ooobasisdir}/program/classes/lucene-core-2.3.jar
%{ooobasisdir}/program/classes/officebean.jar
%{ooobasisdir}/program/classes/query.jar
%{ooobasisdir}/program/classes/report.jar
%{ooobasisdir}/program/classes/sandbox.jar
%{ooobasisdir}/program/classes/sdbc_hsqldb.jar
%{!?with_system_xalan:%{ooobasisdir}/program/classes/serializer.jar}
%{ooobasisdir}/program/classes/table.jar
%{ooobasisdir}/program/classes/unoil.jar
%{ooobasisdir}/program/classes/web.jar
%{!?with_system_xalan:%{ooobasisdir}/program/classes/xalan.jar}
%{!?with_system_xerces:%{ooobasisdir}/program/classes/xercesImpl.jar}
%{ooobasisdir}/program/classes/xmerge.jar
%{!?with_system_xml_apis:%{ooobasisdir}/program/classes/xml-apis.jar}
%endif

%dir %{ooobasisdir}/program/resource
%{ooobasisdir}/program/resource/accen-US.res
%{ooobasisdir}/program/resource/avmediaen-US.res
%{ooobasisdir}/program/resource/basctlen-US.res
%{ooobasisdir}/program/resource/bf_frmen-US.res
%{ooobasisdir}/program/resource/bf_ofaen-US.res
%{ooobasisdir}/program/resource/bf_schen-US.res
%{ooobasisdir}/program/resource/bf_sden-US.res
%{ooobasisdir}/program/resource/bf_svten-US.res
%{ooobasisdir}/program/resource/bf_svxen-US.res
%{ooobasisdir}/program/resource/bf_swen-US.res
%{ooobasisdir}/program/resource/biben-US.res
%{ooobasisdir}/program/resource/calen-US.res
%{ooobasisdir}/program/resource/chartcontrolleren-US.res
%{ooobasisdir}/program/resource/dbaen-US.res
%{ooobasisdir}/program/resource/dbmmen-US.res
%{ooobasisdir}/program/resource/dbwen-US.res
%{ooobasisdir}/program/resource/deploymenten-US.res
%{ooobasisdir}/program/resource/deploymentguien-US.res
%{ooobasisdir}/program/resource/dkten-US.res
%{ooobasisdir}/program/resource/egien-US.res
%{ooobasisdir}/program/resource/emeen-US.res
%{ooobasisdir}/program/resource/epben-US.res
%{ooobasisdir}/program/resource/epgen-US.res
%{ooobasisdir}/program/resource/eppen-US.res
%{ooobasisdir}/program/resource/epsen-US.res
%{ooobasisdir}/program/resource/epten-US.res
%{ooobasisdir}/program/resource/euren-US.res
%{ooobasisdir}/program/resource/fps_officeen-US.res
%{ooobasisdir}/program/resource/frmen-US.res
%{ooobasisdir}/program/resource/fween-US.res
%{ooobasisdir}/program/resource/galen-US.res
%{ooobasisdir}/program/resource/impen-US.res
%{ooobasisdir}/program/resource/ofaen-US.res
%{ooobasisdir}/program/resource/pcren-US.res
%{ooobasisdir}/program/resource/pdffilteren-US.res
%{ooobasisdir}/program/resource/preloaden-US.res
%{ooobasisdir}/program/resource/productregistrationen-US.res
%{ooobasisdir}/program/resource/sanen-US.res
%{ooobasisdir}/program/resource/sben-US.res
%{ooobasisdir}/program/resource/sden-US.res
%{ooobasisdir}/program/resource/sdbten-US.res
%{ooobasisdir}/program/resource/sfxen-US.res
%{ooobasisdir}/program/resource/spaen-US.res
%{ooobasisdir}/program/resource/svsen-US.res
%{ooobasisdir}/program/resource/svten-US.res
%{ooobasisdir}/program/resource/svxen-US.res
%{ooobasisdir}/program/resource/swen-US.res
%{ooobasisdir}/program/resource/textconversiondlgsen-US.res
%{ooobasisdir}/program/resource/tfuen-US.res
%{ooobasisdir}/program/resource/tken-US.res
%{ooobasisdir}/program/resource/tplen-US.res
%{ooobasisdir}/program/resource/updchken-US.res
%{ooobasisdir}/program/resource/upden-US.res
%{ooobasisdir}/program/resource/uuien-US.res
%{ooobasisdir}/program/resource/vclen-US.res
%{ooobasisdir}/program/resource/wzien-US.res
%{ooobasisdir}/program/resource/xmlsecen-US.res
%{ooobasisdir}/program/resource/xsltdlgen-US.res

%dir %{ooobasisdir}/share
%dir %{ooobasisdir}/share/Scripts
%{ooobasisdir}/share/Scripts/beanshell
%{ooobasisdir}/share/Scripts/javascript
%if %{with java}
%{ooobasisdir}/share/Scripts/java
%endif

%dir %{ooobasisdir}/share/autocorr
%{ooobasisdir}/share/autocorr/acor_*.dat
%dir %{ooobasisdir}/share/autotext
%{ooobasisdir}/share/autotext/en-US
%{ooobasisdir}/share/basic
%dir %{ooobasisdir}/share/config
%{ooobasisdir}/share/config/images.zip
%{ooobasisdir}/share/config/images_classic.zip
%{ooobasisdir}/share/config/images_crystal.zip
%{ooobasisdir}/share/config/images_hicontrast.zip
%{ooobasisdir}/share/config/images_industrial.zip
%{ooobasisdir}/share/config/images_tango.zip
%{ooobasisdir}/share/config/javasettingsunopkginstall.xml
%{ooobasisdir}/share/config/*.xpm
%dir %{ooobasisdir}/share/config/soffice.cfg
%{ooobasisdir}/share/config/soffice.cfg/global
%dir %{ooobasisdir}/share/config/soffice.cfg/modules
%{ooobasisdir}/share/config/soffice.cfg/modules/BasicIDE
%{ooobasisdir}/share/config/soffice.cfg/modules/StartModule
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbapp
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbapp/accelerator
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbbrowser
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbbrowser/accelerator
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbquery
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbquery/accelerator
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbreport
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbreport/accelerator
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbtdata
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbtdata/accelerator
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/scalc
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/scalc/accelerator
%{ooobasisdir}/share/config/soffice.cfg/modules/schart
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/sdraw
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/sdraw/accelerator
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/sglobal
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/sglobal/accelerator
%{ooobasisdir}/share/config/soffice.cfg/modules/sglobal/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/sglobal/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/sglobal/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/sglobal/toolbar
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/sweb
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/sweb/accelerator
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/simpress
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/simpress/accelerator
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swform
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swform/accelerator
%{ooobasisdir}/share/config/soffice.cfg/modules/swform/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/swform/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/swform/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/swform/toolbar
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swreport
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swreport/accelerator
%{ooobasisdir}/share/config/soffice.cfg/modules/swreport/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/swreport/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/swreport/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/swreport/toolbar
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swriter
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swriter/accelerator
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swxform
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swxform/accelerator
%{ooobasisdir}/share/config/soffice.cfg/modules/swxform/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/swxform/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/swxform/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/swxform/toolbar
%{ooobasisdir}/share/config/symbol
%{ooobasisdir}/share/config/webcast
%{ooobasisdir}/share/config/wizard
%dir %{ooobasisdir}/share/dtd
%{ooobasisdir}/share/dtd/officedocument
%{ooobasisdir}/share/fingerprint
%{ooobasisdir}/share/fonts
%{ooobasisdir}/share/gallery
%{ooobasisdir}/share/psprint
%dir %{ooobasisdir}/share/registry
%dir %{ooobasisdir}/share/registry/data
%dir %{ooobasisdir}/share/registry/data/org
%dir %{ooobasisdir}/share/registry/data/org/openoffice
%{ooobasisdir}/share/registry/data/org/openoffice/FirstStartWizard.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Inet.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/LDAP.xcu.sample
%{ooobasisdir}/share/registry/data/org/openoffice/Setup.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/UserProfile.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/VCL.xcu
%dir %{ooobasisdir}/share/registry/data/org/openoffice/Office
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Calc.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Canvas.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Common.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/DataAccess.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Embedding.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/ExtendedColorScheme.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/ExtensionManager.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/FormWizard.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Impress.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Jobs.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Labels.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Logging.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Math.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Paths.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/ProtocolHandler.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Scripting.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Security.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/SFX.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/TableWizard.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Views.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/WebWizard.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/Writer.xcu
%dir %{ooobasisdir}/share/registry/data/org/openoffice/Office/UI
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/BaseWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/BasicIDECommands.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/BasicIDEWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/BibliographyCommands.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/ChartCommands.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/ChartWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/Controller.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/DbBrowserWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/DbQueryWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/DbRelationWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/DbTableWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/DbTableDataWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/DbuCommands.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/DrawImpressCommands.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/Factories.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/GenericCategories.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/GenericCommands.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/StartModuleCommands.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/StartModuleWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/WriterFormWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/WriterReportWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/XFormsWindowState.xcu
%dir %{ooobasisdir}/share/registry/data/org/openoffice/TypeDetection
%{ooobasisdir}/share/registry/data/org/openoffice/TypeDetection/UISort.xcu
%dir %{ooobasisdir}/share/registry/data/org/openoffice/ucb
%{ooobasisdir}/share/registry/data/org/openoffice/ucb/Configuration.xcu
%{ooobasisdir}/share/registry/ldap
%dir %{ooobasisdir}/share/registry/modules
%dir %{ooobasisdir}/share/registry/modules/org
%dir %{ooobasisdir}/share/registry/modules/org/openoffice
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/Office
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/Office/Common
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Common/Common-unx.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Common/Common-UseOOoFileDialogs.xcu
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/Office/Embedding
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-chart.xcu
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/Office/Linguistic
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Linguistic/Linguistic-lingucomponent-hyphenator.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Linguistic/Linguistic-lingucomponent-spellchecker.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Linguistic/Linguistic-lingucomponent-thesaurus.xcu
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/Office/Scripting
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/Office/Writer
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/Setup
%{ooobasisdir}/share/registry/modules/org/openoffice/Setup/Langpack-en-US.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Setup/Setup-start.xcu
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_base_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_chart_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_chart_bf_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_global_bf_filters.xcu
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/GraphicFilter
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/GraphicFilter/fcfg_internalgraphics_filters.xcu
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Misc
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_base_others.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_chart_others.xcu
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_base_types.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_chart_types.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_internalgraphics_types.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_chart_bf_types.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_global_bf_types.xcu
%dir %{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/UISort
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-calc.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-draw.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-impress.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-math.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-writer.xcu
%dir %{ooobasisdir}/share/registry/res
%{ooobasisdir}/share/registry/res/en-US
%dir %{ooobasisdir}/share/registry/schema
%dir %{ooobasisdir}/share/registry/schema/org
%dir %{ooobasisdir}/share/registry/schema/org/openoffice
%{ooobasisdir}/share/registry/schema/org/openoffice/FirstStartWizard.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Inet.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/LDAP.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Setup.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/System.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/UserProfile.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/VCL.xcs
%dir %{ooobasisdir}/share/registry/schema/org/openoffice/Office
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Addons.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/CalcAddIns.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Calc.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Canvas.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Chart.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Commands.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Common.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Compatibility.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/DataAccess.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Draw.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Embedding.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Events.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/ExtendedColorScheme.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/ExtensionManager.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/FormWizard.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Impress.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Java.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Jobs.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Labels.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Linguistic.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Logging.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Math.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/OptionsDialog.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Paths.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/ProtocolHandler.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Recovery.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Scripting.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Security.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/SFX.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Substitution.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/TabBrowse.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/TableWizard.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/TypeDetection.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Views.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/WebWizard.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/WriterWeb.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/Writer.xcs
%dir %{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/BaseWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/BasicIDECommands.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/BasicIDEWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/BibliographyCommands.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/BibliographyWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/Category.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/ChartCommands.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/ChartWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/Commands.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/Controller.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/DbBrowserWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/DbQueryWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/DbRelationWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/DbTableWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/DbTableDataWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/DbuCommands.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/DrawImpressCommands.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/Factories.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/GenericCategories.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/GenericCommands.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/GlobalSettings.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/MathWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/StartModuleCommands.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/StartModuleWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/WindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/WriterFormWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/WriterReportWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/XFormsWindowState.xcs
%dir %{ooobasisdir}/share/registry/schema/org/openoffice/TypeDetection
%{ooobasisdir}/share/registry/schema/org/openoffice/TypeDetection/Filter.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/TypeDetection/GraphicFilter.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/TypeDetection/Misc.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/TypeDetection/Types.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/TypeDetection/UISort.xcs
%dir %{ooobasisdir}/share/registry/schema/org/openoffice/ucb
%{ooobasisdir}/share/registry/schema/org/openoffice/ucb/Configuration.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/ucb/Hierarchy.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/ucb/Store.xcs

%dir %{ooobasisdir}/share/samples
%dir %{ooobasisdir}/share/samples/en-US

%dir %{ooobasisdir}/share/template
%{ooobasisdir}/share/template/en-US
%dir %{ooobasisdir}/share/template/wizard
%dir %{ooobasisdir}/share/template/wizard/letter
%{ooobasisdir}/share/template/wizard/letter/en-US

%dir %{ooobasisdir}/share/wordbook
%{ooobasisdir}/share/wordbook/en-US

%dir %{ooobasisdir}/share/xslt
%{ooobasisdir}/share/xslt/common
%dir %{ooobasisdir}/share/xslt/export
%{ooobasisdir}/share/xslt/export/common
%{ooobasisdir}/share/xslt/export/spreadsheetml
%{ooobasisdir}/share/xslt/export/uof
%{ooobasisdir}/share/xslt/export/wordml
%{ooobasisdir}/share/xslt/import

# symlink to directory
%attr(755,root,root) %{ooobasisdir}/ure-link

%dir %{_libdir}/%{name}/program
%attr(755,root,root) %{_libdir}/%{name}/program/libnpsoplugin.so
%attr(755,root,root) %{_libdir}/%{name}/program/oosplash.bin
%attr(755,root,root) %{_libdir}/%{name}/program/spadmin
%attr(755,root,root) %{_libdir}/%{name}/program/soffice
%attr(755,root,root) %{_libdir}/%{name}/program/soffice.bin
%attr(755,root,root) %{_libdir}/%{name}/program/unoinfo
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg.bin
%{_libdir}/%{name}/program/bootstraprc
%{_libdir}/%{name}/program/fundamentalrc
%{_libdir}/%{name}/program/openabout_pld.bmp
%{_libdir}/%{name}/program/openintro_pld.bmp
%{_libdir}/%{name}/program/redirectrc
%{_libdir}/%{name}/program/setuprc
#%dir %{_sysconfdir}/%{name}
%{_libdir}/%{name}/program/sofficerc
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/sofficerc
#%{_sysconfdir}/%{name}/unorc
%{_libdir}/%{name}/program/versionrc

%dir %{_libdir}/%{name}/program/resource
%{_libdir}/%{name}/program/resource/oooen-US.res

# symlinks
%{_libdir}/%{name}/basis-link
%{_libdir}/%{name}/licenses
%{_libdir}/%{name}/readmes
%{_libdir}/%{name}/share


%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/licenses
%{_datadir}/%{name}/licenses/LICENSE_en-US
%{_datadir}/%{name}/licenses/LICENSE_en-US.html
%dir %{_datadir}/%{name}/readmes
%{_datadir}/%{name}/readmes/README_en-US
%{_datadir}/%{name}/readmes/README_en-US.html
%dir %{_datadir}/%{name}/share
%dir %{_datadir}/%{name}/share/config
%{_datadir}/%{name}/share/config/images_brand.zip
%dir %{_datadir}/%{name}/share/readme
%{_datadir}/%{name}/share/readme/LICENSE_en-US*
%{_datadir}/%{name}/share/readme/README_en-US*
%dir %{_datadir}/%{name}/share/registry
%dir %{_datadir}/%{name}/share/registry/data
%dir %{_datadir}/%{name}/share/registry/data/org
%dir %{_datadir}/%{name}/share/registry/data/org/openoffice
%dir %{_datadir}/%{name}/share/registry/data/org/openoffice/Office
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Compatibility.xcu
%dir %{_datadir}/%{name}/share/registry/modules
%dir %{_datadir}/%{name}/share/registry/modules/org
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/Office
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-brand.xcu
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/UI
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/UI/UI-brand.xcu
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-brand.xcu


%{_datadir}/mime/packages/openoffice.xml

%{_desktopdir}/ootemplate.desktop
%{_desktopdir}/ooooo-extension-manager.desktop

%{_iconsdir}/hicolor/*/apps/ooo-gulls.png
%{_iconsdir}/hicolor/*/apps/ooo-printeradmin.png
%{_iconsdir}/hicolor/*/apps/ooo-template.png
%{_pixmapsdir}/ooo-gulls.png
%{_pixmapsdir}/ooo-template.png

%{_mandir}/man1/ooffice.1
%{_mandir}/man1/oofromtemplate.1
%{_mandir}/man1/openoffice.1*
%{_mandir}/man1/unopkg.1*

%if %{with kde}
%files libs-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{ooobasisdir}/program/kde-open-url
%attr(755,root,root) %{ooobasisdir}/program/kdebe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/kdefilepicker
%attr(755,root,root) %{ooobasisdir}/program/fps_kde.uno.so
%attr(755,root,root) %{ooobasisdir}/program/libkabdrv1.so
%attr(755,root,root) %{ooobasisdir}/program/libkab1.so
%attr(755,root,root) %{ooobasisdir}/program/libvclplug_kde*.so
%endif

%files libs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{ooobasisdir}/program/fps_gnome.uno.so
%attr(755,root,root) %{ooobasisdir}/program/gnome-open-url
%attr(755,root,root) %{ooobasisdir}/program/gnome-open-url.bin
%attr(755,root,root) %{ooobasisdir}/program/libevoab2.so
%attr(755,root,root) %{ooobasisdir}/program/libvclplug_gtk*.so
%if %{with gnomevfs}
%attr(755,root,root) %{ooobasisdir}/program/gconfbe1.uno.so
%attr(755,root,root) %{ooobasisdir}/program/ucpgvfs1.uno.so
%endif
## GIO files
#%attr(755,root,root) %{ooobasisdir}/program/ucpgio1.uno.so
#%{ooobasisdir}/share/registry/modules/org/openoffice/ucb/Configuration/Configuration-gio.xcu
##

%files base
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oobase
%attr(755,root,root) %{_libdir}/%{name}/program/sbase
%{_mandir}/man1/oobase.1
%{_desktopdir}/oobase.desktop
%{_iconsdir}/hicolor/*/apps/ooo-base.png
%{_pixmapsdir}/ooo-base.png
%attr(755,root,root) %{ooobasisdir}/program/libabpl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libadabasuil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdbpl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/librptl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/librptuil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/librptxmll[ipx].so
%{ooobasisdir}/program/resource/abpen-US.res
%{ooobasisdir}/program/resource/adabasuien-US.res
%{ooobasisdir}/program/resource/cnren-US.res
%{ooobasisdir}/program/resource/dbpen-US.res
%{ooobasisdir}/program/resource/dbuen-US.res
%{ooobasisdir}/program/resource/rpten-US.res
%{ooobasisdir}/program/resource/rptuien-US.res
%{ooobasisdir}/program/resource/sdbclen-US.res
%{ooobasisdir}/program/resource/sdberren-US.res
%{ooobasisdir}/share/config/soffice.cfg/modules/dbapp/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/dbapp/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbapp/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbapp/toolbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbbrowser/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/dbbrowser/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbbrowser/toolbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbquery/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/dbquery/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbquery/toolbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbrelation
%{ooobasisdir}/share/config/soffice.cfg/modules/dbreport/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/dbreport/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbreport/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbreport/toolbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbtable
%{ooobasisdir}/share/config/soffice.cfg/modules/dbtdata/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/dbtdata/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbtdata/toolbar
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/DbReportWindowState.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/ReportCommands.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Common/Common-base.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-report.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Setup/Setup-base.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Setup/Setup-report.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_database_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_database_others.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_database_types.xcu
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/ReportDesign.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/DbReportWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/ReportCommands.xcs
%{ooobasisdir}/help/en/sdatabase.*

%files calc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oocalc
%attr(755,root,root) %{_libdir}/%{name}/program/scalc
%{_mandir}/man1/oocalc.1
%{_desktopdir}/oocalc.desktop
%{_iconsdir}/hicolor/*/apps/ooo-calc.png
%{_pixmapsdir}/ooo-calc.png
%{ooobasisdir}/help/en/scalc.*
%attr(755,root,root) %{ooobasisdir}/program/libanalysisl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libcalcl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdatel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/liblpsolve55.so
%attr(755,root,root) %{ooobasisdir}/program/libscdl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libscl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libscuil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsolverl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libvbaobjl[ipx].uno.so
%{ooobasisdir}/program/resource/analysisen-US.res
%{ooobasisdir}/program/resource/dateen-US.res
%{ooobasisdir}/program/resource/solveren-US.res
%{ooobasisdir}/program/resource/scen-US.res
%{ooobasisdir}/share/config/soffice.cfg/modules/scalc/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/scalc/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/scalc/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/scalc/toolbar
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/CalcCommands.xcu
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/CalcWindowState.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Common/Common-calc.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-calc.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Setup/Setup-calc.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_calc_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_calc_types.xcu
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/CalcCommands.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/CalcWindowState.xcs

#BF
%{ooobasisdir}/program/resource/bf_scen-US.res
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_calc_bf_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_calc_bf_types.xcu

%files draw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oodraw
%attr(755,root,root) %{_libdir}/%{name}/program/sdraw
%{_mandir}/man1/oodraw.1
%{_desktopdir}/oodraw.desktop
%{_iconsdir}/hicolor/*/apps/ooo-draw.png
%{_pixmapsdir}/ooo-draw.png
%{ooobasisdir}/help/en/sdraw.*
%{ooobasisdir}/share/config/soffice.cfg/modules/sdraw/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/sdraw/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/sdraw/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/sdraw/toolbar
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/DrawWindowState.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Common/Common-draw.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-draw.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Setup/Setup-draw.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_draw_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_draw_types.xcu
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/DrawWindowState.xcs

#BF
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_draw_bf_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_draw_bf_types.xcu

%files emailmerge
%defattr(644,root,root,755)
%{ooobasisdir}/program/mailmerge.py*
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Writer/Writer-javamail.xcu

%files writer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oowriter
%attr(755,root,root) %{ooobasisdir}/program/libhwp.so
%attr(755,root,root) %{ooobasisdir}/program/liblwpftl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libmsworksl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libswdl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libswuil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libt602filterl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libwpftl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libwriterfilterl[ipx].so
%attr(755,root,root) %{_libdir}/%{name}/program/swriter
%{_mandir}/man1/oowriter.1
%{_desktopdir}/oowriter.desktop
%{_iconsdir}/hicolor/*/apps/ooo-writer.png
%{_pixmapsdir}/ooo-writer.png
%{ooobasisdir}/help/en/swriter.*
%if %{with java}
%{ooobasisdir}/program/classes/writer2latex.jar
%endif
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/WriterCommands.xcu
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/WriterCommands.xcs
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/WriterGlobalWindowState.xcu
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/WriterGlobalWindowState.xcs
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/WriterWebWindowState.xcu
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/WriterWebWindowState.xcs
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/WriterWindowState.xcs
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/WriterWindowState.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Common/Common-writer.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Setup/Setup-writer.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-writer.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_global_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_writer_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_global_types.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_writer_types.xcu
%{ooobasisdir}/share/xslt/wiki
%{ooobasisdir}/program/resource/t602filteren-US.res
%{ooobasisdir}/share/config/soffice.cfg/modules/sbibliography
%{ooobasisdir}/share/config/soffice.cfg/modules/swriter/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/swriter/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/swriter/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/swriter/toolbar

#BF
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_writer_bf_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_writer_bf_types.xcu

%files impress
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ooimpress
%attr(755,root,root) %{_libdir}/%{name}/program/simpress
%attr(755,root,root) %{ooobasisdir}/program/libanimcore.so
%attr(755,root,root) %{ooobasisdir}/program/libplaceware*.so
%{_mandir}/man1/ooimpress.1
%{_desktopdir}/ooimpress.desktop
%{_iconsdir}/hicolor/*/apps/ooo-impress.png
%{_pixmapsdir}/ooo-impress.png
%{ooobasisdir}/help/en/simpress.*
%{ooobasisdir}/share/config/soffice.cfg/simpress
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/Effects.xcu
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/Effects.xcs
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/ImpressWindowState.xcu
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/ImpressWindowState.xcs
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Common/Common-impress.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-impress.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Setup/Setup-impress.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_impress_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_impress_types.xcu
%{ooobasisdir}/share/config/soffice.cfg/modules/simpress/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/simpress/accelerator/default.xml
%{ooobasisdir}/share/config/soffice.cfg/modules/simpress/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/simpress/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/simpress/toolbar

#BF
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_impress_bf_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_impress_bf_types.xcu

%files math
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oomath
%{_mandir}/man1/oomath.1
%{_desktopdir}/oomath.desktop
%{_iconsdir}/hicolor/*/apps/ooo-math.png
%{_pixmapsdir}/ooo-math.png
%{ooobasisdir}/help/en/smath.*
%attr(755,root,root) %{ooobasisdir}/program/libsmdl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsml[ipx].so
%attr(755,root,root) %{_libdir}/%{name}/program/smath
%{ooobasisdir}/share/dtd/math
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/MathCommands.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Common/Common-math.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Setup/Setup-math.xcu
%{ooobasisdir}/share/registry/schema/org/openoffice/Office/UI/MathCommands.xcs
%{ooobasisdir}/share/registry/data/org/openoffice/Office/UI/MathWindowState.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-math.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_math_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_math_types.xcu
%{ooobasisdir}/program/resource/smen-US.res
%{ooobasisdir}/share/config/soffice.cfg/modules/smath

#BF
%{ooobasisdir}/program/resource/bf_smen-US.res
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_math_bf_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_math_bf_types.xcu

%files web
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ooweb
%{_mandir}/man1/ooweb.1
%{_desktopdir}/ooweb.desktop
%{_iconsdir}/hicolor/*/apps/ooo-web.png
%{_pixmapsdir}/ooo-web.png
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_web_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_web_types.xcu
%{ooobasisdir}/share/config/soffice.cfg/modules/sweb/accelerator/en-US
%{ooobasisdir}/share/config/soffice.cfg/modules/sweb/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/sweb/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/sweb/toolbar

#BF
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_web_bf_types.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_web_bf_filters.xcu

%files graphicfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{ooobasisdir}/program/libflashl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsvgfilterl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libwpgimportl[ipx].so
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_drawgraphics_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_impressgraphics_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_drawgraphics_types.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_impressgraphics_types.xcu

%files xsltfilter
%defattr(644,root,root,755)
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_xslt_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_xslt_types.xcu
%{ooobasisdir}/share/xslt/docbook
%{ooobasisdir}/share/xslt/export/xhtml
%{ooobasisdir}/share/xslt/odfflatxml

%if %{with java}
%files javafilter
%defattr(644,root,root,755)
%{ooobasisdir}/program/classes/pexcel.jar
%{ooobasisdir}/program/classes/pocketword.jar
%{ooobasisdir}/program/classes/aportisdoc.jar
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_palm_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_pocketexcel_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_pocketword_filters.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_palm_types.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_pocketexcel_types.xcu
%{ooobasisdir}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_pocketword_types.xcu
%endif

%files testtools
%defattr(644,root,root,755)
%attr(755,root,root) %{ooobasisdir}/program/libcommunil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsimplecml[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/testtool.bin
%{ooobasisdir}/program/resource/stten-US.res
%{ooobasisdir}/program/hid.lst
%{ooobasisdir}/program/testtoolrc

%files ure
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/ure
%dir %{_libdir}/%{name}/ure/bin
%attr(755,root,root) %{_libdir}/%{name}/ure/bin/regcomp
%attr(755,root,root) %{_libdir}/%{name}/ure/bin/regcomp.bin
%attr(755,root,root) %{_libdir}/%{name}/ure/bin/regmerge
%attr(755,root,root) %{_libdir}/%{name}/ure/bin/regview
%attr(755,root,root) %{_libdir}/%{name}/ure/bin/startup.sh
%attr(755,root,root) %{_libdir}/%{name}/ure/bin/uno
%attr(755,root,root) %{_libdir}/%{name}/ure/bin/uno.bin
%{_libdir}/%{name}/ure/bin/versionrc
%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/ure/bin/javaldx
%endif
%dir %{_libdir}/%{name}/ure/lib
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/namingservice.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libaffine_uno_uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/bootstrap.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/acceptor.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/bridgefac.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/connector.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/introspection.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/invocadapt.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/proxyfac.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/reflection.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/remotebridge.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libunsafe_uno_uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/streams.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/textinstream.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/textoutstream.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/uuresolver.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libstore.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libuno_cppu.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libuno_cppuhelpergcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libuno_purpenvhelpergcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libuno_sal.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libuno_salhelpergcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/liburp_uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/stocservices.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/invocation.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libgcc3_uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjvmaccessgcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjvmfwk.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libreg.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/librmcxt.so.3
%{_libdir}/%{name}/ure/lib/jvmfwk3rc
%{_libdir}/%{name}/ure/lib/unorc
%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjava_uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjuh.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjuhx.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/sunjavaplugin.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/javaloader.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/javavm.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjpipe.so
%{_libdir}/%{name}/ure/lib/JREProperties.class
%endif
%dir %{_libdir}/%{name}/ure/share
%if %{with java}
%dir %{_libdir}/%{name}/ure/share/java
%{_libdir}/%{name}/ure/share/java/java_uno.jar
%{_libdir}/%{name}/ure/share/java/juh.jar
%{_libdir}/%{name}/ure/share/java/jurt.jar
%{_libdir}/%{name}/ure/share/java/ridl.jar
%{_libdir}/%{name}/ure/share/java/unoloader.jar
%endif
%dir %{_libdir}/%{name}/ure/share/misc
%{_libdir}/%{name}/ure/share/misc/services.rdb
%{_libdir}/%{name}/ure/share/misc/types.rdb
%if %{with java}
%{_libdir}/%{name}/ure/share/misc/javavendors.xml
%endif

%files pyuno
%defattr(644,root,root,755)
%attr(755,root,root) %{ooobasisdir}/program/libpyuno.so
%attr(755,root,root) %{ooobasisdir}/program/pythonloader.uno.so
%attr(755,root,root) %{ooobasisdir}/program/pyuno.so
%{ooobasisdir}/program/pythonloader.unorc
%{ooobasisdir}/program/officehelper.py
%{ooobasisdir}/program/pythonloader.py
%{ooobasisdir}/program/pythonscript.py
%{ooobasisdir}/program/uno.py
%{ooobasisdir}/program/unohelper.py
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Scripting/Scripting-python.xcu

# samples there
%{ooobasisdir}/share/Scripts/python

%if %{with mozilla}
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libnpsoplugin.so
%attr(755,root,root) %{ooobasisdir}/program/nsplugin
%endif

%if %{with i18n}
%files i18n-af -f af.lang
%defattr(644,root,root,755)

%files i18n-ar -f ar.lang
%defattr(644,root,root,755)

%files i18n-as_IN -f as_IN.lang
%defattr(644,root,root,755)

%files i18n-be_BY -f be_BY.lang
%defattr(644,root,root,755)

%files i18n-bg -f bg.lang
%defattr(644,root,root,755)

%files i18n-bn -f bn.lang
%defattr(644,root,root,755)

%files i18n-bn_BD -f bn_BD.lang
%defattr(644,root,root,755)

%files i18n-bn_IN -f bn_IN.lang
%defattr(644,root,root,755)

%files i18n-br -f br.lang
%defattr(644,root,root,755)

%files i18n-bs -f bs.lang
%defattr(644,root,root,755)

%files i18n-by -f by.lang
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
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbreport/accelerator/de-DE
%{ooobasisdir}/share/config/soffice.cfg/modules/dbreport/accelerator/de-DE/default.xml

%files i18n-dz -f dz.lang
%defattr(644,root,root,755)

%files i18n-el -f el.lang
%defattr(644,root,root,755)

%files i18n-en_GB -f en_GB.lang
%defattr(644,root,root,755)

%files i18n-en_ZA -f en_ZA.lang
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

%files i18n-fr -f fr.lang
%defattr(644,root,root,755)

%files i18n-ga -f ga.lang
%defattr(644,root,root,755)

%files i18n-gd -f gd.lang
%defattr(644,root,root,755)

%files i18n-gl -f gl.lang
%defattr(644,root,root,755)

%files i18n-gu_IN -f gu_IN.lang
%defattr(644,root,root,755)

%files i18n-gu -f gu.lang
%defattr(644,root,root,755)

%files i18n-he -f he.lang
%defattr(644,root,root,755)

%files i18n-hi_IN -f hi_IN.lang
%defattr(644,root,root,755)

%files i18n-hr -f hr.lang
%defattr(644,root,root,755)

%files i18n-hu -f hu.lang
%defattr(644,root,root,755)

%files i18n-it -f it.lang
%defattr(644,root,root,755)

%files i18n-ja -f ja.lang
%defattr(644,root,root,755)

%files i18n-ka -f ka.lang
%defattr(644,root,root,755)

%files i18n-km -f km.lang
%defattr(644,root,root,755)

%files i18n-kn_IN -f kn.lang
%defattr(644,root,root,755)

%files i18n-ko -f ko.lang
%defattr(644,root,root,755)
%{ooobasisdir}/share/registry/modules/org/openoffice/Office/Common/Common-korea.xcu

%files i18n-ku -f ku.lang
%defattr(644,root,root,755)

%files i18n-lo -f lo.lang
%defattr(644,root,root,755)

%files i18n-lt -f lt.lang
%defattr(644,root,root,755)

%files i18n-lv -f lv.lang
%defattr(644,root,root,755)

%files i18n-mk -f mk.lang
%defattr(644,root,root,755)

%files i18n-ml_IN -f ml_IN.lang
%defattr(644,root,root,755)

%files i18n-mn -f mn.lang
%defattr(644,root,root,755)

%files i18n-mr_IN -f mr_IN.lang
%defattr(644,root,root,755)

%files i18n-ms -f ms.lang
%defattr(644,root,root,755)

%files i18n-my -f my.lang
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

%files i18n-oc -f oc.lang
%defattr(644,root,root,755)

%files i18n-or_IN -f or_IN.lang
%defattr(644,root,root,755)

%files i18n-pa_IN -f pa_IN.lang
%defattr(644,root,root,755)

%files i18n-pl -f pl.lang
%defattr(644,root,root,755)

%files i18n-pt -f pt.lang
%defattr(644,root,root,755)

%files i18n-pt_BR -f pt_BR.lang
%defattr(644,root,root,755)

%files i18n-ru -f ru.lang
%defattr(644,root,root,755)

%files i18n-rw -f rw.lang
%defattr(644,root,root,755)

%files i18n-sh -f sh.lang
%defattr(644,root,root,755)

%files i18n-sk -f sk.lang
%defattr(644,root,root,755)

%files i18n-sl -f sl.lang
%defattr(644,root,root,755)

%files i18n-sr -f sr.lang
%defattr(644,root,root,755)

%files i18n-ss -f ss.lang
%defattr(644,root,root,755)

%files i18n-st -f st.lang
%defattr(644,root,root,755)

%files i18n-sv -f sv.lang
%defattr(644,root,root,755)

%files i18n-sw -f sw.lang
%defattr(644,root,root,755)

%files i18n-sw_TZ -f sw_TZ.lang
%defattr(644,root,root,755)

%files i18n-ta_IN -f ta_IN.lang
%defattr(644,root,root,755)

%files i18n-te_IN -f te_IN.lang
%defattr(644,root,root,755)

%files i18n-tg -f tg.lang
%defattr(644,root,root,755)

%files i18n-th -f th.lang
%defattr(644,root,root,755)

%files i18n-ti_ER -f ti_ER.lang
%defattr(644,root,root,755)

%files i18n-tn -f tn.lang
%defattr(644,root,root,755)

%files i18n-tr -f tr.lang
%defattr(644,root,root,755)

%files i18n-ts -f ts.lang
%defattr(644,root,root,755)

%files i18n-uk -f uk.lang
%defattr(644,root,root,755)

%files i18n-ur_IN -f ur_IN.lang
%defattr(644,root,root,755)

%files i18n-uz -f uz.lang
%defattr(644,root,root,755)

%files i18n-ve -f ve.lang
%defattr(644,root,root,755)

%files i18n-vi -f vi.lang
%defattr(644,root,root,755)

%files i18n-xh -f xh.lang
%defattr(644,root,root,755)

%files i18n-zh_CN -f zh_CN.lang
%defattr(644,root,root,755)

%files i18n-zh_TW -f zh_TW.lang
%defattr(644,root,root,755)

%files i18n-zu -f zu.lang
%defattr(644,root,root,755)
%endif

%files -n bash-completion-openoffice
%defattr(644,root,root,755)
/etc/bash_completion.d/*
