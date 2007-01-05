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
#       - bcond with_mono is broken (cli_types.dll not found, and can't be made)
#	- build on 64-bit architectures
#       - adapt help-support.diff to PLD
#	- make --without xvfb working, required
#	  REMOVE USE of Xvfb from build-galleries script (ooo-build-2.0.1.2/bin/build-galleries line 84)
#	  then remove that bcond
#	- create subpackage with OpenSymbol fonts (or remove it)
# MAYBE TODO:
#	- drop requirement on nas-devel
#	- --with-system-myspell + myspell package as in Debian
#	- in gtk version menu highlight has almost the same colour as menu text
#	- 6 user/config/*.so? files shared between -i18n-en and -i18n-sl
#	- add ooglobal symlink and it's ooo-wrapper entry (among calc|draw|impress|math|web|writer)
#	- add %{_libdir}/%{name}/share/autocorr/acor_(ll)-(LL).dat files to package (marked with %lang)
#	- fix locale names and other locale related things
#       - can't be just i18n-{be,gu,hi,kn,pa,ta} instead of *-{be_BY,*_IN}?
#   - more system libs todo:
#	$ grep SYSTEM ooo-build-ooe680-m6/build/ooe680-m6/config_office/config.log |grep NO
#	SYSTEM_AGG='NO'
#	SYSTEM_HSQLDB='NO'
#	SYSTEM_HUNSPELL='NO'
#	SYSTEM_HYPH='NO'
#	SYSTEM_MYSPELL='NO'
#	SYSTEM_MYTHES='NO'
#	SYSTEM_XALAN='NO'
#	SYSTEM_XERCES='NO'
#	SYSTEM_XML_APIS='NO'
#	SYSTEM_XT='NO'			bcond system_xt (doesn't work - xt in PLD is too old or broken)
#

# Conditional build:
%bcond_without	gnomevfs	# GNOME VFS and Evolution 2 support
%bcond_without	java		# without Java support (disables help support)
%bcond_without	kde		# KDE L&F packages
%bcond_with	mono		# enable compilation of mono bindings
%bcond_without	mozilla		# without mozilla
%bcond_with	seamonkey	# use seamonkey instead of firefox
%bcond_without	i18n		# do not create i18n packages

%bcond_without	system_db		# with internal berkeley db
%bcond_without	system_mdbtools
%bcond_with	system_xt
%bcond_without	system_beanshell
%bcond_without	system_libhnj		# with internal ALTLinuxhyph

%bcond_without	xvfb		# using Xvfb in build-galleries script (without xvfb broken)

%define		ver		2.1.0
%define		_rel		0.15
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
Patch107:	%{name}-stl-amd64.patch
URL:		http://www.openoffice.org/
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
%if %{with xvfb}
#BuildRequires:	xorg-app-mkfontdir	(missing PreReq in fonts?)
BuildRequires:	xorg-font-font-cursor-misc
BuildRequires:	xorg-font-font-misc-misc-base
BuildRequires:	xorg-xserver-Xvfb
%endif
%{?with_system_xt:BuildRequires:	xt}
BuildRequires:	zip
BuildRequires:	zlib-devel
%if %{with java}
BuildRequires:	ant
%{?with_system_db:BuildRequires:	db-java >= 4.3}
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
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-calc = %{epoch}:%{version}-%{release}
Requires:	%{name}-draw = %{epoch}:%{version}-%{release}
Requires:	%{name}-emailmerge = %{epoch}:%{version}-%{release}
Requires:	%{name}-graphicfilter = %{epoch}:%{version}-%{release}
Requires:	%{name}-impress = %{epoch}:%{version}-%{release}
Requires:	%{name}-javafilter = %{epoch}:%{version}-%{release}
Requires:	%{name}-math = %{epoch}:%{version}-%{release}
Requires:	%{name}-pyuno = %{epoch}:%{version}-%{release}
Requires:	%{name}-testtools = %{epoch}:%{version}-%{release}
Requires:	%{name}-writer = %{epoch}:%{version}-%{release}
Requires:	%{name}-xsltfilter = %{epoch}:%{version}-%{release}
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

%package libs-kde
Summary:	OpenOffice.org KDE Interface
Summary(pl):	Interfejs KDE dla OpenOffice.org
Group:		X11/Libraries
Requires:	%{name}-dirs = %{epoch}:%{version}-%{release}
Provides:	%{name}-libs = %{epoch}:%{version}-%{release}
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
Requires:	%{name}-dirs = %{epoch}:%{version}-%{release}
Provides:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-en
Obsoletes:	openoffice-i18n-en-gtk
Obsoletes:	openoffice-libs-gtk

%description libs-gtk
OpenOffice.org productivity suite - GTK+ Interface.

%description libs-gtk -l pl
Pakiet biurowy OpenOffice.org - Interfejs GTK+.

%package dirs
Summary:	Common directories for OpenOffice.org
Group:		X11/Applications

%description dirs
Common directories for OpenOffice.org.

%package core
Summary:	Core modules for OpenOffice.org
Group:		X11/Applications
Requires(post,postun):	fontpostinst
Requires:	%{name}-dirs = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	oooqs
Obsoletes:	openoffice-libs
Obsoletes:	openoffice.org-libs < 1:2.1.0-0.m6.0.11
# libcups.so.2 is dlopened (in cupsmgr.cxx); maybe Suggests instead?
Requires:	cups-lib
Requires:	libstdc++ >= 5:3.2.1
Requires:	mktemp
Requires:	sed
Obsoletes:	openoffice
#Suggests:	chkfontpath

%description core
Core libraries and support files for OpenOffice.org

%package pyuno
Summary:	python bindings for OpenOffice.org
Group:		Libraries
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	python

%description pyuno
Cool python bindings for the OpenOffice.org UNO component model.
Allows scripts both external to OpenOffice.org and within the internal
OpenOffice.org scripting module to be written in python

%package base
Summary:	database frontend for OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description base
GUI database frontend for OpenOffice.org. Allows creation and
management of databases through a GUI.

%package writer
Summary:	writer module for OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	libwpd >= 0.8.0

%description writer
Wordprocessor application of OpenOffice.org

%package emailmerge
Summary:	email mail merge component for OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-pyuno = %{epoch}:%{version}-%{release}
Requires:	%{name}-writer = %{epoch}:%{version}-%{release}

%description emailmerge
Enables OpenOffice.org writer module to enable mail merge to email

%package calc
Summary:	calc module for OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description calc
Spreadsheet application of OpenOffice.org

%package draw
Summary:	draw module for OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description draw
Drawing application of OpenOffice.org

%package impress
Summary:	impress module for OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description impress
Presentation application of OpenOffice.org

%package math
Summary:	math module for OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description math
Math editor of OpenOffice.org

%package graphicfilter
Summary:	extra graphicfilter module for OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description graphicfilter
Graphicfilter module for OpenOffice.org, provides additional svg and
flash export filters.

%package xsltfilter
Summary:	extra xsltfilter module for OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description xsltfilter
xsltfilter module for OpenOffice.org, provides additional docbook and
xhtml export transforms. Install this to enable docbook export.

%package javafilter
Summary:	extra javafilter module for OpenOffice.org
Group:		X11/Applications
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description javafilter
javafilter module for OpenOffice.org, provides additional aportisdoc,
pocket excel and pocket word import filters.

%package testtools
Summary:	testtools for OpenOffice.org
Group:		Development/Libraries
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description testtools
QA tools for OpenOffice.org, enables automated testing.

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

%ifarch %{x8664}
echo "[ PLD64bitfixes ]" >> patches/src680/apply
# patches applied by ooo (extension .diff is required)
for P in %{PATCH107}; do
	PATCHNAME=PLD-${P##*/%{name}-}
	PATCHNAME=${PATCHNAME%.patch}.diff
	install $P patches/src680/$PATCHNAME
	echo $PATCHNAME >> patches/src680/apply
done
%endif

echo "[ PLDOnly ]" >> patches/src680/apply
# patches applied by ooo (extension .diff is required)
for P in %{PATCH102} %{PATCH104} %{PATCH105} %{PATCH106}; do
	PATCHNAME=PLD-${P##*/%{name}-}
	PATCHNAME=${PATCHNAME%.patch}.diff
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
	--with-lang=%{?with_i18n:ALL} \
%if %{with java}
	--with-java \
	--with-jdk-home=$JAVA_HOME \
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
echo "$CONFOPTS" > distro-configs/PLD64.conf.in

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

# is below comment true?
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

chmod +x $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*.so

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

%post core
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:
[ ! -x /usr/bin/update-mime-database ] || /usr/bin/update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:
fontpostinst TTF

%postun core
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
[ ! -x /usr/bin/update-mime-database ] || /usr/bin/update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:
fontpostinst TTF

%files
%defattr(644,root,root,755)

%files dirs
%defattr(644,root,root,755)
%dir %{_sysconfdir}/openoffice.org
%dir %{_libdir}/%{name}
%if %{with java}
%dir %{_libdir}/%{name}/help/en
%dir %{_libdir}/%{name}/program/classes
%endif
%dir %{_libdir}/%{name}/program
%dir %{_libdir}/%{name}/program/resource
%dir %{_libdir}/%{name}/share
%dir %{_libdir}/%{name}/share/Scripts
%dir %{_libdir}/%{name}/share/config
%dir %{_libdir}/%{name}/share/registry
%dir %{_libdir}/%{name}/share/registry/data
%dir %{_libdir}/%{name}/share/registry/data/org
%dir %{_libdir}/%{name}/share/registry/data/org/openoffice
%dir %{_libdir}/%{name}/share/registry/data/org/openoffice/Office
%dir %{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI
%dir %{_libdir}/%{name}/share/registry/modules
%dir %{_libdir}/%{name}/share/registry/modules/org
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/Office
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Scripting
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Writer
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/GraphicFilter
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Misc
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types
%dir %{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort
%dir %{_libdir}/%{name}/share/registry/schema
%dir %{_libdir}/%{name}/share/registry/schema/org
%dir %{_libdir}/%{name}/share/registry/schema/org/openoffice
%dir %{_libdir}/%{name}/share/registry/schema/org/openoffice/Office
%dir %{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI
%dir %{_libdir}/%{name}/share/registry/schema/org/openoffice/TypeDetection
%dir %{_libdir}/%{name}/share/registry/schema/org/openoffice/ucb

%files core
%defattr(644,root,root,755)
%doc %{_libdir}/%{name}/LICENSE*
%doc %{_libdir}/%{name}/*README*
%attr(755,root,root) %{_libdir}/%{name}/install-dict
%{_libdir}/%{name}/program/*.rdb
%{_libdir}/%{name}/program/*.bmp
%{_libdir}/%{name}/program/sofficerc
%{_libdir}/%{name}/program/unorc
%{_libdir}/%{name}/program/bootstraprc
%{_libdir}/%{name}/program/configmgrrc
%dir %{_libdir}/%{name}/licenses
%dir %{_libdir}/%{name}/readmes
%dir %{_libdir}/%{name}/share/autocorr
%dir %{_libdir}/%{name}/share/autotext
%{_libdir}/%{name}/share/basic
%{_libdir}/%{name}/share/config/symbol
%{_libdir}/%{name}/share/config/webcast
%{_libdir}/%{name}/share/config/*.xpm
%{_libdir}/%{name}/share/config/images.zip
%{_libdir}/%{name}/share/config/images_crystal.zip
%{_libdir}/%{name}/share/config/images_industrial.zip
%{_libdir}/%{name}/share/config/images_hicontrast.zip
%{_libdir}/%{name}/share/config/wizard
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
%{_libdir}/%{name}/share/readme
%dir %{_libdir}/%{name}/share/registry/res

%dir %{_libdir}/%{name}/share/registry/data/org/openoffice/TypeDetection
%dir %{_libdir}/%{name}/share/registry/data/org/openoffice/ucb
%{_libdir}/%{name}/share/registry/data/org/openoffice/FirstStartWizard.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Inet.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/LDAP.xcu.sample
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Calc.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Common.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Compatibility.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/DataAccess.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Embedding.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/FormWizard.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Jobs.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Labels.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Math.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Paths.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/ProtocolHandler.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/SFX.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Scripting.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Security.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/TableWizard.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/BaseWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/BasicIDECommands.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/BasicIDEWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/BibliographyCommands.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/ChartCommands.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/ChartWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/Controller.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbBrowserWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbQueryWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbRelationWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbTableWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/DbuCommands.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/DrawImpressCommands.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/Factories.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/GenericCategories.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/GenericCommands.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/MathWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/StartModuleCommands.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/StartModuleWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Views.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/WebWizard.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/Writer.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Setup.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/TypeDetection/UISort.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/VCL.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/ucb/Configuration.xcu

%{_libdir}/%{name}/share/registry/schema/org/openoffice/FirstStartWizard.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Inet.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/LDAP.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Addons.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Calc.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/CalcAddIns.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Chart.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Commands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Common.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Compatibility.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/DataAccess.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Draw.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Embedding.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Events.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/FormWizard.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Impress.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Java.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Jobs.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Labels.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Linguistic.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Math.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/OptionsDialog.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Paths.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/ProtocolHandler.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Recovery.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/SFX.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Scripting.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Security.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Substitution.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/TabBrowse.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/TableWizard.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/TypeDetection.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/BaseWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/BasicIDECommands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/BasicIDEWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/BibliographyCommands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/BibliographyWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/Category.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/ChartCommands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/ChartWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/Commands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/Controller.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbBrowserWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbQueryWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbRelationWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbTableWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DbuCommands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DrawImpressCommands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/Factories.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/GenericCategories.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/GenericCommands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/GlobalSettings.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/MathWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/StartModuleCommands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/StartModuleWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Views.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/WebWizard.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/Writer.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/WriterWeb.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Setup.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/System.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/TypeDetection/Filter.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/TypeDetection/GraphicFilter.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/TypeDetection/Misc.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/TypeDetection/Types.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/TypeDetection/UISort.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/UserProfile.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/VCL.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/ucb/Configuration.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/ucb/Hierarchy.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/ucb/Store.xcs

%{_libdir}/%{name}/share/registry/ldap

%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-UseOOoFileDialogs.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-dicooo.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-unx.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-calc.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-chart.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-draw.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-impress.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-math.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Embedding/Embedding-writer.xcu
%if %{with java}
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-cjk_ja.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-cjk_ko.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-cjk_zh-CN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-cjk_zh-TW.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_ar.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_fa.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_gu-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_he.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_hi-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_km.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_lo.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_ne.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_pa-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_ta-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_th.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-ctl_vi.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-korea.xcu
# move it to -writer ?
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Writer/Writer-cjk_ja.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Writer/Writer-cjk_ko.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Writer/Writer-cjk_zh-CN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Writer/Writer-cjk_zh-TW.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-af.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ar.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-as-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-be-BY.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-bg.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-bn-BD.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-bn-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-bn.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-br.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-bs.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ca.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-cs.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-cy.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-da.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-de.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-el.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-en-GB.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-en-US.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-en-ZA.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-eo.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-es.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-et.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-eu.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-fa.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-fi.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-fr.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ga.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-gl.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-gu-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-he.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-hi-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-hr.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-hu.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-it.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ja.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-km.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-kn-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ko.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ku.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-lo.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-lt.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-lv.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-mk.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ml-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-mr-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ms.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-nb.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ne.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-nl.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-nn.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-nr.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ns.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-or-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-pa-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-pl.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-pt-BR.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-pt.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ru.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-rw.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sh-YU.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sk.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sl.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sr-CS.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ss.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-st.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sv.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sw-TZ.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sw.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-sx.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ta-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-te-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-tg.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-th.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ti-ER.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-tn.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-tr.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ts.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-uk.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ur-IN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-ve.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-vi.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-xh.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-zh-CN.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-zh-TW.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Langpack-zu.xcu
%endif
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_global_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_base_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_chart_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/GraphicFilter/fcfg_internalgraphics_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_base_others.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_chart_others.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_base_types.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_chart_types.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_internalgraphics_types.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-calc.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-draw.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-impress.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-math.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/UISort/UISort-writer.xcu

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

# Programs
%attr(755,root,root) %{_bindir}/ooconfig
%attr(755,root,root) %{_bindir}/ooffice
%attr(755,root,root) %{_bindir}/oofromtemplate
%attr(755,root,root) %{_bindir}/ootool
%attr(755,root,root) %{_bindir}/ooweb

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
%{_libdir}/%{name}/program/setuprc
%attr(755,root,root) %{_libdir}/%{name}/program/smath
%attr(755,root,root) %{_libdir}/%{name}/program/soffice
%attr(755,root,root) %{_libdir}/%{name}/program/spadmin
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
%{_libdir}/%{name}/program/versionrc

%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/program/javaldx
%attr(755,root,root) %{_libdir}/%{name}/program/java-set-classpath
%{_libdir}/%{name}/program/jvmfwk3rc
%{_libdir}/%{name}/program/JREProperties.class

%dir %{_libdir}/%{name}/help
%{_libdir}/%{name}/help/en/*.html
%{_libdir}/%{name}/help/en/*.css
%{_libdir}/%{name}/help/en/sbasic.*
%{_libdir}/%{name}/help/en/schart.*
%{_libdir}/%{name}/help/en/shared.*
%{_libdir}/%{name}/help/*.xsl

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
%{_libdir}/%{name}/program/classes/hsqldb.jar
%{_libdir}/%{name}/program/classes/java_uno.jar
%{_libdir}/%{name}/program/classes/java_uno_accessbridge.jar
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
%{_libdir}/%{name}/program/classes/serializer.jar
%{_libdir}/%{name}/program/classes/table.jar
%{_libdir}/%{name}/program/classes/unoil.jar
%{_libdir}/%{name}/program/classes/unoloader.jar
%{_libdir}/%{name}/program/classes/web.jar
%{_libdir}/%{name}/program/classes/xalan.jar
%{_libdir}/%{name}/program/classes/xercesImpl.jar
%{_libdir}/%{name}/program/classes/xmerge.jar
%{_libdir}/%{name}/program/classes/xml-apis.jar

%{_libdir}/%{name}/share/Scripts/beanshell
%{_libdir}/%{name}/share/Scripts/javascript
%{_libdir}/%{name}/share/Scripts/java
%{_libdir}/%{name}/share/config/javavendors.xml

%dir %{_libdir}/%{name}/share/xslt
%{_libdir}/%{name}/share/xslt/common
%dir %{_libdir}/%{name}/share/xslt/export
%{_libdir}/%{name}/share/xslt/export/common
%{_libdir}/%{name}/share/xslt/export/spreadsheetml
%{_libdir}/%{name}/share/xslt/export/wordml
%{_libdir}/%{name}/share/xslt/import

%endif

%{_datadir}/mime/packages/openoffice.xml

%{_desktopdir}/template.desktop
%{_desktopdir}/web.desktop

%{_pixmapsdir}/ooo-gulls.png
%{_pixmapsdir}/ooo-template.png
%{_pixmapsdir}/ooo-web.png

%{_mandir}/man1/ooffice.1
%{_mandir}/man1/oofromtemplate.1
%{_mandir}/man1/ooweb.1
%{_mandir}/man1/openoffice.1*

# en-US
%{_libdir}/%{name}/presets/config/*_en-US.so*
%{_libdir}/%{name}/share/autocorr/acor_*.dat
%{_libdir}/%{name}/share/autotext/en-US
%{_libdir}/%{name}/share/registry/res/en-US
%{_libdir}/%{name}/share/template/en-US
%dir %{_libdir}/%{name}/share/template/wizard/letter/en-US
%{_libdir}/%{name}/share/template/wizard/letter/en-US/*.ott
%{_libdir}/%{name}/share/wordbook/en-US

%{_libdir}/%{name}/program/resource/abp680en-US.res
%{_libdir}/%{name}/program/resource/analysis680en-US.res
%{_libdir}/%{name}/program/resource/avmedia680en-US.res
%{_libdir}/%{name}/program/resource/basctl680en-US.res
%{_libdir}/%{name}/program/resource/bf_frm680en-US.res
%{_libdir}/%{name}/program/resource/bf_ofa680en-US.res
%{_libdir}/%{name}/program/resource/bf_sc680en-US.res
%{_libdir}/%{name}/program/resource/bf_sch680en-US.res
%{_libdir}/%{name}/program/resource/bf_sd680en-US.res
%{_libdir}/%{name}/program/resource/bf_sfx680en-US.res
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
%{_libdir}/%{name}/program/resource/sch680en-US.res
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

%{_libdir}/%{name}/licenses/LICENSE_en-US
%{_libdir}/%{name}/licenses/LICENSE_en-US.html
%{_libdir}/%{name}/readmes/README_en-US
%{_libdir}/%{name}/readmes/README_en-US.html

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
%attr(755,root,root) %{_libdir}/%{name}/program/libanimcore.so
%attr(755,root,root) %{_libdir}/%{name}/program/libavmedia680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libavmediagst.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasctl680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbasegfx680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_frm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_lng680*.so
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
%attr(755,root,root) %{_libdir}/%{name}/program/libevoab2.so
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
%attr(755,root,root) %{_libdir}/%{name}/program/libhunspell.so
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
%attr(755,root,root) %{_libdir}/%{name}/program/libqstart_gtk680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/librecentfile.so
%attr(755,root,root) %{_libdir}/%{name}/program/libres680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsb680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsch680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libschd680*.so
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

%files base
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oobase
%attr(755,root,root) %{_libdir}/%{name}/program/sbase
%{_mandir}/man1/oobase.1
%{_desktopdir}/base.desktop
%{_pixmapsdir}/ooo-base.png
%{_libdir}/%{name}/program/resource/cnr680en-US.res
%if %{with java}
%{_libdir}/%{name}/help/en/sdatabase.*
%endif
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-base.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-base.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_database_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Misc/fcfg_database_others.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_database_types.xcu

%files calc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oocalc
%attr(755,root,root) %{_libdir}/%{name}/program/libanalysis680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libbf_sc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libcalc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libdate680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsc680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libscui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/scalc
%{_mandir}/man1/oocalc.1
%{_desktopdir}/calc.desktop
%{_pixmapsdir}/ooo-calc.png
%if %{with java}
%{_libdir}/%{name}/help/en/scalc.*
%endif
%{_libdir}/%{name}/program/resource/analysis680en-US.res
%{_libdir}/%{name}/program/resource/bf_sc680en-US.res
%{_libdir}/%{name}/program/resource/date680en-US.res
%{_libdir}/%{name}/program/resource/sc680en-US.res
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/CalcCommands.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/CalcWindowState.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-calc.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-calc.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_calc_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_calc_types.xcu
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/CalcCommands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/CalcWindowState.xcs

%files draw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oodraw
%attr(755,root,root) %{_libdir}/%{name}/program/sdraw
%{_mandir}/man1/oodraw.1
%{_desktopdir}/draw.desktop
%{_pixmapsdir}/ooo-draw.png
%if %{with java}
%{_libdir}/%{name}/help/en/sdraw.*
%endif
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/DrawWindowState.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-draw.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-draw.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_draw_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_draw_types.xcu
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/DrawWindowState.xcs

%files emailmerge
%defattr(644,root,root,755)
%{_libdir}/%{name}/program/mailmerge.py*
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Writer/Writer-javamail.xcu

%files writer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oowriter
%attr(755,root,root) %{_libdir}/%{name}/program/libhwp.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libswui680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libwpft680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/swriter
%{_mandir}/man1/oowriter.1
%{_desktopdir}/writer.desktop
%{_pixmapsdir}/ooo-writer.png
%if %{with java}
%{_libdir}/%{name}/help/en/swriter.*
%{_libdir}/%{name}/program/classes/writer2latex.jar
%endif
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/WriterCommands.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/WriterGlobalWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/WriterWebWindowState.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/WriterWindowState.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-writer.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-writer.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_global_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_web_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_writer_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_global_types.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_web_types.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_writer_types.xcu
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WriterCommands.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WriterGlobalWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WriterWebWindowState.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/WriterWindowState.xcs

%files impress
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ooimpress
%attr(755,root,root) %{_libdir}/%{name}/program/libanimcore.so
%attr(755,root,root) %{_libdir}/%{name}/program/libplaceware*.so
%attr(755,root,root) %{_libdir}/%{name}/program/simpress
%{_mandir}/man1/ooimpress.1
%{_desktopdir}/impress.desktop
%{_pixmapsdir}/ooo-impress.png
%if %{with java}
%{_libdir}/%{name}/help/en/simpress.*
%endif
%{_libdir}/%{name}/share/config/soffice.cfg
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/Effects.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/ImpressWindowState.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-impress.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-impress.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_impress_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_impress_types.xcu
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/Effects.xcs
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/ImpressWindowState.xcs

%files math
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oomath
%attr(755,root,root) %{_libdir}/%{name}/program/libsm680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsmd680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/smath
%{_mandir}/man1/oomath.1
%{_desktopdir}/math.desktop
%{_pixmapsdir}/ooo-math.png
%if %{with java}
%{_libdir}/%{name}/help/en/smath.*
%endif
%{_libdir}/%{name}/program/resource/bf_sm680en-US.res
%{_libdir}/%{name}/program/resource/sm680en-US.res
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/MathCommands.xcu
%{_libdir}/%{name}/share/registry/data/org/openoffice/Office/UI/MathWindowState.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Common/Common-math.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Setup/Setup-math.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_math_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_math_types.xcu
%{_libdir}/%{name}/share/registry/schema/org/openoffice/Office/UI/MathCommands.xcs

%files graphicfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libflash680*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libsvgfilter680*.so
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_drawgraphics_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_impressgraphics_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_drawgraphics_types.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_impressgraphics_types.xcu

%files xsltfilter
%defattr(644,root,root,755)
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_xslt_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_xslt_types.xcu
%if %{with java}
# not exists when --system-libxslt ?
%{_libdir}/%{name}/share/xslt/docbook
%{_libdir}/%{name}/share/xslt/export/xhtml
%endif

%if %{with java}
%files javafilter
%defattr(644,root,root,755)
%{_libdir}/%{name}/program/classes/aportisdoc.jar
%{_libdir}/%{name}/program/classes/pexcel.jar
%{_libdir}/%{name}/program/classes/pocketword.jar
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_palm_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_pocketexcel_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Filter/fcfg_pocketword_filters.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_palm_types.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_pocketexcel_types.xcu
%{_libdir}/%{name}/share/registry/modules/org/openoffice/TypeDetection/Types/fcfg_pocketword_types.xcu
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
%{_libdir}/%{name}/share/registry/modules/org/openoffice/Office/Scripting/Scripting-python.xcu

# samples there
%{_libdir}/%{name}/share/Scripts/python

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
%endif

%files -n bash-completion-openoffice
%defattr(644,root,root,755)
/etc/bash_completion.d/*
