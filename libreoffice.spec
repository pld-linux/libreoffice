# NOTE:
#	- normal build (i686) requires about 27 GB of disk space:
#		$BUILD_ROOT	7.0 GB
#		BUILD		18  GB
#		RPMS		1.8 GB
#		SRPMS		0.4 GB
#
# Conditional build:
%bcond_with	gnomevfs	# GNOME VFS and Evolution 2 support
%bcond_without	java		# without Java support (disables help support)
%bcond_with	kde		# KDE L&F packages
%bcond_without	kde4		# KDE4 L&F packages
%bcond_with	mono		# enable compilation of mono bindings
%bcond_without	mozilla		# without mozilla components
%bcond_without	i18n		# do not create i18n packages
%bcond_with	ccache		# use ccache to speed up builds
%bcond_with	icecream	# use icecream to speed up builds
%bcond_with	msaccess	# with ms access import pieces
%bcond_with	parallelbuild	# use greater number of jobs to speed up build (default: 1)

%bcond_without	system_beanshell
%bcond_without	system_db		# without system (i.e. with internal) Berkeley DB
%bcond_with	system_libhnj		# with system ALTLinuxhyph (NFY)
%bcond_without	system_mdbtools		# with system mdbtools
%bcond_without	system_xalan
%bcond_without	system_xerces
%bcond_without	system_xml_apis
%bcond_with	system_hsqldb
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

%define		upd			320
%define		mws			OOO%{upd}
%define		tag			%(echo %{mws} | tr A-Z a-z)-%{milestone}
%define		milestone	m12
%define		_tag		%(echo %{tag} | tr - _)
%define		_rel		0.1

Summary:	LibreOffice - powerful office suite
Summary(pl.UTF-8):	LibreOffice - potężny pakiet biurowy
Name:		libreoffice
Version:	3.3.0.1
Release:	0.1
License:	GPL/LGPL
Group:		X11/Applications
# we use git because released tarballs are buggy too often
# git clone git://anongit.freedesktop.org/git/libreoffice/build
# cd build
# git checkout -b ooo-build-3-2 origin/ooo-build-3-2
Source0:	libreoffice-build-%{version}.tar.gz
# Source0-md5:	65990cb6b5a7f7ee4db882812e93e0d0
Source1:	http://download.go-oo.org/DEV300/ooo-cli-prebuilt-3.3.tar.bz2
# Source1-md5:	b4e4ad9da4cf1033096609c95ad50bdb
Source2:	http://download.documentfoundation.org/libreoffice/src/libreoffice-artwork-%{version}.tar.bz2
# Source2-md5:	18d08617d191cdb81227be47a1cff3f9
Source3:	http://download.documentfoundation.org/libreoffice/src/libreoffice-base-%{version}.tar.bz2
# Source3-md5:	18d08617d191cdb81227be47a1cff3f9
Source4:	http://download.documentfoundation.org/libreoffice/src/libreoffice-bootstrap-%{version}.tar.bz2
# Source4-md5:	18d08617d191cdb81227be47a1cff3f9
Source5:	http://download.documentfoundation.org/libreoffice/src/libreoffice-calc-%{version}.tar.bz2
# Source5-md5:	18d08617d191cdb81227be47a1cff3f9
Source6:	http://download.documentfoundation.org/libreoffice/src/libreoffice-components-%{version}.tar.bz2
# Source6-md5:	18d08617d191cdb81227be47a1cff3f9
Source7:	http://download.documentfoundation.org/libreoffice/src/libreoffice-extensions-%{version}.tar.bz2
# Source7-md5:	18d08617d191cdb81227be47a1cff3f9
Source8:	http://download.documentfoundation.org/libreoffice/src/libreoffice-extras-%{version}.tar.bz2
# Source8-md5:	18d08617d191cdb81227be47a1cff3f9
Source9:	http://download.documentfoundation.org/libreoffice/src/libreoffice-filters-%{version}.tar.bz2
# Source9-md5:	18d08617d191cdb81227be47a1cff3f9
Source10:	http://download.documentfoundation.org/libreoffice/src/libreoffice-help-%{version}.tar.bz2
# Source10-md5:	18d08617d191cdb81227be47a1cff3f9
Source11:	http://download.documentfoundation.org/libreoffice/src/libreoffice-impress-%{version}.tar.bz2
# Source11-md5:	18d08617d191cdb81227be47a1cff3f9
Source12:	http://download.documentfoundation.org/libreoffice/src/libreoffice-l10n-%{version}.tar.bz2
# Source12-md5:	18d08617d191cdb81227be47a1cff3f9
Source13:	http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-core-%{version}.tar.bz2
# Source13-md5:	18d08617d191cdb81227be47a1cff3f9
Source14:	http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-extern-%{version}.tar.bz2
# Source14-md5:	18d08617d191cdb81227be47a1cff3f9
Source15:	http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-extern-sys-%{version}.tar.bz2
# Source15-md5:	18d08617d191cdb81227be47a1cff3f9
Source16:	http://download.documentfoundation.org/libreoffice/src/libreoffice-libs-gui-%{version}.tar.bz2
# Source16-md5:	18d08617d191cdb81227be47a1cff3f9
Source17:	http://download.documentfoundation.org/libreoffice/src/libreoffice-postprocess-%{version}.tar.bz2
# Source17-md5:	18d08617d191cdb81227be47a1cff3f9
Source18:	http://download.documentfoundation.org/libreoffice/src/libreoffice-sdk-%{version}.tar.bz2
# Source18-md5:	18d08617d191cdb81227be47a1cff3f9
Source19:	http://download.documentfoundation.org/libreoffice/src/libreoffice-testing-%{version}.tar.bz2
# Source19-md5:	18d08617d191cdb81227be47a1cff3f9
Source20:	http://download.documentfoundation.org/libreoffice/src/libreoffice-ure-%{version}.tar.bz2
# Source20-md5:	18d08617d191cdb81227be47a1cff3f9
Source21:	http://download.documentfoundation.org/libreoffice/src/libreoffice-writer-%{version}.tar.bz2
# Source21-md5:	18d08617d191cdb81227be47a1cff3f9
Source22:	http://download.go-oo.org/SRC680/biblio.tar.bz2
# Source22-md5:	18d08617d191cdb81227be47a1cff3f9
Source23:	http://download.go-oo.org/SRC680/extras-3.1.tar.bz2
# Source23-md5:	18d08617d191cdb81227be47a1cff3f9
Source100:	http://hg.services.openoffice.org/binaries/fdb27bfe2dbe2e7b57ae194d9bf36bab-SampleICC-1.3.2.tar.gz
# Source100-md5:
Source101:	http://hg.services.openoffice.org/binaries/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip
# Source101-md5:
Source102:	http://hg.services.openoffice.org/binaries/26b3e95ddf3d9c077c480ea45874b3b8-lp_solve_5.5.tar.gz
# Source102-md5:
Source103:	http://hg.services.openoffice.org/binaries/cf8a6967f7de535ae257fa411c98eb88-mdds_0.3.0.tar.bz2
# Source103-md5:
Source104:	http://hg.services.openoffice.org/binaries/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
# Source104-md5:
Source105:	http://hg.services.openoffice.org/binaries/128cfc86ed5953e57fe0f5ae98b62c2e-libtextcat-2.2.tar.gz
# Source105-md5:
Source106:	http://hg.services.openoffice.org/binaries/d0b5af6e408b8d2958f3d83b5244f5e8-hyphen-2.4.tar.gz
# Source106-md5:
Source107:	http://hg.services.openoffice.org/binaries/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz
# Source107-md5:
Source108:	http://hg.services.openoffice.org/binaries/1756c4fa6c616ae15973c104cd8cb256-Adobe-Core35_AFMs-314.tar.gz
# Source108-md5:
Source109:	http://hg.services.openoffice.org/binaries/ada24d37d8d638b3d8a9985e80bc2978-source-9.0.0.7-bj.zip
# Source109-md5:
Source110:	http://hg.services.openoffice.org/binaries/067201ea8b126597670b5eff72e1f66c-mythes-1.2.0.tar.gz
# Source110-md5:
Source111:	http://hg.services.openoffice.org/binaries/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
# Source111-md5:
Source112:	http://download.go-oo.org/src/0f63ee487fda8f21fafa767b3c447ac9-ixion-0.2.0.tar.gz
# Source112-md5:
Source113:	http://hg.services.openoffice.org/binaries/8ea307d71d11140574bfb9fcc2487e33-libbase.zip
# Source113-md5:
Source114:	http://hg.services.openoffice.org/binaries/a06a496d7a43cbdc35e69dbe678efadb-libloader.zip
# Source114-md5:
Source115:	http://hg.services.openoffice.org/binaries/39bb3fcea1514f1369fcfc87542390fd-sacjava-1.3.zip
# Source115-md5:
Source116:	http://hg.services.openoffice.org/binaries/f3e2febd267c8e4b13df00dac211dd6d-flute.zip
# Source116-md5:
Source117:	http://hg.services.openoffice.org/binaries/5aba06ede2daa9f2c11892fbd7bc3057-libserializer.zip
# Source117-md5:
Source118:	http://hg.services.openoffice.org/binaries/f7925ba8491fe570e5164d2c72791358-libfonts.zip
# Source118-md5:
Source119:	http://hg.services.openoffice.org/binaries/d1a3205871c3c52e8a50c9f18510ae12-libformula.zip
# Source119-md5:
Source120:	http://hg.services.openoffice.org/binaries/67b42915c8432abf0a922438f00860a2-libxml.zip
# Source120-md5:
Source121:	http://hg.services.openoffice.org/binaries/dbb3757275dc5cc80820c0b4dd24ed95-librepository.zip
# Source121-md5:
Source122:	http://hg.services.openoffice.org/binaries/79600e696a98ff95c2eba976f7a8dfbb-liblayout.zip
# Source122-md5:
Source123:	http://hg.services.openoffice.org/binaries/d4c4d91ab3a8e52a2e69d48d34ef4df4-core.zip
# Source123-md5:
Source124:	http://hg.services.openoffice.org/binaries/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip
# Source124-md5:
#Source53:	%{name}-splash.bmp
#Source54:	%{name}-about.bmp
# patches applied in prep section
Patch0:		%{name}-build-apply.patch
# https://bugs.freedesktop.org/show_bug.cgi?id=31871
Patch100:	%{name}-hotfix-with-lang-all.patch
URL:		http://www.documentfoundation.org/
BuildRequires:	libwpd-devel >= 0.9.0
BuildRequires:	libwps-devel >= 0.2.0
BuildRequires:	libwpg-devel >= 0.2.0
BuildRequires:	java-lucene
BuildRequires:	java-lucene-contrib
BuildRequires:	silgraphite-devel
BuildRequires:	java-commons-codec
BuildRequires:	java-commons-lang
BuildRequires:	java-commons-httpclient
BuildRequires:	java-commons-logging
BuildRequires:	java-servletapi

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
%{?with_system_hsqldb:BuildRequires:	java-hsqldb}
%{?with_system_hunspell:BuildRequires:	hunspell-devel >=1.2.2}
%{?with_icecream:BuildRequires:	icecream}
BuildRequires:	icu
%{?with_system_beanshell:BuildRequires:	java-beanshell}
%if %{with kde}
BuildRequires:	kde4-kde3support-devel
%endif
%if %{with kde4}
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	qt4-build
%endif
BuildRequires:	libart_lgpl-devel
BuildRequires:	libbonobo-devel >= 2.0
%{?with_system_libhnj:BuildRequires:	libhnj-devel}
BuildRequires:	libicu-devel >= 4.0
BuildRequires:	libjpeg-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel >= 5:3.2.1
BuildRequires:	libsvg-devel >= 0.1.4
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
BuildRequires:	perl-devel
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
BuildRequires:	ant >= 1.7.0
BuildRequires:	ant-apache-regexp
%{?with_system_db:BuildRequires:	db-java >= 4.3}
BuildRequires:	jdk >= 1.4.0_00
BuildRequires:	jre-X11
%endif
BuildRequires:	xulrunner-devel
BuildConflicts:	xmlsec1-devel
# contains (dlopened) *.so libs
BuildConflicts:	xmlsec1-nss
BuildConflicts:	java-gcj-compat
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-calc = %{version}-%{release}
Requires:	%{name}-draw = %{version}-%{release}
Requires:	%{name}-emailmerge = %{version}-%{release}
Requires:	%{name}-graphicfilter = %{version}-%{release}
Requires:	%{name}-impress = %{version}-%{release}
%{?with_java:Requires:	%{name}-javafilter = %{version}-%{release}}
Requires:	%{name}-math = %{version}-%{release}
Requires:	%{name}-pyuno = %{version}-%{release}
Requires:	%{name}-testtools = %{version}-%{release}
Requires:	%{name}-web = %{version}-%{release}
Requires:	%{name}-writer = %{version}-%{release}
Requires:	%{name}-xsltfilter = %{version}-%{release}
Obsoletes:	openoffice.org
ExclusiveArch:	%{ix86} %{x8664} ppc sparc sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing -O2

# No ELF objects there to strip/chrpath, skips processing:
# - share/ - 17000 files of 415M
# - help/ - 6500 files of 1.4G
# - program/resource/ - 5610 files of 216M
%define		_noautostrip	.*\\(%{_datadir}\\|%{_libdir}/%{name}/basis*/program/resource\\)/.*
%define		_noautochrpath	.*\\(%{_datadir}\\|%{_libdir}/%{name}/basis*/program/resource\\)/.*

%define		ooobasisdir	%{_libdir}/%{name}/basis3.3

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
Requires(post,postun):	shared-mime-info
Requires:	%{name}-ure = %{version}-%{release}
# libcups.so.2 is dlopened (in cupsmgr.cxx); maybe Suggests instead?
Requires:	cups-lib
Requires:	fonts-TTF-OpenSymbol
%{?with_system_hsqldb:Requires:	java-hsqldb}
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
Obsoletes:	openoffice.org-core
Obsoletes:	openoffice.org-dirs
Obsoletes:	openoffice.org-i18n-bn_BD
Obsoletes:	openoffice.org-i18n-bn_IN
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
Obsoletes:	openoffice.org-i18n-sw
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
Obsoletes:	openoffice.org-pyuno

%description pyuno
Cool Python bindings for the LibreOffice UNO component model.
Allows scripts both external to LibreOffice and within the internal
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
The Presentation Minimizer is used to reduce the file size of the current 
presentation. Images will be compressed, and data that is no longer needed will 
be removed.

%package presenter-screen
Summary:	Presenter Screen for LibreOffice presentations
Group:		X11/Applications
Requires:	%{name}-impress = %{version}-%{release}

%description presenter-screen
The Presenter Screen is used to provides information on a second screen, that 
typically is not visible to the audience when delivering a presentation. e.g. 
slide notes.

%package report-builder
Summary:	Create database reports from LibreOffice
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Requires:	java-commons-logging

%description report-builder
Creates database reports from LibreOffice databases. The report builder can
define group and page headers as well as group, page footers and calculation
fields to accomplish complex database reports.

%package wiki-publisher
Summary:	Create Wiki articles on MediaWiki servers with LibreOffice
Group:		X11/Applications
Requires:	%{name}-writer = %{version}-%{release}
Requires:	java-commons-codec
Requires:	java-commons-httpclient
Requires:	java-commons-lang
Requires:	java-commons-logging

%description wiki-publisher
The Wiki Publisher enables you to create Wiki articles on MediaWiki servers 
without having to know the syntax of the MediaWiki markup language. Publish 
your new and existing documents transparently with writer to a wiki page.

%package base
Summary:	Database frontend for LibreOffice
Summary(pl.UTF-8):	Frontend do baz danych dla LibreOffice
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-base

%description base
GUI database frontend for LibreOffice. Allows creation and
management of databases through a GUI.

%description base -l pl.UTF-8
Graficzny frontend do baz danych dla LibreOffice. Pozwala na
tworzenie i zarządzanie bazami poprzez graficzny interfejs
użytkownika.

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
Requires:	%{name}-core = %{version}-%{release}
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
Requires:	%{name}-core = %{version}-%{release}
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
Requires:	%{name}-core = %{version}-%{release}
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
Requires:	%{name}-core = %{version}-%{release}
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
Requires:	%{name}-core = %{version}-%{release}
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
Moduł xsltfilter dla LibreOffice, udostępnia dodatkowe
przekształcenia wyjściowe dla formatów docbook i xhtml. Jest potrzebny
do eksportu do docbooka.

%package javafilter
Summary:	Extra javafilter module for LibreOffice
Summary(pl.UTF-8):	Dodatkowy moduł javafilter dla LibreOffice
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-javafilter

%description javafilter
javafilter module for LibreOffice, provides additional aportisdoc,
Pocket Excel and Pocket Word import filters.

%description javafilter -l pl.UTF-8
Moduł javafilter dla LibreOffice, udostępnia dodatkowe filtry
importu aportisdoc, Pocket Excel i Pocket Word.

%package testtools
Summary:	testtools for LibreOffice
Summary(pl.UTF-8):	Narzędzia testowe dla LibreOffice
Group:		Development/Libraries
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-testtools

%description testtools
QA tools for LibreOffice, enables automated testing.

%description testtools -l pl.UTF-8
Narzędzia QA dla LibreOffice, pozwalają na automatyczne testowanie.

# FIXME
%package ure
Summary:	UNO Runtime Environment
Group:		Libraries
Obsoletes:	openoffice.org-ure

%description ure
UNO is the component model of LibreOffice. UNO offers
interoperability between programming languages, other components
models and hardware architectures, either in process or over process
boundaries, in the Intranet as well as in the Internet. UNO components
may be implemented in and accessed from any programming language for
which a UNO implementation (AKA language binding) and an appropriate
bridge or adapter exists.

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

%package i18n-af
Summary:	LibreOffice - interface in Afrikaans language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku afrykanerskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-af
Obsoletes:	openoffice-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af-gtk
Obsoletes:	openoffice.org-i18n-af-kde
Obsoletes:	openoffice.org-i18n-af

%description i18n-af
This package provides resources containing menus and dialogs in
Afrikaans language.

%description i18n-af -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
afrykanerskim.

%package i18n-ar
Summary:	LibreOffice - interface in Arabic language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku arabskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ar
Obsoletes:	openoffice-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar-gtk
Obsoletes:	openoffice.org-i18n-ar-kde
Obsoletes:	openoffice.org-i18n-ar

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
Obsoletes:	openoffice.org-i18n-bg-gtk
Obsoletes:	openoffice.org-i18n-bg-kde
Obsoletes:	openoffice.org-i18n-bg

%description i18n-bg
This package provides resources containing menus and dialogs in
Bulgarian language.

%description i18n-bg -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
bułgarskim.

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
This package provides resources containing menus and dialogs in Tibetan
language.

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
Obsoletes:	openoffice.org-i18n-ca-gtk
Obsoletes:	openoffice.org-i18n-ca-kde
Obsoletes:	openoffice.org-i18n-ca

%description i18n-ca
This package provides resources containing menus and dialogs in
Catalan language.

%description i18n-ca -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
katalońskim.

%package i18n-cs
Summary:	LibreOffice - interface in Czech language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku czeskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-cs
Obsoletes:	openoffice-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs-gtk
Obsoletes:	openoffice.org-i18n-cs-kde
Obsoletes:	openoffice.org-i18n-cs

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
Obsoletes:	openoffice.org-i18n-cy-gtk
Obsoletes:	openoffice.org-i18n-cy-kde
Obsoletes:	openoffice.org-i18n-cy

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
Obsoletes:	openoffice.org-i18n-da-gtk
Obsoletes:	openoffice.org-i18n-da-kde
Obsoletes:	openoffice.org-i18n-da

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
Obsoletes:	openoffice.org-i18n-de-gtk
Obsoletes:	openoffice.org-i18n-de-kde
Obsoletes:	openoffice.org-i18n-de

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
Obsoletes:	openoffice.org-i18n-el-gtk
Obsoletes:	openoffice.org-i18n-el-kde
Obsoletes:	openoffice.org-i18n-el

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
Obsoletes:	openoffice.org-i18n-es-gtk
Obsoletes:	openoffice.org-i18n-es-kde
Obsoletes:	openoffice.org-i18n-es

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
Obsoletes:	openoffice.org-i18n-et-gtk
Obsoletes:	openoffice.org-i18n-et-kde
Obsoletes:	openoffice.org-i18n-et

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

%description i18n-eu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
perskim.

%package i18n-fi
Summary:	LibreOffice - interface in Finnish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku fińskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-fi
Obsoletes:	openoffice-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi-gtk
Obsoletes:	openoffice.org-i18n-fi-kde
Obsoletes:	openoffice.org-i18n-fi

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
Obsoletes:	openoffice.org-i18n-fr-gtk
Obsoletes:	openoffice.org-i18n-fr-kde
Obsoletes:	openoffice.org-i18n-fr

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
Obsoletes:	openoffice.org-i18n-ga-gtk
Obsoletes:	openoffice.org-i18n-ga-kde
Obsoletes:	openoffice.org-i18n-ga

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
Obsoletes:	openoffice.org-i18n-gd

%description i18n-gd
This package provides resources containing menus and dialogs in
Scottish Gaelic language.

%description i18n-gd -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
gaelickim szkockim.

%package i18n-gl
Summary:	LibreOffice - interface in Galician language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku galicyjskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-gl
Obsoletes:	openoffice-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl-gtk
Obsoletes:	openoffice.org-i18n-gl-kde
Obsoletes:	openoffice.org-i18n-gl

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
Obsoletes:	openoffice.org-i18n-he-gtk
Obsoletes:	openoffice.org-i18n-he-kde
Obsoletes:	openoffice.org-i18n-he

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
Obsoletes:	openoffice.org-i18n-hr-gtk
Obsoletes:	openoffice.org-i18n-hr-kde
Obsoletes:	openoffice.org-i18n-hr

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
Obsoletes:	openoffice.org-i18n-hu-gtk
Obsoletes:	openoffice.org-i18n-hu-kde
Obsoletes:	openoffice.org-i18n-hu

%description i18n-hu
This package provides resources containing menus and dialogs in
Hungarian language.

%description i18n-hu -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
węgierskim.

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
Obsoletes:	openoffice.org-i18n-it-gtk
Obsoletes:	openoffice.org-i18n-it-kde
Obsoletes:	openoffice.org-i18n-it

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
Obsoletes:	openoffice.org-i18n-ja-gtk
Obsoletes:	openoffice.org-i18n-ja-kde
Obsoletes:	openoffice.org-i18n-ja

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

%package i18n-kid
Summary:	LibreOffice - interface in Koshin language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku koshin
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-kid

%description i18n-kid
This package provides resources containing menus and dialogs in Koshin
language.

%description i18n-kid -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
koshin.

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
Obsoletes:	openoffice.org-i18n-ko-gtk
Obsoletes:	openoffice.org-i18n-ko-kde
Obsoletes:	openoffice.org-i18n-ko

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

%package i18n-ky
Summary:	LibreOffice - interface in Kyrgyz language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku kirgiskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ky

%description i18n-ky
This package provides resources containing menus and dialogs in
Kyrgyz language.

%description i18n-ky -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
kirgiskim.

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
Obsoletes:	openoffice.org-i18n-lt-gtk
Obsoletes:	openoffice.org-i18n-lt-kde
Obsoletes:	openoffice.org-i18n-lt

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
This package provides resources containing menus and dialogs in
Meitei language.

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

%package i18n-ms
Summary:	LibreOffice - interface in Malay language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku malajskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-ms
Obsoletes:	openoffice-i18n-ms-gtk
Obsoletes:	openoffice.org-i18n-ms-gtk
Obsoletes:	openoffice.org-i18n-ms-kde
Obsoletes:	openoffice.org-i18n-ms

%description i18n-ms
This package provides resources containing menus and dialogs in Malay
language.

%description i18n-ms -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
malajskim.

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
Obsoletes:	openoffice.org-i18n-nb-gtk
Obsoletes:	openoffice.org-i18n-nb-kde
Obsoletes:	openoffice.org-i18n-nb

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
Obsoletes:	openoffice.org-i18n-nl-gtk
Obsoletes:	openoffice.org-i18n-nl-kde
Obsoletes:	openoffice.org-i18n-nl

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
Obsoletes:	openoffice.org-i18n-nn-gtk
Obsoletes:	openoffice.org-i18n-nn-kde
Obsoletes:	openoffice.org-i18n-nn

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
Obsoletes:	openoffice.org-i18n-nso-gtk
Obsoletes:	openoffice.org-i18n-nso-kde
Obsoletes:	openoffice.org-i18n-nso

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
This package provides resources containing menus and dialogs in
Oromo language.

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

%package i18n-pap
Summary:	LibreOffice - interface in Papiamento language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku papiamento
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-pap

%description i18n-pap
This package provides resources containing menus and dialogs in
Papiamento language.

%description i18n-pap -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
papiamento.

%package i18n-pl
Summary:	LibreOffice - interface in Polish language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku polskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-pl
Obsoletes:	openoffice-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl-gtk
Obsoletes:	openoffice.org-i18n-pl-kde
Obsoletes:	openoffice.org-i18n-pl

%description i18n-pl
This package provides resources containing menus and dialogs in Polish
language.

%description i18n-pl -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
polskim.

%package i18n-ps
Summary:	LibreOffice - interface in Pashto language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku paszto
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ps

%description i18n-ps
This package provides resources containing menus and dialogs in
Pashto language.

%description i18n-ps -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
paszto.

%package i18n-pt
Summary:	LibreOffice - interface in Portuguese language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku portugalskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice-i18n-pt
Obsoletes:	openoffice-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt-gtk
Obsoletes:	openoffice.org-i18n-pt-kde
Obsoletes:	openoffice.org-i18n-pt

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
Obsoletes:	openoffice.org-i18n-pt_BR-gtk
Obsoletes:	openoffice.org-i18n-pt_BR-kde
Obsoletes:	openoffice.org-i18n-pt_BR

%description i18n-pt_BR
This package provides resources containing menus and dialogs in
Brazilian Portuguese language.

%description i18n-pt_BR -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
portugalskim dla Brazylii.

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
Obsoletes:	openoffice.org-i18n-ru-gtk
Obsoletes:	openoffice.org-i18n-ru-kde
Obsoletes:	openoffice.org-i18n-ru

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

%package i18n-sc
Summary:	LibreOffice - interface in Sardinian language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku sardyńskim
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sc

%description i18n-sc
This package provides resources containing menus and dialogs in
Sardinian language.

%description i18n-sc -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
sardyńskim.

%package i18n-sd
Summary:	LibreOffice - interface in Sindhi language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku sindhi
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-sd

%description i18n-sd
This package provides resources containing menus and dialogs in
Sindhi language.

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
Obsoletes:	openoffice.org-i18n-sk-gtk
Obsoletes:	openoffice.org-i18n-sk-kde
Obsoletes:	openoffice.org-i18n-sk

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
Obsoletes:	openoffice.org-i18n-sl-gtk
Obsoletes:	openoffice.org-i18n-sl-kde
Obsoletes:	openoffice.org-i18n-sl

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
Obsoletes:	openoffice.org-i18n-sv-gtk
Obsoletes:	openoffice.org-i18n-sv-kde
Obsoletes:	openoffice.org-i18n-sv

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

%package i18n-ti
Summary:	LibreOffice - interface in Tigrigna language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku tigrinia
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ti_ER

%description i18n-ti
This package provides resources containing menus and dialogs in
Tigrigna language.

%description i18n-ti -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
tigrinia.

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
Obsoletes:	openoffice.org-i18n-tr-gtk
Obsoletes:	openoffice.org-i18n-tr-kde
Obsoletes:	openoffice.org-i18n-tr

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
Obsoletes:	openoffice.org-i18n-uk-gtk
Obsoletes:	openoffice.org-i18n-uk-kde
Obsoletes:	openoffice.org-i18n-uk

%description i18n-uk
This package provides resources containing menus and dialogs in
Ukrainian language.

%description i18n-uk -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
ukraińskim.

%package i18n-ur
Summary:	LibreOffice - interface in Urdu language
Summary(pl.UTF-8):	LibreOffice - interfejs w języku urdu
Group:		I18n
Requires:	%{name}-core = %{version}-%{release}
Obsoletes:	openoffice.org-i18n-ur_IN

%description i18n-ur
This package provides resources containing menus and dialogs in Urdu
language.

%description i18n-ur -l pl.UTF-8
Ten pakiet dostarcza zasoby zawierające menu i okna dialogowe w języku
urdu.

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
Obsoletes:	openoffice.org-i18n-zh_CN-gtk
Obsoletes:	openoffice.org-i18n-zh_CN-kde
Obsoletes:	openoffice.org-i18n-zh_CN

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
Obsoletes:	openoffice.org-i18n-zh_TW-gtk
Obsoletes:	openoffice.org-i18n-zh_TW-kde
Obsoletes:	openoffice.org-i18n-zh_TW

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
Obsoletes:	openoffice.org-i18n-zu-gtk
Obsoletes:	openoffice.org-i18n-zu-kde
Obsoletes:	openoffice.org-i18n-zu

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
%setup -q -n %{name}-build-%{version}
%patch0 -p1

install -d src

# sources, icons, KDE_icons. You can verify that all needed sources
# are here by running ./download script manually after rpmbuild -bp
ln -sf %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
	%{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} \
	%{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
	%{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} \
	%{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} \
	%{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE100} \
	%{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} \
	%{SOURCE105} %{SOURCE106} %{SOURCE107} %{SOURCE108} \
	%{SOURCE109} %{SOURCE110} %{SOURCE111} %{SOURCE112} \
	%{SOURCE113} %{SOURCE114} %{SOURCE115} %{SOURCE116} \
	%{SOURCE117} %{SOURCE118} %{SOURCE119} %{SOURCE120} \
	%{SOURCE121} %{SOURCE122} %{SOURCE123} %{SOURCE124} \
	src

ln -s %{PATCH100} patches/hotfixes/%{basename:%{PATCH100}}.diff

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

export DEFAULT_TO_ENGLISH_FOR_PACKING=1

%if %{with parallelbuild}
RPM_BUILD_NR_THREADS=$(echo %{_smp_mflags} | cut -dj -f2)
[ -z "$RPM_BUILD_NR_THREADS" ] && RPM_BUILD_NR_THREADS=1
%else
RPM_BUILD_NR_THREADS="1"
%endif

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
	--with-system-apache-commons \
	--with-system-boost \
	--with-system-cairo \
	--with-system-curl \
	--with-system-cppunit \
	--with-system-dicts \
	--with-external-dict-dir=/usr/share/myspell \
	--with-system-expat \
	--with-system-graphite \
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
	--with-system-lucene \
	--with-lucene-analyzers-jar=%{_javadir}/lucene-analyzers.jar \
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
	--with-system-servlet-api \
	--with-system-sndfile \
	--with-system-stdlibs \
	--with-system-vigra \
	--with-system-x11-extensions-headers \
	--with-system-xrender \
	--with-system-xrender-headers=yes \
	--with-system-zlib \
%if %{with mozilla}
	--with-system-mozilla=libxul \
%else
	--disable-mozilla \
%endif
	--with-dynamic-xinerama \
	--with-distro="${DISTRO}" \
	--enable-gtk \
	%{?with_kde:--enable-kde --disable-kde4} \
	%{?with_kde4:--enable-kde4 --disable-kde} \
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
	--enable-gio \
%endif
	--with-docdir=%{_docdir}/%{name}-%{version} \
	--with-python=%{__python} \
	--without-stlport \
	--with-x \
	--without-fonts \
	--without-gpc \
	--disable-epm \
	--disable-fontooo \
	--%{?with_msaccess:en}%{!?with_msaccess:dis}able-access \
	--enable-cairo \
	--enable-crypt-link \
	--enable-dbus \
	--%{?with_mono:en}%{!?with_mono:dis}able-mono \
	--enable-pam-link \
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
	--disable-strip \
	--with-num-cpus=$RPM_BUILD_NR_THREADS \
	--with-build-version=%{version}-%{release} \
	--with-tag=%{tag} \
	--with-drink=coffee \
	--enable-split-app-modules \
	--enable-split-opt-features \
	--disable-access \
	--without-git \
	--enable-minimizer \
	--enable-presenter-console \
	--enable-pdfimport \
	--enable-cups \
	--enable-fontconfig \
	--enable-lockdown \
	--disable-layout \
	--with-use-shell=bash \
	--enable-wiki-publisher \
	--enable-report-builder \
	--disable-fetch-external
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
bash ./configure \
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
	#cp -a build/%{tag}/solver/%{upd}/unxlng*.pro/bin/regcomp{,.bin} $RPM_BUILD_ROOT%{ooobasisdir}/program/

	# Rename .desktop files to avoid conflicts with other applications .desktops
	# TODO: make patch instead.
	for a in $RPM_BUILD_ROOT%{_desktopdir}/*.desktop; do
		d=$(dirname "$a")
		f=$(basename "$a")
		mv $a $d/oo$f
	done

	#install %{SOURCE53} $RPM_BUILD_ROOT%{_libdir}/%{name}/program/openintro_pld.bmp
	#install %{SOURCE54} $RPM_BUILD_ROOT%{_libdir}/%{name}/program/openabout_pld.bmp

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
		# %{basisdir}/share/registry/.*[_-]$lang.xcd
		grep "/share/registry/.*[_-]${lang}.xcd$" ${lfile} >> ${langfn}.lang || :
		# %{basisdir}/share/template/$lang
		grep "/share/template/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/${lang}/" ${lfile} >> ${langfn}.lang || :
		# %{basisdir}/share/template/wizard/letter/lang
		grep "/share/template/wizard/letter/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}$" build/common_list.txt >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}/" ${lfile} >> ${langfn}.lang || :
		grep "/share/template/wizard/letter/${lang}/" build/common_list.txt >> ${langfn}.lang || :
		# %{basisdir}/share/wordbook/$lang
		grep "/share/wordbook/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/wordbook/${lang}/" ${lfile} >> ${langfn}.lang || :
		# %{basisdir}/share/samples/$lang
		grep "/share/samples/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/share/samples/${lang}/" ${lfile} >> ${langfn}.lang || :
		# %{basisdir}/help/$lang
		grep "/help/${lang}$" ${lfile} >> ${langfn}.lang || :
		grep "/help/${lang}/" ${lfile} >> ${langfn}.lang || :
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
%doc %{_libdir}/%{name}/CREDITS*
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
%{ooobasisdir}/presets/config/libreoffice.soc
%{ooobasisdir}/presets/config/scribus.soc
%{ooobasisdir}/presets/config/standard.so?
%{ooobasisdir}/presets/config/tango.soc
%{ooobasisdir}/presets/config/web.soc
%{ooobasisdir}/presets/database
%{ooobasisdir}/presets/gallery
%{ooobasisdir}/presets/psprint

%dir %{ooobasisdir}/program
%attr(755,root,root) %{ooobasisdir}/program/basprov*.uno.so
%attr(755,root,root) %{ooobasisdir}/program/cairocanvas.uno.so
%attr(755,root,root) %{ooobasisdir}/program/canvasfactory.uno.so
%attr(755,root,root) %{ooobasisdir}/program/cde-open-url
%attr(755,root,root) %{ooobasisdir}/program/cmdmail.uno.so
%attr(755,root,root) %{ooobasisdir}/program/configmgr.uno.so
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
%attr(755,root,root) %{ooobasisdir}/program/libdesktop_detectorl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libdict_ja.so
%attr(755,root,root) %{ooobasisdir}/program/libdict_zh.so
%attr(755,root,root) %{ooobasisdir}/program/libdrawinglayerl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libeditengl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libeggtrayl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libegil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libembobj.so
%attr(755,root,root) %{ooobasisdir}/program/libemboleobj.so
%attr(755,root,root) %{ooobasisdir}/program/libemel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libepbl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libepgl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libeppl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libepsl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libeptl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/liberal[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libetil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libevtatt.so
%attr(755,root,root) %{ooobasisdir}/program/libexlinkl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libexpl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfileacc.so
%attr(755,root,root) %{ooobasisdir}/program/libfilel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfilterconfig1.so
%attr(755,root,root) %{ooobasisdir}/program/libflatl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libforl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libforuil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfrml[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfwel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfwil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfwkl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfwll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libfwml[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libguesslangl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libhelplinkerl[ipx].so
%{!?with_system_hunspell:%attr(755,root,root) %{ooobasisdir}/program/libhunspell.so}
%attr(755,root,root) %{ooobasisdir}/program/libhyphenl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libi18nisolang1gcc3.so
%attr(755,root,root) %{ooobasisdir}/program/libi18npaperl[ipx].so
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
%attr(755,root,root) %{ooobasisdir}/program/libmsfilterl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libmsformsl[ipx].uno.so
%attr(755,root,root) %{ooobasisdir}/program/libmtfrenderer.uno.so
%attr(755,root,root) %{ooobasisdir}/program/libmysqll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libodbcl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libodbcbasel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/liboffaccl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/liboooimprovecorel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libooxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libpackage2.so
%attr(755,root,root) %{ooobasisdir}/program/libpcrl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libpdffilterl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libpll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libpreloadl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libprotocolhandlerl[ipx].so
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
%attr(755,root,root) %{ooobasisdir}/program/libsdfiltl[ipx].so
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
%attr(755,root,root) %{ooobasisdir}/program/libsvxcorel[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsvxl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libswl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libtextcat.so
%attr(755,root,root) %{ooobasisdir}/program/libtextconv_dict.so
%attr(755,root,root) %{ooobasisdir}/program/libtextconversiondlgsl[ipx].so
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
%attr(755,root,root) %{ooobasisdir}/program/libvbahelperl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libvbaswobjl[ipx].uno.so
%attr(755,root,root) %{ooobasisdir}/program/libvcll[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libvclplug_genl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libvclplug_svpl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libxcrl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libxmlfal[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libxmlfdl[ipx].so
## maybe external is possible?
# - external broken in 3.0.1
###%attr(755,root,root) %{ooobasisdir}/program/libxmlsec1*.so
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
%attr(755,root,root) %{ooobasisdir}/program/migrationoo3.uno.so
%attr(755,root,root) %{ooobasisdir}/program/open-url
%attr(755,root,root) %{ooobasisdir}/program/pagein*
%attr(755,root,root) %{ooobasisdir}/program/passwordcontainer.uno.so
%attr(755,root,root) %{ooobasisdir}/program/pluginapp.bin
%attr(755,root,root) %{ooobasisdir}/program/productregistration.uno.so
## seems to be exactly the same as in -ure
#%attr(755,root,root) %{ooobasisdir}/program/regcomp
#%attr(755,root,root) %{ooobasisdir}/program/regcomp.bin
##
%attr(755,root,root) %{ooobasisdir}/program/sax.uno.so
%attr(755,root,root) %{ooobasisdir}/program/senddoc
%attr(755,root,root) %{ooobasisdir}/program/simplecanvas.uno.so
%attr(755,root,root) %{ooobasisdir}/program/slideshow.uno.so
%attr(755,root,root) %{ooobasisdir}/program/spadmin.bin
%attr(755,root,root) %{ooobasisdir}/program/stringresource*.uno.so
%attr(755,root,root) %{ooobasisdir}/program/syssh.uno.so
%attr(755,root,root) %{ooobasisdir}/program/ucpexpand1.uno.so
%attr(755,root,root) %{ooobasisdir}/program/ucpext.uno.so
%attr(755,root,root) %{ooobasisdir}/program/ucptdoc1.uno.so
%attr(755,root,root) %{ooobasisdir}/program/updatefeed.uno.so
%attr(755,root,root) %{ooobasisdir}/program/uri-encode
%attr(755,root,root) %{ooobasisdir}/program/vbaevents*.uno.so
%attr(755,root,root) %{ooobasisdir}/program/vclcanvas.uno.so

%if %{with java}
%attr(755,root,root) %{ooobasisdir}/program/libhsqldb.so
%attr(755,root,root) %{ooobasisdir}/program/libjdbcl[ipx].so
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
%{ooobasisdir}/program/classes/commonwizards.jar
%{ooobasisdir}/program/classes/fax.jar
%{ooobasisdir}/program/classes/form.jar
%{!?with_system_hsqldb:%{ooobasisdir}/program/classes/hsqldb.jar}
%{ooobasisdir}/program/classes/js.jar
%{ooobasisdir}/program/classes/letter.jar
%{ooobasisdir}/program/classes/officebean.jar
%{ooobasisdir}/program/classes/query.jar
%{ooobasisdir}/program/classes/report.jar
%{ooobasisdir}/program/classes/saxon9.jar
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
%{ooobasisdir}/program/resource/cuien-US.res
%{ooobasisdir}/program/resource/chartcontrolleren-US.res
%{ooobasisdir}/program/resource/dbaen-US.res
%{ooobasisdir}/program/resource/dbmmen-US.res
%{ooobasisdir}/program/resource/dbwen-US.res
%{ooobasisdir}/program/resource/deploymenten-US.res
%{ooobasisdir}/program/resource/deploymentguien-US.res
%{ooobasisdir}/program/resource/dkten-US.res
%{ooobasisdir}/program/resource/editengen-US.res
%{ooobasisdir}/program/resource/egien-US.res
%{ooobasisdir}/program/resource/emeen-US.res
%{ooobasisdir}/program/resource/epben-US.res
%{ooobasisdir}/program/resource/epgen-US.res
%{ooobasisdir}/program/resource/eppen-US.res
%{ooobasisdir}/program/resource/epsen-US.res
%{ooobasisdir}/program/resource/epten-US.res
%{ooobasisdir}/program/resource/euren-US.res
%{ooobasisdir}/program/resource/foren-US.res
%{ooobasisdir}/program/resource/foruien-US.res
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
%{ooobasisdir}/share/config/images_oxygen.zip
%{ooobasisdir}/share/config/images_tango.zip
%{ooobasisdir}/share/config/javasettingsunopkginstall.xml
%{ooobasisdir}/share/config/*.xpm
%dir %{ooobasisdir}/share/config/soffice.cfg
%dir %{ooobasisdir}/share/config/soffice.cfg/modules
%{ooobasisdir}/share/config/soffice.cfg/modules/BasicIDE
%{ooobasisdir}/share/config/soffice.cfg/modules/StartModule
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbapp
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbbrowser
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbquery
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbreport
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/dbtdata
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/scalc
%{ooobasisdir}/share/config/soffice.cfg/modules/schart
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/sdraw
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/sglobal
%{ooobasisdir}/share/config/soffice.cfg/modules/sglobal/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/sglobal/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/sglobal/toolbar
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/sweb
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/simpress
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swform
%{ooobasisdir}/share/config/soffice.cfg/modules/swform/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/swform/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/swform/toolbar
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swreport
%{ooobasisdir}/share/config/soffice.cfg/modules/swreport/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/swreport/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/swreport/toolbar
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swriter
%dir %{ooobasisdir}/share/config/soffice.cfg/modules/swxform
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
%{ooobasisdir}/share/registry/Langpack-en-US.xcd
%{ooobasisdir}/share/registry/binfilter.xcd
%{ooobasisdir}/share/registry/lingucomponent.xcd
%{ooobasisdir}/share/registry/main.xcd
%{ooobasisdir}/share/registry/oo-ad-ldap.xcd.sample
%{ooobasisdir}/share/registry/oo-ldap.xcd.sample
%dir %{ooobasisdir}/share/registry/res
%{ooobasisdir}/share/registry/res/fcfg_langpack_en-US.xcd

%dir %{ooobasisdir}/share/samples
%dir %{ooobasisdir}/share/samples/en-US

%dir %{ooobasisdir}/share/template
%{ooobasisdir}/share/template/en-US
%dir %{ooobasisdir}/share/template/wizard
%{ooobasisdir}/share/template/wizard/bitmap
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
%{_libdir}/%{name}/program/about.png
%{_libdir}/%{name}/program/intro.png
%{_libdir}/%{name}/program/redirectrc
%{_libdir}/%{name}/program/setuprc
%{_libdir}/%{name}/program/shell
%{_libdir}/%{name}/program/sofficerc
%{_libdir}/%{name}/program/versionrc

%dir %{_libdir}/%{name}/program/resource
%{_libdir}/%{name}/program/resource/oooen-US.res

# symlinks
%{_libdir}/%{name}/basis-link
#%{_libdir}/%{name}/licenses
%{_libdir}/%{name}/readmes
%{_libdir}/%{name}/share


%dir %{_datadir}/%{name}
#%dir %{_datadir}/%{name}/licenses
#%{_datadir}/%{name}/licenses/LICENSE_en-US
%dir %{_datadir}/%{name}/readmes
%{_datadir}/%{name}/readmes/README_en-US
%dir %{_datadir}/%{name}/share
%dir %{_datadir}/%{name}/share/config
%{_datadir}/%{name}/share/config/images_brand.zip
%dir %{_datadir}/%{name}/share/extensions
%{_datadir}/%{name}/share/extensions/package.txt
#%dir %{_datadir}/%{name}/share/readme
#%{_datadir}/%{name}/share/readme/LICENSE_en-US*
#%{_datadir}/%{name}/share/readme/README_en-US*
%dir %{_datadir}/%{name}/share/registry
%{_datadir}/%{name}/share/registry/brand.xcd

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

%if %{with kde4}
%files libs-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{ooobasisdir}/program/kde-open-url
%attr(755,root,root) %{ooobasisdir}/program/fps_kde4.uno.so
%attr(755,root,root) %{ooobasisdir}/program/libvclplug_kde4*.so
%endif

%files libs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{ooobasisdir}/program/fps_gnome.uno.so
%attr(755,root,root) %{ooobasisdir}/program/gconfbe1.uno.so
%attr(755,root,root) %{ooobasisdir}/program/gnome-open-url
%attr(755,root,root) %{ooobasisdir}/program/gnome-open-url.bin
%attr(755,root,root) %{ooobasisdir}/program/libevoabl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libvclplug_gtk*.so
%if %{with gnomevfs}
%attr(755,root,root) %{ooobasisdir}/program/ucpgvfs1.uno.so
%else
%attr(755,root,root) %{ooobasisdir}/program/ucpgio1.uno.so
%endif

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
%{ooobasisdir}/share/config/soffice.cfg/modules/dbapp/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbapp/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbapp/toolbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbbrowser/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbbrowser/toolbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbquery/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbquery/toolbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbrelation
%{ooobasisdir}/share/config/soffice.cfg/modules/dbreport/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbreport/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbreport/toolbar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbtable
%{ooobasisdir}/share/config/soffice.cfg/modules/dbtdata/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/dbtdata/toolbar
%{ooobasisdir}/share/registry/base.xcd
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
%attr(755,root,root) %{ooobasisdir}/program/libscfiltl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libscl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libscuil[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsolverl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libvbaobjl[ipx].uno.so
%{ooobasisdir}/program/resource/analysisen-US.res
%{ooobasisdir}/program/resource/bf_scen-US.res
%{ooobasisdir}/program/resource/dateen-US.res
%{ooobasisdir}/program/resource/solveren-US.res
%{ooobasisdir}/program/resource/scen-US.res
%{ooobasisdir}/share/config/soffice.cfg/modules/scalc/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/scalc/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/scalc/toolbar
%{ooobasisdir}/share/registry/calc.xcd

%files draw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oodraw
%attr(755,root,root) %{_libdir}/%{name}/program/sdraw
%{_mandir}/man1/oodraw.1
%{_desktopdir}/oodraw.desktop
%{_iconsdir}/hicolor/*/apps/ooo-draw.png
%{_pixmapsdir}/ooo-draw.png
%{ooobasisdir}/help/en/sdraw.*
%{ooobasisdir}/share/config/soffice.cfg/modules/sdraw/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/sdraw/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/sdraw/toolbar
%{ooobasisdir}/share/registry/draw.xcd

%files emailmerge
%defattr(644,root,root,755)
%{ooobasisdir}/program/mailmerge.py*

%files writer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oowriter
%attr(755,root,root) %{ooobasisdir}/program/libhwp.so
%attr(755,root,root) %{ooobasisdir}/program/liblwpftl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libmswordl[ipx].so
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
%{ooobasisdir}/program/resource/t602filteren-US.res
%{ooobasisdir}/share/config/soffice.cfg/modules/sbibliography
%{ooobasisdir}/share/config/soffice.cfg/modules/swriter/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/swriter/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/swriter/toolbar
%{ooobasisdir}/share/registry/writer.xcd

%files impress
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ooimpress
%attr(755,root,root) %{_libdir}/%{name}/program/simpress
%attr(755,root,root) %{ooobasisdir}/program/OGLTrans.uno.so
%attr(755,root,root) %{ooobasisdir}/program/libanimcore.so
%attr(755,root,root) %{ooobasisdir}/program/libplaceware*.so
%{_mandir}/man1/ooimpress.1
%{_desktopdir}/ooimpress.desktop
%{_iconsdir}/hicolor/*/apps/ooo-impress.png
%{_pixmapsdir}/ooo-impress.png
%{ooobasisdir}/help/en/simpress.*
%{ooobasisdir}/share/config/soffice.cfg/simpress
%{ooobasisdir}/share/config/soffice.cfg/modules/simpress/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/simpress/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/simpress/toolbar
%{ooobasisdir}/share/registry/impress.xcd
%{ooobasisdir}/share/registry/ogltrans.xcd

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
%{ooobasisdir}/program/resource/bf_smen-US.res
%{ooobasisdir}/program/resource/smen-US.res
%{ooobasisdir}/share/config/soffice.cfg/modules/smath
%{ooobasisdir}/share/registry/math.xcd

%files web
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ooweb
%{_mandir}/man1/ooweb.1
%{_desktopdir}/ooweb.desktop
%{_iconsdir}/hicolor/*/apps/ooo-web.png
%{_pixmapsdir}/ooo-web.png
%{ooobasisdir}/share/config/soffice.cfg/modules/sweb/menubar
%{ooobasisdir}/share/config/soffice.cfg/modules/sweb/statusbar
%{ooobasisdir}/share/config/soffice.cfg/modules/sweb/toolbar

%files graphicfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{ooobasisdir}/program/libflashl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libsvgfilterl[ipx].so
%attr(755,root,root) %{ooobasisdir}/program/libwpgimportl[ipx].so
%{ooobasisdir}/share/registry/graphicfilter.xcd

%files xsltfilter
%defattr(644,root,root,755)
%{ooobasisdir}/share/registry/xsltfilter.xcd
%{ooobasisdir}/share/xslt/docbook
%{ooobasisdir}/share/xslt/export/xhtml
%{ooobasisdir}/share/xslt/odfflatxml

%if %{with java}
%files javafilter
%defattr(644,root,root,755)
%{ooobasisdir}/program/classes/pexcel.jar
%{ooobasisdir}/program/classes/pocketword.jar
%{ooobasisdir}/program/classes/aportisdoc.jar
%{ooobasisdir}/share/registry/palm.xcd
%{ooobasisdir}/share/registry/pocketexcel.xcd
%{ooobasisdir}/share/registry/pocketword.xcd
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
%attr(755,root,root) %{_libdir}/%{name}/ure/lib/liblog_uno_uno.so
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
%{ooobasisdir}/share/registry/pyuno.xcd

# samples there
%{ooobasisdir}/share/Scripts/python

# FIXME: extensions should be moved to libdir (they provide arch-dependent files)
%files pdfimport
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/share/extensions/pdfimport
%attr(755,root,root) %{_datadir}/%{name}/share/extensions/pdfimport/pdfimport.uno.so
%attr(755,root,root) %{_datadir}/%{name}/share/extensions/pdfimport/xpdfimport
%{_datadir}/%{name}/share/extensions/pdfimport/META-INF
%{_datadir}/%{name}/share/extensions/pdfimport/basic
%{_datadir}/%{name}/share/extensions/pdfimport/description.xml
%{_datadir}/%{name}/share/extensions/pdfimport/help
%{_datadir}/%{name}/share/extensions/pdfimport/images
%{_datadir}/%{name}/share/extensions/pdfimport/registration
%{_datadir}/%{name}/share/extensions/pdfimport/*.xcu
%{_datadir}/%{name}/share/extensions/pdfimport/*.pdf

%files presentation-minimizer
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/share/extensions/presentation-minimizer
%attr(755,root,root) %{_datadir}/%{name}/share/extensions/presentation-minimizer/SunPresentationMinimizer.uno.so
%{_datadir}/%{name}/share/extensions/presentation-minimizer/META-INF
%{_datadir}/%{name}/share/extensions/presentation-minimizer/bitmaps
%{_datadir}/%{name}/share/extensions/presentation-minimizer/description.xml
%{_datadir}/%{name}/share/extensions/presentation-minimizer/help
%{_datadir}/%{name}/share/extensions/presentation-minimizer/registr*

%files presenter-screen
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}/share/extensions/presenter-screen
%attr(755,root,root) %{_datadir}/%{name}/share/extensions/presenter-screen/PresenterScreen.uno.so
%{_datadir}/%{name}/share/extensions/presenter-screen/META-INF
%{_datadir}/%{name}/share/extensions/presenter-screen/bitmaps
%{_datadir}/%{name}/share/extensions/presenter-screen/description.xml
%{_datadir}/%{name}/share/extensions/presenter-screen/help
%{_datadir}/%{name}/share/extensions/presenter-screen/registry

%files report-builder
%defattr(644,root,root,755)
%{_datadir}/%{name}/share/extensions/report-builder

%files wiki-publisher
%defattr(644,root,root,755)
%{_datadir}/%{name}/share/extensions/wiki-publisher

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

%files i18n-as -f as.lang
%defattr(644,root,root,755)

%files i18n-be_BY -f be_BY.lang
%defattr(644,root,root,755)

%files i18n-bg -f bg.lang
%defattr(644,root,root,755)

%files i18n-bn -f bn.lang
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

%files i18n-is -f is.lang
%defattr(644,root,root,755)

%files i18n-it -f it.lang
%defattr(644,root,root,755)

%files i18n-ja -f ja.lang
%defattr(644,root,root,755)

%files i18n-ka -f ka.lang
%defattr(644,root,root,755)

%files i18n-kid -f kid.lang
%defattr(644,root,root,755)

%files i18n-kk -f kk.lang
%defattr(644,root,root,755)

%files i18n-km -f km.lang
%defattr(644,root,root,755)

%files i18n-kn_IN -f kn.lang
%defattr(644,root,root,755)

%files i18n-ko -f ko.lang
%defattr(644,root,root,755)

%files i18n-kok -f kok.lang
%defattr(644,root,root,755)

%files i18n-ks -f ks.lang
%defattr(644,root,root,755)

%files i18n-ku -f ku.lang
%defattr(644,root,root,755)

%files i18n-ky -f ky.lang
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

%files i18n-om -f om.lang
%defattr(644,root,root,755)

%files i18n-or -f or.lang
%defattr(644,root,root,755)

%files i18n-pa_IN -f pa_IN.lang
%defattr(644,root,root,755)

%files i18n-pap -f pap.lang
%defattr(644,root,root,755)

%files i18n-pl -f pl.lang
%defattr(644,root,root,755)

%files i18n-ps -f ps.lang
%defattr(644,root,root,755)

%files i18n-pt -f pt.lang
%defattr(644,root,root,755)

%files i18n-pt_BR -f pt_BR.lang
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

%files i18n-sc -f sc.lang
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

%files i18n-ti -f ti.lang
%defattr(644,root,root,755)

%files i18n-tn -f tn.lang
%defattr(644,root,root,755)

%files i18n-tr -f tr.lang
%defattr(644,root,root,755)

%files i18n-ts -f ts.lang
%defattr(644,root,root,755)

%files i18n-ug -f ug.lang
%defattr(644,root,root,755)

%files i18n-uk -f uk.lang
%defattr(644,root,root,755)

%files i18n-ur -f ur.lang
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
