# NOTE:
#	- normal build requires little less than 4GB of disk space
#	- full debug build requires about 9GB of disk space
# TODO:
#	- drop requirement on nas-devel
#	- fix locale names and other locale related things
#	- --with-system-myspell + myspell package as in Debian
#	- --with-system-neon - check compilation (works with 0.23 but not 0.24)
#	- in gtk version menu highlight has almost the same colour as menu text
#	- 6 user/config/*.so? files shared between -i18n-en and -i18n-sl
#	- remove oohtml symlink (there is ooweb),
#	- add ooglobal symlink and it's ooo-wrapper entry (among calc|draw|impress|math|web|writer)

# Conditional build:
%bcond_with	java		# Java support
%bcond_with	vfs		# Enable GNOME VFS and Evolution 2 support

%define		ver		1.1
%define		rel		3
%define		ooobver		1.3.5
%define		subver		645
%define		fullver		%{ver}.%{rel}
%define		dfullver	%(echo %{fullver} | tr . _)
%define		specflags	-fno-strict-aliasing

Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	%{fullver}
Release:	3%{?with_vfs:vfs}
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
# Source0:	http://ooo.ximian.com/packages/OOO_1_1_2/ooo-build-%{ooobver}.tar.gz
Source0:	http://ooo.ximian.com/packages/snap/ooo-build-ooo-build-1-3-%{ooobver}-20041112.tar.gz
# Source0-md5:	cc6fd08174597bdd0f1793a6dcc818a7
Source1:	http://ooo.ximian.com/packages/OOO_%{dfullver}/OOO_%{dfullver}.tar.bz2
# Source1-md5:	f7f13576ad04e6a958dcd9d4cb569538
Source2:	http://ooo.ximian.com/packages/ooo-icons-OOO_1_1-10.tar.gz
# Source2-md5:	be79d3cb5f64d2c0ac8a75e65a59cb09
Source3:	http://kde.openoffice.org/files/documents/159/1975/ooo-KDE_icons-OOO_1_1-0.3.tar.gz
# Source3-md5:	05ff784fff01c54cd3dd7b975b46bae2
Source4:	http://ooo.ximian.com/packages/libwpd-snap-20040823.tar.gz
# Source4-md5:	c3d8c9f5ae2abbe1b7091817265b9ef3
Source10:	oocalc.desktop
Source11:	oodraw.desktop
Source12:	ooffice.desktop
Source13:	ooglobal.desktop
Source14:	ooimpress.desktop
Source15:	oomath.desktop
Source16:	ooprinteradmin.desktop
Source17:	oosetup.desktop
Source18:	ooweb.desktop
Source19:	oowriter.desktop

# we keep these in ooo-build repository
# PLD splash screen
#Source20:	%{name}-about.bmp
#Source21:	%{name}-intro.bmp

%define		cftp	http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib

# Help content
Source400:	%{cftp}/helpcontent/helpcontent_01_unix.tgz
# Source400-md5:	7da2aff674c2c84aba8b21ac2ab16bb6
Source401:	%{cftp}/helpcontent/helpcontent_31_unix.tgz
# Source401-md5:	c7e618e2d9b8bd25cae12954ef2548c9
Source402:	%{cftp}/helpcontent/helpcontent_33_unix.tgz
# Source402-md5:	68d58bc30b485a77c0a0fba08af3aee3
Source403:	%{cftp}/helpcontent/helpcontent_34_unix.tgz
# Source403-md5:	8696bbee3dc4d5b6fd60218123016e29
Source404:	%{cftp}/helpcontent/helpcontent_39_unix.tgz
# Source404-md5:	c2ae86d02f462d2b663d621190f5ef34
Source405:	%{cftp}/helpcontent/helpcontent_46_unix.tgz
# Source405-md5:	7b013981edce2fabe4a8751ff64a8d58
Source406:	%{cftp}/helpcontent/helpcontent_49_unix.tgz
# Source406-md5:	a39f44ec40f452c963a4a187f31d1acb
Source407:	%{cftp}/helpcontent/helpcontent_55_unix.tgz
# Source407-md5:	804d3ce61e11335193a410aaf9603f8e
Source408:	%{cftp}/helpcontent/helpcontent_81_unix.tgz
# Source408-md5:	81b705057a0e14ebcbf02fac4762781a
Source409:	%{cftp}/helpcontent/helpcontent_82_unix.tgz
# Source409-md5:	3121fbd251176d7c7b6e33ecec744c65
Source410:	%{cftp}/helpcontent/helpcontent_86_unix.tgz
# Source410-md5:	aee37935139c5ccd4b6d8abdd2037c66
Source411:	%{cftp}/helpcontent/helpcontent_88_unix.tgz
# Source411-md5:	3b00571318e45965dee0545d86306d65
Source412:	%{cftp}/helpcontent/helpcontent_90_unix.tgz
# Source412-md5:	9521a01c5817e87178f356762f8cdab5

Patch0:		%{name}-rh-disable-spellcheck-all-langs.patch
# PLD-specific, they ooo-build people don't like it
Patch1:		%{name}-files.patch
# Enable VFS support during build
Patch2:		%{name}-vfs.patch

URL:		http://www.openoffice.org/
BuildRequires:	ImageMagick
BuildRequires:	STLport-devel >= 4.5.3-6
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison >= 1.875-4
BuildRequires:	cups-devel
BuildRequires:	curl-devel
BuildRequires:	db-cxx-devel
BuildRequires:	db-devel
BuildRequires:	/usr/bin/getopt
%if %{with vfs}
BuildRequires:	gnome-vfs2
%endif
%if %{with java}
BuildRequires:	db-java >= 4.2.52-4
BuildRequires:	jar
BuildRequires:	jdk
%else
BuildRequires:	libxslt-progs
%endif
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	libart_lgpl-devel
BuildRequires:	libstdc++-devel >= 5:3.2.1
BuildRequires:	nas-devel
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
BuildRequires:	sane-backends-devel
BuildRequires:	startup-notification-devel
BuildRequires:	tcsh
BuildRequires:	unixODBC-devel
BuildRequires:	unzip
BuildRequires:	zip
BuildRequires:	zlib-devel
BuildRequires:	qt-devel
BuildRequires:	kdelibs-devel
BuildRequires:	gtk+2-devel
# checked for by ooo-build configure, but not used now
#BuildRequires:	evolution-data-server-devel >= 0.0.92
#BuildRequires:	gnome-vfs2-devel >= 2.0
#BuildRequires:	libxml2-devel >= 2.0
BuildConflicts:	java-sun = 1.4.2
Requires(post,postun):	fontpostinst
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	cups-lib
Requires:	db
Requires:	libstdc++ >= 5:3.2.1
Requires:	mktemp
Requires:	sed
ExclusiveArch:	%{ix86} ppc sparc sparcv9
#Suggested:	chkfontpath
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

%description libs
OpenOffice.org productivity suite - shared libraries.

%description libs -l pl
Pakiet biurowy OpenOffice.org - biblioteki.

%package libs-kde
Summary:	OpenOffice.org KDE Interface
Summary(pl):	Interfejs KDE dla OpenOffice.org
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-i18n-en-kde
Obsoletes:	%{name}-i18n-en

%description libs-kde
OpenOffice.org productivity suite - KDE Interface.

%description libs-kde -l pl
Pakiet biurowy OpenOffice.org - Interfejs KDE.

%package libs-gtk
Summary:	OpenOffice.org GTK+ Interface
Summary(pl):	Interfejs GTK+ dla OpenOffice.org
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-i18n-en-gtk
Obsoletes:	%{name}-i18n-en

%description libs-gtk
OpenOffice.org productivity suite - GTK+ Interface.

%description libs-gtk -l pl
Pakiet biurowy OpenOffice.org - Interfejs GTK+.

%package i18n-af-gtk
Summary:	OpenOffice.org - interface in Afrikaans language
Summary(pl):	OpenOffice.org - interfejs w jêzyku afrykanerskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-af

%description i18n-af-gtk
This package provides resources containing menus and dialogs in
Afrikaans language.

%description i18n-af-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
afrykanerskim.

%files i18n-af-gtk -f af.lang.gnome

%package i18n-ar-gtk
Summary:	OpenOffice.org - interface in Arabic language
Summary(pl):	OpenOffice.org - interfejs w jêzyku arabskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ar

%description i18n-ar-gtk
This package provides resources containing menus and dialogs in
Arabic language.

%description i18n-ar-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
arabskim.

%files i18n-ar-gtk -f ar.lang.gnome

%package i18n-bg-gtk
Summary:	OpenOffice.org - interface in Bulgarian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku bu³garskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-bg

%description i18n-bg-gtk
This package provides resources containing menus and dialogs in
Bulgarian language.

%description i18n-bg-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
bu³garskim.

#%files i18n-bg-gtk -f bg.lang.gnome

%package i18n-ca-gtk
Summary:	OpenOffice.org - interface in Catalan language
Summary(pl):	OpenOffice.org - interfejs w jêzyku kataloñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ca

%description i18n-ca-gtk
This package provides resources containing menus and dialogs in
Catalan language.

%description i18n-ca-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
kataloñskim.

%files i18n-ca-gtk -f ca.lang.gnome

%package i18n-cs-gtk
Summary:	OpenOffice.org - interface in Czech language
Summary(pl):	OpenOffice.org - interfejs w jêzyku czeskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-cs

%description i18n-cs-gtk
This package provides resources containing menus and dialogs in
Czech language.

%description i18n-cs-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
czeskim.

%files i18n-cs-gtk -f cs.lang.gnome

%package i18n-cy-gtk
Summary:	OpenOffice.org - interface in Cymraeg language
Summary(pl):	OpenOffice.org - interfejs w jêzyku walijskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-cy

%description i18n-cy-gtk
This package provides resources containing menus and dialogs in
Cymraeg language.

%description i18n-cy-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
walijskim.

%files i18n-cy-gtk -f cy.lang.gnome

%package i18n-da-gtk
Summary:	OpenOffice.org - interface in Danish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku duñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-da

%description i18n-da-gtk
This package provides resources containing menus and dialogs in
Danish language.

%description i18n-da-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
duñskim.

%files i18n-da-gtk -f da.lang.gnome

%package i18n-de-gtk
Summary:	OpenOffice.org - interface in German language
Summary(pl):	OpenOffice.org - interfejs w jêzyku niemieckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-de

%description i18n-de-gtk
This package provides resources containing menus and dialogs in
German language.

%description i18n-de-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
niemieckim.

%files i18n-de-gtk -f de.lang.gnome

%package i18n-el-gtk
Summary:	OpenOffice.org - interface in Greek language
Summary(pl):	OpenOffice.org - interfejs w jêzyku greckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-el

%description i18n-el-gtk
This package provides resources containing menus and dialogs in
Greek language.

%description i18n-el-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
greckim.

%files i18n-el-gtk -f el.lang.gnome

%package i18n-es-gtk
Summary:	OpenOffice.org - interface in Spanish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hiszpañskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-es

%description i18n-es-gtk
This package provides resources containing menus and dialogs in
Spanish language.

%description i18n-es-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hiszpañskim.

%files i18n-es-gtk -f es.lang.gnome

%package i18n-et-gtk
Summary:	OpenOffice.org - interface in Estonian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku estoñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-et

%description i18n-et-gtk
This package provides resources containing menus and dialogs in
Estonian language.

%description i18n-et-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
estoñskim.

%files i18n-et-gtk -f et.lang.gnome

%package i18n-fi-gtk
Summary:	OpenOffice.org - interface in Finnish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku fiñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fi

%description i18n-fi-gtk
This package provides resources containing menus and dialogs in
Finnish language.

%description i18n-fi-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
fiñskim.

%files i18n-fi-gtk -f fi.lang.gnome

%package i18n-fo-gtk
Summary:	OpenOffice.org - interface in Faroese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku farerskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fo

%description i18n-fo-gtk
This package provides resources containing menus and dialogs in
Faroese language.

%description i18n-fo-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
farerskim.

#%files i18n-fo-gtk -f fo.lang.gnome

%package i18n-fr-gtk
Summary:	OpenOffice.org - interface in French language
Summary(pl):	OpenOffice.org - interfejs w jêzyku francuskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fr

%description i18n-fr-gtk
This package provides resources containing menus and dialogs in
French language.

%description i18n-fr-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
francuskim.

%files i18n-fr-gtk -f fr.lang.gnome

%package i18n-ga-gtk
Summary:	OpenOffice.org - interface in Irish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku irlandzkim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ga

%description i18n-ga-gtk
This package provides resources containing menus and dialogs in
Irish language.

%description i18n-ga-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
irlandzkim.

#%files i18n-ga-gtk -f ga.lang.gnome

%package i18n-gl-gtk
Summary:	OpenOffice.org - interface in Galician language
Summary(pl):	OpenOffice.org - interfejs w jêzyku galicyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-gl

%description i18n-gl-gtk
This package provides resources containing menus and dialogs in
Galician language.

%description i18n-gl-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
galicyjskim.

#%files i18n-gl-gtk -f gl.lang.gnome

%package i18n-he-gtk
Summary:	OpenOffice.org - interface in Hebrew language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hebrajskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-he

%description i18n-he-gtk
This package provides resources containing menus and dialogs in
Hebrew language.

%description i18n-he-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hebrajskim.

%files i18n-he-gtk -f he.lang.gnome

%package i18n-hi-gtk
Summary:	OpenOffice.org - interface in Hindi language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hindi
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hi

%description i18n-hi-gtk
This package provides resources containing menus and dialogs in
Hindi language.

%description i18n-hi-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hindi.

%files i18n-hi-gtk -f hi.lang.gnome

%package i18n-hr-gtk
Summary:	OpenOffice.org - interface in Croatian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku chorwackim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hr

%description i18n-hr-gtk
This package provides resources containing menus and dialogs in
Croatian language.

%description i18n-hr-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chorwackim.

#%files i18n-hr-gtk -f hr.lang.gnome

%package i18n-hu-gtk
Summary:	OpenOffice.org - interface in Hungarian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku wêgierskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hu

%description i18n-hu-gtk
This package provides resources containing menus and dialogs in
Hungarian language.

%description i18n-hu-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
wêgierskim.

%files i18n-hu-gtk -f hu.lang.gnome

%package i18n-ia-gtk
Summary:	OpenOffice.org - interface in Interlingua language
Summary(pl):	OpenOffice.org - interfejs w jêzyku interlingua
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ia

%description i18n-ia-gtk
This package provides resources containing menus and dialogs in
Interlingua language.

%description i18n-ia-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
interlingua.

#%files i18n-ia-gtk -f ia.lang.gnome

%package i18n-id-gtk
Summary:	OpenOffice.org - interface in Indonesian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku indonezyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-id

%description i18n-id-gtk
This package provides resources containing menus and dialogs in
Indonesian language.

%description i18n-id-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
indonezyjskim.

#%files i18n-id-gtk -f id.lang.gnome

%package i18n-it-gtk
Summary:	OpenOffice.org - interface in Italian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku w³oskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-it

%description i18n-it-gtk
This package provides resources containing menus and dialogs in
Italian language.

%description i18n-it-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
w³oskim.

%files i18n-it-gtk -f it.lang.gnome

%package i18n-ja-gtk
Summary:	OpenOffice.org - interface in Japan language
Summary(pl):	OpenOffice.org - interfejs w jêzyku japoñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ja

%description i18n-ja-gtk
This package provides resources containing menus and dialogs in
Japan language.

%description i18n-ja-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
japoñskim.

%files i18n-ja-gtk -f ja.lang.gnome

%package i18n-ko-gtk
Summary:	OpenOffice.org - interface in Korean language
Summary(pl):	OpenOffice.org - interfejs w jêzyku koreañskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ko

%description i18n-ko-gtk
This package provides resources containing menus and dialogs in
Korean language.

%description i18n-ko-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
koreañskim.

%files i18n-ko-gtk -f ko.lang.gnome

%package i18n-la-gtk
Summary:	OpenOffice.org - interface in Latin language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ³aciñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-la

%description i18n-la-gtk
This package provides resources containing menus and dialogs in
Latin language.

%description i18n-la-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
³aciñskim.

#%files i18n-la-gtk -f la.lang.gnome

%package i18n-lt-gtk
Summary:	OpenOffice.org - interface in Lithuanian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku litewskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-lt

%description i18n-lt-gtk
This package provides resources containing menus and dialogs in
Lithuanian language.

%description i18n-lt-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
litewskim.

#%files i18n-lt-gtk -f lt.lang.gnome

%package i18n-med-gtk
Summary:	OpenOffice.org - interface in Melpa language
Summary(pl):	OpenOffice.org - interfejs w jêzyku melpa
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-med

%description i18n-med-gtk
This package provides resources containing menus and dialogs in
Melpa language.

%description i18n-med-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
melpa.

#%files i18n-med-gtk -f med.lang.gnome

%package i18n-mi-gtk
Summary:	OpenOffice.org - interface in Maori language
Summary(pl):	OpenOffice.org - interfejs w jêzyku maoryjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-mi

%description i18n-mi-gtk
This package provides resources containing menus and dialogs in
Maori language.

%description i18n-mi-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
maoryjskim.

#%files i18n-mi-gtk -f mi.lang.gnome

%package i18n-ms-gtk
Summary:	OpenOffice.org - interface in Malay language
Summary(pl):	OpenOffice.org - interfejs w jêzyku malajskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ms

%description i18n-ms-gtk
This package provides resources containing menus and dialogs in
Malay language.

%description i18n-ms-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
malajskim.

#%files i18n-ms-gtk -f ms.lang.gnome

%package i18n-nb-gtk
Summary:	OpenOffice.org - interface in Norwegian Bokmaal language
Summary(pl):	OpenOffice.org - interfejs w jêzyku norweskim (odmiana Bokmaal)
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nb

%description i18n-nb-gtk
This package provides resources containing menus and dialogs in
Norwegian Bokmaal language.

%description i18n-nb-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
norweskim w odmianie Bokmaal.

%files i18n-nb-gtk -f nb.lang.gnome

%package i18n-nl-gtk
Summary:	OpenOffice.org - interface in Dutch language
Summary(pl):	OpenOffice.org - interfejs w jêzyku holenderskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nl

%description i18n-nl-gtk
This package provides resources containing menus and dialogs in
Dutch language.

%description i18n-nl-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
holenderskim.

%files i18n-nl-gtk -f nl.lang.gnome

%package i18n-nn-gtk
Summary:	OpenOffice.org - interface in Norwegian Nynorsk language
Summary(pl):	OpenOffice.org - interfejs w jêzyku norweskim (odmiana Nynorsk)
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nn

%description i18n-nn-gtk
This package provides resources containing menus and dialogs in
Norwegian Nynorsk language.

%description i18n-nn-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
norweskim w odmianie Nynorsk.

%files i18n-nn-gtk -f nn.lang.gnome

%package i18n-nso-gtk
Summary:	OpenOffice.org - interface in Northern Sotho language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ludu Soto
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nso

%description i18n-nso-gtk
This package provides resources containing menus and dialogs in
Northern Sotho language.

%description i18n-nso-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
ludu Soto.

%files i18n-nso-gtk -f ns.lang.gnome

%package i18n-pl-gtk
Summary:	OpenOffice.org - interface in Polish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku polskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pl

%description i18n-pl-gtk
This package provides resources containing menus and dialogs in
Polish language.

%description i18n-pl-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
polskim.

%files i18n-pl-gtk -f pl.lang.gnome

%package i18n-pt-gtk
Summary:	OpenOffice.org - interface in Portuguese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku portugalskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pt

%description i18n-pt-gtk
This package provides resources containing menus and dialogs in
Portuguese language.

%description i18n-pt-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
portugalskim.

%files i18n-pt-gtk -f pt.lang.gnome

%package i18n-pt_BR-gtk
Summary:	OpenOffice.org - interface in Brazilian Portuguese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku portugalskim dla Brazylii
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pt_BR

%description i18n-pt_BR-gtk
This package provides resources containing menus and dialogs in
Brazilian Portuguese language.

%description i18n-pt_BR-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
portugalskim dla Brazylii.

%files i18n-pt_BR-gtk -f pt-BR.lang.gnome

%package i18n-ro-gtk
Summary:	OpenOffice.org - interface in Romanian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku rumuñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ro

%description i18n-ro-gtk
This package provides resources containing menus and dialogs in
Romanian language.

%description i18n-ro-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
rumuñskim.

#%files i18n-ro-gtk -f ro.lang.gnome

%package i18n-ru-gtk
Summary:	OpenOffice.org - interface in Russian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku rosyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ru

%description i18n-ru-gtk
This package provides resources containing menus and dialogs in
Russian language.

%description i18n-ru-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
rosyjskim.

%files i18n-ru-gtk -f ru.lang.gnome

%package i18n-sk-gtk
Summary:	OpenOffice.org - interface in Slovak language
Summary(pl):	OpenOffice.org - interfejs w jêzyku s³owackim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sk

%description i18n-sk-gtk
This package provides resources containing menus and dialogs in
Slovak language.

%description i18n-sk-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
s³owackim.

%files i18n-sk-gtk -f sk.lang.gnome

%package i18n-sl-gtk
Summary:	OpenOffice.org - interface in Slovenian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku s³oweñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sl

%description i18n-sl-gtk
This package provides resources containing menus and dialogs in
Slovenian language.

%description i18n-sl-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
s³oweñskim.

%files i18n-sl-gtk -f sl.lang.gnome

%package i18n-sv-gtk
Summary:	OpenOffice.org - interface in Swedish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku szwedzkim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sv

%description i18n-sv-gtk
This package provides resources containing menus and dialogs in
Swedish language.

%description i18n-sv-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
szwedzkim.

%files i18n-sv-gtk -f sv.lang.gnome

%package i18n-tr-gtk
Summary:	OpenOffice.org - interface in Turkish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku tureckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-tr

%description i18n-tr-gtk
This package provides resources containing menus and dialogs in
Turkish language.

%description i18n-tr-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tureckim.

%files i18n-tr-gtk -f tr.lang.gnome

%package i18n-uk-gtk
Summary:	OpenOffice.org - interface in Ukrainian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ukraiñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-uk

%description i18n-uk-gtk
This package provides resources containing menus and dialogs in
Ukrainian language.

%description i18n-uk-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
ukraiñskim.

#%files i18n-uk-gtk -f uk.lang.gnome

%package i18n-zh_CN-gtk
Summary:	OpenOffice.org - interface in Chinese language for China
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim dla Chin
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_CN

%description i18n-zh_CN-gtk
This package provides resources containing menus and dialogs in
Chinese language for China.

%description i18n-zh_CN-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim dla Chin.

%files i18n-zh_CN-gtk -f zh-CN.lang.gnome

%package i18n-zh_TW-gtk
Summary:	OpenOffice.org - interface in Chinese language for Taiwan
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim dla Tajwanu
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_TW

%description i18n-zh_TW-gtk
This package provides resources containing menus and dialogs in
Chinese language for Taiwan.

%description i18n-zh_TW-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim dla Tajwanu.

%files i18n-zh_TW-gtk -f zh-TW.lang.gnome

%package i18n-zu-gtk
Summary:	OpenOffice.org - interface in Zulu language
Summary(pl):	OpenOffice.org - interfejs w jêzyku zuluskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zu

%description i18n-zu-gtk
This package provides resources containing menus and dialogs in
Zulu language.

%description i18n-zu-gtk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
zuluskim.

%files i18n-zu-gtk -f zu.lang.gnome

%package i18n-af-kde
Summary:	OpenOffice.org - interface in Afrikaans language
Summary(pl):	OpenOffice.org - interfejs w jêzyku afrykanerskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-af

%description i18n-af-kde
This package provides resources containing menus and dialogs in
Afrikaans language.

%description i18n-af-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
afrykanerskim.

%files i18n-af-kde -f af.lang.kde

%package i18n-ar-kde
Summary:	OpenOffice.org - interface in Arabic language
Summary(pl):	OpenOffice.org - interfejs w jêzyku arabskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ar

%description i18n-ar-kde
This package provides resources containing menus and dialogs in
Arabic language.

%description i18n-ar-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
arabskim.

%files i18n-ar-kde -f ar.lang.kde

%package i18n-bg-kde
Summary:	OpenOffice.org - interface in Bulgarian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku bu³garskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-bg

%description i18n-bg-kde
This package provides resources containing menus and dialogs in
Bulgarian language.

%description i18n-bg-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
bu³garskim.

#%files i18n-bg-kde -f bg.lang.kde

%package i18n-ca-kde
Summary:	OpenOffice.org - interface in Catalan language
Summary(pl):	OpenOffice.org - interfejs w jêzyku kataloñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ca

%description i18n-ca-kde
This package provides resources containing menus and dialogs in
Catalan language.

%description i18n-ca-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
kataloñskim.

%files i18n-ca-kde -f ca.lang.kde

%package i18n-cs-kde
Summary:	OpenOffice.org - interface in Czech language
Summary(pl):	OpenOffice.org - interfejs w jêzyku czeskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-cs

%description i18n-cs-kde
This package provides resources containing menus and dialogs in
Czech language.

%description i18n-cs-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
czeskim.

%files i18n-cs-kde -f cs.lang.kde

%package i18n-cy-kde
Summary:	OpenOffice.org - interface in Cymraeg language
Summary(pl):	OpenOffice.org - interfejs w jêzyku walijskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-cy

%description i18n-cy-kde
This package provides resources containing menus and dialogs in
Cymraeg language.

%description i18n-cy-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
walijskim.

%files i18n-cy-kde -f cy.lang.kde

%package i18n-da-kde
Summary:	OpenOffice.org - interface in Danish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku duñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-da

%description i18n-da-kde
This package provides resources containing menus and dialogs in
Danish language.

%description i18n-da-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
duñskim.

%files i18n-da-kde -f da.lang.kde

%package i18n-de-kde
Summary:	OpenOffice.org - interface in German language
Summary(pl):	OpenOffice.org - interfejs w jêzyku niemieckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-de

%description i18n-de-kde
This package provides resources containing menus and dialogs in
German language.

%description i18n-de-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
niemieckim.

%files i18n-de-kde -f de.lang.kde

%package i18n-el-kde
Summary:	OpenOffice.org - interface in Greek language
Summary(pl):	OpenOffice.org - interfejs w jêzyku greckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-el

%description i18n-el-kde
This package provides resources containing menus and dialogs in
Greek language.

%description i18n-el-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
greckim.

%files i18n-el-kde -f el.lang.kde

%package i18n-es-kde
Summary:	OpenOffice.org - interface in Spanish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hiszpañskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-es

%description i18n-es-kde
This package provides resources containing menus and dialogs in
Spanish language.

%description i18n-es-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hiszpañskim.

%files i18n-es-kde -f es.lang.kde

%package i18n-et-kde
Summary:	OpenOffice.org - interface in Estonian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku estoñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-et

%description i18n-et-kde
This package provides resources containing menus and dialogs in
Estonian language.

%description i18n-et-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
estoñskim.

%files i18n-et-kde -f et.lang.kde

%package i18n-fi-kde
Summary:	OpenOffice.org - interface in Finnish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku fiñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fi

%description i18n-fi-kde
This package provides resources containing menus and dialogs in
Finnish language.

%description i18n-fi-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
fiñskim.

%files i18n-fi-kde -f fi.lang.kde

%package i18n-fo-kde
Summary:	OpenOffice.org - interface in Faroese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku farerskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fo

%description i18n-fo-kde
This package provides resources containing menus and dialogs in
Faroese language.

%description i18n-fo-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
farerskim.

#%files i18n-fo-kde -f fo.lang.kde

%package i18n-fr-kde
Summary:	OpenOffice.org - interface in French language
Summary(pl):	OpenOffice.org - interfejs w jêzyku francuskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-fr

%description i18n-fr-kde
This package provides resources containing menus and dialogs in
French language.

%description i18n-fr-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
francuskim.

%files i18n-fr-kde -f fr.lang.kde

%package i18n-ga-kde
Summary:	OpenOffice.org - interface in Irish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku irlandzkim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ga

%description i18n-ga-kde
This package provides resources containing menus and dialogs in
Irish language.

%description i18n-ga-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
irlandzkim.

#%files i18n-ga-kde -f ga.lang.kde

%package i18n-gl-kde
Summary:	OpenOffice.org - interface in Galician language
Summary(pl):	OpenOffice.org - interfejs w jêzyku galicyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-gl

%description i18n-gl-kde
This package provides resources containing menus and dialogs in
Galician language.

%description i18n-gl-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
galicyjskim.

#%files i18n-gl-kde -f gl.lang.kde

%package i18n-he-kde
Summary:	OpenOffice.org - interface in Hebrew language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hebrajskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-he

%description i18n-he-kde
This package provides resources containing menus and dialogs in
Hebrew language.

%description i18n-he-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hebrajskim.

%files i18n-he-kde -f he.lang.kde

%package i18n-hi-kde
Summary:	OpenOffice.org - interface in Hindi language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hindi
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hi

%description i18n-hi-kde
This package provides resources containing menus and dialogs in
Hindi language.

%description i18n-hi-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hindi.

%files i18n-hi-kde -f hi.lang.kde

%package i18n-hr-kde
Summary:	OpenOffice.org - interface in Croatian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku chorwackim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hr

%description i18n-hr-kde
This package provides resources containing menus and dialogs in
Croatian language.

%description i18n-hr-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chorwackim.

#%files i18n-hr-kde -f hr.lang.kde

%package i18n-hu-kde
Summary:	OpenOffice.org - interface in Hungarian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku wêgierskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-hu

%description i18n-hu-kde
This package provides resources containing menus and dialogs in
Hungarian language.

%description i18n-hu-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
wêgierskim.

%files i18n-hu-kde -f hu.lang.kde

%package i18n-ia-kde
Summary:	OpenOffice.org - interface in Interlingua language
Summary(pl):	OpenOffice.org - interfejs w jêzyku interlingua
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ia

%description i18n-ia-kde
This package provides resources containing menus and dialogs in
Interlingua language.

%description i18n-ia-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
interlingua.

#%files i18n-ia-kde -f ia.lang.kde

%package i18n-id-kde
Summary:	OpenOffice.org - interface in Indonesian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku indonezyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-id

%description i18n-id-kde
This package provides resources containing menus and dialogs in
Indonesian language.

%description i18n-id-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
indonezyjskim.

#%files i18n-id-kde -f id.lang.kde

%package i18n-it-kde
Summary:	OpenOffice.org - interface in Italian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku w³oskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-it

%description i18n-it-kde
This package provides resources containing menus and dialogs in
Italian language.

%description i18n-it-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
w³oskim.

%files i18n-it-kde -f it.lang.kde

%package i18n-ja-kde
Summary:	OpenOffice.org - interface in Japan language
Summary(pl):	OpenOffice.org - interfejs w jêzyku japoñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ja

%description i18n-ja-kde
This package provides resources containing menus and dialogs in
Japan language.

%description i18n-ja-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
japoñskim.

%files i18n-ja-kde -f ja.lang.kde

%package i18n-ko-kde
Summary:	OpenOffice.org - interface in Korean language
Summary(pl):	OpenOffice.org - interfejs w jêzyku koreañskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ko

%description i18n-ko-kde
This package provides resources containing menus and dialogs in
Korean language.

%description i18n-ko-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
koreañskim.

%files i18n-ko-kde -f ko.lang.kde

%package i18n-la-kde
Summary:	OpenOffice.org - interface in Latin language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ³aciñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-la

%description i18n-la-kde
This package provides resources containing menus and dialogs in
Latin language.

%description i18n-la-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
³aciñskim.

#%files i18n-la-kde -f la.lang.kde

%package i18n-lt-kde
Summary:	OpenOffice.org - interface in Lithuanian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku litewskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-lt

%description i18n-lt-kde
This package provides resources containing menus and dialogs in
Lithuanian language.

%description i18n-lt-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
litewskim.

#%files i18n-lt-kde -f lt.lang.kde

%package i18n-med-kde
Summary:	OpenOffice.org - interface in Melpa language
Summary(pl):	OpenOffice.org - interfejs w jêzyku melpa
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-med

%description i18n-med-kde
This package provides resources containing menus and dialogs in
Melpa language.

%description i18n-med-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
melpa.

#%files i18n-med-kde -f med.lang.kde

%package i18n-mi-kde
Summary:	OpenOffice.org - interface in Maori language
Summary(pl):	OpenOffice.org - interfejs w jêzyku maoryjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-mi

%description i18n-mi-kde
This package provides resources containing menus and dialogs in
Maori language.

%description i18n-mi-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
maoryjskim.

#%files i18n-mi-kde -f mi.lang.kde

%package i18n-ms-kde
Summary:	OpenOffice.org - interface in Malay language
Summary(pl):	OpenOffice.org - interfejs w jêzyku malajskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ms

%description i18n-ms-kde
This package provides resources containing menus and dialogs in
Malay language.

%description i18n-ms-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
malajskim.

#%files i18n-ms-kde -f ms.lang.kde

%package i18n-nb-kde
Summary:	OpenOffice.org - interface in Norwegian Bokmaal language
Summary(pl):	OpenOffice.org - interfejs w jêzyku norweskim (odmiana Bokmaal)
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nb

%description i18n-nb-kde
This package provides resources containing menus and dialogs in
Norwegian Bokmaal language.

%description i18n-nb-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
norweskim w odmianie Bokmaal.

%files i18n-nb-kde -f nb.lang.kde

%package i18n-nl-kde
Summary:	OpenOffice.org - interface in Dutch language
Summary(pl):	OpenOffice.org - interfejs w jêzyku holenderskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nl

%description i18n-nl-kde
This package provides resources containing menus and dialogs in
Dutch language.

%description i18n-nl-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
holenderskim.

%files i18n-nl-kde -f nl.lang.kde

%package i18n-nn-kde
Summary:	OpenOffice.org - interface in Norwegian Nynorsk language
Summary(pl):	OpenOffice.org - interfejs w jêzyku norweskim (odmiana Nynorsk)
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nn

%description i18n-nn-kde
This package provides resources containing menus and dialogs in
Norwegian Nynorsk language.

%description i18n-nn-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
norweskim w odmianie Nynorsk.

%files i18n-nn-kde -f nn.lang.kde

%package i18n-nso-kde
Summary:	OpenOffice.org - interface in Northern Sotho language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ludu Soto
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-nso

%description i18n-nso-kde
This package provides resources containing menus and dialogs in
Northern Sotho language.

%description i18n-nso-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
ludu Soto.

%files i18n-nso-kde -f ns.lang.kde

%package i18n-pl-kde
Summary:	OpenOffice.org - interface in Polish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku polskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pl

%description i18n-pl-kde
This package provides resources containing menus and dialogs in
Polish language.

%description i18n-pl-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
polskim.

%files i18n-pl-kde -f pl.lang.kde

%package i18n-pt-kde
Summary:	OpenOffice.org - interface in Portuguese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku portugalskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pt

%description i18n-pt-kde
This package provides resources containing menus and dialogs in
Portuguese language.

%description i18n-pt-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
portugalskim.

%files i18n-pt-kde -f pt.lang.kde

%package i18n-pt_BR-kde
Summary:	OpenOffice.org - interface in Brazilian Portuguese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku portugalskim dla Brazylii
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-pt_BR

%description i18n-pt_BR-kde
This package provides resources containing menus and dialogs in
Brazilian Portuguese language.

%description i18n-pt_BR-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
portugalskim dla Brazylii.

%files i18n-pt_BR-kde -f pt-BR.lang.kde

%package i18n-ro-kde
Summary:	OpenOffice.org - interface in Romanian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku rumuñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ro

%description i18n-ro-kde
This package provides resources containing menus and dialogs in
Romanian language.

%description i18n-ro-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
rumuñskim.

#%files i18n-ro-kde -f ro.lang.kde

%package i18n-ru-kde
Summary:	OpenOffice.org - interface in Russian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku rosyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-ru

%description i18n-ru-kde
This package provides resources containing menus and dialogs in
Russian language.

%description i18n-ru-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
rosyjskim.

%files i18n-ru-kde -f ru.lang.kde

%package i18n-sk-kde
Summary:	OpenOffice.org - interface in Slovak language
Summary(pl):	OpenOffice.org - interfejs w jêzyku s³owackim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sk

%description i18n-sk-kde
This package provides resources containing menus and dialogs in
Slovak language.

%description i18n-sk-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
s³owackim.

%files i18n-sk-kde -f sk.lang.kde

%package i18n-sl-kde
Summary:	OpenOffice.org - interface in Slovenian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku s³oweñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sl

%description i18n-sl-kde
This package provides resources containing menus and dialogs in
Slovenian language.

%description i18n-sl-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
s³oweñskim.

%files i18n-sl-kde -f sl.lang.kde

%package i18n-sv-kde
Summary:	OpenOffice.org - interface in Swedish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku szwedzkim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-sv

%description i18n-sv-kde
This package provides resources containing menus and dialogs in
Swedish language.

%description i18n-sv-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
szwedzkim.

%files i18n-sv-kde -f sv.lang.kde

%package i18n-tr-kde
Summary:	OpenOffice.org - interface in Turkish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku tureckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-tr

%description i18n-tr-kde
This package provides resources containing menus and dialogs in
Turkish language.

%description i18n-tr-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tureckim.

%files i18n-tr-kde -f tr.lang.kde

%package i18n-uk-kde
Summary:	OpenOffice.org - interface in Ukrainian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ukraiñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-uk

%description i18n-uk-kde
This package provides resources containing menus and dialogs in
Ukrainian language.

%description i18n-uk-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
ukraiñskim.

#%files i18n-uk-kde -f uk.lang.kde

%package i18n-zh_CN-kde
Summary:	OpenOffice.org - interface in Chinese language for China
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim dla Chin
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_CN

%description i18n-zh_CN-kde
This package provides resources containing menus and dialogs in
Chinese language for China.

%description i18n-zh_CN-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim dla Chin.

%files i18n-zh_CN-kde -f zh-CN.lang.kde

%package i18n-zh_TW-kde
Summary:	OpenOffice.org - interface in Chinese language for Taiwan
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim dla Tajwanu
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zh
Obsoletes:	openoffice-i18n-zh_TW

%description i18n-zh_TW-kde
This package provides resources containing menus and dialogs in
Chinese language for Taiwan.

%description i18n-zh_TW-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim dla Tajwanu.

%files i18n-zh_TW-kde -f zh-TW.lang.kde

%package i18n-zu-kde
Summary:	OpenOffice.org - interface in Zulu language
Summary(pl):	OpenOffice.org - interfejs w jêzyku zuluskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	openoffice-i18n-zu

%description i18n-zu-kde
This package provides resources containing menus and dialogs in
Zulu language.

%description i18n-zu-kde -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
zuluskim.

%files i18n-zu-kde -f zu.lang.kde

%prep
%setup -q -n ooo-build-%{ooobver}
%patch0 -p1
%patch1 -p1 

%if %{with vfs}
%patch2 -p1
%endif

install -d src
# sources, icons, KDE_icons
ln -sf %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} src
# help files
ln -sf %{SOURCE400} %{SOURCE401} %{SOURCE402} %{SOURCE403} %{SOURCE404} \
	%{SOURCE405} %{SOURCE406} %{SOURCE407} %{SOURCE408} %{SOURCE409} \
	%{SOURCE410} %{SOURCE411} %{SOURCE412} src

# we keep these in ooo-build repository
#ln -s %{SOURCE20} src/openabout_pld.bmp
#ln -s %{SOURCE21} src/openintro_pld.bmp

%build
# Make sure we have /proc mounted - otherwise idlc will fail later.
if [ ! -r /proc/version ]; then
	echo "You need to have /proc mounted in order to build this package!"
	exit 1
fi

CC="%{__cc}"
CXX="%{__cxx}"
ENVCFLAGS="%{rpmcflags}"
ENVCFLAGSCXX="%{rpmcflags}"
DESTDIR=$RPM_BUILD_ROOT
IGNORE_MANIFEST_CHANGES=1
export CC CXX ENVCFLAGS ENVCFLAGSCXX DESTDIR IGNORE_MANIFEST_CHANGES

%if %{with java}
GCJ=gcj
JAVA_HOME=%{_libdir}/java
DB_JAR="%{_javadir}/db.jar"
export JAVA_HOME DB_JAR GCJ
%endif

RPM_BUILD_NR_THREADS="%(echo "%{__make}" | sed -e 's#.*-j\([[:space:]]*[0-9]\+\)#\1#g' | xargs)"
[ "$RPM_BUILD_NR_THREADS" = "%{__make}" ] && RPM_BUILD_NR_THREADS=1

CONFOPTS=" \
%ifarch ppc
	--with-arch=ppc \
%endif
%ifarch sparc sparcv9
	--with-arch=sparc \
%endif
	--with-tag=OOO_%{dfullver} \
	--with-ccache-allowed \
	--with-system-gcc \
	--with-system-zlib \
	--with-system-sane-headers \
	--with-system-x11-extensions-headers \
	--with-system-unixodbc-headers \
	--with-system-db \
	--with-system-curl \
	--with-system-freetype \
	--with-system-nas \
	--with-system-xrender \
	--with-dynamic-xinerama \
	--with-vendor="PLD" \
	--with-distro="PLD" \
	--with-icons=gnome,kde \
	--enable-gtk \
	--enable-kde \
	--with-installed-ooo-dirname=%{name} \
%if %{with java}
	--enable-java \
	--with-jdk-home=$JAVA_HOME \
%else
	--disable-java \
%endif
	--with-python=%{_bindir}/python \
	--with-stlport4-home=/usr \
	--with-lang=ALL \
	--with-x \
	--without-fonts \
	--disable-fontooo \
	--enable-fontconfig \
	--enable-libsn \
	--enable-libart \
	--disable-mozilla \
	--disable-rpath \
%if 0%{?debug:1}
	--enable-debug \
	--enable-crashdump=yes \
	--enable-symbols=FULL \
%else
	--enable-crashdump=no \
	--disable-symbols \
%endif
	--with-num-jobs=$RPM_BUILD_NR_THREADS
"

# for cvs snaps
[ -x ./autogen.sh ] && ./autogen.sh $CONFOPTS

# build-ooo script will pickup these
CONFIGURE_OPTIONS="$CONFOPTS"; export CONFIGURE_OPTIONS

# main build
%configure \
	$CONFOPTS

# this limits processing some files but doesn't limit parallel build
# processes of main OOo build (since OOo uses it's own build system)
%{__make} -j1

# hack for parallel build
if [ "$RPM_BUILD_NCPUS" -gt 1 ]; then
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
sed -i -e 's#^BUILD_NCPUS=.*#BUILD_NCPUS=1#g' bin/setup

DESTDIR=$RPM_BUILD_ROOT; export DESTDIR
TMP="%{tmpdir}"; export TMP
TEMP="%{tmpdir}"; export TEMP

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
sed -e 's#DESTINATIONPATH=.*#DESTINATIONPATH=<home>/.openoffice#g' etc/redhat-autoresponse.conf > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/autoresponse.conf

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE10} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE11} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE12} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE13} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE14} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE15} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE16} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE17} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE18} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE19} $RPM_BUILD_ROOT%{_desktopdir}

# Add in the regcomp tool since some people need it for 3rd party add-ons
cp -f build/OOO_%{dfullver}/solver/%{subver}/unxlng*.pro/bin/regcomp $RPM_BUILD_ROOT%{_libdir}/%{name}/program

# mimelnk, icons
install -d $RPM_BUILD_ROOT{%{_datadir}/mimelnk/application,%{_pixmapsdir}}

cp -a build/OOO_%{dfullver}/sysui/desktop/gnome/icons/*/*.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a build/OOO_%{dfullver}/sysui/desktop/gnome/icons/*.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a build/OOO_%{dfullver}/sysui/desktop/kde/vnd*.desktop $RPM_BUILD_ROOT%{_datadir}/mimelnk/application

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
install fonts/opens___.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

# We don't need spadmin (gtk) or the setup application
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/setup
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/crash_report.bin
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/openoffice-setup.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/openoffice-printeradmin.desktop

rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome

#rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/gnomeint

# some libs creep in somehow
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libstl*.so*

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
langlist="`bin/openoffice-xlate-lang -i all`"

for lang in $langlist; do
	echo "%%defattr(644,root,root,755)" > ${lang}.lang

	# help files
	if [ -f build/help_${lang}_list.txt ]; then
		cat build/help_${lang}_list.txt >> ${lang}.lang
	fi

	lfile="build/lang_${lang}_list.txt"
	if [ -f ${lfile} ]; then
		longlang="`bin/openoffice-xlate-lang -l ${lang}`"
		# share/*/${longlang}
		grep "^%%dir.*/${longlang}/\$" ${lfile} > tmp.lang
		# share/registry/res/${lang} (but en-US for en)
		grep "^%%dir.*/res/${lang}[^/]*/\$" ${lfile} >> tmp.lang
		# ... translate %dir into whole tree, handle special wordbook/english case
		sed -e 's,^%%dir ,,;s,\(wordbook/english/\)$,\1soffice.dic,;s,/$,,' tmp.lang >> ${lang}.lang
		# share/autocorr/acor${somecodes}.dat (if exist)
		grep '/autocorr/acor.*dat$' ${lfile} >> ${lang}.lang || :
		# user/config/* (if exist, without parent directory)
		grep '/user/config/..*' ${lfile} >> ${lang}.lang || :
		cp ${lang}.lang ${lang}.lang.gnome
		cp ${lang}.lang ${lang}.lang.kde
		# program/resource.*/*${code}.res (for kde and gnome versions)
 		grep '/program/resource.gnome/.*res$' ${lfile} >> ${lang}.lang.gnome
		grep '/program/resource.kde/.*res$' ${lfile} >> ${lang}.lang.kde
	fi
done

find $RPM_BUILD_ROOT -type f -name '*.so' -exec chmod 755 "{}" ";"
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%post libs
fontpostinst TTF

%postun libs
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc %{_libdir}/%{name}/LICENSE*
%doc %{_libdir}/%{name}/*README*

%dir %{_sysconfdir}/openoffice
%config %{_sysconfdir}/openoffice/autoresponse.conf

%attr(755,root,root) %{_libdir}/%{name}/install-dict

%{_libdir}/%{name}/program/*.rdb
%{_libdir}/%{name}/program/*.bmp
%{_libdir}/%{name}/program/user_registry.xsl
%{_libdir}/%{name}/program/sofficerc
%{_libdir}/%{name}/program/unorc
%{_libdir}/%{name}/program/bootstraprc
%{_libdir}/%{name}/program/configmgrrc
%{_libdir}/%{name}/program/instdb.ins

%dir %{_libdir}/%{name}/help
#%{_libdir}/%{name}/help/en
%{_libdir}/%{name}/help/main_transform.xsl

%dir %{_libdir}/%{name}/share
%dir %{_libdir}/%{name}/share/autocorr
%dir %{_libdir}/%{name}/share/autotext
%{_libdir}/%{name}/share/basic
%dir %{_libdir}/%{name}/share/bookmark
%dir %{_libdir}/%{name}/share/config
%{_libdir}/%{name}/share/config/symbol
%{_libdir}/%{name}/share/config/webcast
%{_libdir}/%{name}/share/config/*.xpm
%dir %{_libdir}/%{name}/share/database
%dir %{_libdir}/%{name}/share/dict
%dir %{_libdir}/%{name}/share/dict/ooo
%{_libdir}/%{name}/share/dtd
%{_libdir}/%{name}/share/fonts
%{_libdir}/%{name}/share/gallery
%{_libdir}/%{name}/share/psprint
%dir %{_libdir}/%{name}/share/samples
%dir %{_libdir}/%{name}/share/template
%dir %{_libdir}/%{name}/share/wordbook
%dir %{_libdir}/%{name}/share/wordbook/english
%{_libdir}/%{name}/share/wordbook/english/sun.dic
%{_libdir}/%{name}/share/readme

%dir %{_libdir}/%{name}/share/registry
%dir %{_libdir}/%{name}/share/registry/res
%{_libdir}/%{name}/share/registry/data
%{_libdir}/%{name}/share/registry/schema

#%{_libdir}/%{name}/share/autotext/english
# XXX: in ooo-build only template/english/wizard/bitmaps is in main?
#%{_libdir}/%{name}/share/template/english
%ghost %{_libdir}/%{name}/share/dict/ooo/dictionary.lst

%dir %{_libdir}/%{name}/user
%dir %{_libdir}/%{name}/user/autotext
%{_libdir}/%{name}/user/basic
%dir %{_libdir}/%{name}/user/config
%{_libdir}/%{name}/user/config/autotbl.fmt
%{_libdir}/%{name}/user/config/cmyk.soc
%{_libdir}/%{name}/user/config/gallery.soc
%{_libdir}/%{name}/user/config/html.soc
%{_libdir}/%{name}/user/config/standard.so?
%{_libdir}/%{name}/user/config/sun-color.soc
%{_libdir}/%{name}/user/config/web.soc
%{_libdir}/%{name}/user/database
%{_libdir}/%{name}/user/gallery
%{_libdir}/%{name}/user/psprint

#%{_libdir}/%{name}/user/autotext/english

# Programs
%attr(755,root,root) %{_bindir}/oo*
%attr(755,root,root) %{_sbindir}/oopadmin
%attr(755,root,root) %{_libdir}/%{name}/spadmin
%attr(755,root,root) %{_libdir}/%{name}/program/*.bin
%attr(755,root,root) %{_libdir}/%{name}/program/fromtemplate
%attr(755,root,root) %{_libdir}/%{name}/program/mozwrapper
%attr(755,root,root) %{_libdir}/%{name}/program/nswrapper
%attr(755,root,root) %{_libdir}/%{name}/program/ooovirg
%attr(755,root,root) %{_libdir}/%{name}/program/pagein*
%attr(755,root,root) %{_libdir}/%{name}/program/python.sh
%attr(755,root,root) %{_libdir}/%{name}/program/pythonloader.unorc
%attr(755,root,root) %{_libdir}/%{name}/program/pyunorc
%attr(755,root,root) %{_libdir}/%{name}/program/regcomp
%attr(755,root,root) %{_libdir}/%{name}/program/sagenda
%attr(755,root,root) %{_libdir}/%{name}/program/scalc
%attr(755,root,root) %{_libdir}/%{name}/program/sdraw
%attr(755,root,root) %{_libdir}/%{name}/program/setup
%{_libdir}/%{name}/program/setuprc
%attr(755,root,root) %{_libdir}/%{name}/program/sfax
%attr(755,root,root) %{_libdir}/%{name}/program/simpress
%attr(755,root,root) %{_libdir}/%{name}/program/slabel
%attr(755,root,root) %{_libdir}/%{name}/program/sletter
%attr(755,root,root) %{_libdir}/%{name}/program/smaster
%attr(755,root,root) %{_libdir}/%{name}/program/smath
%attr(755,root,root) %{_libdir}/%{name}/program/smemo
%attr(755,root,root) %{_libdir}/%{name}/program/soffice
%attr(755,root,root) %{_libdir}/%{name}/program/spadmin
%attr(755,root,root) %{_libdir}/%{name}/program/svcard
%attr(755,root,root) %{_libdir}/%{name}/program/sweb
%attr(755,root,root) %{_libdir}/%{name}/program/swriter
%attr(755,root,root) %{_libdir}/%{name}/program/*.py

%if %{with java}
%attr(755,root,root) %{_sbindir}/oojvmsetup
%attr(755,root,root) %{_libdir}/%{name}/program/javaldx
%attr(755,root,root) %{_libdir}/%{name}/program/jvmsetup
%{_libdir}/%{name}/program/classes
%{_libdir}/%{name}/share/xslt
%endif

%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/o*.1*

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/program
%dir %{_libdir}/%{name}/program/filter

%attr(755,root,root) %{_libdir}/%{name}/program/*.so
%exclude %{_libdir}/%{name}/program/libvclplug_gtk*.so
%exclude %{_libdir}/%{name}/program/libvclplug_kde*.so
%exclude %{_libdir}/%{name}/program/libfps_kde.so
%exclude %{_libdir}/%{name}/program/libfps_gnome.so
%attr(755,root,root) %{_libdir}/%{name}/program/*.so.*
%attr(755,root,root) %{_libdir}/%{name}/program/filter/*.so

%{_fontsdir}/TTF/*.ttf

%files libs-kde -f en.lang.kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/kdefilepicker
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_kde*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfps_kde.so
%dir %{_libdir}/%{name}/program/resource.kde

%files libs-gtk -f en.lang.gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libvclplug_gtk*.so
%attr(755,root,root) %{_libdir}/%{name}/program/libfps_gnome.so
%dir %{_libdir}/%{name}/program/resource.gnome
