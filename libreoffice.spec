# NOTE:
#	- normal build (athlon) requires about 25 GB of disk space:
#		$BUILD_ROOT	7.0 GB
#		BUILD	       16.2 GB
#		SRPMS		0.3 GB
#		RPMS		1.2 GB
#
# 2.3.0 NOTES/TODO:
#  - needs some help to build: when the build fails complaining about --enable-gtk,
#    go to rpm/BUILD/ooo-build-trunk dir, type make and go grab some coffee. 
#    After some time it will eventually fail on sc/util (_sv_rules empty), workaround:
#    comment out the `.IF "$(VBA_EXTENSION)"=="YES"' section (3 lines) in 
#    build/current/sc/util/makefile.mk, and rerun the build. It will complete, yet it will
#    fail on install...
#    
#
# TODO:
#   /usr/share/openoffice.org/share/registry/modules/org/openoffice/Office/Common/Common-ctl_dz.xcu
#   /usr/share/openoffice.org/share/registry/modules/org/openoffice/Setup/Langpack-dz.xcu
#   - --with mono wants static mono
#	- without system_db will not work (w/ java) as it will use db4.2 which is too old (see r1.650)
#	- problems with gcc-4.2.0: oowriter is useless (invisble text till refresh)
#	- fix help files (broken links)
#	- LFS support is disabled (no_lfs_hack.patch for xml2cmp crash) because it need LFS-ready STLport
#	- maybe it could be build with gcc-java
#   - adapt help-support.diff to PLD
#	- configure --without-ppds --without afms
#	- /share/config/soffice.cfg/global/accelerator/es/ should be in i18n-es
#	- fix locale names and other locale related things
#   - can't be just i18n-{be,gu,hi,kn,pa,ta} instead of *-{be_BY,*_IN}?
#   - more system libs todo:
#	- (SYSTEM_HYPH) bcond system_libhnj doesn't work - needs Debian-patched version of libhnj
#	- --with-system-mythes + mythes package (http://lingucomponent.openoffice.org/thesaurus.html)
#   - --with-system-mspack - use libmspack already installed on system
#	- bcond system_xt doesn't work - xt in PLD is too old or broken
#
#	$ grep SYSTEM ooo-build-ooe680-m6/build/ooe680-m6/config_office/config.log |grep NO
#
# MAYBE TODO:
#	- drop requirement on nas-devel
#	- in gtk version menu highlight has almost the same colour as menu text
#	- 6 user/config/*.so? files shared between -i18n-en and -i18n-sl
#	- add ooglobal symlink and it's ooo-wrapper entry (among calc|draw|impress|math|web|writer)

# Conditional build:
%bcond_without	gnomevfs	# GNOME VFS and Evolution 2 support
%bcond_without	java		# without Java support (disables help support)
%bcond_without	kde		# KDE L&F packages
%bcond_with	mono		# enable compilation of mono bindings
%bcond_without	mozilla		# without mozilla components
%bcond_without	i18n		# do not create i18n packages
%bcond_with	ccache		# use ccache to speed up builds
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

%define		upd			680
%define		mws			OOG%{upd}
%define		tag			%(echo %{mws} | tr A-Z a-z)-%{milestone}
%define		milestone	m6
%define		_tag		%(echo %{tag} | tr - _)
%define		_rel		0.0.2

Summary:	OpenOffice.org - powerful office suite
Summary(pl.UTF-8):	OpenOffice.org - potężny pakiet biurowy
Name:		openoffice.org
Version:	2.3.0
Release:	%{_tag}.%{_rel}
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
# svn export http://svn.gnome.org/svn/ooo-build/trunk ooo-build-trunk
Source0:	ooo-build-r10528.tar.bz2
# Source0-md5:	38c96dad2491e1dab116083450ed5070
Source1:	http://go-oo.org/packages/%{mws}/%{tag}-core.tar.bz2
# Source1-md5:	02ef9044f6339bdd76cd1a37291b406d
Source2:	http://go-oo.org/packages/%{mws}/%{tag}-system.tar.bz2
# Source2-md5:	593aa8e2a8c311cc216170e0f0a34355
Source3:	http://go-oo.org/packages/%{mws}/%{tag}-binfilter.tar.bz2
# Source3-md5:	c79086fb3c1f3309ba3ccf7a660ce23c
Source4:	http://go-oo.org/packages/%{mws}/%{tag}-lang.tar.bz2
# Source4-md5:	e7057a8dbfc7f0ee6b065e556b382ac4
Source10:	http://go-oo.org/packages/SRC680/ooo_custom_images-13.tar.bz2
# Source10-md5:	2480af7f890c8175c7f9e183a1b39ed2
Source11:	http://go-oo.org/packages/SRC680/ooo_crystal_images-6.tar.bz2
# Source11-md5:	586d0f26b3f79d89bbb5b25b874e3df6
Source12:	http://go-oo.org/packages/SRC680/extras-2.tar.bz2
# Source12-md5:	733051ebeffae5232a2eb760162da020
Source15:	http://go-oo.org/packages/xt/xt-20051206-src-only.zip
# Source15-md5:	0395e6e7da27c1cea7e1852286f6ccf9
Source16:	http://go-oo.org/packages/SRC680/lp_solve_5.5.0.10_source.tar.gz
# Source16-md5:	26b3e95ddf3d9c077c480ea45874b3b8
Source17:	http://go-oo.org/packages/SRC680/biblio.tar.bz2
# Source17-md5:	1948e39a68f12bfa0b7eb309c14d940c
Source18:	http://go-oo.org/packages/%{mws}/cli_types.dll
# Source18-md5:	3cdaf368e99caa3331130a5edf148490
Source19:	http://go-oo.org/packages/%{mws}/cli_types_bridgetest.dll
# Source19-md5:	cadc605a6b0265b8167001b4788ff113
Source20:	http://go-oo.org/packages/SRC680/libwps-0.1.0~svn20070129.tar.gz
# Source20-md5:	2e442485100f7e00685737513f853546
Source21:	http://go-oo.org/packages/SRC680/libwpg-0.1.0.tar.gz
# Source21-md5:	1d9644fb4c90511255c1576b4b30b1d2
Source22:       http://download.go-oo.org/SRC680/oox.2007-09-05.tar.bz2
# Source22-md5:	42aceb3508ff8b5ed04d0451b30f6ccf
Source50:	openabout_pld.png
# Source50-md5:	64a945a07b64ebc0a12adfde4c99da8a
# patches applied in prep section
Patch0:		%{name}-PLD.patch
#Patch1:		%{name}-sc-dataform.patch
Patch2:		%{name}-stl5_fix.patch
Patch3:		%{name}-mdbtools_fix.diff
Patch4:		%{name}-nolfs_hack.patch
Patch6:		%{name}-java16.patch
Patch7:		%{name}-nodictinst.patch
Patch8:		%{name}-73257.patch
Patch9:		%{name}-apply.patch
# patches applied by ooo-patching-system
Patch100:	%{name}-STL-lib64.diff
Patch101:	%{name}-64bit-inline.diff
Patch102:	%{name}-build-pld-splash.diff
Patch104:	%{name}-portaudio_v19.diff
Patch107:	%{name}-stl-amd64.patch
Patch108:	%{name}-java6.patch
Patch109:	%{name}-agg25.patch
Patch110:	%{name}-nsplugin-path.diff
Patch111:	%{name}-perl-nodiag.patch
Patch112:	%{name}-gcc42-swregion.diff
URL:		http://www.openoffice.org/
BuildRequires:	/usr/bin/getopt
BuildRequires:	STLport-devel >= 2:5.0.0
%{?with_system_agg:BuildRequires:	agg-devel}
BuildRequires:	autoconf >= 2.51
BuildRequires:	automake >= 1:1.9
%{?with_system_beanshell:BuildRequires:	beanshell}
BuildRequires:	bison >= 1.875-4
BuildRequires:	boost-devel
BuildRequires:	boost-mem_fn-devel
BuildRequires:	boost-spirit-devel
BuildRequires:	boost-uBLAS-devel
BuildRequires:	cairo-devel >= 0.5.2
%{?with_ccache:BuildRequires:	ccache}
BuildRequires:	cups-devel
BuildRequires:	curl-devel >= 7.9.8
%{?with_system_db:BuildRequires:	db-cxx-devel}
%{?with_system_db:BuildRequires:	db-devel}
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.1
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel}
BuildRequires:	gperf
BuildRequires:	gstreamer-devel >= 0.10.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	gtk+2-devel
%{?with_system_hsqldb:BuildRequires:	hsqldb >= 1.8.0.8}
%{?with_system_hunspell:BuildRequires:	hunspell-devel}
BuildRequires:	icu
%{?with_kde:BuildRequires:	kdelibs-devel}
BuildRequires:	libart_lgpl-devel
BuildRequires:	libbonobo-devel >= 2.0
%{?with_csystem_libhnj:BuildRequires:	libhnj-devel}
BuildRequires:	libicu-devel >= 3.4
BuildRequires:	libjpeg-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel >= 5:3.2.1
BuildRequires:	libsvg-devel >= 0.1.4
BuildRequires:	libwpd-devel >= 0.8.6
BuildRequires:	libwps-devel
BuildRequires:	libxml2-devel >= 2.0
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
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel
BuildRequires:	python >= 2.2
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	sablotron-devel
BuildRequires:	sane-backends-devel
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	tcsh
BuildRequires:	unixODBC-devel >= 2.2.12-2
BuildRequires:	unzip
%{?with_system_xalan:BuildRequires:	xalan-j}
%{?with_system_xerces:BuildRequires:	xerces-j}
%{?with_system_xml_apis:BuildRequires:	xml-commons}
BuildRequires:	xmlsec1-nss-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
%{?with_system_xt:BuildRequires:	xt}
BuildRequires:	zip
BuildRequires:	zlib-devel
%if %{with java}
BuildRequires:	ant
%{?with_system_db:BuildRequires:	db-java >= 4.3}
BuildRequires:	jar
BuildRequires:	jdk >= 1.4.0_00
BuildRequires:	jre-X11
%else
BuildRequires:	libxslt-progs
%endif
BuildRequires:	xulrunner-devel
BuildConflicts:	STLport4
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
Requires:	fonts-TTF-OpenSymbol = %{epoch}:%{version}-%{release}
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
%{?with_system_beanshell:Requires:	beanshell}
# libcups.so.2 is dlopened (in cupsmgr.cxx); maybe Suggests instead?
Requires:	cups-lib
%{?with_system_hsqldb:Requires:	hsqldb >= 1.8.0}
Requires:	libstdc++ >= 5:3.2.1
Requires:	mktemp
Requires:	sed
%{?with_system_xalan:Requires:	xalan-j}
%{?with_system_xerces:Requires:	xerces-j}
%{?with_system_xml_apis:Requires:	xml-commons}
%{?with_system_xt:Requires:	xt}
Obsoletes:	oooqs
Obsoletes:	openoffice
Obsoletes:	openoffice-libs
Obsoletes:	openoffice.org-dirs
Obsoletes:	openoffice.org-libs < 1:2.1.0-0.m6.0.11
#Suggests:	chkfontpath

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

%package -n fonts-TTF-OpenSymbol
Summary:	OpenSymbol fonts
Summary(pl.UTF-8):	Fonty OpenSymbol
Group:		Fonts
Requires(post,postun):	fontpostinst
Obsoletes:	openoffice.org-fonts-OpenSymbol

%description -n fonts-TTF-OpenSymbol
OpenSymbol TrueType fonts.

%description -n fonts-TTF-OpenSymbol -l pl.UTF-8
Fonty TrueType OpenSymbol.

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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-br
This package provides resources containing menus and dialogs in Breton
language.

%description i18n-br -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bretońskim.

%package i18n-bs
Summary:	OpenOffice.org - interface in Bosnian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku bośniańskim
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-bs
This package provides resources containing menus and dialogs in
Bosnian language.

%description i18n-bs -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bośniańskim

%package i18n-ca
Summary:	OpenOffice.org - interface in Catalan language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku katalońskim
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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

%package i18n-fo
Summary:	OpenOffice.org - interface in Faroese language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku farerskim
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fo
Obsoletes:	openoffice-i18n-fo-gtk
Obsoletes:	openoffice.org-i18n-fo-gtk
Obsoletes:	openoffice.org-i18n-fo-kde

%description i18n-fo
This package provides resources containing menus and dialogs in
Faroese language.

%description i18n-fo -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
farerskim.

%package i18n-fr
Summary:	OpenOffice.org - interface in French language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku francuskim
Group:		X11/Applications
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
Group:		X11/Applications
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

%package i18n-gl
Summary:	OpenOffice.org - interface in Galician language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku galicyjskim
Group:		X11/Applications
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
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-gu_IN
This package provides resources containing menus and dialogs in
Gujarati language.

%description i18n-gu_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gudźarati.

%package i18n-he
Summary:	OpenOffice.org - interface in Hebrew language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku hebrajskim
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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

%package i18n-ia
Summary:	OpenOffice.org - interface in Interlingua language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku interlingua
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ia
Obsoletes:	openoffice-i18n-ia-gtk
Obsoletes:	openoffice.org-i18n-ia-gtk
Obsoletes:	openoffice.org-i18n-ia-kde

%description i18n-ia
This package provides resources containing menus and dialogs in
Interlingua language.

%description i18n-ia -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
interlingua.

%package i18n-id
Summary:	OpenOffice.org - interface in Indonesian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku indonezyjskim
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-id
Obsoletes:	openoffice-i18n-id-gtk
Obsoletes:	openoffice.org-i18n-id-gtk
Obsoletes:	openoffice.org-i18n-id-kde

%description i18n-id
This package provides resources containing menus and dialogs in
Indonesian language.

%description i18n-id -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
indonezyjskim.

%package i18n-it
Summary:	OpenOffice.org - interface in Italian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku włoskim
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ka
This package provides resources containing menus and dialogs in Georgian
language.

%package i18n-km
Summary:	OpenOffice.org - interface in Khmer language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku khmerskim
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ku
This package provides resources containing menus and dialogs in
Kurdish language.

%description i18n-ku -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kurdyjskim.

%package i18n-la
Summary:	OpenOffice.org - interface in Latin language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku łacińskim
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-la
Obsoletes:	openoffice-i18n-la-gtk
Obsoletes:	openoffice.org-i18n-la-gtk
Obsoletes:	openoffice.org-i18n-la-kde

%description i18n-la
This package provides resources containing menus and dialogs in Latin
language.

%description i18n-la -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
łacińskim.

%package i18n-lo
Summary:	OpenOffice.org - interface in Lao language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku laotańskim
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-lv
This package provides resources containing menus and dialogs in
Latvian language.

%description i18n-lv -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
łotewskim.

%package i18n-med
Summary:	OpenOffice.org - interface in Melpa language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku melpa
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-med
Obsoletes:	openoffice-i18n-med-gtk
Obsoletes:	openoffice.org-i18n-med-gtk
Obsoletes:	openoffice.org-i18n-med-kde

%description i18n-med
This package provides resources containing menus and dialogs in Melpa
language.

%description i18n-med -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
melpa.

%package i18n-mi
Summary:	OpenOffice.org - interface in Maori language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku maoryjskim
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-mi
Obsoletes:	openoffice-i18n-mi-gtk
Obsoletes:	openoffice.org-i18n-mi-gtk
Obsoletes:	openoffice.org-i18n-mi-kde

%description i18n-mi
This package provides resources containing menus and dialogs in Maori
language.

%description i18n-mi -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
maoryjskim.

%package i18n-mk
Summary:	OpenOffice.org - interface in Macedonian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku macedońskim
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-mr_IN
This package provides resources containing menus and dialogs in
Marathi language for India.

%description i18n-mr_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
marathi dla Indii.

%package i18n-ms
Summary:	OpenOffice.org - interface in Malay language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku malajskim
Group:		X11/Applications
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

%package i18n-nb
Summary:	OpenOffice.org - interface in Norwegian Bokmaal language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku norweskim (odmiana Bokmaal)
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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

%package i18n-or_IN
Summary:	OpenOffice.org - interface in Oriya language for India
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku orija dla Indii
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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

%package i18n-ro
Summary:	OpenOffice.org - interface in Romanian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku rumuńskim
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ro
Obsoletes:	openoffice-i18n-ro-gtk
Obsoletes:	openoffice.org-i18n-ro-gtk
Obsoletes:	openoffice.org-i18n-ro-kde

%description i18n-ro
This package provides resources containing menus and dialogs in
Romanian language.

%description i18n-ro -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
rumuńskim.

%package i18n-ru
Summary:	OpenOffice.org - interface in Russian language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku rosyjskim
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-sr
This package provides resources containing menus and dialogs in
Serbian language.

%description i18n-sr -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
serbskim.

%package i18n-ss
Summary:	OpenOffice.org - interface in Siswant language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku siswati
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ss
This package provides resources containing menus and dialogs in
Siswant language.

%description i18n-ss -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
siswati.

%package i18n-st
Summary:	OpenOffice.org - interface in Southern Sotho language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku południowym sotho
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-sw_TZ
This package provides resources containing menus and dialogs in
Swahili language for Tanzania.

%description i18n-sw_TZ -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
suahili dla Tanzanii.

%package i18n-sx
Summary:	OpenOffice.org - interface in Sutu language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku sutu
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-sx
This package provides resources containing menus and dialogs in Sutu
language.

%description i18n-sx -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
sutu.

%package i18n-ta_IN
Summary:	OpenOffice.org - interface in Tamil language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku tamiskim
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description i18n-ur_IN
This package provides resources containing menus and dialogs in Urdu
language for India.

%description i18n-ur_IN -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
urdu dla Indii.

%package i18n-ve
Summary:	OpenOffice.org - interface in Venda language
Summary(pl.UTF-8):	OpenOffice.org - interfejs w języku venda
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
Group:		X11/Applications
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
%setup -q -n ooo-build-trunk
install -d src

# sources, icons, KDE_icons
ln -sf %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
	%{SOURCE10} %{SOURCE11} %{SOURCE12} \
	%{SOURCE15} %{SOURCE16} %{SOURCE17} \
	%{SOURCE18} %{SOURCE19} \
	%{SOURCE20} %{SOURCE21} %{SOURCE22} \
	src

cp %{SOURCE50} src

# fixes for the patch subsystem
%patch0 -p1
#%patch1 -p0

#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
%patch6 -p1
#%if %{with system_myspell}
#%patch7 -p1
#%endif
#%patch8 -p1
#%patch9 -p1

# 64 bit related patches (not applied now)
#install %{PATCH100} patches/64bit
#install %{PATCH101} patches/64bit/64bit-inline.diff

#%ifarch %{x8664}
#echo "[ PLD64bitfixes ]" >> patches/src680/apply
## patches applied by ooo (extension .diff is required)
#for P in %{PATCH107}; do
#	PATCHNAME=PLD-${P##*/%{name}-}
#	PATCHNAME=${PATCHNAME%.patch}.diff
#	install $P patches/src680/$PATCHNAME
#	echo $PATCHNAME >> patches/src680/apply
#done
#%endif

echo "[ PLDOnly ]" >> patches/src680/apply
# patches applied by ooo (extension .diff is required)
#for P in %{PATCH102} %{PATCH104} %{PATCH108} %{PATCH109} %{PATCH111} %{PATCH112}; do
for P in %{PATCH108}; do
	PATCHNAME=PLD-${P##*/%{name}-}
	PATCHNAME=${PATCHNAME%.patch}.diff
	install $P patches/src680/$PATCHNAME
	echo $PATCHNAME >> patches/src680/apply
done
#cp %{PATCH110} patches/src680/nsplugin-path.diff

%build
# Make sure we have /proc mounted - otherwise idlc will fail later.
if [ ! -f /proc/cpuinfo ]; then
	echo "You need to have /proc mounted in order to build this package!"
	exit 1
fi

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

export ENVCFLAGS="%{rpmcflags}"
# disable STLport 5.1 containers extension, doesn't work with map indexed by enum
export ENVCFLAGSCXX="%{rpmcflags} -fpermissive -D_STLP_NO_CONTAINERS_EXTENSION"
export DESTDIR=$RPM_BUILD_ROOT
export IGNORE_MANIFEST_CHANGES=1
export QTINC="%{_includedir}/qt"
export QTLIB="%{_libdir}"

%if %{with java}
export JAVA_HOME="%{java_home}"
export DB_JAR="%{_javadir}/db.jar"
export ANT_HOME="%{_datadir}/ant"
%endif

export DEFAULT_TO_ENGLISH_FOR_PACKING=1

RPM_BUILD_NR_THREADS="%(echo "%{__make}" | sed -e 's#.*-j\([[:space:]]*[0-9]\+\)#\1#g')"
[ "$RPM_BUILD_NR_THREADS" = "%{__make}" ] && RPM_BUILD_NR_THREADS=1
RPM_BUILD_NR_THREADS=$(echo $RPM_BUILD_NR_THREADS)

if [ -f "%{_javadir}/serializer.jar" ];then
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
	--with-system-expat \
	--with-system-freetype \
	--with-system-gcc \
	--without-system-icu \
	--with-system-jpeg \
	--with-system-libsvg \
	--with-system-libwpd \
	--with-system-libwps \
	--with-system-libxml \
	--with-system-nas \
	--with-system-neon \
	--with-system-odbc-headers \
	--with-system-portaudio \
	--with-system-python \
	--with-system-sablot \
	--with-system-sane-header \
	--with-system-sndfile \
	--with-system-stdlibs \
	--with-system-x11-extensions-headers \
	--with-system-xmlsec \
	--with-system-xrender \
	--with-system-xrender-headers=yes \
	--with-system-zlib \
%if %{with mozilla}
	--with-system-mozilla \
	--with-xulrunner \
%else
	--disable-mozilla \
%endif
	--with-dynamic-xinerama \
	--with-intro-bitmaps="\$SRCDIR/openintro_pld.bmp" \
	--with-about-bitmaps="\$SRCDIR/openabout_pld.png" \
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
	--with-system-libxslt \
%endif
%if %{with gnomevfs}
	--enable-gnome-vfs \
%else
	--disable-gnome-vfs \
%endif
	--with-docdir=%{_docdir}/%{name}-%{version} \
	--with-python=%{__python} \
	--with-stlport=/usr \
	--with-x \
	--without-fonts \
	--without-gpc \
	--disable-epm \
	--disable-fontooo \
	--disable-strip \
	--%{?with_msaccess:en}%{!?with_msaccess:dis}able-access \
	--enable-cairo \
	--enable-crypt-link \
	--%{?with_mono:en}%{!?with_mono:dis}able-mono \
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
	--with-num-cpus=$RPM_BUILD_NR_THREADS \
	--with-build-version=%{version}-%{release} \
	--with-tag=%{tag} \
	--with-drink=coffee \
	--enable-split-app-modules \
	--enable-split-opt-features
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
%configure \
	CC="$CC" \
	CXX="$CXX" \
	CPP="$CPP" \
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
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	# clean file listings
	rm -f build/*_list.txt

	# limit to single process installation, it's safe at least
	%{__sed} -i -e 's#^BUILD_NCPUS=.*#BUILD_NCPUS=1#g' bin/setup

	export DESTDIR=$RPM_BUILD_ROOT
	export TMP="%{tmpdir}"
	export TEMP="%{tmpdir}"
	export DEFAULT_TO_ENGLISH_FOR_PACKING=1

	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT

	# save orignal install layout
	find $RPM_BUILD_ROOT -ls > ls.txt
	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	# do we need those? large comparing to png
	rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/*.svg

	# is below comment true?
	# OOo should not install the Vera fonts, they are Required: now
	rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/share/fonts/truetype/*

	# some libs creep in somehow
	rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libstl*.so*
	rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libsndfile*
	rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libgcc_s.so*
	rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libstdc++*so*

	rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/sopatchlevel.sh

	# Remove setup log
	rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/setup.log

	rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/xdg
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

	%if %{with mono}
	rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/mono-ooo-2.1.pc
	%endif

	# Remove dictionaries (in separate pkg)
	rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo/*
	%if %{with system_myspell}
	rmdir $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo
	ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo
	%else
	touch $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo/dictionary.lst
	%endif

	%if %{with mozilla}
	install -d $RPM_BUILD_ROOT%{_browserpluginsdir}
	ln -s %{_libdir}/%{name}/program/libnpsoplugin.so $RPM_BUILD_ROOT%{_browserpluginsdir}
	%endif

	# configs
	install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
	mv $RPM_BUILD_ROOT{%{_libdir}/%{name}/program,%{_sysconfdir}/%{name}}/sofficerc
	ln -s %{_sysconfdir}/%{name}/sofficerc $RPM_BUILD_ROOT%{_libdir}/%{name}/program

	perl -pi -e 's/^[       ]*LD_LIBRARY_PATH/# LD_LIBRARY_PATH/;s/export LD_LIBRARY_PATH/# export LD_LIBRARY_PATH/' \
		$RPM_BUILD_ROOT%{_libdir}/%{name}/program/setup

	chmod +x $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*.so

	install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
	# put share to %{_datadir} so we're able to produce noarch packages
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/share $RPM_BUILD_ROOT%{_datadir}/%{name}
	ln -s ../../share/%{name}/share $RPM_BUILD_ROOT%{_libdir}/%{name}/share
	# more non-archidecture dependant nature data
	%if %{with java}
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/help $RPM_BUILD_ROOT%{_datadir}/%{name}
	ln -s ../../share/%{name}/help $RPM_BUILD_ROOT%{_libdir}/%{name}/help
	%endif
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/licenses $RPM_BUILD_ROOT%{_datadir}/%{name}
	ln -s ../../share/%{name}/licenses $RPM_BUILD_ROOT%{_libdir}/%{name}/licenses
	mv $RPM_BUILD_ROOT%{_libdir}/%{name}/readmes $RPM_BUILD_ROOT%{_datadir}/%{name}
	ln -s ../../share/%{name}/readmes $RPM_BUILD_ROOT%{_libdir}/%{name}/readmes

	# fix python
	sed -i -e 's|#!/bin/python|#!%{_bindir}/python|g' $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*.py

	# Copy fixed OpenSymbol to correct location
	install -d $RPM_BUILD_ROOT%{_fontsdir}/TTF
	install build/%{tag}/extras/source/truetype/symbol/opens___.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

	# Add in the regcomp tool since some people need it for 3rd party add-ons
	cp -a build/%{tag}/solver/%{upd}/unxlng*.pro/bin/regcomp{,.bin} $RPM_BUILD_ROOT%{_libdir}/%{name}/program/

	# Rename .desktop files to avoid conflicts with other applications .desktops
	# TODO: make patch instead.
	for a in $RPM_BUILD_ROOT%{_desktopdir}/*.desktop; do
		d=$(dirname "$a")
		f=$(basename "$a")
		mv $a $d/oo$f
	done

	touch installed.stamp
fi

# Find out locales
find_lang() {
	local lang="$1"
	echo "%%defattr(644,root,root,755)" > ${lang}.lang

	# help files
	if [ -f build/help_${lang}_list.txt ]; then
		cat build/help_${lang}_list.txt >> ${lang}.lang
	fi

	lfile="build/lang_${lang}_list.txt"
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
		# lib/openoffice.org/share/samples/$lang
		grep "/share/samples/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/share/samples/${lang}/" ${lfile} >> ${lang}.lang || :
		%if %{with java}
		grep "/help/${lang}$" ${lfile} >> ${lang}.lang || :
		grep "/help/${lang}/" ${lfile} >> ${lang}.lang || :
		%endif
		grep "/share/config/soffice.cfg/modules/swform/accelerator/${lang}/" build/common_list.txt >> ${lang}.lang || :
		grep "/share/config/soffice.cfg/modules/swreport/accelerator/${lang}/" build/common_list.txt >> ${lang}.lang || :
		grep "/share/config/soffice.cfg/modules/swxform/accelerator/${lang}/" build/common_list.txt >> ${lang}.lang || :
	fi
}

rm -f *.lang*
langlist=$(ls build/lang_*_list.txt | sed -e 's=build/lang_\(.*\)_list.txt=\1=g')

for lang in $langlist; do
	find_lang $lang
done

%{__sed} -i -e '
	s,%{_libdir}/%{name}/help,%{_datadir}/%{name}/help,;
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
if [ -L %{_libdir}/%{name}/presets ]; then
	rm -f %{_libdir}/%{name}/presets
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

%post -n fonts-TTF-OpenSymbol
fontpostinst TTF

%postun -n fonts-TTF-OpenSymbol
fontpostinst TTF

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

# TODO: check where these really belong
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_go680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdeploymentmisc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvbaobj680*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/stringresource680*.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/updatefeed.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/fastsax.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libacc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libaffine_uno_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasebmp680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_sb680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libguesslang680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/liblog680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/liboox680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/librpt680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/librptui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/librptxml680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsax680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libt602filter680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextcat.so
%attr(755,root,root) %{_libdir}/%{name}/program/libunsafe_uno_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_svp680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwpgimport680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwriterfilter680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/simplecanvas.uno.so
%{_datadir}/%{name}/share/config/images_tango.zip
%{_datadir}/%{name}/share/registry/data/org/openoffice/UserProfile.xcu
#%{_libdir}/%{name}/program/resource/scsolver680en-US.res
%{_libdir}/%{name}/program/root3.dat
%{_libdir}/%{name}/program/root4.dat
%{_libdir}/%{name}/program/root5.dat
%{_libdir}/%{name}/program/resource/acc680en-US.res
%{_libdir}/%{name}/program/resource/chartcontroller680en-US.res
%{_libdir}/%{name}/program/resource/rpt680en-US.res
%{_libdir}/%{name}/program/resource/rptui680en-US.res
%{_libdir}/%{name}/program/resource/sb680en-US.res
%{_libdir}/%{name}/program/resource/sdbcl680en-US.res
%{_libdir}/%{name}/program/resource/t602filter680en-US.res
%{_datadir}/%{name}/share/config/javasettingsunopkginstall.xml

%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/swform
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/swform/accelerator
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swform/accelerator/en-US
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swform/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swform/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swform/statusbar
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport/accelerator
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swreport/accelerator/en-US
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform/accelerator
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform/menubar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform/statusbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform/toolbar
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swxform/accelerator/en-US


%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/sofficerc

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/program
%dir %{_libdir}/%{name}/program/resource

%attr(755,root,root) %{_libdir}/%{name}/install-dict
%{_libdir}/%{name}/program/*.rdb
%{_libdir}/%{name}/program/*.bmp
%{_libdir}/%{name}/program/sofficerc
%{_libdir}/%{name}/program/unorc
%{_libdir}/%{name}/program/bootstraprc
%{_libdir}/%{name}/program/configmgrrc

# symlinks
%{_libdir}/%{name}/licenses
%{_libdir}/%{name}/readmes
%{_libdir}/%{name}/share

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/share
%dir %{_datadir}/%{name}/share/Scripts
%dir %{_datadir}/%{name}/share/config
%dir %{_datadir}/%{name}/share/registry
%dir %{_datadir}/%{name}/share/registry/data
%dir %{_datadir}/%{name}/share/registry/data/org
%dir %{_datadir}/%{name}/share/registry/data/org/openoffice
%dir %{_datadir}/%{name}/share/registry/data/org/openoffice/Office
%dir %{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI
%dir %{_datadir}/%{name}/share/registry/modules
%dir %{_datadir}/%{name}/share/registry/modules/org
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/Office
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Scripting
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Writer
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/GraphicFilter
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Misc
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types
%dir %{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort
%dir %{_datadir}/%{name}/share/registry/schema
%dir %{_datadir}/%{name}/share/registry/schema/org
%dir %{_datadir}/%{name}/share/registry/schema/org/openoffice
%dir %{_datadir}/%{name}/share/registry/schema/org/openoffice/Office
%dir %{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI
%dir %{_datadir}/%{name}/share/registry/schema/org/openoffice/TypeDetection
%dir %{_datadir}/%{name}/share/registry/schema/org/openoffice/ucb
%dir %{_datadir}/%{name}/share/autocorr
%dir %{_datadir}/%{name}/share/autotext

%{_datadir}/%{name}/share/basic
%{_datadir}/%{name}/share/config/symbol
%{_datadir}/%{name}/share/config/webcast
%{_datadir}/%{name}/share/config/*.xpm
%{_datadir}/%{name}/share/config/images.zip
%{_datadir}/%{name}/share/config/images_crystal.zip
%{_datadir}/%{name}/share/config/images_industrial.zip
%{_datadir}/%{name}/share/config/images_hicontrast.zip
%dir %{_datadir}/%{name}/share/config/soffice.cfg
%{_datadir}/%{name}/share/config/soffice.cfg/global/
%dir %{_datadir}/%{name}/share/config/soffice.cfg/modules/
%{_datadir}/%{name}/share/config/soffice.cfg/modules/BasicIDE
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sglobal
%{_datadir}/%{name}/share/config/soffice.cfg/modules/StartModule
%{_datadir}/%{name}/share/config/wizard
%dir %{_datadir}/%{name}/share/dict
%{!?with_system_myspell:%dir %{_datadir}/%{name}/share/dict/ooo}
%{?with_system_myspell:%{_datadir}/%{name}/share/dict/ooo}
%{!?with_system_myspell:%ghost %{_datadir}/%{name}/share/dict/ooo/dictionary.lst}
%{_datadir}/%{name}/share/dtd
%{_datadir}/%{name}/share/fingerprint
%{_datadir}/%{name}/share/fonts
%{_datadir}/%{name}/share/gallery
%{_datadir}/%{name}/share/psprint
%dir %{_datadir}/%{name}/share/samples
%dir %{_datadir}/%{name}/share/samples/en-US
%dir %{_datadir}/%{name}/share/template
%dir %{_datadir}/%{name}/share/template/wizard
%dir %{_datadir}/%{name}/share/template/wizard/letter
%dir %{_datadir}/%{name}/share/wordbook
%{_datadir}/%{name}/share/readme
%dir %{_datadir}/%{name}/share/registry/res
%dir %{_datadir}/%{name}/share/registry/data/org/openoffice/TypeDetection
%dir %{_datadir}/%{name}/share/registry/data/org/openoffice/ucb
%{_datadir}/%{name}/share/registry/data/org/openoffice/FirstStartWizard.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Inet.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/LDAP.xcu.sample
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Calc.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Common.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Compatibility.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/DataAccess.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Embedding.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/ExtendedColorScheme.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/ExtensionManager.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/FormWizard.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Impress.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Jobs.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Labels.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Logging.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Math.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Paths.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/ProtocolHandler.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Scripting.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Security.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/SFX.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/TableWizard.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/BaseWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/BasicIDECommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/BasicIDEWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/BibliographyCommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/ChartCommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/ChartWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/Controller.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbBrowserWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbQueryWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbRelationWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbReportWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbTableWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbuCommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/DrawImpressCommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/Factories.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/GenericCategories.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/GenericCommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/MathWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/ReportCommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/StartModuleCommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/StartModuleWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/WriterFormWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/WriterReportWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/XFormsWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Views.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/WebWizard.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/Writer.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Setup.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/TypeDetection/UISort.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/VCL.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/ucb/Configuration.xcu
%{_datadir}/%{name}/share/registry/schema/org/openoffice/FirstStartWizard.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Inet.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/LDAP.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Addons.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/CalcAddIns.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Calc.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Chart.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Commands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Common.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Compatibility.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/DataAccess.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Draw.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Embedding.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Events.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/ExtendedColorScheme.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/ExtensionManager.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/FormWizard.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Impress.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Java.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Jobs.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Labels.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Linguistic.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Logging.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Math.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/OptionsDialog.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Paths.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/ProtocolHandler.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Recovery.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/ReportDesign.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Scripting.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Security.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/SFX.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Substitution.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/TabBrowse.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/TableWizard.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/TypeDetection.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/BaseWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/BasicIDECommands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/BasicIDEWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/BibliographyCommands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/BibliographyWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/Category.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/ChartCommands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/ChartWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/Commands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/Controller.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbBrowserWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbQueryWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbRelationWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbReportWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbTableWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbuCommands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DrawImpressCommands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/Factories.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/GenericCategories.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/GenericCommands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/GlobalSettings.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/MathWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/ReportCommands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/StartModuleCommands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/StartModuleWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WriterFormWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WriterReportWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/XFormsWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Views.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/WebWizard.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/WriterWeb.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/Writer.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Setup.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/System.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/TypeDetection/Filter.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/TypeDetection/GraphicFilter.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/TypeDetection/Misc.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/TypeDetection/Types.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/TypeDetection/UISort.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/UserProfile.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/VCL.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/ucb/Configuration.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/ucb/Hierarchy.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/ucb/Store.xcs
%{_datadir}/%{name}/share/registry/ldap
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-cjk_ja.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-cjk_ko.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-cjk_zh-CN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-cjk_zh-TW.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_ar.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_dz.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_fa.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_gu-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_he.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_hi-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_km.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_lo.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_ne.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_pa-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_ta-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_th.xcu
#%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_vi.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-dicooo.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-korea.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-unx.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-UseOOoFileDialogs.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-calc.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-chart.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-draw.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-impress.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-math.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-report.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-writer.xcu
# move it to -writer ?
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Writer/Writer-cjk_ja.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Writer/Writer-cjk_ko.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Writer/Writer-cjk_zh-CN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Writer/Writer-cjk_zh-TW.xcu
# move to locale pkgs?
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-af.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ar.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-as-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-be-BY.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-bg.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-bn-BD.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-bn-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-bn.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-br.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-bs.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ca.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-cs.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-cy.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-da.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-de.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-dz.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-el.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-en-GB.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-en-US.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-en-ZA.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-eo.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-es.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-et.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-eu.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-fa.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-fi.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-fr.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ga.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-gl.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-gu-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-he.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-hi-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-hr.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-hu.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-it.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ja.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-km.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-kn-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ko.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ku.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-lo.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-lt.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-lv.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-mk.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ml-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-mr-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ms.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-nb.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ne.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-nl.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-nn.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-nr.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ns.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-or-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-pa-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-pl.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-pt-BR.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-pt.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ru.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-rw.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sh-YU.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sk.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sl.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sr-CS.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ss.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-st.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sv.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sw-TZ.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sw.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sx.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ta-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-te-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-tg.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-th.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ti-ER.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-tn.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-tr.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ts.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-uk.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ur-IN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ve.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-vi.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-xh.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-zh-CN.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-zh-TW.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-zu.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ka.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-report.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_global_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_base_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_chart_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/GraphicFilter/fcfg_internalgraphics_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_base_others.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_chart_others.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_base_types.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_chart_types.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_internalgraphics_types.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-calc.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-draw.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-impress.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-math.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-writer.xcu

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

# Programs
%attr(755,root,root) %{_bindir}/ooconfig
%attr(755,root,root) %{_bindir}/ooffice
%attr(755,root,root) %{_bindir}/oofromtemplate
%attr(755,root,root) %{_bindir}/ootool

%attr(755,root,root) %{_libdir}/%{name}/program/configimport.bin
%attr(755,root,root) %{_libdir}/%{name}/program/gengal.bin
%{_libdir}/%{name}/program/pkgchk
%attr(755,root,root) %{_libdir}/%{name}/program/pkgchk.bin
%attr(755,root,root) %{_libdir}/%{name}/program/pluginapp.bin
%attr(755,root,root) %{_libdir}/%{name}/program/setofficelang.bin
%attr(755,root,root) %{_libdir}/%{name}/program/soffice.bin
%attr(755,root,root) %{_libdir}/%{name}/program/spadmin.bin
%attr(755,root,root) %{_libdir}/%{name}/program/uno
%attr(755,root,root) %{_libdir}/%{name}/program/uno.bin
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg.bin
%attr(755,root,root) %{_libdir}/%{name}/program/ooqstart
%attr(755,root,root) %{_libdir}/%{name}/program/pagein*
%attr(755,root,root) %{_libdir}/%{name}/program/regcomp
%attr(755,root,root) %{_libdir}/%{name}/program/regcomp.bin
%{_libdir}/%{name}/program/setuprc
%attr(755,root,root) %{_libdir}/%{name}/program/smath
%attr(755,root,root) %{_libdir}/%{name}/program/soffice
%attr(755,root,root) %{_libdir}/%{name}/program/spadmin
%attr(755,root,root) %{_libdir}/%{name}/program/open-url
%attr(755,root,root) %{_libdir}/%{name}/program/gengal
%attr(755,root,root) %{_libdir}/%{name}/program/configimport
%attr(755,root,root) %{_libdir}/%{name}/program/sbase
%attr(755,root,root) %{_libdir}/%{name}/program/senddoc
%attr(755,root,root) %{_libdir}/%{name}/program/setofficelang
%attr(755,root,root) %{_libdir}/%{name}/program/unopkg
%attr(755,root,root) %{_libdir}/%{name}/program/uri-encode
%attr(755,root,root) %{_libdir}/%{name}/program/viewdoc
%{_libdir}/%{name}/program/versionrc

%if %{with mono}
%{_libdir}/%{name}/program/cli_basetypes.dll
%{_libdir}/%{name}/program/cli_cppuhelper.dll
%{_libdir}/%{name}/program/cli_types.dll
%{_libdir}/%{name}/program/cli_uno_bridge.dll
%{_libdir}/%{name}/program/cli_ure.dll
%attr(755,root,root) %{_libdir}/%{name}/program/libcli_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcli_uno_glue.so
%endif

%if %{with java}
%{_libdir}/%{name}/help
%dir %{_datadir}/%{name}/help
%dir %{_datadir}/%{name}/help/en
%{_datadir}/%{name}/help/en/*.html
%{_datadir}/%{name}/help/en/*.css
%{_datadir}/%{name}/help/en/sbasic.*
%{_datadir}/%{name}/help/en/schart.*
%{_datadir}/%{name}/help/en/shared.*
%{_datadir}/%{name}/help/*.xsl

%attr(755,root,root) %{_libdir}/%{name}/program/javaldx
%attr(755,root,root) %{_libdir}/%{name}/program/java-set-classpath
%{_libdir}/%{name}/program/jvmfwk3rc
%{_libdir}/%{name}/program/JREProperties.class

%dir %{_libdir}/%{name}/program/classes
%{_libdir}/%{name}/program/classes/ScriptFramework.jar
%{_libdir}/%{name}/program/classes/ScriptProviderForBeanShell.jar
%{_libdir}/%{name}/program/classes/ScriptProviderForJava.jar
%{_libdir}/%{name}/program/classes/ScriptProviderForJavaScript.jar
%{_libdir}/%{name}/program/classes/XMergeBridge.jar
%{_libdir}/%{name}/program/classes/XSLTFilter.jar
%{_libdir}/%{name}/program/classes/XSLTValidate.jar
%{_libdir}/%{name}/program/classes/agenda.jar
%{_libdir}/%{name}/program/classes/classes.jar
%{_libdir}/%{name}/program/classes/commonwizards.jar
%{_libdir}/%{name}/program/classes/fax.jar
%{_libdir}/%{name}/program/classes/form.jar
%{!?with_system_hsqldb:%{_libdir}/%{name}/program/classes/hsqldb.jar}
%{_libdir}/%{name}/program/classes/java_uno.jar
#%{_libdir}/%{name}/program/classes/java_uno_accessbridge.jar
%{_libdir}/%{name}/program/classes/js.jar
%{_libdir}/%{name}/program/classes/juh.jar
%{_libdir}/%{name}/program/classes/jurt.jar
%{_libdir}/%{name}/program/classes/jut.jar
%{_libdir}/%{name}/program/classes/letter.jar
%{_libdir}/%{name}/program/classes/officebean.jar
%{_libdir}/%{name}/program/classes/query.jar
%{_libdir}/%{name}/program/classes/report.jar
%{_libdir}/%{name}/program/classes/ridl.jar
%{_libdir}/%{name}/program/classes/sandbox.jar
%{_libdir}/%{name}/program/classes/sdbc_hsqldb.jar
%{!?with_system_xalan:%{_libdir}/%{name}/program/classes/serializer.jar}
%{_libdir}/%{name}/program/classes/table.jar
%{_libdir}/%{name}/program/classes/unoil.jar
%{_libdir}/%{name}/program/classes/unoloader.jar
%{_libdir}/%{name}/program/classes/web.jar
%{!?with_system_xalan:%{_libdir}/%{name}/program/classes/xalan.jar}
%{!?with_system_xerces:%{_libdir}/%{name}/program/classes/xercesImpl.jar}
%{_libdir}/%{name}/program/classes/xmerge.jar
%{!?with_system_xml_apis:%{_libdir}/%{name}/program/classes/xml-apis.jar}

%{_datadir}/%{name}/share/Scripts/beanshell
%{_datadir}/%{name}/share/Scripts/javascript
%{_datadir}/%{name}/share/Scripts/java
%{_datadir}/%{name}/share/config/javavendors.xml

%dir %{_datadir}/%{name}/share/xslt
%{_datadir}/%{name}/share/xslt/common
%dir %{_datadir}/%{name}/share/xslt/export
%{_datadir}/%{name}/share/xslt/export/common
%{_datadir}/%{name}/share/xslt/export/spreadsheetml
%{_datadir}/%{name}/share/xslt/export/wordml
%{_datadir}/%{name}/share/xslt/import
%{_datadir}/%{name}/share/xslt/odfflatxml
%{_datadir}/%{name}/share/xslt/wiki
%endif

%{_datadir}/mime/packages/openoffice.xml

%{_desktopdir}/ootemplate.desktop

%{_iconsdir}/hicolor/*/apps/ooo-gulls.png
%{_iconsdir}/hicolor/*/apps/ooo-printeradmin.png
%{_iconsdir}/hicolor/*/apps/ooo-template.png
%{_pixmapsdir}/ooo-gulls.png
%{_pixmapsdir}/ooo-template.png

%{_mandir}/man1/ooffice.1
%{_mandir}/man1/oofromtemplate.1
%{_mandir}/man1/openoffice.1*

# en-US
# TODO: use find lang for en-US too?
%{_libdir}/%{name}/presets/config/*_en-US.so*
%{_datadir}/%{name}/share/autocorr/acor_*.dat
%{_datadir}/%{name}/share/autotext/en-US
%{_datadir}/%{name}/share/registry/res/en-US
%{_datadir}/%{name}/share/template/en-US
%dir %{_datadir}/%{name}/share/template/wizard/letter/en-US
%{_datadir}/%{name}/share/template/wizard/letter/en-US/*.ott
%{_datadir}/%{name}/share/wordbook/en-US

%{_libdir}/%{name}/program/resource/abp680en-US.res
%{_libdir}/%{name}/program/resource/analysis680en-US.res
%{_libdir}/%{name}/program/resource/avmedia680en-US.res
%{_libdir}/%{name}/program/resource/basctl680en-US.res
%{_libdir}/%{name}/program/resource/bf_frm680en-US.res
%{_libdir}/%{name}/program/resource/bf_ofa680en-US.res
%{_libdir}/%{name}/program/resource/bf_sc680en-US.res
%{_libdir}/%{name}/program/resource/bf_sch680en-US.res
%{_libdir}/%{name}/program/resource/bf_sd680en-US.res
#%{_libdir}/%{name}/program/resource/bf_sfx680en-US.res
%{_libdir}/%{name}/program/resource/bf_svx680en-US.res
%{_libdir}/%{name}/program/resource/bf_sw680en-US.res
%{_libdir}/%{name}/program/resource/bib680en-US.res
%{_libdir}/%{name}/program/resource/cal680en-US.res
%{_libdir}/%{name}/program/resource/date680en-US.res
%{_libdir}/%{name}/program/resource/dba680en-US.res
%{_libdir}/%{name}/program/resource/dbp680en-US.res
%{_libdir}/%{name}/program/resource/dbu680en-US.res
%{_libdir}/%{name}/program/resource/dbw680en-US.res
%{_libdir}/%{name}/program/resource/deployment680en-US.res
%{_libdir}/%{name}/program/resource/deploymentgui680en-US.res
%{_libdir}/%{name}/program/resource/dkt680en-US.res
%{_libdir}/%{name}/program/resource/egi680en-US.res
%{_libdir}/%{name}/program/resource/eme680en-US.res
%{_libdir}/%{name}/program/resource/epb680en-US.res
%{_libdir}/%{name}/program/resource/epg680en-US.res
%{_libdir}/%{name}/program/resource/epp680en-US.res
%{_libdir}/%{name}/program/resource/eps680en-US.res
%{_libdir}/%{name}/program/resource/ept680en-US.res
%{_libdir}/%{name}/program/resource/eur680en-US.res
%{_libdir}/%{name}/program/resource/fps_office680en-US.res
%{_libdir}/%{name}/program/resource/frm680en-US.res
%{_libdir}/%{name}/program/resource/fwe680en-US.res
%{_libdir}/%{name}/program/resource/gal680en-US.res
%{_libdir}/%{name}/program/resource/imp680en-US.res
%{_libdir}/%{name}/program/resource/ofa680en-US.res
%{_libdir}/%{name}/program/resource/ooo680en-US.res
%{_libdir}/%{name}/program/resource/pcr680en-US.res
%{_libdir}/%{name}/program/resource/pdffilter680en-US.res
%{_libdir}/%{name}/program/resource/preload680en-US.res
%{_libdir}/%{name}/program/resource/productregistration680en-US.res
%{_libdir}/%{name}/program/resource/san680en-US.res
%{_libdir}/%{name}/program/resource/sc680en-US.res
#%{_libdir}/%{name}/program/resource/sch680en-US.res
%{_libdir}/%{name}/program/resource/sd680en-US.res
%{_libdir}/%{name}/program/resource/sdbt680en-US.res
%{_libdir}/%{name}/program/resource/sfx680en-US.res
%{_libdir}/%{name}/program/resource/spa680en-US.res
%{_libdir}/%{name}/program/resource/svs680en-US.res
%{_libdir}/%{name}/program/resource/svt680en-US.res
%{_libdir}/%{name}/program/resource/svx680en-US.res
%{_libdir}/%{name}/program/resource/sw680en-US.res
%{_libdir}/%{name}/program/resource/textconversiondlgs680en-US.res
%{_libdir}/%{name}/program/resource/tfu680en-US.res
%{_libdir}/%{name}/program/resource/tk680en-US.res
%{_libdir}/%{name}/program/resource/tpl680en-US.res
%{_libdir}/%{name}/program/resource/updchk680en-US.res
%{_libdir}/%{name}/program/resource/uui680en-US.res
%{_libdir}/%{name}/program/resource/vcl680en-US.res
%{_libdir}/%{name}/program/resource/wzi680en-US.res
%{_libdir}/%{name}/program/resource/xmlsec680en-US.res
%{_libdir}/%{name}/program/resource/xsltdlg680en-US.res

%dir %{_datadir}/%{name}/licenses
%{_datadir}/%{name}/licenses/LICENSE_en-US
%{_datadir}/%{name}/licenses/LICENSE_en-US.html

%dir %{_datadir}/%{name}/readmes
%{_datadir}/%{name}/readmes/README_en-US
%{_datadir}/%{name}/readmes/README_en-US.html

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
%{!?with_system_agg:%attr(755,root,root) %{_libdir}/%{name}/program/libagg680*.so}
%attr(755,root,root) %{_libdir}/%{name}/program/libanimcore.so
%attr(755,root,root) %{_libdir}/%{name}/program/libavmedia680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libavmediagst.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasctl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasegfx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_frm680*.so
#%attr(755,root,root) %{_libdir}/%{name}/program/libbf_lng680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_migratefilter680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_ofa680*.so
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
%attr(755,root,root) %{_libdir}/%{name}/program/libcanvastools680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcollator_data.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcomphelp4gcc3.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcppcanvas680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libctl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcui680*.so
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
%attr(755,root,root) %{_libdir}/%{name}/program/libevtatt.so
%attr(755,root,root) %{_libdir}/%{name}/program/libexlink680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libexp680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfile680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfileacc.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfilterconfig1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libflat680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfrm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwe680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwi680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwk680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfwm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libgcc3_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libgo680*.so
%{!?with_system_hunspell:%attr(755,root,root) %{_libdir}/%{name}/program/libhunspell.so}
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
%attr(755,root,root) %{_libdir}/%{name}/program/libj680l*_g.so
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
#%attr(755,root,root) %{_libdir}/%{name}/program/libmdb680*.so
#%attr(755,root,root) %{_libdir}/%{name}/program/libmdbimpl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmsworks680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libmysql2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libodbc2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libodbcbase2.so
%attr(755,root,root) %{_libdir}/%{name}/program/liboffacc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpackage2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpcr680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpdffilter680*.so
#%attr(755,root,root) %{_libdir}/%{name}/program/libpk680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpreload680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libprotocolhandler680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libpsp680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libqstart_gtk680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/librecentfile.so
%attr(755,root,root) %{_libdir}/%{name}/program/libres680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsb680*.so
#%attr(755,root,root) %{_libdir}/%{name}/program/libsch680*.so
#%attr(755,root,root) %{_libdir}/%{name}/program/libschd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscn680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscriptframe.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdbc2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdbt680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsdui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsfx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libso680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsot680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspa680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspell680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libspl_unx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsrtrs1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsts680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvt680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsw680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextconv_dict.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtextconversiondlgs680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtfu680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtk680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libtvhlp1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucb1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libucbhelper4gcc3.so
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

%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/program/javaloader.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/javavm.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libhsqldb2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjava_uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjdbc2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjpipe.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjuh.so
%attr(755,root,root) %{_libdir}/%{name}/program/libjuhx.so
%attr(755,root,root) %{_libdir}/%{name}/program/libofficebean.so
%attr(755,root,root) %{_libdir}/%{name}/program/sunjavaplugin.so
%{_libdir}/%{name}/program/libjvmaccessgcc3.so
%{_libdir}/%{name}/program/libjvmfwk.so
%endif

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

%files -n fonts-TTF-OpenSymbol
%defattr(644,root,root,755)
%{_fontsdir}/TTF/*.ttf

%if %{with kde}
%files libs-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/kde-open-url
%attr(755,root,root) %{_libdir}/%{name}/program/kdebe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/kdefilepicker
%attr(755,root,root) %{_libdir}/%{name}/program/fps_kde.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/libkabdrv1.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_kde*.so
%endif

%files libs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/fps_gnome.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/gnome-open-url
%attr(755,root,root) %{_libdir}/%{name}/program/gnome-open-url.bin
%attr(755,root,root) %{_libdir}/%{name}/program/gnome-set-default-application
%attr(755,root,root) %{_libdir}/%{name}/program/libevoab2.so
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_gtk*.so
%if %{with gnomevfs}
%attr(755,root,root) %{_libdir}/%{name}/program/gconfbe1.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/ucpgvfs1.uno.so
%endif

%files base
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oobase
%attr(755,root,root) %{_libdir}/%{name}/program/sbase
%{_mandir}/man1/oobase.1
%{_desktopdir}/oobase.desktop
%{_iconsdir}/hicolor/*/apps/ooo-base.png
%{_pixmapsdir}/ooo-base.png
%{_libdir}/%{name}/program/resource/cnr680en-US.res
%if %{with java}
%{_datadir}/%{name}/help/en/sdatabase.*
%endif
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbapp
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbbrowser
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbquery
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbrelation
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbreport
%{_datadir}/%{name}/share/config/soffice.cfg/modules/dbtable
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-base.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-base.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_database_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_database_others.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_database_types.xcu

%files calc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oocalc
%attr(755,root,root) %{_libdir}/%{name}/program/libanalysis680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_sc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcalc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdate680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libchartcontroller680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libchartmodel680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcharttools680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libchartview680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/scalc
%{_mandir}/man1/oocalc.1
%{_desktopdir}/oocalc.desktop
%{_iconsdir}/hicolor/*/apps/ooo-calc.png
%{_pixmapsdir}/ooo-calc.png
%if %{with java}
%{_datadir}/%{name}/help/en/scalc.*
%endif
%{_libdir}/%{name}/program/resource/analysis680en-US.res
%{_libdir}/%{name}/program/resource/bf_sc680en-US.res
%{_libdir}/%{name}/program/resource/date680en-US.res
%{_libdir}/%{name}/program/resource/sc680en-US.res
%{_datadir}/%{name}/share/config/soffice.cfg/modules/scalc
%{_datadir}/%{name}/share/config/soffice.cfg/modules/schart
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/CalcCommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/CalcWindowState.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-calc.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-calc.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_calc_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_calc_types.xcu
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/CalcCommands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/CalcWindowState.xcs

%files draw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oodraw
%attr(755,root,root) %{_libdir}/%{name}/program/sdraw
%{_mandir}/man1/oodraw.1
%{_desktopdir}/oodraw.desktop
%{_iconsdir}/hicolor/*/apps/ooo-draw.png
%{_pixmapsdir}/ooo-draw.png
%if %{with java}
%{_datadir}/%{name}/help/en/sdraw.*
%endif
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sdraw
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/DrawWindowState.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-draw.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-draw.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_draw_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_draw_types.xcu
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DrawWindowState.xcs

%files emailmerge
%defattr(644,root,root,755)
%{_libdir}/%{name}/program/mailmerge.py*
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Writer/Writer-javamail.xcu

%files writer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oowriter
%attr(755,root,root) %{_libdir}/%{name}/program/libhwp.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwpft680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/swriter
%{_mandir}/man1/oowriter.1
%{_desktopdir}/oowriter.desktop
%{_iconsdir}/hicolor/*/apps/ooo-writer.png
%{_pixmapsdir}/ooo-writer.png
%if %{with java}
%{_datadir}/%{name}/help/en/swriter.*
%{_libdir}/%{name}/program/classes/writer2latex.jar
%endif
%{_datadir}/%{name}/share/config/soffice.cfg/modules/swriter
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sbibliography
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/WriterCommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/WriterGlobalWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/WriterWebWindowState.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/WriterWindowState.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-writer.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-writer.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_global_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_web_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_writer_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_global_types.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_web_types.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_writer_types.xcu
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WriterCommands.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WriterGlobalWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WriterWebWindowState.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WriterWindowState.xcs

%files impress
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ooimpress
%attr(755,root,root) %{_libdir}/%{name}/program/libanimcore.so
%attr(755,root,root) %{_libdir}/%{name}/program/libplaceware*.so
%attr(755,root,root) %{_libdir}/%{name}/program/simpress
%{_mandir}/man1/ooimpress.1
%{_desktopdir}/ooimpress.desktop
%{_iconsdir}/hicolor/*/apps/ooo-impress.png
%{_pixmapsdir}/ooo-impress.png
%if %{with java}
%{_datadir}/%{name}/help/en/simpress.*
%endif
%{_datadir}/%{name}/share/config/soffice.cfg/modules/simpress
%{_datadir}/%{name}/share/config/soffice.cfg/simpress/
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/Effects.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/ImpressWindowState.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-impress.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-impress.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_impress_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_impress_types.xcu
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/Effects.xcs
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/ImpressWindowState.xcs

%files math
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oomath
%attr(755,root,root) %{_libdir}/%{name}/program/libsm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsmd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/smath
%{_mandir}/man1/oomath.1
%{_desktopdir}/oomath.desktop
%{_iconsdir}/hicolor/*/apps/ooo-math.png
%{_pixmapsdir}/ooo-math.png
%if %{with java}
%{_datadir}/%{name}/help/en/smath.*
%endif
%{_libdir}/%{name}/program/resource/bf_sm680en-US.res
%{_libdir}/%{name}/program/resource/sm680en-US.res
%{_datadir}/%{name}/share/config/soffice.cfg/modules/smath
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/MathCommands.xcu
%{_datadir}/%{name}/share/registry/data/org/openoffice/Office/UI/MathWindowState.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-math.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-math.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_math_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_math_types.xcu
%{_datadir}/%{name}/share/registry/schema/org/openoffice/Office/UI/MathCommands.xcs

%files web
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ooweb
%{_datadir}/%{name}/share/config/soffice.cfg/modules/sweb
%{_mandir}/man1/ooweb.1
%{_desktopdir}/ooweb.desktop
%{_iconsdir}/hicolor/*/apps/ooo-web.png
%{_pixmapsdir}/ooo-web.png

%files graphicfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libflash680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvgfilter680*.so
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_drawgraphics_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_impressgraphics_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_drawgraphics_types.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_impressgraphics_types.xcu

%files xsltfilter
%defattr(644,root,root,755)
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_xslt_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_xslt_types.xcu
%if %{with java}
# not exists when --system-libxslt ?
%{_datadir}/%{name}/share/xslt/docbook
%{_datadir}/%{name}/share/xslt/export/xhtml
%endif

%if %{with java}
%files javafilter
%defattr(644,root,root,755)
%{_libdir}/%{name}/program/classes/aportisdoc.jar
%{_libdir}/%{name}/program/classes/pexcel.jar
%{_libdir}/%{name}/program/classes/pocketword.jar
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_palm_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_pocketexcel_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_pocketword_filters.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_palm_types.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_pocketexcel_types.xcu
%{_datadir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_pocketword_types.xcu
%endif

%files testtools
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libcommuni680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsimplecm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/testtool.bin
%if %{with java}
%{_libdir}/%{name}/program/hid.lst
%endif
%{_libdir}/%{name}/program/resource/stt680en-US.res
%{_libdir}/%{name}/program/testtoolrc

%files pyuno
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libpyuno.so
%attr(755,root,root) %{_libdir}/%{name}/program/pythonloader.uno.so
%attr(755,root,root) %{_libdir}/%{name}/program/pyuno.so
%{_libdir}/%{name}/program/pythonloader.unorc
%{_libdir}/%{name}/program/officehelper.py
%{_libdir}/%{name}/program/pythonloader.py
%{_libdir}/%{name}/program/pythonscript.py
%{_libdir}/%{name}/program/uno.py
%{_libdir}/%{name}/program/unohelper.py
%{_datadir}/%{name}/share/registry/modules/org/openoffice/Office/Scripting/Scripting-python.xcu

# samples there
%{_datadir}/%{name}/share/Scripts/python

%if %{with mozilla}
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libnpsoplugin.so
%attr(755,root,root) %{_libdir}/%{name}/program/nsplugin
%attr(755,root,root) %{_libdir}/%{name}/program/libnpsoplugin.so
%endif

%if %{with i18n}
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

%files i18n-dz -f dz.lang
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

%files i18n-ka -f ka.lang
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
%endif

%files -n bash-completion-openoffice
%defattr(644,root,root,755)
/etc/bash_completion.d/*
