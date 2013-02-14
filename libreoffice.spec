# TODO:
# - fix configure arguments (+ compare with FC)
#
# NOTE - FIXME FOR 3.4.3 !!!:
#	- normal build (i686) requires about 27 GB of disk space:
#		$BUILD_ROOT	7.0 GB
#		BUILD		18  GB
#		RPMS		1.8 GB
#		SRPMS		0.4 GB
#
# Conditional build:
%bcond_without	java		# without Java support (disables help support)
%bcond_with	kde		# KDE L&F packages
%bcond_without	kde4		# KDE4 L&F packages
%bcond_with	mono		# enable compilation of mono bindings
%bcond_without	mozilla		# without mozilla components
%bcond_without	i18n        # do not create i18n packages (extra build time)
%bcond_with	ccache		# use ccache to speed up builds
%bcond_with	icecream	# use icecream to speed up builds
%bcond_with	msaccess	# with ms access import pieces
%bcond_without	parallelbuild	# use greater number of jobs to speed up build (default: 1)
%bcond_without	binfilter	# build without old binary filters

%bcond_without	system_beanshell
%bcond_without	system_db		# without system (i.e. with internal) Berkeley DB
%bcond_with	system_libhnj		# with system ALTLinuxhyph (NFY)
%bcond_without	system_mdbtools		# with system mdbtools
%bcond_without	system_xalan
%bcond_with	system_hsqldb
%bcond_with	system_agg		# with system agg
%bcond_without	system_hunspell
%bcond_without	system_myspell

# this list is same as icedtea6
%ifnarch i486 i586 i686 pentium3 pentium4 athlon %{x8664}
%undefine	with_java
%endif

%if %{without java}
%undefine	with_system_beanshell
%undefine	with_system_xalan
%undefine	with_system_hsqldb
%endif

%define		major_ver		4.0.0

Summary:	LibreOffice - powerful office suite
Summary(pl.UTF-8):	LibreOffice - potężny pakiet biurowy
Name:		libreoffice
Version:	%{major_ver}.3
Release:	0.1
License:	GPL/LGPL
Group:		X11/Applications
# we use git because released tarballs are buggy too often
# git clone git://anongit.freedesktop.org/git/libreoffice/build
# cd build
# git checkout -b libreoffice-3-3 origin/libreoffice-3-3
Source0:	http://download.documentfoundation.org/libreoffice/src/%{major_ver}/%{name}-%{version}.tar.xz
# Source0-md5:	a3c01489036823e9f5b5caf3a8db1f9e
Source1:	http://download.documentfoundation.org/libreoffice/src/%{major_ver}/%{name}-dictionaries-%{version}.tar.xz
# Source1-md5:	99b7a045525411c9148331ab04bdedff
Source2:	http://download.documentfoundation.org/libreoffice/src/%{major_ver}/%{name}-help-%{version}.tar.xz
# Source2-md5:	716f624d7a39b99da8a5d550b6a87875
Source3:	http://download.documentfoundation.org/libreoffice/src/%{major_ver}/%{name}-translations-%{version}.tar.xz
# Source3-md5:	09ec7331354c6f9a0b2f48efe344ce7d

Source20:       http://dev-www.libreoffice.org/src/0168229624cfac409e766913506961a8-ucpp-1.3.2.tar.gz
# Source20-md5:	0168229624cfac409e766913506961a8
Source21:	http://dev-www.libreoffice.org/src/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip
# Source21-md5:	17410483b5b5f267aa18b7e00b65e6e0
Source22:	http://dev-www.libreoffice.org/src/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz
# Source22-md5:	1f24ab1d39f4a51faf22244c94a6203f
Source23:	http://dev-www.libreoffice.org/src/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
# Source23-md5:	798b2ffdc8bcfe7bca2cf92b62caf685
Source24:	http://dev-www.libreoffice.org/src/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip
# Source24-md5:	35c94d2df8893241173de1d16b6034c0
Source25:	http://dev-www.libreoffice.org/src/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
# Source25-md5:	a7983f859eafb2677d7ff386a023bc40

Patch0:		%{name}-hamcrest.patch
URL:		http://www.documentfoundation.org/
BuildRequires:	/usr/bin/getopt
BuildRequires:	GConf2-devel
BuildRequires:	ImageMagick
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
%{?with_system_agg:BuildRequires:	agg-devel}
BuildRequires:	atk-devel >= 1:1.9.0
BuildRequires:	autoconf >= 2.51
BuildRequires:	automake >= 1:1.9
BuildRequires:	bash
BuildRequires:	bison >= 1.875-4
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	cairo-devel >= 1.2.0
%{?with_ccache:BuildRequires:	ccache}
BuildRequires:	clucene-core-devel >= 2.3
BuildRequires:	cppunit-devel >= 1.12.0
BuildRequires:	cups-devel
BuildRequires:	curl-devel >= 7.9.8
%{?with_system_db:BuildRequires:	db-cxx-devel}
%{?with_system_db:BuildRequires:	db-devel}
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	glib2-devel >= 2.13.5
BuildRequires:	gperf
BuildRequires:	graphite2-devel
BuildRequires:	gstreamer-devel >= 0.10.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	gtk+2-devel >= 2:2.10
%{?with_system_hunspell:BuildRequires:	hunspell-devel >=1.2.2}
BuildRequires:	hyphen-devel
%{?with_icecream:BuildRequires:	icecream}
BuildRequires:	icu
%{?with_system_beanshell:BuildRequires:	java-beanshell}
BuildRequires:	java-commons-codec
BuildRequires:	java-commons-httpclient
BuildRequires:	java-commons-lang
BuildRequires:	java-commons-logging
BuildRequires:	java-flow-engine
BuildRequires:	java-hamcrest
%{?with_system_hsqldb:BuildRequires:	java-hsqldb}
BuildRequires:	java-junit
BuildRequires:	java-lucene
BuildRequires:	java-lucene-contrib
BuildRequires:	java-servletapi
BuildRequires:	libcmis-devel >= 0.3
BuildRequires:	liblangtag-devel
BuildRequires:	libmspub-devel
BuildRequires:	liborcus-devel
BuildRequires:	libvisio-devel
BuildRequires:	libwpd-devel >= 0.9.0
BuildRequires:	libwpg-devel >= 0.2.0
BuildRequires:	libwps-devel >= 0.2.0
BuildRequires:	lp_solve-devel
BuildRequires:	silgraphite-devel
%if %{with kde}
BuildRequires:	kde4-kde3support-devel
%endif
%if %{with kde4}
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	qt4-build
%endif
BuildRequires:	java-libxml
BuildRequires:	java-sac
BuildRequires:	libart_lgpl-devel
BuildRequires:	libbonobo-devel >= 2.0
BuildRequires:	libcdr-devel >= 0.0.8
%{?with_system_libhnj:BuildRequires:	libhnj-devel}
BuildRequires:	libicu-devel >= 4.0
BuildRequires:	libjpeg-devel
BuildRequires:	librsvg-devel >= 2.14
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel >= 5:3.2.1
BuildRequires:	libsvg-devel >= 0.1.4
BuildRequires:	libexttextcat-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel
BuildRequires:	libxslt-progs
%{?with_access:%{?with_system_mdbtools:BuildRequires:	mdbtools-devel >= 0.6}}
BuildRequires:	mdds-devel >= 0.6.0
%{?with_mono:BuildRequires:	mono-csharp >= 1.2.3}
%{?with_mono:BuildRequires:	mono-static >= 1.2.3}
%{?with_system_myspell:BuildRequires:	myspell-devel}
BuildRequires:	mythes-devel
BuildRequires:	nas-devel >= 1.7-1
BuildRequires:	neon-devel
BuildRequires:	nspr-devel >= 1:4.6-0.20041030.3
BuildRequires:	nss-devel >= 1:3.10
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	pango-devel >= 1:1.17.3
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-base
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	poppler-cpp-devel >= 0.8.0
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
BuildRequires:	unixODBC-devel >= 2.2.12-2
BuildRequires:	unzip
BuildRequires:	vigra-devel
%{?with_system_xalan:BuildRequires:	xalan-j}
BuildRequires:	xorg-font-font-adobe-utopia-type1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	zip >= 3.0
BuildRequires:	zlib-devel
%if %{with java}
BuildRequires:	ant >= 1.7.0
BuildRequires:	ant-apache-regexp
%{?with_system_db:BuildRequires:	db-java >= 4.3}
BuildRequires:	jdk >= 1.4.0_00
BuildRequires:	jre-X11
%endif
BuildRequires:	xulrunner-devel
BuildConflicts:	xmlsec1-devel
# contains (dlopened) *.so libs
BuildConflicts:	java-gcj-compat
BuildConflicts:	xmlsec1-nss
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-calc = %{version}-%{release}
Requires:	%{name}-draw = %{version}-%{release}
Requires:	%{name}-emailmerge = %{version}-%{release}
Requires:	%{name}-graphicfilter = %{version}-%{release}
Requires:	%{name}-impress = %{version}-%{release}
%{?with_java:Requires:	%{name}-javafilter = %{version}-%{release}}
Requires:	%{name}-math = %{version}-%{release}
Requires:	%{name}-pdfimport = %{version}-%{release}
Requires:	%{name}-postgresql = %{version}-%{release}
Requires:	%{name}-presentation-minimizer = %{version}-%{release}
Requires:	%{name}-presenter-screen = %{version}-%{release}
Requires:	%{name}-pyuno = %{version}-%{release}
Requires:	%{name}-report-builder = %{version}-%{release}
Requires:	%{name}-web = %{version}-%{release}
Requires:	%{name}-wiki-publisher = %{version}-%{release}
Requires:	%{name}-writer = %{version}-%{release}
Requires:	%{name}-xsltfilter = %{version}-%{release}
Obsoletes:	openoffice.org
Obsoletes:	openoffice.org-testtools
Obsoletes:	libreoffice-testtools
ExclusiveArch:	%{ix86} %{x8664} ppc sparc sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing -O2

# No ELF objects there to strip/chrpath, skips processing:
# - share/ - 17000 files of 415M
# - help/ - 6500 files of 1.4G
# - program/resource/ - 5610 files of 216M
%define		_noautostrip	.*\\(%{_datadir}\\|%{_libdir}/%{name}/program/resource\\)/.*
%define		_noautochrpath	.*\\(%{_datadir}\\|%{_libdir}/%{name}/program/resource\\)/.*

%description
LibreOffice is an open-source project sponsored by Sun Microsystems
and hosted by CollabNet. In October of 2000, Sun released the source
code of its popular StarOfficeTM productivity suite under open-source
licenses. The aim of the LibreOffice project is to create, using
open-source methods, the next generation of open-network productivity
services, including the establishment of open, XML-based standards for
office productivity file formats and language-independent bindings to
component APIs.

Features of LibreOffice include:
 - Downloadable source code,
 - CVS control, and
 - Infrastructure for community involvement, including guidelines and
   discussion groups.

%description -l pl.UTF-8
LibreOffice jest projektem open-source sponsorowanym przez Sun
Microsystems i przechowywanym przez CollabNet. W październiku 2000
roku Sun udostępnił kod źródłowy popularnego pakietu biurowego
StarOfficeTM na zasadach licencji open-source. Głównym celem
LibreOffice jest stworzenie sieciowego pakietu biurowego następnej
generacji, wykorzystując open-source'owe metody pracy.

Do zalet LibreOffice można zaliczyć:
 - dostępny cały czas kod źródłowy,
 - kontrola CVS,
 - infrastruktura służąca do komunikowania się w ramach projektu.

%package libs-kde
Summary:	LibreOffice KDE Interface
Summary(pl.UTF-8):	Interfejs KDE dla LibreOffice
Group:		X11/Libraries
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en-kde
Obsoletes:	openoffice-libs-kde
Obsoletes:	openoffice.org-libs-kde

%description libs-kde
LibreOffice productivity suite - KDE Interface.

%description libs-kde -l pl.UTF-8
Pakiet biurowy LibreOffice - Interfejs KDE.

%package libs-gtk
Summary:	LibreOffice GTK+ Interface
Summary(pl.UTF-8):	Interfejs GTK+ dla LibreOffice
Group:		X11/Libraries
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en-gtk
Obsoletes:	openoffice-libs-gtk
Obsoletes:	openoffice.org-libs-gtk

%description libs-gtk
LibreOffice productivity suite - GTK+ Interface.

%description libs-gtk -l pl.UTF-8
Pakiet biurowy LibreOffice - Interfejs GTK+.

%package core
Summary:	Core modules for LibreOffice
Summary(pl.UTF-8):	Podstawowe moduły dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	%{name}-ure = %{version}-%{release}
# libcups.so.2 is dlopened (in cupsmgr.cxx); maybe Suggests instead?
Requires:	cups-lib
Requires:	fonts-TTF-OpenSymbol
Requires:	hicolor-icon-theme
%{?with_system_beanshell:Requires:	java-beanshell}
%{?with_system_hsqldb:Requires:	java-hsqldb}
Requires:	libstdc++ >= 5:3.2.1
Requires:	mktemp
Requires:	saxon
Requires:	sed
%{?with_system_xalan:Requires:	xalan-j}
#Suggests:	chkfontpath
Obsoletes:	libreoffice-i18n-kid
Obsoletes:	libreoffice-i18n-ky
Obsoletes:	libreoffice-i18n-ms
Obsoletes:	libreoffice-i18n-pap
Obsoletes:	libreoffice-i18n-ps
Obsoletes:	libreoffice-i18n-sc
Obsoletes:	libreoffice-i18n-ti
Obsoletes:	libreoffice-i18n-ur
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
Obsoletes:	openoffice.org-core
Obsoletes:	openoffice.org-dirs
Obsoletes:	openoffice.org-i18n-bn_BD
Obsoletes:	openoffice.org-i18n-by
Obsoletes:	openoffice.org-i18n-fo
Obsoletes:	openoffice.org-i18n-fo-gtk
Obsoletes:	openoffice.org-i18n-fo-kde
Obsoletes:	openoffice.org-i18n-gu_IN
Obsoletes:	openoffice.org-i18n-ia
Obsoletes:	openoffice.org-i18n-ia-gtk
Obsoletes:	openoffice.org-i18n-ia-kde
Obsoletes:	openoffice.org-i18n-id
Obsoletes:	openoffice.org-i18n-id-gtk
Obsoletes:	openoffice.org-i18n-id-kde
Obsoletes:	openoffice.org-i18n-kid
Obsoletes:	openoffice.org-i18n-ky
Obsoletes:	openoffice.org-i18n-la
Obsoletes:	openoffice.org-i18n-la-gtk
Obsoletes:	openoffice.org-i18n-la-kde
Obsoletes:	openoffice.org-i18n-med
Obsoletes:	openoffice.org-i18n-med-gtk
Obsoletes:	openoffice.org-i18n-med-kde
Obsoletes:	openoffice.org-i18n-mi
Obsoletes:	openoffice.org-i18n-mi-gtk
Obsoletes:	openoffice.org-i18n-mi-kde
Obsoletes:	openoffice.org-i18n-ms
Obsoletes:	openoffice.org-i18n-pap
Obsoletes:	openoffice.org-i18n-ro
Obsoletes:	openoffice.org-i18n-ro-gtk
Obsoletes:	openoffice.org-i18n-ro-kde
Obsoletes:	openoffice.org-i18n-sc
Obsoletes:	openoffice.org-i18n-sw
Obsoletes:	openoffice.org-i18n-sx
Obsoletes:	openoffice.org-i18n-ti
Obsoletes:	openoffice.org-i18n-ur
Obsoletes:	openoffice.org-libs < 1:2.1.0-0.m6.0.11

%description core
Core libraries and support files for LibreOffice.

%description core -l pl.UTF-8
Podstawowe moduły dla LibreOffice.

%package pyuno
Summary:	Python bindings for LibreOffice
Summary(pl.UTF-8):	Wiązania Pythona dla LibreOffice
Group:		Libraries
Requires:	%{name}-core = %{version}-%{release}
Requires:	python
Provides:	pyuno
Obsoletes:	openoffice.org-pyuno

%description pyuno
Cool Python bindings for the LibreOffice UNO component model. Allows
scripts both external to LibreOffice and within the internal
LibreOffice scripting module to be written in Python.

%description pyuno -l pl.UTF-8
Wiązania Pythona dla modelu komponentów UNO LibreOffice. Pozwala na
oskryptowanie zarówno na zewnątrz LibreOffice, jak i na używanie
skryptów w Pythonie w wewnętrznym module skryptów LibreOffice.

%package pdfimport
Summary:	PDF Importer for LibreOffice Draw
Group:		X11/Applications
Requires:	%{name}-draw = %{version}-%{release}

%description pdfimport
The PDF Importer imports PDF into drawing documents to preserve layout
and enable basic editing of PDF documents.

%package presentation-minimizer
Summary:	Shrink LibreOffice presentations
Group:		X11/Applications
Requires:	%{name}-impress = %{version}-%{release}

%description presentation-minimizer
The Presentation Minimizer is used to reduce the file size of the
current presentation. Images will be compressed, and data that is no
longer needed will be removed.

%package presenter-screen
Summary:	Presenter Screen for LibreOffice presentations
Group:		X11/Applications
Requires:	%{name}-impress = %{version}-%{release}

%description presenter-screen
The Presenter Screen is used to provides information on a second
screen, that typically is not visible to the audience when delivering
a presentation. e.g. slide notes.

%package report-builder
Summary:	Create database reports from LibreOffice
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Requires:	java-commons-logging

%description report-builder
Creates database reports from LibreOffice databases. The report
builder can define group and page headers as well as group, page
footers and calculation fields to accomplish complex database reports.

%package wiki-publisher
Summary:	Create Wiki articles on MediaWiki servers with LibreOffice
Group:		X11/Applications
Requires:	%{name}-writer = %{version}-%{release}
Requires:	java-commons-codec
Requires:	java-commons-httpclient
Requires:	java-commons-lang
Requires:	java-commons-logging

%description wiki-publisher
The Wiki Publisher enables you to create Wiki articles on MediaWiki
servers without having to know the syntax of the MediaWiki markup
language. Publish your new and existing documents transparently with
writer to a wiki page.

%package base
Summary:	Database frontend for LibreOffice
Summary(pl.UTF-8):	Frontend do baz danych dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-base

%description base
GUI database frontend for LibreOffice. Allows creation and management
of databases through a GUI.

%description base -l pl.UTF-8
Graficzny frontend do baz danych dla LibreOffice. Pozwala na tworzenie
i zarządzanie bazami poprzez graficzny interfejs użytkownika.

%package web
Summary:	Web module for LibreOffice
Summary(pl.UTF-8):	Moduł Web dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-writer = %{version}-%{release}
Obsoletes:	openoffice.org-web

%description web
Web publishing application of LibreOffice.

%description web -l pl.UTF-8
Aplikacja do tworzenia stron WWW z LibreOffice.

%package writer
Summary:	Writer module for LibreOffice
Summary(pl.UTF-8):	Moduł Writer dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-writer

%description writer
Wordprocessor application of LibreOffice.

%description writer -l pl.UTF-8
Procesor tekstu z LibreOffice.

%package emailmerge
Summary:	email mail merge component for LibreOffice
Summary(pl.UTF-8):	Kompolent email mail merge dla LibreOffice
Group:		X11/Applications
Requires:	%{name}-pyuno = %{version}-%{release}
Requires:	%{name}-writer = %{version}-%{release}
Obsoletes:	openoffice.org-emailmerge

%description emailmerge
Enables LibreOffice Writer module to enable mail merge to email.

%description emailmerge -l pl.UTF-8
Komponent umożliwiający modułowi Writer włączanie poczty do poczty
elektronicznej.

%package calc
Summary:	Calc module for LibreOffice
Summary(pl.UTF-8):	Moduł Calc dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-calc

%description calc
Spreadsheet application of LibreOffice.

%description calc -l pl.UTF-8
Arkusz kalkulacyjny z LibreOffice.

%package draw
Summary:	Draw module for LibreOffice
Summary(pl.UTF-8):	Moduł Draw dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-draw

%description draw
Drawing application of LibreOffice.

%description draw -l pl.UTF-8
Aplikacja rysunkowa z LibreOffice.

%package impress
Summary:	Impress module for LibreOffice
Summary(pl.UTF-8):	Moduł Impress dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-impress

%description impress
Presentation application of LibreOffice.

%description impress -l pl.UTF-8
Aplikacja do tworzenia prezentacji z LibreOffice.

%package math
Summary:	Math module for LibreOffice
Summary(pl.UTF-8):	Moduł Math dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-core = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	openoffice.org-math

%description math
Math editor of LibreOffice.

%description math -l pl.UTF-8
Edytor równań matematycznych z LibreOffice.

%package graphicfilter
Summary:	Extra graphicfilter module for LibreOffice
Summary(pl.UTF-8):	Dodatkowy moduł graphicfilter dla LibreOffice
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-graphicfilter

%description graphicfilter
Graphicfilter module for LibreOffice, provides additional SVG and
Flash export filters.

%description graphicfilter -l pl.UTF-8
Moduł graphicfilter dla LibreOffice, udostępnia dodatkowe filtry
eksportu SVG i Flash.

%package xsltfilter
Summary:	Extra xsltfilter module for LibreOffice
Summary(pl.UTF-8):	Dodatkowy moduł xsltfilter dla LibreOffice
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-xsltfilter

%description xsltfilter
xsltfilter module for LibreOffice, provides additional docbook and
xhtml export transforms. Install this to enable docbook export.

%description xsltfilter -l pl.UTF-8
Moduł xsltfilter dla LibreOffice, udostępnia dodatkowe przekształcenia
wyjściowe dla formatów docbook i xhtml. Jest potrzebny do eksportu do
docbooka.

%package javafilter
Summary:	Extra javafilter module for LibreOffice
Summary(pl.UTF-8):	Dodatkowy moduł javafilter dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-javafilter

%description javafilter
javafilter module for LibreOffice, provides additional aportisdoc,
Pocket Excel and Pocket Word import filters.

%description javafilter -l pl.UTF-8
Moduł javafilter dla LibreOffice, udostępnia dodatkowe filtry importu
aportisdoc, Pocket Excel i Pocket Word.

%package postgresql
Summary:	PostgreSQL connector for LibreOffice
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	postgresql-libs

%description postgresql
A PostgreSQL connector for the database front-end for LibreOffice.
Allows creation and management of PostgreSQL databases through a GUI.

# FIXME
%package ure
Summary:	UNO Runtime Environment
Group:		Libraries
Obsoletes:	openoffice.org-ure

%description ure
UNO is the component model of LibreOffice. UNO offers interoperability
between programming languages, other components models and hardware
architectures, either in process or over process boundaries, in the
Intranet as well as in the Internet. UNO components may be implemented
in and accessed from any programming language for which a UNO
implementation (AKA language binding) and an appropriate bridge or
adapter exists.

%package -n browser-plugin-%{name}
Summary:	LibreOffice plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczka LibreOffice dla przeglądarek WWW
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Obsoletes:	browser-plugin-openoffice.org

%description -n browser-plugin-%{name}
LibreOffice plugin for WWW browsers.

This plugin allows browsers to display OOo documents inline.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka LibreOffice dla przeglądarek WWW.

Ta wtyczka umożliwia wyświetlanie dokumentów OOo wewnątrz stron.

%package binfilter
Summary:	Legacy binary filters for LibreOffice
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}

%description binfilter
Filters for old StarOffice binary formats.

%package i18n-af
Summary:	LibreOffice - interface in Afrikaans language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku afrykanerskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-af
Obsoletes:	openoffice-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af
Obsoletes:	openoffice.org-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af-kde

%description i18n-af
This package provides resources containing menus and dialogs in
Afrikaans language.

%description i18n-af -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
afrykanerskim.

%package i18n-am
Summary:	LibreOffice - interface in Amharic language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku amharskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}

%description i18n-am
This package provides resources containing menus and dialogs in
Amharic language.

%description i18n-am -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
amharskim.

%package i18n-ar
Summary:	LibreOffice - interface in Arabic language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku arabskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ar
Obsoletes:	openoffice-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar
Obsoletes:	openoffice.org-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar-kde

%description i18n-ar
This package provides resources containing menus and dialogs in Arabic
language.

%description i18n-ar -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
arabskim.

%package i18n-as
Summary:	LibreOffice - interface in Assamese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku asamskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-as_IN

%description i18n-as
This package provides resources containing menus and dialogs in
Assamese language.

%description i18n-as -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
asamskim.

%package i18n-ast
Summary:	LibreOffice - interface in Asturian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku asturyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ast

%description i18n-ast
This package provides resources containing menus and dialogs in
Asturian language.

%description i18n-ast -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
asturyjskim.

%package i18n-be_BY
Summary:	LibreOffice - interface in Belarusian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku białoruskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-be_BY

%description i18n-be_BY
This package provides resources containing menus and dialogs in
Belarusian language.

%description i18n-be_BY -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
białoruskim.

%package i18n-bg
Summary:	LibreOffice - interface in Bulgarian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku bułgarskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-bg
Obsoletes:	openoffice-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg
Obsoletes:	openoffice.org-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg-kde

%description i18n-bg
This package provides resources containing menus and dialogs in
Bulgarian language.

%description i18n-bg -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bułgarskim.

%package i18n-bn_IN
Summary:	LibreOffice - interface in Indian Bangla language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku indyjskim bengalskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-bn_IN

%description i18n-bn_IN
This package provides resources containing menus and dialogs in Indian
Bangla language.

%description i18n-bn_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
indyjskim bengalskim.

%package i18n-bn
Summary:	LibreOffice - interface in Bangla language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku bengalskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-bn

%description i18n-bn
This package provides resources containing menus and dialogs in Bangla
language.

%description i18n-bn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bengalskim.

%package i18n-bo
Summary:	LibreOffice - interface in Tibetan language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tybetańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-bo

%description i18n-bo
This package provides resources containing menus and dialogs in
Tibetan language.

%description i18n-bo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tybetańskim.

%package i18n-br
Summary:	LibreOffice - interface in Breton language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku bretońskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-br

%description i18n-br
This package provides resources containing menus and dialogs in Breton
language.

%description i18n-br -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bretońskim.

%package i18n-brx
Summary:	LibreOffice - interface in Bodo language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku boro
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-brx

%description i18n-brx
This package provides resources containing menus and dialogs in Bodo
language.

%description i18n-brx -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
boro.

%package i18n-bs
Summary:	LibreOffice - interface in Bosnian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku bośniackim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-bs

%description i18n-bs
This package provides resources containing menus and dialogs in
Bosnian language.

%description i18n-bs -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bośniackim.

%package i18n-ca
Summary:	LibreOffice - interface in Catalan language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku katalońskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ca
Obsoletes:	openoffice-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca
Obsoletes:	openoffice.org-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca-kde

%description i18n-ca
This package provides resources containing menus and dialogs in
Catalan language.

%description i18n-ca -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
katalońskim.

%package i18n-ca_XV
Summary:	LibreOffice - interface in Catalan Valencian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku katalońskim walenckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}

%description i18n-ca_XV
This package provides resources containing menus and dialogs in
Catalan Valencian language.

%description i18n-ca_XV -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
katalońskim walenckim.

%package i18n-cs
Summary:	LibreOffice - interface in Czech language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku czeskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-cs
Obsoletes:	openoffice-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs
Obsoletes:	openoffice.org-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs-kde

%description i18n-cs
This package provides resources containing menus and dialogs in Czech
language.

%description i18n-cs -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
czeskim.

%package i18n-cy
Summary:	LibreOffice - interface in Cymraeg language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku walijskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-cy
Obsoletes:	openoffice-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy
Obsoletes:	openoffice.org-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy-kde

%description i18n-cy
This package provides resources containing menus and dialogs in
Cymraeg language.

%description i18n-cy -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
walijskim.

%package i18n-da
Summary:	LibreOffice - interface in Danish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku duńskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-da
Obsoletes:	openoffice-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da
Obsoletes:	openoffice.org-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da-kde

%description i18n-da
This package provides resources containing menus and dialogs in Danish
language.

%description i18n-da -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
duńskim.

%package i18n-de
Summary:	LibreOffice - interface in German language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku niemieckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-de
Obsoletes:	openoffice-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de
Obsoletes:	openoffice.org-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de-kde

%description i18n-de
This package provides resources containing menus and dialogs in German
language.

%description i18n-de -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
niemieckim.

%package i18n-dgo
Summary:	LibreOffice - interface in Dogri language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku dogri
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-dgo

%description i18n-dgo
This package provides resources containing menus and dialogs in Dogri
language.

%description i18n-dgo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
dogri.

%package i18n-dz
Summary:	LibreOffice - interface in Dzongkha language
Summary(pl.UTF-8):	Openoffice.org - interfejs w języku dżongkha
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-dz

%description i18n-dz
This package provides resources containing menus and dialogs in
Dzongkha language.

%description i18n-dz -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
dżongkha.

%package i18n-el
Summary:	LibreOffice - interface in Greek language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku greckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-el
Obsoletes:	openoffice-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el
Obsoletes:	openoffice.org-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el-kde

%description i18n-el
This package provides resources containing menus and dialogs in Greek
language.

%description i18n-el -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
greckim.

%package i18n-en_GB
Summary:	LibreOffice - interface in English language for United Kingdom
Summary(pl.UTF-8):	LibreOffice - interfejs w języku anglieskim dla Wielkiej Brytanii
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-en_GB

%description i18n-en_GB
This package provides resources containing menus and dialogs in
English language for United Kingdom.

%description i18n-en_GB -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
anglieskim dla Wielkiej Brytanii.

%package i18n-en_ZA
Summary:	LibreOffice - interface in English language for South Africa
Summary(pl.UTF-8):	LibreOffice - interfejs w języku anglieskim dla Południowej Afryki
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-en_ZA

%description i18n-en_ZA
This package provides resources containing menus and dialogs in
English language for South Africa.

%description i18n-en_ZA -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
anglieskim dla Południowej Afryki.

%package i18n-eo
Summary:	LibreOffice - interface in Esperanto language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku esperanto
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-eo

%description i18n-eo
This package provides resources containing menus and dialogs in
Esperanto language.

%description i18n-eo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
esperanto.

%package i18n-es
Summary:	LibreOffice - interface in Spanish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku hiszpańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-es
Obsoletes:	openoffice-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es
Obsoletes:	openoffice.org-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es-kde

%description i18n-es
This package provides resources containing menus and dialogs in
Spanish language.

%description i18n-es -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
hiszpańskim.

%package i18n-et
Summary:	LibreOffice - interface in Estonian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku estońskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-et
Obsoletes:	openoffice-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et
Obsoletes:	openoffice.org-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et-kde

%description i18n-et
This package provides resources containing menus and dialogs in
Estonian language.

%description i18n-et -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
estońskim.

%package i18n-eu
Summary:	LibreOffice - interface in Basque (Euskara) language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku baskijskim (euskera)
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-eu
Obsoletes:	openoffice-i18n-eu-gtk
Obsoletes:	openoffice-i18n-eu-kde
Obsoletes:	openoffice.org-i18n-eu

%description i18n-eu
This package provides resources containing menus and dialogs in Basque
(Euskara) language.

%description i18n-eu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
baskijskim (euskera).

%package i18n-fa
Summary:	LibreOffice - interface in Persian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku perskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-fa
Obsoletes:	openoffice-i18n-fa-gtk
Obsoletes:	openoffice-i18n-fa-kde
Obsoletes:	openoffice.org-i18n-fa

%description i18n-fa
This package provides resources containing menus and dialogs in
Persian language.

%description i18n-fa -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
perskim.

%package i18n-fi
Summary:	LibreOffice - interface in Finnish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku fińskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-fi
Obsoletes:	openoffice-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi
Obsoletes:	openoffice.org-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi-kde

%description i18n-fi
This package provides resources containing menus and dialogs in
Finnish language.

%description i18n-fi -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
fińskim.

%package i18n-fr
Summary:	LibreOffice - interface in French language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku francuskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-fr
Obsoletes:	openoffice-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr
Obsoletes:	openoffice.org-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr-kde

%description i18n-fr
This package provides resources containing menus and dialogs in French
language.

%description i18n-fr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
francuskim.

%package i18n-ga
Summary:	LibreOffice - interface in Irish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku irlandzkim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ga
Obsoletes:	openoffice-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga
Obsoletes:	openoffice.org-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga-kde

%description i18n-ga
This package provides resources containing menus and dialogs in Irish
language.

%description i18n-ga -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
irlandzkim.

%package i18n-gd
Summary:	LibreOffice - interface in Scottish Gaelic language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku gaelickim szkockim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}

%description i18n-gd
This package provides resources containing menus and dialogs in
Scottish Gaelic language.

%description i18n-gd -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gaelicki szkocki.

%package i18n-gl
Summary:	LibreOffice - interface in Galician language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku galicyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-gl
Obsoletes:	openoffice-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl
Obsoletes:	openoffice.org-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl-kde

%description i18n-gl
This package provides resources containing menus and dialogs in
Galician language.

%description i18n-gl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
galicyjskim.

%package i18n-gu
Summary:	LibreOffice - interface in Gujarati language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku gudźarati
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-gu

%description i18n-gu
This package provides resources containing menus and dialogs in
Gujarati language.

%description i18n-gu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gudźarati.

%package i18n-he
Summary:	LibreOffice - interface in Hebrew language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku hebrajskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-he
Obsoletes:	openoffice-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he
Obsoletes:	openoffice.org-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he-kde

%description i18n-he
This package provides resources containing menus and dialogs in Hebrew
language.

%description i18n-he -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
hebrajskim.

%package i18n-hi
Summary:	LibreOffice - interface in Hindi language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku hindi
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-hi
Obsoletes:	openoffice-i18n-hi-gtk
Obsoletes:	openoffice.org-i18n-hi-gtk
Obsoletes:	openoffice.org-i18n-hi-kde
Obsoletes:	openoffice.org-i18n-hi_IN

%description i18n-hi
This package provides resources containing menus and dialogs in Hindi
language.

%description i18n-hi -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
hindi.

%package i18n-hr
Summary:	LibreOffice - interface in Croatian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku chorwackim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-hr
Obsoletes:	openoffice-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr
Obsoletes:	openoffice.org-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr-kde

%description i18n-hr
This package provides resources containing menus and dialogs in
Croatian language.

%description i18n-hr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
chorwackim.

%package i18n-hu
Summary:	LibreOffice - interface in Hungarian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku węgierskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-hu
Obsoletes:	openoffice-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu
Obsoletes:	openoffice.org-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu-kde

%description i18n-hu
This package provides resources containing menus and dialogs in
Hungarian language.

%description i18n-hu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
węgierskim.

%package i18n-id
Summary:	LibreOffice - interface in Indonesian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku indonezyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}

%description i18n-id
This package provides resources containing menus and dialogs in
Indonesian language.

%description i18n-id -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
indonezyjskim.

%package i18n-is
Summary:	LibreOffice - interface in Icelandic language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku islandzkim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-is

%description i18n-is
This package provides resources containing menus and dialogs in
Icelandic language.

%description i18n-is -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
islandzkim.

%package i18n-it
Summary:	LibreOffice - interface in Italian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku włoskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-it
Obsoletes:	openoffice-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it
Obsoletes:	openoffice.org-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it-kde

%description i18n-it
This package provides resources containing menus and dialogs in
Italian language.

%description i18n-it -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
włoskim.

%package i18n-ja
Summary:	LibreOffice - interface in Japan language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku japońskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ja
Obsoletes:	openoffice-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja
Obsoletes:	openoffice.org-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja-kde

%description i18n-ja
This package provides resources containing menus and dialogs in Japan
language.

%description i18n-ja -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
japońskim.

%package i18n-ka
Summary:	LibreOffice - interface in Georgian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku gruzińskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ka

%description i18n-ka
This package provides resources containing menus and dialogs in
Georgian language.

%description i18n-ka -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gruzińskim.

%package i18n-kk
Summary:	LibreOffice - interface in Kazakh language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kazachskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-kk

%description i18n-kk
This package provides resources containing menus and dialogs in Kazakh
language.

%description i18n-kk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kazachskim.

%package i18n-km
Summary:	LibreOffice - interface in Khmer language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku khmerskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-km

%description i18n-km
This package provides resources containing menus and dialogs in Khmer
language.

%description i18n-km -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
khmerskim.

%package i18n-kn_IN
Summary:	LibreOffice - interface in Kannada language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kannara
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-kn
Obsoletes:	openoffice-i18n-kn-gtk
Obsoletes:	openoffice-i18n-kn-kde
Obsoletes:	openoffice.org-i18n-kn_IN

%description i18n-kn_IN
This package provides resources containing menus and dialogs in
Kannada language.

%description i18n-kn_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kannara.

%package i18n-ko
Summary:	LibreOffice - interface in Korean language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku koreańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ko
Obsoletes:	openoffice-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko
Obsoletes:	openoffice.org-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko-kde

%description i18n-ko
This package provides resources containing menus and dialogs in Korean
language.

%description i18n-ko -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
koreańskim.

%package i18n-kok
Summary:	LibreOffice - interface in Konkani language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku konkani
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-kok

%description i18n-kok
This package provides resources containing menus and dialogs in
Konkani language.

%description i18n-kok -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
konkani.

%package i18n-ks
Summary:	LibreOffice - interface in Kashmiri language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kaszmirskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ks

%description i18n-ks
This package provides resources containing menus and dialogs in
Kashmiri language.

%description i18n-ks -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kaszmirskim.

%package i18n-ku
Summary:	LibreOffice - interface in Kurdish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kurdyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ku

%description i18n-ku
This package provides resources containing menus and dialogs in
Kurdish language.

%description i18n-ku -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kurdyjskim.

%package i18n-lb
Summary:	LibreOffice - interface in Luxembourgish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku luksemburgskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-lb

%description i18n-lb
This package provides resources containing menus and dialogs in
Luxembourgish language.

%description i18n-lb -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
luksemburgskim.

%package i18n-lo
Summary:	LibreOffice - interface in Lao language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku laotańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-lo

%description i18n-lo
This package provides resources containing menus and dialogs in Lao
language.

%description i18n-lo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
laotańskim.

%package i18n-lt
Summary:	LibreOffice - interface in Lithuanian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku litewskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-lt
Obsoletes:	openoffice-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt
Obsoletes:	openoffice.org-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt-kde

%description i18n-lt
This package provides resources containing menus and dialogs in
Lithuanian language.

%description i18n-lt -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
litewskim.

%package i18n-lv
Summary:	LibreOffice - interface in Latvian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku łotewskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-lv

%description i18n-lv
This package provides resources containing menus and dialogs in
Latvian language.

%description i18n-lv -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
łotewskim.

%package i18n-mai
Summary:	LibreOffice - interface in Maithili language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku maithili
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-mai

%description i18n-mai
This package provides resources containing menus and dialogs in
Maithili language.

%description i18n-mai -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
maithili.

%package i18n-mk
Summary:	LibreOffice - interface in Macedonian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku macedońskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-mk

%description i18n-mk
This package provides resources containing menus and dialogs in
Macedonian language.

%description i18n-mk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
macedońskim.

%package i18n-ml
Summary:	LibreOffice - interface in Malayalam language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku malajalamskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ml_IN

%description i18n-ml
This package provides resources containing menus and dialogs in
Malayalam language.

%description i18n-ml -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
malajalamskim.

%package i18n-mni
Summary:	LibreOffice - interface in Meitei language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku manipuri
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-mni

%description i18n-mni
This package provides resources containing menus and dialogs in Meitei
language.

%description i18n-mni -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
manipuri.

%package i18n-mr
Summary:	LibreOffice - interface in Marathi language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku marathi
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-mr_IN

%description i18n-mr
This package provides resources containing menus and dialogs in
Marathi language.

%description i18n-mr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
marathi.

%package i18n-mn
Summary:	LibreOffice - interface in Mongolian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku mongolskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-mn

%description i18n-mn
This package provides resources containing menus and dialogs in
Mongolian language.

%description i18n-mn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
mongolskim.

%package i18n-my
Summary:	LibreOffice - interface in Burmese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku birmańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-my

%description i18n-my
This package provides resources containing menus and dialogs in
Burmese language.

%description i18n-my -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
birmańskim.

%package i18n-nb
Summary:	LibreOffice - interface in Norwegian Bokmaal language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku norweskim (odmiana Bokmaal)
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-nb
Obsoletes:	openoffice-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb
Obsoletes:	openoffice.org-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb-kde

%description i18n-nb
This package provides resources containing menus and dialogs in
Norwegian Bokmaal language.

%description i18n-nb -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
norweskim w odmianie Bokmaal.

%package i18n-ne
Summary:	LibreOffice - interface in Nepali language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku nepalskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ne

%description i18n-ne
This package provides resources containing menus and dialogs in Nepali
language.

%description i18n-ne -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
nepalskim.

%package i18n-nl
Summary:	LibreOffice - interface in Dutch language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku holenderskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-nl
Obsoletes:	openoffice-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl
Obsoletes:	openoffice.org-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl-kde

%description i18n-nl
This package provides resources containing menus and dialogs in Dutch
language.

%description i18n-nl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
holenderskim.

%package i18n-nn
Summary:	LibreOffice - interface in Norwegian Nynorsk language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku norweskim (odmiana Nynorsk)
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-nn
Obsoletes:	openoffice-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn
Obsoletes:	openoffice.org-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn-kde

%description i18n-nn
This package provides resources containing menus and dialogs in
Norwegian Nynorsk language.

%description i18n-nn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
norweskim w odmianie Nynorsk.

%package i18n-nr
Summary:	LibreOffice - interface in South Ndebele language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku ndebele (południowym)
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-nr

%description i18n-nr
This package provides resources containing menus and dialogs in South
Ndebele language.

%description i18n-nr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ndebele (południowym).

%package i18n-nso
Summary:	LibreOffice - interface in Northern Sotho language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku ludu Soto
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-nso
Obsoletes:	openoffice-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso
Obsoletes:	openoffice.org-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso-kde

%description i18n-nso
This package provides resources containing menus and dialogs in
Northern Sotho language.

%description i18n-nso -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ludu Soto.

%package i18n-oc
Summary:	LibreOffice - interface in Occitan language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku oksytańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-oc

%description i18n-oc
This package provides resources containing menus and dialogs in
Occitan language.

%description i18n-oc -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
oksytańskim.

%package i18n-om
Summary:	LibreOffice - interface in Oromo language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku oromo
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-om

%description i18n-om
This package provides resources containing menus and dialogs in Oromo
language.

%description i18n-om -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
oromo.

%package i18n-or
Summary:	LibreOffice - interface in Oriya language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku orija
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-or_IN

%description i18n-or
This package provides resources containing menus and dialogs in Oriya
language.

%description i18n-or -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
orija.

%package i18n-pa_IN
Summary:	LibreOffice - interface in Punjabi language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku pendżabskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-pa_IN

%description i18n-pa_IN
This package provides resources containing menus and dialogs in
Punjabi language.

%description i18n-pa_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
pendżabskim.

%package i18n-pl
Summary:	LibreOffice - interface in Polish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku polskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-pl
Obsoletes:	openoffice-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl
Obsoletes:	openoffice.org-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl-kde

%description i18n-pl
This package provides resources containing menus and dialogs in Polish
language.

%description i18n-pl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
polskim.

%package i18n-pt
Summary:	LibreOffice - interface in Portuguese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku portugalskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-pt
Obsoletes:	openoffice-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt
Obsoletes:	openoffice.org-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt-kde

%description i18n-pt
This package provides resources containing menus and dialogs in
Portuguese language.

%description i18n-pt -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
portugalskim.

%package i18n-pt_BR
Summary:	LibreOffice - interface in Brazilian Portuguese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku portugalskim dla Brazylii
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-pt_BR
Obsoletes:	openoffice-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR
Obsoletes:	openoffice.org-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR-kde

%description i18n-pt_BR
This package provides resources containing menus and dialogs in
Brazilian Portuguese language.

%description i18n-pt_BR -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
portugalskim dla Brazylii.

%package i18n-qtz
Summary:	LibreOffice - interface in "KeyID language" pseudo-locale
Summary(pl.UTF-8):	LibreOffice - interfejs w pseudo-lokalizacji "KeyID"
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-qtz

%description i18n-qtz
The "KeyID language" is a pseudo-locale that is available in
LibreOffice. It shows all KeyID's in the UI itself.

%description i18n-qtz -l pl.UTF-8
"Język KeyID" jest pseudo-lokalizacją dostępną w LibreOffice.
Pokazuje wszystkie wartości KeyID w interfejsie programu.

%package i18n-ro
Summary:	LibreOffice - interface in Romanian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku rumuńskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ro

%description i18n-ro
This package provides resources containing menus and dialogs in
Romanian language.

%description i18n-ro -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
rumuńskim.

%package i18n-ru
Summary:	LibreOffice - interface in Russian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku rosyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ru
Obsoletes:	openoffice-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru
Obsoletes:	openoffice.org-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru-kde

%description i18n-ru
This package provides resources containing menus and dialogs in
Russian language.

%description i18n-ru -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
rosyjskim.

%package i18n-rw
Summary:	LibreOffice - interface in Kinarwanda language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kinya-ruanda
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-rw

%description i18n-rw
This package provides resources containing menus and dialogs in
Kinarwanda language.

%description i18n-rw -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kinya-ruanda.

%package i18n-sa_IN
Summary:	LibreOffice - interface in Sanskrit language
Summary(pl.UTF-8):	LibreOffice - interfejs w sanskrycie
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sa_IN

%description i18n-sa_IN
This package provides resources containing menus and dialogs in
Sanskrit language.

%description i18n-sa_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w
sanskrycie.

%package i18n-sat
Summary:	LibreOffice - interface in Santali language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku santali
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sat

%description i18n-sat
This package provides resources containing menus and dialogs in
Santali language.

%description i18n-sat -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
santali.

%package i18n-sd
Summary:	LibreOffice - interface in Sindhi language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku sindhi
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sd

%description i18n-sd
This package provides resources containing menus and dialogs in Sindhi
language.

%description i18n-sd -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
sindhi.

%package i18n-sh
Summary:	LibreOffice - interface in Serbo-Croatian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku serbsko-chorwackim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sh

%description i18n-sh
This package provides resources containing menus and dialogs in
Serbo-Croatian language.

%description i18n-sh -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
serbsko-chorwackim.

%package i18n-si
Summary:	LibreOffice - interface in Sinhala language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku syngaleskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-si

%description i18n-si
This package provides resources containing menus and dialogs in
Sinhala language.

%description i18n-si -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
syngaleskim.

%package i18n-sk
Summary:	LibreOffice - interface in Slovak language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku słowackim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-sk
Obsoletes:	openoffice-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk
Obsoletes:	openoffice.org-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk-kde

%description i18n-sk
This package provides resources containing menus and dialogs in Slovak
language.

%description i18n-sk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
słowackim.

%package i18n-sl
Summary:	LibreOffice - interface in Slovenian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku słoweńskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-sl
Obsoletes:	openoffice-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl
Obsoletes:	openoffice.org-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl-kde

%description i18n-sl
This package provides resources containing menus and dialogs in
Slovenian language.

%description i18n-sl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
słoweńskim.

%package i18n-sq
Summary:	LibreOffice - interface in Albanian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku albańskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}

%description i18n-sq
This package provides resources containing menus and dialogs in
Albanian language.

%description i18n-sq -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
albańskim.

%package i18n-sr
Summary:	LibreOffice - interface in Serbian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku serbskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sr

%description i18n-sr
This package provides resources containing menus and dialogs in
Serbian language.

%description i18n-sr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
serbskim.

%package i18n-ss
Summary:	LibreOffice - interface in Swati language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku suazi (siswati)
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ss

%description i18n-ss
This package provides resources containing menus and dialogs in Swati
language.

%description i18n-ss -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
suazi (siswati).

%package i18n-st
Summary:	LibreOffice - interface in Southern Sotho language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku południowym sotho
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-st

%description i18n-st
This package provides resources containing menus and dialogs in
Southern Sotho language.

%description i18n-st -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
południowym sotho.

%package i18n-sv
Summary:	LibreOffice - interface in Swedish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku szwedzkim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-sv
Obsoletes:	openoffice-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv
Obsoletes:	openoffice.org-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv-kde

%description i18n-sv
This package provides resources containing menus and dialogs in
Swedish language.

%description i18n-sv -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
szwedzkim.

%package i18n-sw_TZ
Summary:	LibreOffice - interface in Swahili language for Tanzania
Summary(pl.UTF-8):	LibreOffice - interfejs w języku suahili dla Tanzanii
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sw_TZ

%description i18n-sw_TZ
This package provides resources containing menus and dialogs in
Swahili language for Tanzania.

%description i18n-sw_TZ -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
suahili dla Tanzanii.

%package i18n-ta
Summary:	LibreOffice - interface in Tamil language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tamiskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ta_IN

%description i18n-ta
This package provides resources containing menus and dialogs in Tamil
language.

%description i18n-ta -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tamilskim.

%package i18n-te
Summary:	LibreOffice - interface in Telugu language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku telugu
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-te_IN

%description i18n-te
This package provides resources containing menus and dialogs in Telugu
language.

%description i18n-te -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
telugu.

%package i18n-tg
Summary:	LibreOffice - interface in Tajik language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tadżyckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-tg

%description i18n-tg
This package provides resources containing menus and dialogs in Tajik
language.

%description i18n-tg -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tadżyckim.

%package i18n-th
Summary:	LibreOffice - interface in Thai language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tajskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-th
Obsoletes:	openoffice-i18n-th-gtk
Obsoletes:	openoffice-i18n-th-kde
Obsoletes:	openoffice.org-i18n-th

%description i18n-th
This package provides resources containing menus and dialogs in Thai
language.

%description i18n-th -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tajskim.

%package i18n-tn
Summary:	LibreOffice - interface in Tswana language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tswana
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-tn
Obsoletes:	openoffice-i18n-tn-gtk
Obsoletes:	openoffice-i18n-tn-kde
Obsoletes:	openoffice.org-i18n-tn

%description i18n-tn
This package provides resources containing menus and dialogs in Tswana
language.

%description i18n-tn -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tswana.

%package i18n-tr
Summary:	LibreOffice - interface in Turkish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tureckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-tr
Obsoletes:	openoffice-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr
Obsoletes:	openoffice.org-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr-kde

%description i18n-tr
This package provides resources containing menus and dialogs in
Turkish language.

%description i18n-tr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tureckim.

%package i18n-ts
Summary:	LibreOffice - interface in Tsonga language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tsonga
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ts

%description i18n-ts
This package provides resources containing menus and dialogs in Tsonga
language.

%description i18n-ts -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tsonga.

%package i18n-tt
Summary:	LibreOffice - interface in Tatar language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tatarskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-tt

%description i18n-tt
This package provides resources containing menus and dialogs in Tatar
language.

%description i18n-tt -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tatarskim.

%package i18n-ug
Summary:	LibreOffice - interface in Uyghur language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku ujgurskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ug

%description i18n-ug
This package provides resources containing menus and dialogs in Uyghur
language.

%description i18n-ug -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ujgurskim.

%package i18n-uk
Summary:	LibreOffice - interface in Ukrainian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku ukraińskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-uk
Obsoletes:	openoffice-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk
Obsoletes:	openoffice.org-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk-kde

%description i18n-uk
This package provides resources containing menus and dialogs in
Ukrainian language.

%description i18n-uk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ukraińskim.

%package i18n-uz
Summary:	LibreOffice - interface in Uzbek language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku uzbeckim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-uz

%description i18n-uz
This package provides resources containing menus and dialogs in Uzbek.

%description i18n-uz -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
uzbeckim.

%package i18n-ve
Summary:	LibreOffice - interface in Venda language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku venda
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ve

%description i18n-ve
This package provides resources containing menus and dialogs in Venda
language.

%description i18n-ve -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
venda.

%package i18n-vi
Summary:	LibreOffice - interface in Vietnamese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku wietnamskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-vi

%description i18n-vi
This package provides resources containing menus and dialogs in
Vietnamese language.

%description i18n-vi -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
wietnamskim.

%package i18n-xh
Summary:	LibreOffice - interface in Xhosa language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku khosa
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-xh

%description i18n-xh
This package provides resources containing menus and dialogs in Xhosa
language.

%description i18n-xh -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
khosa.

%package i18n-zh_CN
Summary:	LibreOffice - interface in Chinese language for China
Summary(pl.UTF-8):	LibreOffice - interfejs w języku chińskim dla Chin
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_CN
Obsoletes:	openoffice-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN
Obsoletes:	openoffice.org-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN-kde

%description i18n-zh_CN
This package provides resources containing menus and dialogs in
Chinese language for China.

%description i18n-zh_CN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
chińskim dla Chin.

%package i18n-zh_TW
Summary:	LibreOffice - interface in Chinese language for Taiwan
Summary(pl.UTF-8):	LibreOffice - interfejs w języku chińskim dla Tajwanu
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_TW
Obsoletes:	openoffice-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW
Obsoletes:	openoffice.org-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW-kde

%description i18n-zh_TW
This package provides resources containing menus and dialogs in
Chinese language for Taiwan.

%description i18n-zh_TW -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
chińskim dla Tajwanu.

%package i18n-zu
Summary:	LibreOffice - interface in Zulu language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku zuluskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-zu
Obsoletes:	openoffice-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu
Obsoletes:	openoffice.org-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu-kde

%description i18n-zu
This package provides resources containing menus and dialogs in Zulu
language.

%description i18n-zu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
zuluskim.

%package -n bash-completion-%{name}
Summary:	bash-completion for LibreOffice
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla LibreOffice
Group:		Applications/Shells
Requires:	%{name}
Requires:	bash-completion
Obsoletes:	bash-completion-openoffice

%description -n bash-completion-%{name}
bash-completion for LibreOffice.

%description -n bash-completion-%{name} -l pl.UTF-8
bashowe uzupełnianie nazw dla LibreOffice.

%prep
%setup -q -n %{name}-%{version} -a1 -a2 -a3

%patch0 -p0

for dir in *-%{version}; do
	[ -f $dir/ChangeLog ] && mv $dir/ChangeLog ChangeLog-$dir
	rm -rf $dir/git-hooks
	mv $dir/* .
done

install -d ext_sources
ln %{SOURCE20} ext_sources
ln %{SOURCE21} ext_sources
ln %{SOURCE22} ext_sources
ln %{SOURCE23} ext_sources
ln %{SOURCE24} ext_sources
ln %{SOURCE25} ext_sources
:> src.downloaded

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
	-O?|-pipe|-Wall|-g|-fexceptions)
		;;
	*)
		SAFE_CFLAGS="$SAFE_CFLAGS $i"
		;;
	esac
done

export CC="%{__cc}"
export CXX="%{__cxx}"
export CPP="%{__cpp}"

export IGNORE_MANIFEST_CHANGES=1
export QT4INC="%{_includedir}/qt4"
export QT4LIB="%{_libdir}"
export QT4DIR="%{_libdir}/qt4"

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

%if %{with parallelbuild}
RPM_BUILD_NR_THREADS=$(echo %{_smp_mflags} | cut -dj -f2)
[ -z "$RPM_BUILD_NR_THREADS" ] && RPM_BUILD_NR_THREADS=1
%else
RPM_BUILD_NR_THREADS="1"
%endif

%{__aclocal} -I m4
%{__autoconf}
touch autogen.lastrun

%configure \
	--with-parallelism=$RPM_BUILD_NR_THREADS \
	--with-max-jobs=1 \
	--with-unix-wrapper=%{name} \
	--disable-odk \
	%{?with_ccache:--with-gcc-speedup=ccache} \
	%{?with_icecream:--with-gcc-speedup=icecream} \
	%{?with_system_agg:--with-system-agg} \
	%{?with_system_beanshell:--with-system-beanshell} \
	%{?with_system_db:--with-system-db} \
	--with%{!?with_system_hsqldb:out}-system-hsqldb \
	%{?with_system_hunspell:--with-system-hunspell --without-myspell-dicts} \
	%{?with_system_libhnj:--with-system-altlinuxhyphen} \
	%{?with_msaccess:%{?with_system_mdbtools:--with-system-mdbtools}} \
	--with-system-apache-commons \
	--with-system-boost \
	--with-system-cairo \
	--with-system-curl \
	--with-system-cppunit \
	--with-system-dicts \
	--with-external-dict-dir=/usr/share/myspell \
	--with-external-tar=$(pwd)/ext_sources \
	--with-system-expat \
	--with-system-graphite \
	--with-system-icu \
	--with-system-jpeg \
	--with-system-libwpd \
	--with-system-libwpg \
	--with-system-libwps \
	--with-system-libxml \
	--with-system-libxslt \
	--with-system-lucene \
	--with-lucene-analyzers-jar=%{_javadir}/lucene-analyzers.jar \
	--with-system-neon \
	--with-system-openssl \
	--with-system-poppler \
	--with-system-python \
	--with-system-redland \
	--with-system-sane-header \
	--with-system-stdlibs \
	--with-system-vigra \
	--with-system-xrender-headers=yes \
	--with-system-zlib \
	--with-system-libexttextcat \
	--with-system-jfreereport \
	--with-vba-package-format="builtin" \
	--with-system-libs \
	--with-system-headers \
	--with-system-mythes \
	--with-system-dicts \
	--with-system-apache-commons \
	--with-junit=%{_datadir}/java/junit.jar \
	--without-system-saxon \
	--without-system-sampleicc \
	--enable-ext-presenter-minimizer \
	--enable-ext-presenter-console \
	--enable-ext-pdfimport \
	--enable-ext-wiki-publisher \
	--enable-ext-report-builder \
	--enable-ext-scripting-beanshell \
	--enable-ext-scripting-javascript \
	--enable-ext-scripting-python \
%if %{with mozilla}
	--with-system-mozilla=libxul \
%else
	--disable-mozilla \
%endif
	--enable-gtk \
	%{?with_kde:--enable-kde --disable-kde4} \
	%{?with_kde4:--enable-kde4 --disable-kde} \
	--with-lang=%{?with_i18n:ALL} \
%if %{with java}
	--with-java \
	--with-jdk-home=$JAVA_HOME \
	--with-ant-home=$ANT_HOME \
%else
	--without-java \
%endif
	--disable-gnome-vfs \
	--enable-gio \
	--without-stlport \
	--with-x \
	--without-fonts \
	--without-ppds \
	--without-afms \
	--disable-epm \
	--enable-cairo \
	--enable-dbus \
	--enable-opengl \
	--with-openldap \
	--disable-rpath \
%if 0%{?debug:1}
	--enable-debug \
	--enable-crashdump=yes \
	--enable-symbols=FULL \
%else
	--enable-crashdump=no \
	--disable-symbols \
%endif
	--with-build-version=%{version}-%{release} \
	--enable-split-app-modules \
	--enable-split-opt-features \
	--enable-cups \
	--enable-fontconfig \
	--enable-lockdown \
	--disable-layout \
	%{?with_binfilter:--enable-binfilter} \
	--disable-fetch-external

# this limits processing some files but doesn't limit parallel build
# processes of main OOo build (since OOo uses it's own build system)
%{__make} -j1 \
	ARCH_FLAGS="$SAFE_CFLAGS -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CC="$SAFE_CFLAGS -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CXX="$SAFE_CFLAGS -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden" \
	ARCH_FLAGS_OPT="$SAFE_CFLAGS"

%install
# install just once (based on makeinstall.stamp)
# this will make packaging newer versions simplier
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	%{__rm} -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	export QTINC="%{_includedir}/qt"
	export QTLIB="%{_libdir}"
	export QT4DIR="%{_libdir}/qt4"
	export DESTDIR=$RPM_BUILD_ROOT
	export TMP="%{tmpdir}"
	export TMPDIR="%{tmpdir}"
	export TEMP="%{tmpdir}"
	export DEFAULT_TO_ENGLISH_FOR_PACKING=1

	%{__make} distro-pack-install \
		DESTDIR=$RPM_BUILD_ROOT

	# unpack report-builder extension
	install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/report-builder
	unzip -o solver/unxlng*/bin/report-builder.oxt -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/report-builder

	# unpack wiki-publisher extension
	install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/wiki-publisher
	unzip -o solver/unxlng*/bin/wiki-publisher.oxt -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/wiki-publisher

	# unpack presentation-minimizer extension
	install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/presentation-minimizer
	unzip -o solver/unxlng*/bin/presentation-minimizer.oxt -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/presentation-minimizer

	# XXX - gone in 4.0.0.3?
	# unpack presenter screen extension
	#install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/presenter-screen
	#unzip -o solver/unxlng*/bin/presenter-screen.oxt -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/presenter-screen

	# XXX se above
	# unpack pdfimport extension
	#install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/pdfimport
	#unzip -o solver/unxlng*/bin/pdfimport.oxt -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/pdfimport

	# unpack wiki-publisher extension
	install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/wiki-publisher
	unzip -o solver/unxlng*/bin/wiki-publisher.oxt -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/wiki-publisher

	# XXX
	# unpack script-provider-for-python extension
	#install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/script-provider-for-python
	#unzip -o solver/unxlng*/bin/script-provider-for-python.oxt -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/script-provider-for-python

	# save orignal install layout
	find $RPM_BUILD_ROOT -ls > ls.txt
	touch makeinstall.stamp
fi

# mangle files installed in build root
if [ ! -f installed.stamp ]; then
	chmod -Rf a+rX,u+w,g-w,o-w $RPM_BUILD_ROOT

	%if %{with mono}
	%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/mono-ooo-2.1.pc
	%endif

	%if %{with mozilla}
	install -d $RPM_BUILD_ROOT%{_browserpluginsdir}
	ln -s %{_libdir}/%{name}/program/libnpsoplugin.so $RPM_BUILD_ROOT%{_browserpluginsdir}
	%endif

	perl -pi -e 's/^[       ]*LD_LIBRARY_PATH/# LD_LIBRARY_PATH/;s/export LD_LIBRARY_PATH/# export LD_LIBRARY_PATH/' \
		$RPM_BUILD_ROOT%{_libdir}/%{name}/program/setup

	chmod +x $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*.so

	install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
	# put share to %{_datadir} so we're able to produce noarch packages
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/help $RPM_BUILD_ROOT/%{_datadir}/%{name}
	ln -s ../../share/%{name}/help $RPM_BUILD_ROOT%{_libdir}/%{name}/help
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/readmes $RPM_BUILD_ROOT%{_datadir}/%{name}
	ln -s ../../share/%{name}/readmes $RPM_BUILD_ROOT%{_libdir}/%{name}/readmes

	%{__rm} -r $RPM_BUILD_ROOT%{_desktopdir}/*.desktop \
		$RPM_BUILD_ROOT%{_iconsdir}/{gnome,locolor} \
		$RPM_BUILD_ROOT%{_datadir}/application-registry \
		$RPM_BUILD_ROOT%{_datadir}/mime{lnk,-info}
	for a in $RPM_BUILD_ROOT%{_libdir}/%{name}/share/xdg/*.desktop; do
		cp $a $RPM_BUILD_ROOT%{_desktopdir}/libreoffice-$(basename "$a")
	done
	%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/%{name}/share/xdg

	# Make oo* -> lo* symlinks for compatibility with misc software,
	# for example mailcap
	ln -s libreoffice $RPM_BUILD_ROOT%{_bindir}/ooffice
	for a in fromtemplate base calc draw writer impress math web; do
		ln -s lo$a $RPM_BUILD_ROOT%{_bindir}/oo$a
	done

	# remove printeradmin .desktop file and icons
	%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/*/apps/libreoffice-printeradmin.png \
		$RPM_BUILD_ROOT%{_desktopdir}/libreoffice-printeradmin.desktop

	touch installed.stamp
fi

# Find out locales
find_lang() {
	local lang=$(echo $1 | sed -e 's/_/-/')
	local langfn="$1"
	echo "%%defattr(644,root,root,755)" > ${langfn}.lang

	# help files
	if [ -f file-lists/help_${langfn}_list.txt ]; then
		cat file-lists/help_${langfn}_list.txt >> ${langfn}.lang
	fi

	lfile="file-lists/lang_${langfn}_list.txt"
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
		# %{_libdir}/%{name}/share/registry/.*[_-]$lang.xcd
		grep "/share/registry/.*[_-]${lang}.xcd$" ${lfile} >> ${langfn}.lang || :
		# %{_libdir}/%{name}/share/template/$lang
		grep "/share/template/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/${lang}/" ${lfile} >> ${langfn}.lang || :
		# %{_libdir}/%{name}/share/template/wizard/letter/lang
		grep "/share/template/wizard/letter/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}$" file-lists/common_list.txt >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}/" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}/" file-lists/common_list.txt >> ${langfn}.lang || :
		# %{_libdir}/%{name}/share/wordbook/$lang
		grep "/share/wordbook/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/wordbook/${lang}/" ${lfile} >> ${langfn}.lang || :
		# %{_libdir}/%{name}/share/samples/$lang
		grep "/share/samples/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/samples/${lang}/" ${lfile} >> ${langfn}.lang || :
		# %{_libdir}/%{name}/help/$lang
		grep "/help/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/help/${lang}/" ${lfile} >> ${langfn}.lang || :

		for e in pdfimport \
				presentation-minimizer \
				presenter-screen \
				report-builder \
				script-provider-for-python \
				wiki-publisher ; do
			for d in $RPM_BUILD_ROOT%{_libdir}/%{name}/share/extensions/$e/description-${lang}.txt ; do
				[ -f $d ] && echo "%lang(${lang}) $d" | sed -e "s|$RPM_BUILD_ROOT||g" >> $e.lang || :
			done
		done
	fi
}

%if %{with i18n}
%{__rm} -f *.lang*
langlist=$(ls file-lists/lang_*_list.txt | sed -e 's=file-lists/lang_\(.*\)_list.txt=\1=g')

for lang in $langlist; do
	find_lang $lang
done

%{__sed} -i -e '
	s,%{_libdir}/%{name}/readmes,%{_datadir}/%{name}/readmes,;
	s,%{_libdir}/%{name}/help,%{_datadir}/%{name}/help,;
' *.lang
%endif

# Fix incorrect file list, help files listed but not installed
for l in lb bn_IN; do
	%{__sed} -i -e '/.*\/help\/.*/d' $l.lang
done

## Remove unsupported locale files to avoid confusion about unpackaged files
#for l in ???; do
#	for f in `cat file-lists/lang_${l}_list.txt` ; do
#		%{__rm} -f $RPM_BUILD_ROOT/$f
#	done
#done

%clean
rm -rf $RPM_BUILD_ROOT

%post core
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%postun core
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%post base
%update_desktop_database_post
%update_icon_cache hicolor

%postun base
%update_desktop_database_postun
%update_icon_cache hicolor

%post web
%update_desktop_database_post

%postun web
%update_desktop_database_postun

%post writer
%update_desktop_database_post
%update_icon_cache hicolor

%postun writer
%update_desktop_database_postun
%update_icon_cache hicolor

%post calc
%update_desktop_database_post
%update_icon_cache hicolor

%postun calc
%update_desktop_database_postun
%update_icon_cache hicolor

%post draw
%update_desktop_database_post
%update_icon_cache hicolor

%postun draw
%update_desktop_database_postun
%update_icon_cache hicolor

%post impress
%update_desktop_database_post
%update_icon_cache hicolor

%postun impress
%update_desktop_database_postun
%update_icon_cache hicolor

%post math
%update_desktop_database_post
%update_icon_cache hicolor

%postun math
%update_desktop_database_postun
%update_icon_cache hicolor

%post javafilter
%update_desktop_database_post

%postun javafilter
%update_desktop_database_postun

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

# NOTE:
# you may find file-lists/*_list.txt useful to help you package files to packages

%files
%defattr(644,root,root,755)

%files core
%defattr(644,root,root,755)
%doc %{_libdir}/%{name}/CREDITS*
%doc %{_libdir}/%{name}/LICENSE*
%doc %{_libdir}/%{name}/*README*

%attr(755,root,root) %{_bindir}/libreoffice
%attr(755,root,root) %{_bindir}/lofromtemplate
%attr(755,root,root) %{_bindir}/loffice
%attr(755,root,root) %{_bindir}/ooffice
%attr(755,root,root) %{_bindir}/oofromtemplate
%attr(755,root,root) %{_bindir}/soffice
%attr(755,root,root) %{_bindir}/unopkg

%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/help
%{_datadir}/%{name}/help/*.xsl
%dir %{_datadir}/%{name}/help/en
%{_datadir}/%{name}/help/en/*.html
%{_datadir}/%{name}/help/en/*.css
%{_datadir}/%{name}/help/en/sbasic.*
%{_datadir}/%{name}/help/en/schart.*
%{_datadir}/%{name}/help/en/shared.*

%dir %{_libdir}/%{name}/presets
%dir %{_libdir}/%{name}/presets/autotext
%{_libdir}/%{name}/presets/autotext/mytexts.bau
%{_libdir}/%{name}/presets/basic
%dir %{_libdir}/%{name}/presets/config
%{_libdir}/%{name}/presets/config/autotbl.fmt
%{_libdir}/%{name}/presets/config/*.so[bcdegh]
%{_libdir}/%{name}/presets/database
%{_libdir}/%{name}/presets/gallery
%{_libdir}/%{name}/presets/psprint

%dir %{_libdir}/%{name}/program
%attr(755,root,root) %{_libdir}/%{name}/program/basprov*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/cairocanvas.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/canvasfactory.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/cde-open-url
%attr(755,root,root) %{_libdir}/%{name}/program/cmdmail.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/configmgr.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/desktopbe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/dlgprov*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/expwrap.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/fastsax.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/fpicker.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/fps_office.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/fsstorage.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/gengal
%attr(755,root,root) %{_libdir}/%{name}/program/gengal.bin
%attr(755,root,root) %{_libdir}/%{name}/program/hatchwindowfactory.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/i18npool.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/i18nsearch.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/java-set-classpath
%attr(755,root,root) %{_libdir}/%{name}/program/ldapbe2.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libacclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libavmediagst.so
%attr(755,root,root) %{_libdir}/%{name}/program/libavmedialo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasctllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasebmplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasegfxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbiblo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcached1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcanvastoolslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libchartcontrollerlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libchartmodello.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcharttoolslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libchartviewlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcollator_data.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcomphelpgcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcppcanvaslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libctllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcuilo.so
%{!?with_system_db:%attr(755,root,root) %{_libdir}/%{name}/program/libdb-4.2.so}
%attr(755,root,root) %{_libdir}/%{name}/program/libdbalo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbaselo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbaxmllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbmmlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbpool2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbtoolslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbulo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdeployment.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdeploymentgui.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdeploymentmisclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdesktop_detectorlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdict_ja.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdict_zh.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdrawinglayerlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libeditenglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libegilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libembobj.so
%attr(755,root,root) %{_libdir}/%{name}/program/libemelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libepblo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libepglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libepplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libepslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libeptlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liberalo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libetilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libevtattlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libexplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfileacc.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfilelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfilterconfiglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libflatlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libforlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libforuilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfrmlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwklo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwmlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libguesslanglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libhelplinkerlo.so
%{!?with_system_hunspell:%attr(755,root,root) %{_libdir}/%{name}/program/libhunspell.so}
%attr(755,root,root) %{_libdir}/%{name}/program/libhyphenlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libi18nisolang1gcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libi18nregexplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libi18nutilgcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libicdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libicglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libidxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libindex_data.so
%attr(755,root,root) %{_libdir}/%{name}/program/libimelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libipblo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libipdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libipslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libiptlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libipxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libiralo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libitglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libitilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblnglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblnthlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_en.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_es.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_euro.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblocaledata_others.so
%attr(755,root,root) %{_libdir}/%{name}/program/libloglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmcnttype.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmozbootstrap.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmsfilterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmysqllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libodbclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libodbcbaselo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libodfflatxmllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liboffacclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libooxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpackage2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpcrlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpdffilterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libprotocolhandlerlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libqstart_gtklo.so
%attr(755,root,root) %{_libdir}/%{name}/program/librecentfile.so
%attr(755,root,root) %{_libdir}/%{name}/program/libreslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsaxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsblo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscnlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscriptframe.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdbc2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdbtlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsddlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdfiltlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsduilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsfxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsofficeapp.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsotlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspalo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspelllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspl_unxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsrtrs1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvtlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvxcorelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvxlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextfdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextconv_dict.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextconversiondlgslo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtklo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtvhlp1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucb1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucbhelper4gcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpchelp1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpdav1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpfile1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucpftp1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucphier1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucppkg1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libunopkgapp.so
%attr(755,root,root) %{_libdir}/%{name}/program/libunordflo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libunoxmllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libutllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libuuilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvbahelperlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvcllo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_genlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_svplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwpftdrawlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxcrlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlfalo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlfdlo.so
## maybe external is possible?
# - external broken in 3.0.1
###%attr(755,root,root) %{_libdir}/%{name}/program/libxmlsec1*.so
##
%attr(755,root,root) %{_libdir}/%{name}/program/libxmlsecurity.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxoflo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxolo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsec_fw.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsec_xmlsec.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsltdlglo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxsltfilterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libxstor.so
%attr(755,root,root) %{_libdir}/%{name}/program/localebe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/mtfrenderer.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/migrationoo2.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/migrationoo3.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/msforms.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/open-url
%attr(755,root,root) %{_libdir}/%{name}/program/oosplash
%attr(755,root,root) %{_libdir}/%{name}/program/pagein*
%attr(755,root,root) %{_libdir}/%{name}/program/passwordcontainer.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/pluginapp.bin
## seems to be exactly the same as in -ure
#%attr(755,root,root) %{_libdir}/%{name}/program/regcomp
#%attr(755,root,root) %{_libdir}/%{name}/program/regcomp.bin
##
%attr(755,root,root) %{_libdir}/%{name}/program/senddoc
%attr(755,root,root) %{_libdir}/%{name}/program/simplecanvas.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/slideshow.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/spadmin.bin
%attr(755,root,root) %{_libdir}/%{name}/program/stringresource*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/syssh.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/ucpcmis1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/ucpexpand1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/ucpext.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/ucptdoc1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/updatefeed.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/uri-encode
%attr(755,root,root) %{_libdir}/%{name}/program/vbaevents*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/vclcanvas.uno.so

%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/program/libhsqldb.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjdbclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libofficebean.so
%endif

%if %{with mono}
%attr(755,root,root) %{_libdir}/%{name}/program/libcli_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcli_uno_glue.so
%{_libdir}/%{name}/program/cli_basetypes.dll
%{_libdir}/%{name}/program/cli_cppuhelper.dll
%{_libdir}/%{name}/program/cli_types.dll
%{_libdir}/%{name}/program/cli_uno_bridge.dll
%{_libdir}/%{name}/program/cli_ure.dll
%endif

%{_libdir}/%{name}/program/root3.dat
%{_libdir}/%{name}/program/root4.dat
%{_libdir}/%{name}/program/root5.dat
%config(noreplace) %verify(not md5 mtime size) %{_libdir}/%{name}/program/unorc
%{_libdir}/%{name}/program/versionrc

%if %{with java}
%dir %{_libdir}/%{name}/program/classes
%{_libdir}/%{name}/program/classes/ScriptFramework.jar
%{_libdir}/%{name}/program/classes/ScriptProviderForBeanShell.jar
%{_libdir}/%{name}/program/classes/ScriptProviderForJavaScript.jar
%{_libdir}/%{name}/program/classes/ScriptProviderForJava.jar
%{_libdir}/%{name}/program/classes/XMergeBridge.jar
%{_libdir}/%{name}/program/classes/XSLTFilter.jar
%{_libdir}/%{name}/program/classes/XSLTValidate.jar
%{_libdir}/%{name}/program/classes/agenda.jar
%{_libdir}/%{name}/program/classes/commonwizards.jar
%{_libdir}/%{name}/program/classes/fax.jar
%{_libdir}/%{name}/program/classes/form.jar
%{!?with_system_hsqldb:%{_libdir}/%{name}/program/classes/hsqldb.jar}
%{_libdir}/%{name}/program/classes/js.jar
%{_libdir}/%{name}/program/classes/letter.jar
%{_libdir}/%{name}/program/classes/officebean.jar
%{_libdir}/%{name}/program/classes/query.jar
%{_libdir}/%{name}/program/classes/report.jar
%{_libdir}/%{name}/program/classes/saxon9.jar
%{_libdir}/%{name}/program/classes/sdbc_hsqldb.jar
%{!?with_system_xalan:%{_libdir}/%{name}/program/classes/serializer.jar}
%{_libdir}/%{name}/program/classes/table.jar
%{_libdir}/%{name}/program/classes/unoil.jar
%{_libdir}/%{name}/program/classes/web.jar
%{!?with_system_xalan:%{_libdir}/%{name}/program/classes/xalan.jar}
%{_libdir}/%{name}/program/classes/xmerge.jar
%{_libdir}/%{name}/program/services/scriptproviderforbeanshell.rdb
%{_libdir}/%{name}/program/services/scriptproviderforjavascript.rdb
%endif
%dir %{_libdir}/%{name}/program/services
%{_libdir}/%{name}/program/services/services.rdb
%dir %{_libdir}/%{name}/program/types
%{_libdir}/%{name}/program/types/offapi.rdb
%{_libdir}/%{name}/program/types/oovbaapi.rdb

%dir %{_libdir}/%{name}/program/resource
%{_libdir}/%{name}/program/resource/accen-US.res
%{_libdir}/%{name}/program/resource/avmediaen-US.res
%{_libdir}/%{name}/program/resource/basctlen-US.res
%{_libdir}/%{name}/program/resource/biben-US.res
%{_libdir}/%{name}/program/resource/calen-US.res
%{_libdir}/%{name}/program/resource/cuien-US.res
%{_libdir}/%{name}/program/resource/chartcontrolleren-US.res
%{_libdir}/%{name}/program/resource/dbaen-US.res
%{_libdir}/%{name}/program/resource/dbmmen-US.res
%{_libdir}/%{name}/program/resource/dbwen-US.res
%{_libdir}/%{name}/program/resource/deploymenten-US.res
%{_libdir}/%{name}/program/resource/deploymentguien-US.res
%{_libdir}/%{name}/program/resource/dkten-US.res
%{_libdir}/%{name}/program/resource/editengen-US.res
%{_libdir}/%{name}/program/resource/epsen-US.res
%{_libdir}/%{name}/program/resource/euren-US.res
%{_libdir}/%{name}/program/resource/foren-US.res
%{_libdir}/%{name}/program/resource/foruien-US.res
%{_libdir}/%{name}/program/resource/fps_officeen-US.res
%{_libdir}/%{name}/program/resource/frmen-US.res
%{_libdir}/%{name}/program/resource/fween-US.res
%{_libdir}/%{name}/program/resource/galen-US.res
%{_libdir}/%{name}/program/resource/impen-US.res
%{_libdir}/%{name}/program/resource/ofaen-US.res
%{_libdir}/%{name}/program/resource/pcren-US.res
%{_libdir}/%{name}/program/resource/pdffilteren-US.res
%{_libdir}/%{name}/program/resource/sben-US.res
%{_libdir}/%{name}/program/resource/scnen-US.res
%{_libdir}/%{name}/program/resource/sden-US.res
%{_libdir}/%{name}/program/resource/sdbten-US.res
%{_libdir}/%{name}/program/resource/sfxen-US.res
%{_libdir}/%{name}/program/resource/spaen-US.res
%{_libdir}/%{name}/program/resource/svlen-US.res
%{_libdir}/%{name}/program/resource/svten-US.res
%{_libdir}/%{name}/program/resource/svxen-US.res
%{_libdir}/%{name}/program/resource/swen-US.res
%{_libdir}/%{name}/program/resource/textconversiondlgsen-US.res
%{_libdir}/%{name}/program/resource/tken-US.res
%{_libdir}/%{name}/program/resource/tplen-US.res
%{_libdir}/%{name}/program/resource/upden-US.res
%{_libdir}/%{name}/program/resource/uuien-US.res
%{_libdir}/%{name}/program/resource/vclen-US.res
%{_libdir}/%{name}/program/resource/wzien-US.res
%{_libdir}/%{name}/program/resource/xmlsecen-US.res
%{_libdir}/%{name}/program/resource/xsltdlgen-US.res
%{_libdir}/%{name}/program/tde-open-url

%dir %{_libdir}/%{name}/share
%dir %{_libdir}/%{name}/share/Scripts
%{_libdir}/%{name}/share/Scripts/beanshell
%{_libdir}/%{name}/share/Scripts/javascript
%if %{with java}
%{_libdir}/%{name}/share/Scripts/java
%endif

%dir %{_libdir}/%{name}/share/autocorr
%{_libdir}/%{name}/share/autocorr/acor_*.dat
%dir %{_libdir}/%{name}/share/autotext
%{_libdir}/%{name}/share/autotext/en-US
%{_libdir}/%{name}/share/basic
%dir %{_libdir}/%{name}/share/config
%{_libdir}/%{name}/share/config/images.zip
%{_libdir}/%{name}/share/config/images_crystal.zip
%{_libdir}/%{name}/share/config/images_hicontrast.zip
%{_libdir}/%{name}/share/config/images_oxygen.zip
%{_libdir}/%{name}/share/config/images_tango.zip
%{_libdir}/%{name}/share/config/*.xpm
%dir %{_libdir}/%{name}/share/config/soffice.cfg
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules
%{_libdir}/%{name}/share/config/soffice.cfg/modules/BasicIDE
%{_libdir}/%{name}/share/config/soffice.cfg/modules/StartModule
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/dbapp
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/dbbrowser
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/dbquery
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/dbreport
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/dbtdata
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/scalc
%{_libdir}/%{name}/share/config/soffice.cfg/modules/schart
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/sdraw
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/sglobal
%{_libdir}/%{name}/share/config/soffice.cfg/modules/sglobal/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/sglobal/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/sglobal/toolbar
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/sweb
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/simpress
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/swform
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swform/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swform/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swform/toolbar
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/swreport
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swreport/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swreport/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swreport/toolbar
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/swriter
%dir %{_libdir}/%{name}/share/config/soffice.cfg/modules/swxform
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swxform/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swxform/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swxform/toolbar
%{_libdir}/%{name}/share/config/webcast
%{_libdir}/%{name}/share/config/wizard
%dir %{_libdir}/%{name}/share/dtd
%{_libdir}/%{name}/share/dtd/officedocument
%{_libdir}/%{name}/share/fonts
%{_libdir}/%{name}/share/gallery
%{_libdir}/%{name}/share/psprint

%dir %{_libdir}/%{name}/share/registry
%{_libdir}/%{name}/share/registry/Langpack-en-US.xcd
%{_libdir}/%{name}/share/registry/lingucomponent.xcd
%{_libdir}/%{name}/share/registry/main.xcd
%{_libdir}/%{name}/share/registry/oo-ad-ldap.xcd.sample
%{_libdir}/%{name}/share/registry/oo-ldap.xcd.sample
%dir %{_libdir}/%{name}/share/registry/res
%{_libdir}/%{name}/share/registry/res/fcfg_langpack_en-US.xcd

%dir %{_libdir}/%{name}/share/samples
%dir %{_libdir}/%{name}/share/samples/en-US

%dir %{_libdir}/%{name}/share/template
%{_libdir}/%{name}/share/template/en-US
%dir %{_libdir}/%{name}/share/template/common
%{_libdir}/%{name}/share/template/common/layout
%dir %{_libdir}/%{name}/share/template/wizard
%{_libdir}/%{name}/share/template/wizard/bitmap
%dir %{_libdir}/%{name}/share/template/wizard/letter
%{_libdir}/%{name}/share/template/wizard/letter/en-US

%dir %{_libdir}/%{name}/share/wordbook
%{_libdir}/%{name}/share/wordbook/en-GB.dic
%{_libdir}/%{name}/share/wordbook/en-US.dic
%{_libdir}/%{name}/share/wordbook/sl.dic
%{_libdir}/%{name}/share/wordbook/technical.dic

%dir %{_libdir}/%{name}/share/xslt
%{_libdir}/%{name}/share/xslt/common
%dir %{_libdir}/%{name}/share/xslt/export
%{_libdir}/%{name}/share/xslt/export/common
%{_libdir}/%{name}/share/xslt/export/spreadsheetml
%{_libdir}/%{name}/share/xslt/export/uof
%{_libdir}/%{name}/share/xslt/export/wordml
%{_libdir}/%{name}/share/xslt/import

# symlink to directory
%attr(755,root,root) %{_libdir}/%{name}/ure-link

%attr(755,root,root) %{_libdir}/%{name}/program/libnpsoplugin.so
%attr(755,root,root) %{_libdir}/%{name}/program/spadmin
%attr(755,root,root) %{_libdir}/%{name}/program/soffice
%attr(755,root,root) %{_libdir}/%{name}/program/soffice.bin
%attr(755,root,root) %{_libdir}/%{name}/program/unoinfo
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg.bin
%{_libdir}/%{name}/program/bootstraprc
%{_libdir}/%{name}/program/flat_logo.svg
%{_libdir}/%{name}/program/fundamentalrc
%{_libdir}/%{name}/program/intro.png
%{_libdir}/%{name}/program/redirectrc
%{_libdir}/%{name}/program/setuprc
%{_libdir}/%{name}/program/shell
%{_libdir}/%{name}/program/sofficerc

# symlinks
%{_libdir}/%{name}/help
%{_libdir}/%{name}/readmes

%dir %{_datadir}/%{name}/readmes
%{_datadir}/%{name}/readmes/README_en-US
%{_libdir}/%{name}/share/config/images_brand.zip
%dir %{_libdir}/%{name}/share/extensions
%{_libdir}/%{name}/share/extensions/package.txt

%{_datadir}/mime/packages/libreoffice.xml
%{_iconsdir}/hicolor/*/mimetypes/libreoffice-*.png
%{_iconsdir}/hicolor/*/mimetypes/libreoffice-*.svg
%{_iconsdir}/hicolor/*/apps/libreoffice-main.png
%{_iconsdir}/hicolor/*/apps/libreoffice-main.svg

%{_desktopdir}/libreoffice-qstart.desktop
%{_desktopdir}/libreoffice-startcenter.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-startcenter.png
%{_iconsdir}/hicolor/*/apps/libreoffice-startcenter.svg

%{_mandir}/man1/loffice.1
%{_mandir}/man1/lofromtemplate.1
%{_mandir}/man1/libreoffice.1*
%{_mandir}/man1/unopkg.1*

%if %{with kde}
%files libs-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/kde-open-url
%attr(755,root,root) %{_libdir}/%{name}/program/kdebe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/kdefilepicker
%attr(755,root,root) %{_libdir}/%{name}/program/fps_kde.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libkabdrv1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libkab1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_kde*.so
%endif

%if %{with kde4}
%files libs-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/kde-open-url
%attr(755,root,root) %{_libdir}/%{name}/program/kde4be1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_kde4*.so
%endif

%files libs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/gconfbe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/gnome-open-url
%attr(755,root,root) %{_libdir}/%{name}/program/gnome-open-url.bin
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_gtk*.so
%attr(755,root,root) %{_libdir}/%{name}/program/ucpgio1.uno.so
%{_libdir}/%{name}/share/registry/gnome.xcd

%files base
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lobase
%attr(755,root,root) %{_bindir}/oobase
%attr(755,root,root) %{_libdir}/%{name}/program/sbase
%{_mandir}/man1/lobase.1
%{_desktopdir}/libreoffice-base.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-base.png
%{_iconsdir}/hicolor/*/apps/libreoffice-base.svg
%attr(755,root,root) %{_libdir}/%{name}/program/libabplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdbplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/librptlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/librptuilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/librptxmllo.so
%{_libdir}/%{name}/program/resource/abpen-US.res
%{_libdir}/%{name}/program/resource/cnren-US.res
%{_libdir}/%{name}/program/resource/dbpen-US.res
%{_libdir}/%{name}/program/resource/dbuen-US.res
%{_libdir}/%{name}/program/resource/rpten-US.res
%{_libdir}/%{name}/program/resource/rptuien-US.res
%{_libdir}/%{name}/program/resource/sdbclen-US.res
%{_libdir}/%{name}/program/resource/sdberren-US.res
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbapp/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbapp/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbapp/toolbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbbrowser/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbbrowser/toolbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbquery/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbquery/toolbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbrelation
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbreport/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbreport/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbreport/toolbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbtable
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbtdata/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/dbtdata/toolbar
%{_libdir}/%{name}/share/registry/base.xcd
%{_datadir}/%{name}/help/en/sdatabase.*

%files calc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/localc
%attr(755,root,root) %{_bindir}/oocalc
%attr(755,root,root) %{_libdir}/%{name}/program/scalc
%{_mandir}/man1/localc.1
%{_desktopdir}/libreoffice-calc.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-calc.png
%{_iconsdir}/hicolor/*/apps/libreoffice-calc.svg
%{_datadir}/%{name}/help/en/scalc.*
%attr(755,root,root) %{_libdir}/%{name}/program/libanalysislo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcalclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdatelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscfiltlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsclo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscuilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsolverlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/vbaobj.uno.so
%{_libdir}/%{name}/program/resource/analysisen-US.res
%{_libdir}/%{name}/program/resource/dateen-US.res
%{_libdir}/%{name}/program/resource/solveren-US.res
%{_libdir}/%{name}/program/resource/scen-US.res
%{_libdir}/%{name}/share/config/soffice.cfg/modules/scalc/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/scalc/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/scalc/toolbar
%{_libdir}/%{name}/share/registry/calc.xcd

%files draw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lodraw
%attr(755,root,root) %{_bindir}/oodraw
%attr(755,root,root) %{_libdir}/%{name}/program/sdraw
%{_mandir}/man1/lodraw.1
%{_desktopdir}/libreoffice-draw.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-draw.png
%{_iconsdir}/hicolor/*/apps/libreoffice-draw.svg
%{_datadir}/%{name}/help/en/sdraw.*
%{_libdir}/%{name}/share/config/soffice.cfg/modules/sdraw/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/sdraw/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/sdraw/toolbar
%{_libdir}/%{name}/share/registry/draw.xcd

%files emailmerge
%defattr(644,root,root,755)
%{_libdir}/%{name}/program/mailmerge.py*
%{_libdir}/%{name}/program/msgbox.py*

%files writer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lowriter
%attr(755,root,root) %{_bindir}/oowriter
%attr(755,root,root) %{_libdir}/%{name}/program/libhwplo.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblwpftlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmswordlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswuilo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libt602filterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwpftwriterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwriterfilterlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/vbaswobj.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/swriter
%{_mandir}/man1/lowriter.1
%{_desktopdir}/libreoffice-writer.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-writer.png
%{_iconsdir}/hicolor/*/apps/libreoffice-writer.svg
%{_datadir}/%{name}/help/en/swriter.*
%{_libdir}/%{name}/program/resource/t602filteren-US.res
%{_libdir}/%{name}/share/config/soffice.cfg/modules/sbibliography
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swriter/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swriter/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/swriter/toolbar
%{_libdir}/%{name}/share/registry/writer.xcd

%files impress
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/loimpress
%attr(755,root,root) %{_bindir}/ooimpress
%attr(755,root,root) %{_libdir}/%{name}/program/simpress
%attr(755,root,root) %{_libdir}/%{name}/program/OGLTrans.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libanimcorelo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libplaceware*.so
%{_mandir}/man1/loimpress.1
%{_desktopdir}/libreoffice-impress.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-impress.png
%{_iconsdir}/hicolor/*/apps/libreoffice-impress.svg
%{_datadir}/%{name}/help/en/simpress.*
%{_libdir}/%{name}/share/config/soffice.cfg/simpress
%{_libdir}/%{name}/share/config/soffice.cfg/modules/simpress/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/simpress/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/simpress/toolbar
%{_libdir}/%{name}/share/registry/impress.xcd
%{_libdir}/%{name}/share/registry/ogltrans.xcd

%files math
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lomath
%attr(755,root,root) %{_bindir}/oomath
%{_mandir}/man1/lomath.1
%{_desktopdir}/libreoffice-math.desktop
%{_iconsdir}/hicolor/*/apps/libreoffice-math.png
%{_iconsdir}/hicolor/*/apps/libreoffice-math.svg
%{_datadir}/%{name}/help/en/smath.*
%attr(755,root,root) %{_libdir}/%{name}/program/libsmdlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsmlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/smath
%{_libdir}/%{name}/program/resource/smen-US.res
%{_libdir}/%{name}/share/config/soffice.cfg/modules/smath
%{_libdir}/%{name}/share/registry/math.xcd

%files web
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/loweb
%attr(755,root,root) %{_bindir}/ooweb
%{_mandir}/man1/loweb.1
%{_libdir}/%{name}/share/config/soffice.cfg/modules/sweb/menubar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/sweb/statusbar
%{_libdir}/%{name}/share/config/soffice.cfg/modules/sweb/toolbar

%files graphicfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libflashlo.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvgfilterlo.so
%{_libdir}/%{name}/share/registry/graphicfilter.xcd

%files xsltfilter
%defattr(644,root,root,755)
%{_libdir}/%{name}/share/registry/xsltfilter.xcd
%{_libdir}/%{name}/share/xslt/docbook
%{_libdir}/%{name}/share/xslt/export/xhtml
%{_desktopdir}/libreoffice-xsltfilter.desktop

%if %{with java}
%files javafilter
%defattr(644,root,root,755)
%{_libdir}/%{name}/program/classes/pexcel.jar
%{_libdir}/%{name}/program/classes/pocketword.jar
%{_libdir}/%{name}/program/classes/aportisdoc.jar
%{_libdir}/%{name}/share/registry/palm.xcd
%{_libdir}/%{name}/share/registry/pocketexcel.xcd
%{_libdir}/%{name}/share/registry/pocketword.xcd
%{_desktopdir}/libreoffice-javafilter.desktop
%endif

%files postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/postgresql-sdbc.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/postgresql-sdbc-impl.uno.so
%{_libdir}/%{name}/program/postgresql-sdbc.ini
%{_libdir}/%{name}/program/services/postgresql-sdbc.rdb
%{_libdir}/%{name}/share/registry/postgresqlsdbc.xcd

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
%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/ure/bin/javaldx
%endif
%dir %{_libdir}/%{name}/ure/lib
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/namingservice.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libaffine_uno_uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/bootstrap.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/acceptor.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/connector.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/introspection.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/invocadapt.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/proxyfac.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/reflection.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libunsafe_uno_uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/streams.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/textinstream.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/textoutstream.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/uuresolver.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/liblog_uno_uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libsal_textenc.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libstore.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libsunjavaplugin.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libuno_cppu.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libuno_cppuhelpergcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libuno_purpenvhelpergcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libuno_sal.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libuno_salhelpergcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/stocservices.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/invocation.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libgcc3_uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjvmaccessgcc3.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjvmfwk.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libreg.so.3
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/binaryurp.uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libxmlreader.so
%{_libdir}/%{name}/ure/lib/jvmfwk3rc
%{_libdir}/%{name}/ure/lib/unorc
%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjava_uno.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjuh.so
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/libjuhx.so
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

%files pyuno -f script-provider-for-python.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libpyuno.so
%attr(755,root,root) %{_libdir}/%{name}/program/pythonloader.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/pyuno.so
%{_libdir}/%{name}/program/pythonloader.unorc
%{_libdir}/%{name}/program/officehelper.py
%{_libdir}/%{name}/program/pythonloader.py
%{_libdir}/%{name}/program/uno.py
%{_libdir}/%{name}/program/unohelper.py
%{_libdir}/%{name}/share/registry/pyuno.xcd

# script-provider-for-python extension
%dir %{_libdir}/%{name}/share/extensions/script-provider-for-python
%{_libdir}/%{name}/share/extensions/script-provider-for-python/META-INF
%{_libdir}/%{name}/share/extensions/script-provider-for-python/components.rdb
%{_libdir}/%{name}/share/extensions/script-provider-for-python/description.xml
%{_libdir}/%{name}/share/extensions/script-provider-for-python/*.py
%{_libdir}/%{name}/share/extensions/script-provider-for-python/registration

# python wizards
%dir %{_libdir}/%{name}/program/wizards
%{_libdir}/%{name}/program/wizards/*.py
%dir %{_libdir}/%{name}/program/wizards/common
%{_libdir}/%{name}/program/wizards/common/*.py
%dir %{_libdir}/%{name}/program/wizards/document
%{_libdir}/%{name}/program/wizards/document/*.py
%dir %{_libdir}/%{name}/program/wizards/fax
%{_libdir}/%{name}/program/wizards/fax/*.py
%dir %{_libdir}/%{name}/program/wizards/text
%{_libdir}/%{name}/program/wizards/text/*.py
%dir %{_libdir}/%{name}/program/wizards/ui
%{_libdir}/%{name}/program/wizards/ui/*.py
%dir %{_libdir}/%{name}/program/wizards/ui/event
%{_libdir}/%{name}/program/wizards/ui/event/*.py

# samples there
%{_libdir}/%{name}/share/Scripts/python

%files pdfimport -f pdfimport.lang
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/share/extensions/pdfimport
%attr(755,root,root) %{_libdir}/%{name}/share/extensions/pdfimport/pdfimport.uno.so
%attr(755,root,root) %{_libdir}/%{name}/share/extensions/pdfimport/xpdfimport
%{_libdir}/%{name}/share/extensions/pdfimport/META-INF
%{_libdir}/%{name}/share/extensions/pdfimport/basic
%{_libdir}/%{name}/share/extensions/pdfimport/components.rdb
%{_libdir}/%{name}/share/extensions/pdfimport/description.xml
%{_libdir}/%{name}/share/extensions/pdfimport/images
%{_libdir}/%{name}/share/extensions/pdfimport/registration
%{_libdir}/%{name}/share/extensions/pdfimport/*.xcu
%{_libdir}/%{name}/share/extensions/pdfimport/*.pdf

%files presentation-minimizer -f presentation-minimizer.lang
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/share/extensions/presentation-minimizer
%attr(755,root,root) %{_libdir}/%{name}/share/extensions/presentation-minimizer/SunPresentationMinimizer.uno.so
%{_libdir}/%{name}/share/extensions/presentation-minimizer/META-INF
%{_libdir}/%{name}/share/extensions/presentation-minimizer/bitmaps
%{_libdir}/%{name}/share/extensions/presentation-minimizer/components.rdb
%{_libdir}/%{name}/share/extensions/presentation-minimizer/description.xml
%{_libdir}/%{name}/share/extensions/presentation-minimizer/registr*

%files presenter-screen -f presenter-screen.lang
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/share/extensions/presenter-screen
%attr(755,root,root) %{_libdir}/%{name}/share/extensions/presenter-screen/PresenterScreen.uno.so
%{_libdir}/%{name}/share/extensions/presenter-screen/META-INF
%{_libdir}/%{name}/share/extensions/presenter-screen/bitmaps
%{_libdir}/%{name}/share/extensions/presenter-screen/components.rdb
%{_libdir}/%{name}/share/extensions/presenter-screen/description.xml
%{_libdir}/%{name}/share/extensions/presenter-screen/help
%{_libdir}/%{name}/share/extensions/presenter-screen/registry

%files report-builder -f report-builder.lang
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/share/extensions/report-builder
%{_libdir}/%{name}/share/extensions/report-builder/META-INF
%{_libdir}/%{name}/share/extensions/report-builder/images
%{_libdir}/%{name}/share/extensions/report-builder/registration
%{_libdir}/%{name}/share/extensions/report-builder/registry
%{_libdir}/%{name}/share/extensions/report-builder/template
%{_libdir}/%{name}/share/extensions/report-builder/THIRDPARTYREADMELICENSE.html
%{_libdir}/%{name}/share/extensions/report-builder/components.rdb
%{_libdir}/%{name}/share/extensions/report-builder/description.xml
%{_libdir}/%{name}/share/extensions/report-builder/readme*
%{_libdir}/%{name}/share/extensions/report-builder/*.jar

%files wiki-publisher -f wiki-publisher.lang
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/share/extensions/wiki-publisher
%{_libdir}/%{name}/share/extensions/wiki-publisher/META-INF
%{_libdir}/%{name}/share/extensions/wiki-publisher/WikiEditor
%{_libdir}/%{name}/share/extensions/wiki-publisher/filter
%{_libdir}/%{name}/share/extensions/wiki-publisher/help
%{_libdir}/%{name}/share/extensions/wiki-publisher/license
%{_libdir}/%{name}/share/extensions/wiki-publisher/registration
%{_libdir}/%{name}/share/extensions/wiki-publisher/templates
%{_libdir}/%{name}/share/extensions/wiki-publisher/*.xc*
%{_libdir}/%{name}/share/extensions/wiki-publisher/components.rdb
%{_libdir}/%{name}/share/extensions/wiki-publisher/description.xml
%{_libdir}/%{name}/share/extensions/wiki-publisher/mediawiki.jar

%if %{with mozilla}
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libnpsoplugin.so
%attr(755,root,root) %{_libdir}/%{name}/program/nsplugin
%endif

%if %{with binfilter}
%files binfilter
%defattr(644,root,root,755)
%{_libdir}/%{name}/program/legacy_binfilters.rdb
%{_libdir}/%{name}/program/libbf_frmlo.so
%{_libdir}/%{name}/program/libbf_golo.so
%{_libdir}/%{name}/program/libbf_migratefilterlo.so
%{_libdir}/%{name}/program/libbf_ofalo.so
%{_libdir}/%{name}/program/libbf_sblo.so
%{_libdir}/%{name}/program/libbf_schlo.so
%{_libdir}/%{name}/program/libbf_sclo.so
%{_libdir}/%{name}/program/libbf_sdlo.so
%{_libdir}/%{name}/program/libbf_smlo.so
%{_libdir}/%{name}/program/libbf_solo.so
%{_libdir}/%{name}/program/libbf_svtlo.so
%{_libdir}/%{name}/program/libbf_svxlo.so
%{_libdir}/%{name}/program/libbf_swlo.so
%{_libdir}/%{name}/program/libbf_wrapperlo.so
%{_libdir}/%{name}/program/libbf_xolo.so
%{_libdir}/%{name}/program/libbindetlo.so
%{_libdir}/%{name}/program/liblegacy_binfilterslo.so
%{_libdir}/%{name}/program/resource/bf_frmen-US.res
%{_libdir}/%{name}/program/resource/bf_ofaen-US.res
%{_libdir}/%{name}/program/resource/bf_scen-US.res
%{_libdir}/%{name}/program/resource/bf_schen-US.res
%{_libdir}/%{name}/program/resource/bf_sden-US.res
%{_libdir}/%{name}/program/resource/bf_smen-US.res
%{_libdir}/%{name}/program/resource/bf_svten-US.res
%{_libdir}/%{name}/program/resource/bf_svxen-US.res
%{_libdir}/%{name}/program/resource/bf_swen-US.res
%{_libdir}/%{name}/share/registry/binfilter.xcd
%{_desktopdir}/libreoffice-binfilter.desktop
%endif

%if %{with i18n}
%files i18n-af -f af.lang
%defattr(644,root,root,755)

%files i18n-am -f am.lang
%defattr(644,root,root,755)

%files i18n-ar -f ar.lang
%defattr(644,root,root,755)

%files i18n-as -f as.lang
%defattr(644,root,root,755)

%files i18n-ast -f ast.lang
%defattr(644,root,root,755)

%files i18n-be_BY -f be.lang
%defattr(644,root,root,755)

%files i18n-bg -f bg.lang
%defattr(644,root,root,755)

%files i18n-bn -f bn.lang
%defattr(644,root,root,755)

%files i18n-bn_IN -f bn_IN.lang
%defattr(644,root,root,755)

%files i18n-bo -f bo.lang
%defattr(644,root,root,755)

%files i18n-br -f br.lang
%defattr(644,root,root,755)

%files i18n-brx -f brx.lang
%defattr(644,root,root,755)

%files i18n-bs -f bs.lang
%defattr(644,root,root,755)

%files i18n-ca -f ca.lang
%defattr(644,root,root,755)

%files i18n-ca_XV -f ca_XV.lang
%defattr(644,root,root,755)

%files i18n-cs -f cs.lang
%defattr(644,root,root,755)

%files i18n-cy -f cy.lang
%defattr(644,root,root,755)

%files i18n-da -f da.lang
%defattr(644,root,root,755)

%files i18n-de -f de.lang
%defattr(644,root,root,755)

%files i18n-dgo -f dgo.lang
%defattr(644,root,root,755)

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

%files i18n-gu -f gu.lang
%defattr(644,root,root,755)

%files i18n-he -f he.lang
%defattr(644,root,root,755)

%files i18n-hi -f hi.lang
%defattr(644,root,root,755)

%files i18n-hr -f hr.lang
%defattr(644,root,root,755)

%files i18n-hu -f hu.lang
%defattr(644,root,root,755)

%files i18n-id -f id.lang
%defattr(644,root,root,755)

%files i18n-is -f is.lang
%defattr(644,root,root,755)

%files i18n-it -f it.lang
%defattr(644,root,root,755)

%files i18n-ja -f ja.lang
%defattr(644,root,root,755)

%files i18n-ka -f ka.lang
%defattr(644,root,root,755)

%files i18n-kk -f kk.lang
%defattr(644,root,root,755)

%files i18n-km -f km.lang
%defattr(644,root,root,755)

%files i18n-kn_IN -f kn.lang
%defattr(644,root,root,755)

%files i18n-ko -f ko.lang
%defattr(644,root,root,755)
%{_libdir}/%{name}/share/registry/korea.xcd

%files i18n-kok -f kok.lang
%defattr(644,root,root,755)

%files i18n-ks -f ks.lang
%defattr(644,root,root,755)

%files i18n-ku -f ku.lang
%defattr(644,root,root,755)

%files i18n-lb -f lb.lang
%defattr(644,root,root,755)

%files i18n-lo -f lo.lang
%defattr(644,root,root,755)

%files i18n-lt -f lt.lang
%defattr(644,root,root,755)

%files i18n-lv -f lv.lang
%defattr(644,root,root,755)

%files i18n-mai -f mai.lang
%defattr(644,root,root,755)

%files i18n-mk -f mk.lang
%defattr(644,root,root,755)

%files i18n-ml -f ml.lang
%defattr(644,root,root,755)

%files i18n-mn -f mn.lang
%defattr(644,root,root,755)

%files i18n-mni -f mni.lang
%defattr(644,root,root,755)

%files i18n-mr -f mr.lang
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

%files i18n-nso -f nso.lang
%defattr(644,root,root,755)

%files i18n-oc -f oc.lang
%defattr(644,root,root,755)

%files i18n-om -f om.lang
%defattr(644,root,root,755)

%files i18n-or -f or.lang
%defattr(644,root,root,755)

%files i18n-pa_IN -f pa_IN.lang
%defattr(644,root,root,755)

%files i18n-pl -f pl.lang
%defattr(644,root,root,755)

%files i18n-pt -f pt.lang
%defattr(644,root,root,755)

%files i18n-pt_BR -f pt_BR.lang
%defattr(644,root,root,755)

%files i18n-qtz -f qtz.lang
%defattr(644,root,root,755)

%files i18n-ro -f ro.lang
%defattr(644,root,root,755)

%files i18n-ru -f ru.lang
%defattr(644,root,root,755)

%files i18n-rw -f rw.lang
%defattr(644,root,root,755)

%files i18n-sa_IN -f sa_IN.lang
%defattr(644,root,root,755)

%files i18n-sat -f sat.lang
%defattr(644,root,root,755)

%files i18n-sd -f sd.lang
%defattr(644,root,root,755)

%files i18n-sh -f sh.lang
%defattr(644,root,root,755)

%files i18n-si -f si.lang
%defattr(644,root,root,755)

%files i18n-sk -f sk.lang
%defattr(644,root,root,755)

%files i18n-sl -f sl.lang
%defattr(644,root,root,755)

%files i18n-sq -f sq.lang
%defattr(644,root,root,755)

%files i18n-sr -f sr.lang
%defattr(644,root,root,755)

%files i18n-ss -f ss.lang
%defattr(644,root,root,755)

%files i18n-st -f st.lang
%defattr(644,root,root,755)

%files i18n-sv -f sv.lang
%defattr(644,root,root,755)

%files i18n-sw_TZ -f sw_TZ.lang
%defattr(644,root,root,755)

%files i18n-ta -f ta.lang
%defattr(644,root,root,755)

%files i18n-te -f te.lang
%defattr(644,root,root,755)

%files i18n-tg -f tg.lang
%defattr(644,root,root,755)

%files i18n-th -f th.lang
%defattr(644,root,root,755)

%files i18n-tn -f tn.lang
%defattr(644,root,root,755)

%files i18n-tr -f tr.lang
%defattr(644,root,root,755)

%files i18n-ts -f ts.lang
%defattr(644,root,root,755)

%files i18n-tt -f tt.lang
%defattr(644,root,root,755)

%files i18n-ug -f ug.lang
%defattr(644,root,root,755)

%files i18n-uk -f uk.lang
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

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
/etc/bash_completion.d/*
