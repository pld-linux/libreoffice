# NOTE:
#	- normal build requires little less than 4GB of disk space
#	- full debug build requires about 9GB of disk space
# TODO:
#	- drop requirement on XFree86-static
#	- drop requirement on nas-devel
#	- fix locale names and other locale related things
#	- --with-system-myspell + myspell package as in Debian
#	- --with-system-neon - check compilation (works with 0.23 but not 0.24)

# Conditional build:
%bcond_with	java		# Java support
%bcond_with	icons_ximian	# Ximian icons instead of KDE one

%define		ver		1.1
%define		rel		1
%define		ooobver		1.1.55
%define		subver		645
%define		fullver		%{ver}.%{rel}
%define		dfullver	%(echo %{fullver} | tr . _)
%define		specflags	-fno-strict-aliasing

Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	%{fullver}
Release:	5
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://ooo.ximian.com/packages/OOO_%{dfullver}/ooo-build-%{ooobver}.tar.gz
# Source0-md5:	79e885131d99a0a507eb3ffb7ecf19af
Source1:	http://ooo.ximian.com/packages/OOO_%{dfullver}/OOO_%{dfullver}.tar.bz2
# Source1-md5:	550381bc429fbbda54cb84758f14e010
Source2:	http://ooo.ximian.com/packages/ooo-icons-OOO_1_1-9.tar.gz
# Source2-md5:	32a0e62f89ef36a91437fc705fbe6440
Source3:	http://kde.openoffice.org/files/documents/159/1785/ooo-KDE_icons-OOO_1_1-0.1.tar.gz
# Source3-md5:	5157d4453d17cae586ce24989d34357a
Source10:	http://ep09.pld-linux.org/~adgor/pld/%{name}-desktopfiles-0.2.tar.bz2
# Source10-md5:	78ae3bef3e98f711b1afe9fb5717b42e

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
Source407:	%{cftp}/helpcontent/helpcontent_81_unix.tgz
# Source407-md5:	81b705057a0e14ebcbf02fac4762781a
Source408:	%{cftp}/helpcontent/helpcontent_82_unix.tgz
# Source408-md5:	3121fbd251176d7c7b6e33ecec744c65
Source409:	%{cftp}/helpcontent/helpcontent_86_unix.tgz
# Source409-md5:	aee37935139c5ccd4b6d8abdd2037c66
Source410:	%{cftp}/helpcontent/helpcontent_88_unix.tgz
# Source410-md5:	3b00571318e45965dee0545d86306d65

Patch0:		%{name}-rh-disable-spellcheck-all-langs.patch
Patch1:		%{name}-pld-config.patch
Patch2:		%{name}-pld-package-lang.patch
Patch3:		%{name}-pld-section.patch
Patch4:		%{name}-pld-leave-home.patch
Patch5:		%{name}-pld-parallel-build.patch
Patch6:		%{name}-pld-kde-nwf-fonts.patch

URL:		http://www.openoffice.org/
BuildRequires:	ImageMagick
BuildRequires:	STLport-devel >= 4.5.3-6
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-static
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison >= 1.875-4
BuildRequires:	cups-devel
BuildRequires:	curl-devel
BuildRequires:	db-cxx-devel
BuildRequires:	db-devel
BuildRequires:	/usr/bin/getopt
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
BuildRequires:	libstdc++-devel >= 3.2.1
BuildRequires:	nas-devel
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	python-devel
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
BuildConflicts:	java-sun = 1.4.2
Requires(post,postun):	fontpostinst
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n-en = %{epoch}:%{version}-%{release}
Requires:	cups-lib
Requires:	db
Requires:	db-cxx
Requires:	libstdc++ >= 3.2.1
Requires:	startup-notification
ExclusiveArch:	%{ix86} sparc ppc
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
Requires:	%{name}-libs-interface = %{epoch}:%{version}-%{release}

%description libs
OpenOffice.org productivity suite - shared libraries.

%description libs -l pl
Pakiet biurowy OpenOffice.org - biblioteki.

%package libs-kde
Summary:	OpenOffice.org KDE Interface
Summary(pl):	Interfejs KDE dla OpenOffice.org
Group:		X11/Libraries
Provides:	%{name}-libs-interface = %{epoch}:%{version}-%{release}
Provides:	libvcl%{subver}li.so
Obsoletes:	%{name}-libs-gtk
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires(post,preun):	%{name}-libs = %{epoch}:%{version}-%{release}

%description libs-kde
OpenOffice.org productivity suite - KDE Interface.

%description libs-kde -l pl
Pakiet biurowy OpenOffice.org - Interfejs KDE.

%package libs-gtk
Summary:	OpenOffice.org GTK Interface
Summary(pl):	Interfejs GTK dla OpenOffice.org
Group:		X11/Libraries
Provides:	%{name}-libs-interface = %{epoch}:%{version}-%{release}
Provides:	libvcl%{subver}li.so
Obsoletes:	%{name}-libs-kde
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires(post,preun):	%{name}-libs = %{epoch}:%{version}-%{release}

%description libs-gtk
OpenOffice.org productivity suite - GTK Interface.

%description libs-gtk -l pl
Pakiet biurowy OpenOffice.org - Interfejs GTK.

%package mimelinks
Summary:	OpenOffice.org mimelinks
Summary(pl):	Dowi±zania MIME dla OpenOffice.org
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdelibs
Conflicts:	kdelibs >= 9:3.1.9

%description mimelinks
OpenOffice.org mimelinks for KDE versions <= 3.1.5.

%description mimelinks -l pl
Dowi±zania MIME OpenOffice.org dla wersji KDE <= 3.1.5.

%package i18n-af
Summary:	OpenOffice.org - interface in Afrikaans language
Summary(pl):	OpenOffice.org - interfejs w jêzyku afrykanerskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-af
This package provides resources containing menus and dialogs in
Afrikaans language.

%description i18n-af -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
afrykanerskim.

#%files i18n-af -f af.lang

%package i18n-ar
Summary:	OpenOffice.org - interface in Arabic language
Summary(pl):	OpenOffice.org - interfejs w jêzyku arabskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ar
This package provides resources containing menus and dialogs in
Arabic language.

%description i18n-ar -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
arabskim.

%files i18n-ar -f ar.lang

%package i18n-bg
Summary:	OpenOffice.org - interface in Bulgarian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku bu³garskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-bg
This package provides resources containing menus and dialogs in
Bulgarian language.

%description i18n-bg -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
bu³garskim.

#%files i18n-bg -f bg.lang

%package i18n-ca
Summary:	OpenOffice.org - interface in Catalan language
Summary(pl):	OpenOffice.org - interfejs w jêzyku kataloñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ca
This package provides resources containing menus and dialogs in
Catalan language.

%description i18n-ca -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
kataloñskim.

%files i18n-ca -f ca.lang

%package i18n-cs
Summary:	OpenOffice.org - interface in Czech language
Summary(pl):	OpenOffice.org - interfejs w jêzyku czeskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-cs
This package provides resources containing menus and dialogs in
Czech language.

%description i18n-cs -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
czeskim.

%files i18n-cs -f cs.lang

%package i18n-cy
Summary:	OpenOffice.org - interface in Cymraeg language
Summary(pl):	OpenOffice.org - interfejs w jêzyku walijskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-cy
This package provides resources containing menus and dialogs in
Cymraeg language.

%description i18n-cy -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
walijskim.

#%files i18n-cy -f cy.lang

%package i18n-da
Summary:	OpenOffice.org - interface in Danish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku duñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-da
This package provides resources containing menus and dialogs in
Danish language.

%description i18n-da -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
duñskim.

%files i18n-da -f da.lang

%package i18n-de
Summary:	OpenOffice.org - interface in German language
Summary(pl):	OpenOffice.org - interfejs w jêzyku niemieckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-de
This package provides resources containing menus and dialogs in
German language.

%description i18n-de -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
niemieckim.

%files i18n-de -f de.lang

%package i18n-el
Summary:	OpenOffice.org - interface in Greek language
Summary(pl):	OpenOffice.org - interfejs w jêzyku greckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-el
This package provides resources containing menus and dialogs in
Greek language.

%description i18n-el -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
greckim.

%files i18n-el -f el.lang

%package i18n-en
Summary:	OpenOffice.org - interface in English language
Summary(pl):	OpenOffice.org - interfejs w jêzyku angielskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-en
This package provides resources containing menus and dialogs in
English language.

%description i18n-en -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
angielskim.

%files i18n-en -f en.lang

%package i18n-es
Summary:	OpenOffice.org - interface in Spanish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hiszpañskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-es
This package provides resources containing menus and dialogs in
Spanish language.

%description i18n-es -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hiszpañskim.

%files i18n-es -f es.lang

%package i18n-et
Summary:	OpenOffice.org - interface in Estonian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku estoñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-et
This package provides resources containing menus and dialogs in
Estonian language.

%description i18n-et -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
estoñskim.

%files i18n-et -f et.lang

%package i18n-fi
Summary:	OpenOffice.org - interface in Finnish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku fiñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-fi
This package provides resources containing menus and dialogs in
Finnish language.

%description i18n-fi -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
fiñskim.

%files i18n-fi -f fi.lang

%package i18n-fo
Summary:	OpenOffice.org - interface in Faroese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku farerskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-fo
This package provides resources containing menus and dialogs in
Faroese language.

%description i18n-fo -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
farerskim.

#%files i18n-fo -f fo.lang

%package i18n-fr
Summary:	OpenOffice.org - interface in French language
Summary(pl):	OpenOffice.org - interfejs w jêzyku francuskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-fr
This package provides resources containing menus and dialogs in
French language.

%description i18n-fr -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
francuskim.

%files i18n-fr -f fr.lang

%package i18n-ga
Summary:	OpenOffice.org - interface in Irish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku irlandzkim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ga
This package provides resources containing menus and dialogs in
Irish language.

%description i18n-ga -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
irlandzkim.

#%files i18n-ga -f ga.lang

%package i18n-gl
Summary:	OpenOffice.org - interface in Galician language
Summary(pl):	OpenOffice.org - interfejs w jêzyku galicyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-gl
This package provides resources containing menus and dialogs in
Galician language.

%description i18n-gl -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
galicyjskim.

#%files i18n-gl -f gl.lang

%package i18n-hr
Summary:	OpenOffice.org - interface in Croatian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku chorwackim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-hr
This package provides resources containing menus and dialogs in
Croatian language.

%description i18n-hr -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chorwackim.

#%files i18n-hr -f hr.lang

%package i18n-hu
Summary:	OpenOffice.org - interface in Hungarian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku wêgierskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-hu
This package provides resources containing menus and dialogs in
Hungarian language.

%description i18n-hu -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
wêgierskim.

%files i18n-hu -f hu.lang

%package i18n-ia
Summary:	OpenOffice.org - interface in Interlingua language
Summary(pl):	OpenOffice.org - interfejs w jêzyku interlingua
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ia
This package provides resources containing menus and dialogs in
Interlingua language.

%description i18n-ia -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
interlingua.

#%files i18n-ia -f ia.lang

%package i18n-id
Summary:	OpenOffice.org - interface in Indonesian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku indonezyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-id
This package provides resources containing menus and dialogs in
Indonesian language.

%description i18n-id -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
indonezyjskim.

#%files i18n-id -f id.lang

%package i18n-it
Summary:	OpenOffice.org - interface in Italian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku w³oskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-it
This package provides resources containing menus and dialogs in
Italian language.

%description i18n-it -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
w³oskim.

%files i18n-it -f it.lang

%package i18n-ja
Summary:	OpenOffice.org - interface in Japan language
Summary(pl):	OpenOffice.org - interfejs w jêzyku japoñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ja
This package provides resources containing menus and dialogs in
Japan language.

%description i18n-ja -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
japoñskim.

%files i18n-ja -f ja.lang

%package i18n-ko
Summary:	OpenOffice.org - interface in Korean language
Summary(pl):	OpenOffice.org - interfejs w jêzyku koreañskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ko
This package provides resources containing menus and dialogs in
Korean language.

%description i18n-ko -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
koreañskim.

%files i18n-ko -f ko.lang

%package i18n-la
Summary:	OpenOffice.org - interface in Latin language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ³aciñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-la
This package provides resources containing menus and dialogs in
Latin language.

%description i18n-la -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
³aciñskim.

#%files i18n-la -f la.lang

%package i18n-lt
Summary:	OpenOffice.org - interface in Lithuanian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku litewskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-lt
This package provides resources containing menus and dialogs in
Lithuanian language.

%description i18n-lt -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
litewskim.

#%files i18n-lt -f lt.lang

%package i18n-med
Summary:	OpenOffice.org - interface in Melpa language
Summary(pl):	OpenOffice.org - interfejs w jêzyku melpa
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-med
This package provides resources containing menus and dialogs in
Melpa language.

%description i18n-med -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
melpa.

#%files i18n-med -f med.lang

%package i18n-mi
Summary:	OpenOffice.org - interface in Maori language
Summary(pl):	OpenOffice.org - interfejs w jêzyku maoryjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-mi
This package provides resources containing menus and dialogs in
Maori language.

%description i18n-mi -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
maoryjskim.

#%files i18n-mi -f mi.lang

%package i18n-ms
Summary:	OpenOffice.org - interface in Malay language
Summary(pl):	OpenOffice.org - interfejs w jêzyku malajskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ms
This package provides resources containing menus and dialogs in
Malay language.

%description i18n-ms -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
malajskim.

#%files i18n-ms -f ms.lang

%package i18n-nb
Summary:	OpenOffice.org - interface in Norwegian Bokmaal language
Summary(pl):	OpenOffice.org - interfejs w jêzyku norweskim (odmiana Bokmaal)
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-nb
This package provides resources containing menus and dialogs in
Norwegian Bokmaal language.

%description i18n-nb -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
norweskim w odmianie Bokmaal.

#%files i18n-nb -f nb.lang

%package i18n-nl
Summary:	OpenOffice.org - interface in Dutch language
Summary(pl):	OpenOffice.org - interfejs w jêzyku holenderskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-nl
This package provides resources containing menus and dialogs in
Dutch language.

%description i18n-nl -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
holenderskim.

%files i18n-nl -f nl.lang

%package i18n-pl
Summary:	OpenOffice.org - interface in Polish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku polskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-pl
This package provides resources containing menus and dialogs in
Polish language.

%description i18n-pl -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
polskim.

%files i18n-pl -f pl.lang

%package i18n-pt
Summary:	OpenOffice.org - interface in Portuguese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku portugalskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-pt
This package provides resources containing menus and dialogs in
Portuguese language.

%description i18n-pt -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
portugalskim.

%files i18n-pt -f pt.lang

%package i18n-ro
Summary:	OpenOffice.org - interface in Romanian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku rumuñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ro
This package provides resources containing menus and dialogs in
Romanian language.

%description i18n-ro -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
rumuñskim.

#%files i18n-ro -f ro.lang

%package i18n-ru
Summary:	OpenOffice.org - interface in Russian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku rosyjskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-ru
This package provides resources containing menus and dialogs in
Russian language.

%description i18n-ru -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
rosyjskim.

%files i18n-ru -f ru.lang

%package i18n-sk
Summary:	OpenOffice.org - interface in Slovak language
Summary(pl):	OpenOffice.org - interfejs w jêzyku s³owackim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-sk
This package provides resources containing menus and dialogs in
Slovak language.

%description i18n-sk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
s³owackim.

%files i18n-sk -f sk.lang

%package i18n-sl
Summary:	OpenOffice.org - interface in Slovenian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku s³oweñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-sl
This package provides resources containing menus and dialogs in
Slovenian language.

%description i18n-sl -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
s³oweñskim.

%files i18n-sl -f sl.lang

%package i18n-sv
Summary:	OpenOffice.org - interface in Swedish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku szwedzkim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-sv
This package provides resources containing menus and dialogs in
Swedish language.

%description i18n-sv -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
szwedzkim.

%files i18n-sv -f sv.lang

%package i18n-tr
Summary:	OpenOffice.org - interface in Turkish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku tureckim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-tr
This package provides resources containing menus and dialogs in
Turkish language.

%description i18n-tr -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tureckim.

%files i18n-tr -f tr.lang

%package i18n-uk
Summary:	OpenOffice.org - interface in Ukrainian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku ukraiñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-uk
This package provides resources containing menus and dialogs in
Ukrainian language.

%description i18n-uk -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
ukraiñskim.

#%files i18n-uk -f uk.lang

%package i18n-zh
Summary:	OpenOffice.org - interface in Chinese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-zh
This package provides resources containing menus and dialogs in
Chinese language.

%description i18n-zh -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim.

%files i18n-zh -f zh.lang

%prep
%setup -q -n ooo-build-%{ooobver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

install -d src
ln -s %{SOURCE1} src/
ln -s %{SOURCE2} src/
ln -s %{SOURCE3} src/

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
JAVA_HOME="/usr/lib/java"
DB_JAR="%{_javadir}/db.jar"
export JAVA_HOME DB_JAR GCJ
%endif

# parallel build is broken above 4 NCPUS so use 4 as max
RPM_BUILD_NR_THREADS="%(echo "%{__make}" | sed -e 's#.*-j\([[:space:]]*[0-9]\+\)#\1#g' | xargs)"
[ "$RPM_BUILD_NR_THREADS" != "%{__make}" -a "$RPM_BUILD_NR_THREADS" -gt 4 ] && RPM_BUILD_NR_THREADS=4 || RPM_BUILD_NR_THREADS=1

CONFOPTS=" \
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
	--with-vendor="PLD" \
	--with-distro="PLD" \
%if %{with icons_ximian}
	--with-icons="Ximian" \
%else
	--with-icons="KDE" \
%endif
	--with-widgetset=kde \
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
"

# for cvs snaps
[ -x ./autogen.sh ] && ./autogen.sh $CONFOPTS

# build-ooo script will pickup these
CONFIGURE_OPTIONS="$CONFOPTS"; export CONFIGURE_OPTIONS

# main build
%configure $CONFOPTS

%{__make}

# hack for parallel build
if [ "$RPM_BUILD_NCPUS" -gt 1 ]; then
	doit=1
	while [ "$doit" -eq 1 ]; do
		echo "Waiting one more time..."
		FCH=$(nice -n 20 find . -type f ! -mmin +3 -print 2> /dev/null | wc -l)
		[ "$FCH" -eq 0 ] && doit=0 || sleep 30
	done
fi

# gtk version
cd build/OOO_%{dfullver}
chmod -R u+rwX vcl
cp -af vcl vcl.kde
cp -a Linux*Env.Set* vcl.kde
sed -i -e "s#\(.*WITH_WIDGETSET.*\)\".*\"\(.*\)#\1\"gtk\"\2#g" Linux*Env.Set*
sed -i -e "s#\(.*WIDGETSET_CFLAGS.*\)\".*\"\(.*\)#\1\"`pkg-config --cflags gtk+-2.0 gdk-pixbuf-xlib-2.0` -DWIDGETSET_GTK\"\2#g" Linux*Env.Set*
sed -i -e "s#\(.*WIDGETSET_LIBS.*\)\".*\"\(.*\)#\1\"`pkg-config --libs gtk+-2.0 gdk-pixbuf-xlib-2.0`\"\2#g" Linux*Env.Set*
set +e
. ./Linux*Env.Set.sh
cd vcl
rm -rf unxlng*
build
cd ..
mv vcl vcl.gtk
mv vcl.kde vcl

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT; export DESTDIR
TMP="%{tmpdir}"; export TMP
TEMP="%{tmpdir}"; export TEMP

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_libdir}/%{name}/program/libvcl%{subver}li.so \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/program/libvcl%{subver}li-kde.so

install -m755 build/OOO_%{dfullver}/vcl.gtk/unxlngi4.pro/lib/libvcl%{subver}li.so \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/program/libvcl%{subver}li-gtk.so
install -m755 build/OOO_%{dfullver}/vcl.gtk/unxlngi4.pro/bin/*-gnome \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/program/

install -d helptmp && cd helptmp || exit 1
for file in \
	%{SOURCE400} %{SOURCE401} %{SOURCE402} %{SOURCE403} %{SOURCE404} %{SOURCE405} \
	%{SOURCE406} %{SOURCE407} %{SOURCE408} %{SOURCE409} %{SOURCE410}; do
		rm -rf *.*
		nr=$(echo "$file" | sed -e 's#.*_\(.*\)_.*#\1#g')
		lang=$(../bin/openoffice-xlate-lang -i "$nr")
		if [ -z "$lang" ]; then
			echo "Languge not found for [$file]"
			exit 1
		fi
		tar zxf "${file}"
		for ifile in s*.zip; do
			install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/help/${lang}
			unzip -q -d $RPM_BUILD_ROOT%{_libdir}/%{name}/help/${lang} -o "$ifile"
		done
done
cd ..

sed -e 's#DESTINATIONPATH=.*#DESTINATIONPATH=<home>/.openoffice#g' etc/redhat-autoresponse.conf > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/autoresponse.conf

install -d $RPM_BUILD_ROOT%{_desktopdir}
bzip2 -dc %{SOURCE10} | tar xf - -C $RPM_BUILD_ROOT%{_desktopdir}

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
install -d $RPM_BUILD_ROOT%{_datadir}/fonts/openoffice
cp fonts/opens___.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/openoffice
# %%ghost the fonts.cache-1 file
touch $RPM_BUILD_ROOT%{_datadir}/fonts/openoffice/fonts.cache-1

# We don't need spadmin (gtk) or the setup application
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/setup
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/crash_report.bin
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/openoffice-setup.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/openoffice-printeradmin.desktop

# Remove some python cruft
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/program/python-core-*/lib/test

rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome

#rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/gnomeint

# some libs creep in somehow
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/filter/libfreetype.so*
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
rm -f *.lang
langlist=""
for lang in $RPM_BUILD_ROOT%{_libdir}/%{name}/share/registry/res/*; do
	[ ! -d "$lang" ] && continue
	langlist="$langlist $(echo "$lang" | sed -e 's#.*/\(.*\)#\1#g')"
done
for lang in $RPM_BUILD_ROOT%{_libdir}/%{name}/help/*; do
	[ ! -d "$lang" ] && continue
	langlist="$langlist $(echo "$lang" | sed -e 's#.*/\(.*\)#\1#g')"
done
langlist=$(echo "$langlist" | tr ' ' '\n' | sort | uniq)
slanglist=$(echo "$langlist" | awk -F_ ' { print $1 } ' | awk -F- ' { print $1 } ' | sort | uniq | xargs)

for lang in $slanglist; do
	echo "%%defattr(644,root,root,755)" >> ${lang}.lang

	# help files
	if (ls $RPM_BUILD_ROOT%{_libdir}/%{name}/help/*${lang}* 2> /dev/null); then
		echo "%{_libdir}/%{name}/help/*${lang}*" >> ${lang}.lang
		perl -pi -e "s#.*%{_libdir}/%{name}/help/.*${lang}.*##g" build/lang_*_list.txt
	fi

	# registry res
	if (ls $RPM_BUILD_ROOT%{_libdir}/%{name}/share/registry/res/*${lang}* 2> /dev/null); then
		echo "%{_libdir}/%{name}/share/registry/res/*${lang}*" >> ${lang}.lang
		perl -pi -e "s#.*%{_libdir}/%{name}/share/registry/res/.*${lang}.*##g" build/lang_*_list.txt
	fi

	# files from lang_*_list.txt
	ls build/lang_${lang}*_list.txt 2> /dev/null && sed -e "s#$RPM_BUILD_ROOT##g" build/lang_${lang}*_list.txt >> ${lang}.lang || /bin/true

done

# things not catched by automation above
echo "%{_libdir}/%{name}/program/resource/*%{subver}01.res" >> en.lang
echo "%{_libdir}/%{name}/share/wordbook/english" >> en.lang
echo "%{_libdir}/%{name}/share/autocorr/acor1033.dat" >> en.lang
echo "%{_libdir}/%{name}/share/autocorr/acor2057.dat" >> en.lang

find $RPM_BUILD_ROOT -type f -name '*.so' -exec chmod 755 "{}" ";"
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/program/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF %{_fontsdir}/%{name}

%postun
fontpostinst TTF %{_fontsdir}/%{name}

%post libs
if [ -f %{_libdir}/%{name}/program/libvcl%{subver}li-kde.so ]; then
	ln -sf libvcl%{subver}li-kde.so %{_libdir}/%{name}/program/libvcl%{subver}li.so
fi
if [ -f %{_libdir}/%{name}/program/libvcl%{subver}li-gtk.so ]; then
	ln -sf libvcl%{subver}li-gtk.so %{_libdir}/%{name}/program/libvcl%{subver}li.so
fi

%preun libs-kde
rm -f %{_libdir}/%{name}/program/libvcl%{subver}li.so

%post libs-kde
ln -sf libvcl%{subver}li-kde.so %{_libdir}/%{name}/program/libvcl%{subver}li.so

%preun libs-gtk
rm -f %{_libdir}/%{name}/program/libvcl%{subver}li.so

%post libs-gtk
ln -sf libvcl%{subver}li-gtk.so %{_libdir}/%{name}/program/libvcl%{subver}li.so

%files
%defattr(644,root,root,755)
%doc %{_libdir}/%{name}/LICENSE*
%doc %{_libdir}/%{name}/*README*

%dir %{_sysconfdir}/openoffice
%config %{_sysconfdir}/openoffice/autoresponse.conf

%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%attr(755,root,root) %{_libdir}/%{name}/install-dict

%{_libdir}/%{name}/program/*.rdb
%{_libdir}/%{name}/program/*.bmp
%{_libdir}/%{name}/program/user_registry.xsl
%{_libdir}/%{name}/program/sofficerc
%{_libdir}/%{name}/program/unorc
%{_libdir}/%{name}/program/bootstraprc
%{_libdir}/%{name}/program/configmgrrc
%{_libdir}/%{name}/program/instdb.ins

%dir %{_libdir}/%{name}/program/resource

%dir %{_libdir}/%{name}/help
%{_libdir}/%{name}/help/en
%{_libdir}/%{name}/help/main_transform.xsl

%dir %{_libdir}/%{name}/share
%dir %{_libdir}/%{name}/share/autocorr
%dir %{_libdir}/%{name}/share/autotext
%{_libdir}/%{name}/share/basic
%{_libdir}/%{name}/share/config
%dir %{_libdir}/%{name}/share/dict
%dir %{_libdir}/%{name}/share/dict/ooo
%{_libdir}/%{name}/share/dtd
%{_libdir}/%{name}/share/fonts
%{_libdir}/%{name}/share/gallery
%{_libdir}/%{name}/share/psprint
%{_libdir}/%{name}/share/samples
%dir %{_libdir}/%{name}/share/template
%dir %{_libdir}/%{name}/share/wordbook
%{_libdir}/%{name}/share/readme

%dir %{_libdir}/%{name}/share/registry
%dir %{_libdir}/%{name}/share/registry/res
%{_libdir}/%{name}/share/registry/data
%{_libdir}/%{name}/share/registry/schema

%{_libdir}/%{name}/share/autotext/english
%{_libdir}/%{name}/share/template/english
%ghost %{_libdir}/%{name}/share/dict/ooo/dictionary.lst

%dir %{_libdir}/%{name}/user
%dir %{_libdir}/%{name}/user/autotext
%{_libdir}/%{name}/user/basic
%{_libdir}/%{name}/user/config
%{_libdir}/%{name}/user/database
%{_libdir}/%{name}/user/gallery
%{_libdir}/%{name}/user/psprint

%{_libdir}/%{name}/user/autotext/english

# Programs
%attr(755,root,root) %{_bindir}/oo*
%attr(755,root,root) %{_libdir}/%{name}/spadmin
%attr(755,root,root) %{_libdir}/%{name}/program/*.bin
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
%attr(755,root,root) %{_libdir}/%{name}/program/javaldx
%attr(755,root,root) %{_libdir}/%{name}/program/jvmsetup
%{_libdir}/%{name}/program/classes
%{_libdir}/%{name}/share/xslt
%endif

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/program
%dir %{_libdir}/%{name}/program/filter

%attr(755,root,root) %{_libdir}/%{name}/program/*.so
%exclude %{_libdir}/%{name}/program/libvcl*.so
%attr(755,root,root) %{_libdir}/%{name}/program/*.so.*
%attr(755,root,root) %{_libdir}/%{name}/program/filter/*.so

%dir %{_datadir}/fonts/openoffice
%{_datadir}/fonts/openoffice/*.ttf
%ghost %{_datadir}/fonts/openoffice/fonts.cache-1

%files libs-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libvcl*kde.so

%files libs-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/program/libvcl*gtk.so
%attr(755,root,root) %{_libdir}/%{name}/program/getstyle-gnome
%attr(755,root,root) %{_libdir}/%{name}/program/msgbox-gnome

%files mimelinks
%defattr(644,root,root,755)
%{_datadir}/mimelnk/application/*
