# TODO:
#	- check for correct values for PORTBR
#	- spec can use helpcontent* files not mentioned in SourceXX (bug)
#	- some files come from oo build and helpcontent, we must decide
#	  which one should be used
#	- cleanups, cleanups and cleanups

%bcond_without java		# build without java support

%define		ver		1.1.0
%define		rel		%{nil}
%define		fullver		%{ver}%{rel}

Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	%{ver}
Release:	0.2
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
# Previous url: ftp://ftp.openoffice.pl/pub/OpenOffice.ORG/stable/%{fullver}/OOo_%{fullver}_source.tar.bz2
Source0:	ftp://sunsite.icm.edu.pl/packages/OpenOffice/official/stable/%{fullver}/OOo_%{fullver}_source.tar.bz2
# Source0-md5:	bec8b41089ebdad2831f3c456973ad4e
Source1:	ftp://ftp.cs.man.ac.uk/pub/toby/gpc/gpc231.tar.Z
# Source1-md5:	fdb06fdb5a4670b172f9fb738b717be9
Source2:	%{name}-rsfile.txt
Source3:	%{name}-rsfile-local.txt
Source4:	%{name}-xmlparse.sh
Source6:	%{name}-applnk.tar.gz
# Source6-md5:	577bc34d026c951653fbef752d1b5d85
Source7:	%{name}-wrapper
Source8:	%{name}-wrapper-component
Source10:	%{name}-db3.jar
# Source10-md5:	0d15818dea3099eed42b4be9950c69ad
Source11:	%{name}-dictionary.lst.readme
# Source11-md5:	e4c1c2844b4a4cebca33339538da7f1d

%define		helpftp	ftp://openoffice.tu-bs.de/OpenOffice.org/contrib/helpcontent
Source101:	%{helpftp}/helpcontent_01_unix.tgz
# Source101-md5:	ff3eb5095a74ae7a9b2918ef5874288f
Source107:	%{helpftp}/helpcontent_07_unix.tgz
# Source107-md5:	e3ab37cbf2407d909953f06467b27611
Source133:	%{helpftp}/helpcontent_33_unix.tgz
# Source133-md5:	20dcbf3211c20afb27fc5677ab8f69e5
Source134:	%{helpftp}/helpcontent_34_unix.tgz
# Source134-md5:	ba6adc71dc5cb766dd75f5b13a7c6bc8
Source135:	%{helpftp}/helpcontent_35_unix.tgz
# Source135-md5:	cf90274a2e46ddd04422c08157575780
Source139:	%{helpftp}/helpcontent_39_unix.tgz
# Source139-md5:	4c33e3f9f8a64be68c63f33ff1e0e4a7
Source142:	%{helpftp}/helpcontent_42_unix.tgz
# Source142-md5:	a7bcb51e5bff1673b32113308a026563
Source146:	%{helpftp}/helpcontent_46_unix.tgz
# Source146-md5:	5183879d8b57850d433351cb8a5634a8
Source149:	%{helpftp}/helpcontent_49_unix.tgz
# Source149-md5:	68f0db91bb091065a4795d47d6ae0b0b
Source181:	%{helpftp}/helpcontent_81_unix.tgz
# Source181-md5:	df731e483114e1433f799160b2baa942
Source182:	%{helpftp}/helpcontent_82_unix.tgz
# Source182-md5:	ea45780e3027317ec6b4f38f009b579b
Source186:	%{helpftp}/helpcontent_86_unix.tgz
# Source186-md5:	ea0debc121b6912a42cdc24e1b99b625
Source188:	%{helpftp}/helpcontent_88_unix.tgz
# Source188-md5:	260a17a84a16c18b4371a84b95cea2cb

# Localization scripts from Mandrake
Source302:	%{name}-dpack-lang.pl
Source303:	%{name}-transmute-help-errfile.pl
Source304:	%{name}-create-instdb.pl

#Patch0:		%{name}-gcc.patch
#Patch2:		%{name}-mozilla.patch
# Start using some system libraries:
Patch4:		%{name}-system-stlport.patch
Patch5:		%{name}-system-freetype.patch
Patch7:		%{name}-freetype-2.1.patch
# Fix broken makefiles
Patch8:		%{name}-braindamage.patch
# Fix config_office/configure
Patch9:		%{name}-setup-localized-instdb.patch
#Patch11:	%{name}-ac.patch

# Hackery around zipdep
#Patch13:	%{name}-zipdep.patch
# Remove GPC from linking to GPL/LGPL OO.o code!
Patch14:	%{name}-remove-gpc.patch
# Disable stlport from being built
Patch16:	%{name}-no-stlport.patch

# Fix broken inline assembly
Patch18:	%{name}-asm.patch

Patch19:	%{name}-no-mozab.patch
Patch20:	%{name}-no-mozab2.patch

Patch21:	%{name}-system-db.patch

Patch24:	%{name}-autodoc.patch

Patch25:	%{name}-xmlsearch.patch
Patch27:	%{name}-sj2-java.patch

Patch29:	%{name}-gcc2-95.patch
Patch30:	%{name}-system-zlib.patch
Patch31:	%{name}-system-mozilla.patch
Patch32:	%{name}-fix-errno.patch

Patch52:	%{name}-xmlhelp.patch

Patch63:	%{name}-stlutility.patch
Patch64:	%{name}-crashrepgtk.patch

# Fix java/ppc problem 
Patch65:	%{name}-java-ppc.patch 

# Hey, we _really_ want java?
Patch101: openoffice-allow-no-jdk.patch
Patch102: openoffice-berkeleydb-handle-no-solar-java.patch
Patch103: openoffice-desktop-handle-no-solar-java.patch
Patch104: openoffice-javaunohelper-handle-no-solar-java.patch
Patch105: openoffice-jni-uno-handle-no-solar-java.patch
Patch106: openoffice-jurt-handle-no-solar-java.patch
Patch107: openoffice-jvmaccess-handle-no-solar-java.patch
Patch108: openoffice-officecfg-xsltproc.patch
Patch109: openoffice-psprint-handle-no-solar-java.patch
Patch110: openoffice-readlicense-oo-xsltproc.patch
Patch111: openoffice-ridljar-handle-no-solar-java.patch
Patch112: openoffice-setup2-handle-no-solar-java.patch
Patch113: openoffice-sj2-handle-no-solar-java.patch
Patch114: openoffice-solenv-set-solar-java-only-if-unset.patch
Patch115: openoffice-svg-handle-no-solar-java.patch
Patch116: openoffice-xsltfilter-handle-no-solar-java.patch
Patch117: openoffice-xsltvalidate-handle-no-solar-java.patch
Patch118: openoffice-berkeleydb-no-java-fix.patch 
Patch119: openoffice-scp-no-java-fix.patch
Patch120: openoffice-odk-handle-no-solar-java.patch 
Patch121: openoffice-disable-odk-build.patch

# misc patches
Patch201: openoffice-zoom-combobox.spec

URL:		http://www.openoffice.org/
BuildRequires:	STLport-devel >= 4.5.3-6
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison >= 1.875-4
BuildRequires:	db-devel
BuildRequires:	db-cxx-devel
%if %{with java}
BuildRequires:	db4.1-java
BuildRequires:	jar
BuildRequires:	jdk
%elseif
BuildRequires:	libxslt-progs
BuildRequires:	gcc-java-tools
%endif
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.1
#BuildRequires:	gcc-java
BuildConflicts:	java-sun = 1.4.2
BuildRequires:	libstdc++-devel >= 3.2.1
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	tcsh
BuildRequires:	unzip
BuildRequires:	zip
BuildRequires:	zlib-devel
# gtk crashreport static requirements:
BuildRequires:	XFree86-static
BuildRequires:	atk-static
BuildRequires:	expat-static
BuildRequires:	fontconfig-static
BuildRequires:	freetype-static
BuildRequires:	glib2-static
BuildRequires:	glibc-static
BuildRequires:	gtk+2-static
BuildRequires:	libjpeg-static
BuildRequires:	libpng-static
BuildRequires:	libtiff-static
BuildRequires:	pango-static
BuildRequires:	xft-static
BuildRequires:	xrender-static
BuildRequires:	zlib-static
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n-en = %{epoch}:%{version}-%{release}
Requires:	%{name}-dict-en
Requires:	libstdc++ >= 3.2.1
Requires:	db
Requires:	chkfontpath
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


# Supported languages for localized help files (others are not
# complete/advanced enough)
%define helplangs1 ENUS,FREN,GERM,SPAN,ITAL,SWED,RUSS,CZECH,JAPN
%define helplangs2 KOREAN,CHINSIM,CHINTRAD
%define helplangs  %{helplangs1},%{helplangs2}

%define	apps	agenda calc draw fax impress label letter math master memo vcard web writer

%ifarch %{ix86}
%define	_archbuilddir	unxlngi4.pro
%endif
%ifarch ppc 
%define _archbuilddir 	unxlngppc.pro
%endif
%define	installpath	instsetoo/%{_archbuilddir}
%define	subver		645
%define	langinst	01

%define oolib	%{_libdir}/openoffice
%define dictlst	%{oolib}/share/dict/ooo/dictionary.lst

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

%package mimelinks
Summary:	OpenOffice.org mimelinks
Summary(pl):	Dowi±zania MIME dla OpenOffice.org
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description mimelinks
OpenOffice.org mimelinks.

%description mimelinks -l pl
Dowi±zania MIME dla OpenOffice.org.

#
# Internationalization
#
%define		have_ARAB	yes
%define		have_CAT	yes
%define		have_CZECH	yes
%define		have_DAN	yes
%define		have_GERM	yes
%define		have_GREEK	yes
# ENUS should be always "yes"
%define		have_ENUS	yes
%define		have_SPAN	yes
%define		have_FINN	yes
%define		have_FREN	yes
%define		have_ITAL	yes
%define		have_JAPN	yes
%define		have_KOREAN	yes
%define		have_DTCH	yes
%define		have_POL	yes
%define		have_PORT	yes
%define		have_PORTBR	yes
%define		have_RUSS	yes
%define		have_SLOVAK	yes
%define		have_SWED	yes
%define		have_TURK	yes
%define		have_CHINSIM	yes
%define		have_CHINTRAD	yes

%define		ARAB		""
%if %{have_ARAB} == yes
%define		ARAB		ARAB
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

%files i18n-ar -f i18n-ar
%endif

%define		CAT		""
%if %{have_CAT} == yes
%define		CAT		CAT
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

%files i18n-ca -f i18n-ca
%endif

%define		CZECH		""
%if %{have_CZECH} == yes
%define		CZECH		CZECH
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

%files i18n-cs -f i18n-cs
%endif

%define		DAN		""
%if %{have_DAN} == yes
%define		DAN		DAN
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

%files i18n-da -f i18n-da
%endif

%define		GERM		""
%if %{have_GERM} == yes
%define		GERM		GERM
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

%files i18n-de -f i18n-de
%endif

%define		GREEK		""
%if %{have_GREEK} == yes
%define		GREEK		GREEK
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

%files i18n-el -f i18n-el
%endif

%define		ENUS		""
%if %{have_ENUS} == yes
%define		ENUS		ENUS
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

%files i18n-en -f i18n-en
%endif

%define		SPAN		""
%if %{have_SPAN} == yes
%define		SPAN		SPAN
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

%files i18n-es -f i18n-es
%endif

%define		FINN		""
%if %{have_FINN} == yes
%define		FINN		FINN
%package i18n-fi
Summary:	OpenOffice.org - interface in English language
Summary(pl):	OpenOffice.org - interfejs w jêzyku angielskim
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-fi
This package provides resources containing menus and dialogs in
Finnish language.

%description i18n-fi -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
fiñskim.

%files i18n-fi -f i18n-fi
%endif

%define		FREN		""
%if %{have_FREN} == yes
%define		FREN		FREN
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

%files i18n-fr -f i18n-fr
%endif

%define		ITAL		""
%if %{have_ITAL} == yes
%define		ITAL		ITAL
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

%files i18n-it -f i18n-it
%endif

%define		JAPN		""
%if %{have_JAPN} == yes
%define		JAPN		JAPN
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

%files i18n-ja -f i18n-ja
%endif

%define		KOREAN		""
%if %{have_KOREAN} == yes
%define		KOREAN		KOREAN
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

%files i18n-ko -f i18n-ko
%endif

%define		DTCH		""
%if %{have_DTCH}
%define		DTCH		DTCH
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

%files i18n-nl -f i18n-nl
%endif

%define		POL		""
%if %{have_POL} == yes
%define		POL		POL
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

%files i18n-pl -f i18n-pl
%endif

%define		PORT		""
%if %{have_PORT} == yes
%define		PORT		PORT
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

%files i18n-pt -f i18n-pt
%endif

%define		PORTBR		""
%if %{have_PORTBR} == yes
%define		PORTBR		PORTBR
%package i18n-pt_BR
Summary:	OpenOffice.org - interface in Portuguese Brazylian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku portugalskim (brazylia)
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-pt_BR
This package provides resources containing menus and dialogs in
Portuguese Brazylian language.

%description i18n-pt_BR -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
portugalskim (odmiana brazylijska).

%files i18n-pt_BR -f i18n-pt_BR
%endif

%define		RUSS		""
%if %{have_RUSS} == yes
%define		RUSS		RUSS
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

%files i18n-ru -f i18n-ru
%endif

%define		SLOVAK		""
%if %{have_SLOVAK} == yes
%define		SLOVAK		SLOVAK
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

%files i18n-sk -f i18n-sk
%endif

%define		SWED		""
%if %{have_SWED} == yes
%define		SWED		SWED
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

%files i18n-sv -f i18n-sv
%endif

%define		TURK		""
%if %{have_TURK} == yes
%define		TURK		TURK
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

%files i18n-tr -f i18n-tr
%endif

%define		CHINSIM		""
%if %{have_CHINSIM} == yes
%define		CHINSIM		CHINSIM
%package i18n-zh_CN
Summary:	OpenOffice.org - interface in Chinese language for China
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim dla Chin
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-zh_CN
This package provides resources containing menus and dialogs in
Chinese language for China.

%description i18n-zh_CN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim dla Chin.

%files i18n-zh_CN -f i18n-zh_CN
%endif

%define		CHINTRAD		""
%if %{have_CHINTRAD} == yes
%define		CHINTRAD		CHINTRAD
%package i18n-zh_TW
Summary:	OpenOffice.org - interface in Chinese language for Taiwan
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim dla Tajwanu
Group:		Applications/Office
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description i18n-zh_TW
This package provides resources containing menus and dialogs in
Chinese language for Taiwan.

%description i18n-zh_TW -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim dla Tajwanu.

%files i18n-zh_TW -f i18n-zh_TW
%endif

%prep
%setup -q -n oo_1.1_src
#%patch0 -p1
#%patch2 -p1

%patch4 -p1
%patch5 -p1
%patch7 -p1
#%patch9 -p1

# Is gpc used at all?? :
%patch16 -p1

%patch19 -p1
%patch20 -p1
%patch21 -p1

%patch30 -p1

rm -f moz/prj/d.lst
%patch31 -p1

# 1.1 BETA
%patch52 -p1
%patch63 -p1
%patch64 -p1

# java/ppc: broken native threads?
%ifarch ppc
%patch65 -p1 
%endif 

# no-java patch
%if %{without java}
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch117 -p0
%patch118 -p1 
%patch119 -p1 
%patch120 -p0 
%patch121 -p0 
%endif 

# add zoom combobox
%patch201 -p1 

# gcc 2 include error hack:
rm -rf autodoc/source/inc/utility

install %{SOURCE1} external
cd external; tar fxz %{SOURCE1}; cp -fr gpc231/* gpc
cd ..

install -d solver/%{subver}/%{_archbuilddir}/lib
cp -f /lib/libgcc_s.so.1* solver/%{subver}/%{_archbuilddir}/lib
cp /usr/lib/libstdc++.so.5* solver/%{subver}/%{_archbuilddir}/lib

# optimalization
cd solenv/inc
for i in *.mk
do
	cat $i | sed \
		-e 's/-mpentium/%{rpmcflags}/' \
		-e 's/-mpentiumpro/%{rpmcflags}/' \
		-e 's/-mcpu=pentiumpro/%{rpmcflags}/' > $i.new
	mv -f $i.new $i
done

%build
CC=%{__cc}
CXX=%{__cxx}
GCJ=gcj
JAVA_HOME="/usr/lib/java"
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"
export JAVA_HOME CC CXX GCJ CFLAGS CXXFLAGS

cd config_office
%{__autoconf}
%configure2_13 \
%if %{without java}
	--disable-java \
%elseif
	--with-jdk-home=$JAVA_HOME \
%endif
	--with-stlport4-home=/usr \
	--with-lang=ALL \
	--with-x

cd ..

%ifarch %{ix86}
echo -e "#!/bin/tcsh\nsource LinuxIntelEnv.Set\ndmake -p -v\n" > compile
%endif
%ifarch ppc
echo -e "#!/bin/tcsh\nsource LinuxPPCEnv.Set\ndmake -p -v\n" > compile
%endif
echo -e "#!/bin/tcsh\n./bootstrap\n" > prep
chmod u+rx prep compile
./prep

install -d solver/%{subver}/%{_archbuilddir}/bin
%if %{with java}
install /usr/lib/db.jar solver/%{subver}/%{_archbuilddir}/bin/db.jar
%endif 

./compile


%install
rm -rf $RPM_BUILD_ROOT

OOBUILDDIR=`pwd`

%if %{without java}
LD_LIBRARY_PATH="$OOBUILDDIR/solver/%{subver}/%{_archbuilddir}/lib/"
export LD_LIBRARY_PATH
%endif 

install -d $RPM_BUILD_ROOT%{oolib}

LangCode() {
# $1 - from column no.
# $2 - from column value
# $3 - to column no.

l="\n\
01:en:ENUS:English US:english::en-US:\n\
03:pt:PORT:Portuguese:portuguese:por::\n\
07:ru:RUSS:Russian:russian:rus::\n\
30:el:GREEK:Greek:greek:gre::\n\
31:nl:DTCH:Dutch:dutch:dut::\n\
33:fr:FREN:French:french:fre::\n\
34:es:SPAN:Spanish:spanish:spa::\n\
35:fi:FINN:Finnish:finnish:fin::\n\
37:ca:CAT:Catalan:catalan:cat::\n\
39:it:ITAL:Italian:italian:ita::\n\
42:cs:CZECH:Czech:czech:cze::\n\
43:sk:SLOVAK:Slovak:slovak:slk::\n\
45:da:DAN:Danish:danish:dan::\n\
46:sv:SWED:Swedish:swedish:swe::\n\
48:pl:POL:Polish:polish:pol::\n\
49:de:GERM:German:german:ger::\n\
55:pt_BR:PORTBR:Brazilian:portuguese_brazilian::pt-BR:\n\
81:ja:JAPN:Japanese:japanese:jap::\n\
82:ko:KOREAN:Korean:korean:kor::\n\
86:zh_CN:CHINSIM:Chinese Simplified:chinese_simplified::zh-CN:\n\
88:zh_TW:CHINTRAD:Chinese Traditional:chinese_traditional::zh-TW:\n\
90:tr:TURK:Turkish:turkish:tur::\n\
96:ar:ARAB:Arabic:arabic:ara::\n"

echo -e $l | awk -F: "{ split(\$0, A, \":\"); if (A[$1] == \"$2\") print A[$3]; }"
}

LANGS="%{ARAB} %{CAT} %{CZECH} %{DAN} %{GERM} %{GREEK} %{ENUS} %{SPAN} %{FINN}
%{FREN} %{ITAL} %{JAPN} %{KOREAN} %{DTCH} %{POL} %{PORT} %{PORTBR} %{RUSS}
%{SLOVAK} %{SWED} %{TURK} %{CHINSIM} %{CHINTRAD}"

### Instalation
RESPONSE_FILE=$OOBUILDDIR/rsfile.ins
cd %{installpath}/%{langinst}/normal/

# --short-circuit support
suf1="" && suf2=".orig" && [ -f setup.ins.orig ] && suf1=".orig" && suf2=""
cp -f setup.ins$suf1 setup.ins$suf2

cat %{SOURCE2} | sed -e "s|@DESTDIR@|$RPM_BUILD_ROOT%{oolib}|" > $RESPONSE_FILE

# Localize New and Wizard menus and OfficeObjects
TMPFILE=setup.pldtmp && rm -f $TMPFILE && touch $TMPFILE
DIRS=`find ../../ -name "[0-9][0-9]" -and -not -name "%{langinst}" -printf "%%P "`
for i in $DIRS; do
    if [ -f ../../$i/normal/setup.ins ]; then
	CONV=cat
	case "$i" in
	3[347]|4[69]) # fr, es, la, sv, de are latin1 encoded
	    CONV="iconv -f ISO-8859-1// -t UTF-8//";;
	3[19]|45|90) # nl, it, da, tr are unknown, no characters above <U007F>
	    ;;
	0[37]|30|4[28]) # pt, ru, el, cs, pl are already UTF-8 encoded
	    ;;
	esac

	grep -A6 'gid_Configurationitem_Common_\(Objectnames.*_Name\|Menus_.*Titel\)' \
	    ../../$i/normal/setup.ins | $CONV \
	    | sed "s/^--//;/^ConfigurationItem/s/\(Name\|Titel\)/$i&/" >> $TMPFILE
	echo >> $TMPFILE
    fi
done

#cat $TMPFILE | awk ' $1 ~ /Value/ { l=$0; sub(/^.*= "/,"",l); sub(/";.*$/,"",l); sub(/%PRODUCTNAME/,"OpenOffice.org",l); sub(/%PRODUCTVERSION/,"%{version}",l); n=n+1; str="@@REPLACEME" n "@@"; s="\"" str "\""; sub(/".*"/,s); printf "s|%s|%s|\n", str, l > "Common.xml.sed" } { print } ' \
#    >> setup.ins
cat $TMPFILE >> setup.ins

./setup -v -nogui -R:$RESPONSE_FILE

cd $OOBUILDDIR
### end of installation

install -d $RPM_BUILD_ROOT%{oolib}/program/resource
# Copy all localized resources to destination directory
FILES=`find solver/%{subver}/%{_archbuilddir}/bin/ -name "*.res" -maxdepth 1 -printf "%%P "`
for FILE in $FILES
do
    [ ! -f $RPM_BUILD_ROOT%{oolib}/program/resource/$FILE ] && \
	cp solver/%{subver}/%{_archbuilddir}/bin/$FILE \
	    $RPM_BUILD_ROOT%{oolib}/program/resource/$FILE
done

# don't care about main_transform.xsl, it looks safe to overwrite
rm -rf helptmp; mkdir helptmp; cd helptmp
PREF="`dirname %{SOURCE101}`/helpcontent_"
SUFX="_unix.tgz"
for L in $LANGS
do
    CODE=`LangCode 3 $L 1`
    NAME=`LangCode 3 $L 2`
    FILE=$PREF$CODE$SUFX
    install -d $RPM_BUILD_ROOT%{oolib}/help/$NAME
    if [ -f $FILE ]; then
	tar zxvf $FILE
	for file in s*.zip; do
	    unzip -q -d $RPM_BUILD_ROOT%{oolib}/help/$NAME -o $file
	done
	rm -f *.zip;
    fi
done
cd ..

### Extract language packs
cd %{installpath}
install -m 755 %{SOURCE302} oo_dpack_lang
install -m 755 %{SOURCE303} oo_fixup_help

for res in $LANGS
do
    prefix=`LangCode 3 $res 1`
    isocode=`LangCode 3 $res 2`
    tempdir=$RPM_BUILD_ROOT%{oolib}-$isocode
    mkdir -p $tempdir

# may extract help files, if known to be localized enough
    case ",%{helplangs}," in
    *,$res,*)
	./oo_dpack_lang -d=$tempdir -i=$prefix/normal/setup.ins -h
	;;
    *)
	./oo_dpack_lang -d=$tempdir -i=$prefix/normal/setup.ins
	mkdir -p $tempdir/help/$isocode
	;;
    esac

# link ooo resource files to iso files
    ln -sf %{oolib}/program/resource/ooo%{subver}$prefix \
	$tempdir/program/resource/iso%{subver}$prefix

    cp -af $tempdir/* $RPM_BUILD_ROOT%{oolib}
    rm -rf $tempdir

    HOWMUCH=`ls $RPM_BUILD_ROOT%{oolib}/help/$isocode 2>/dev/null | wc -l`
    if [ $HOWMUCH -eq 0 ]; then 
	rm -rf $RPM_BUILD_ROOT%{oolib}/help/$isocode
	ln -sf en $RPM_BUILD_ROOT%{oolib}/help/$isocode
    fi
done
cd $OOBUILDDIR

%if %{without java}
install solver/%{subver}/%{_archbuilddir}/lib/libj%{subver}* $RPM_BUILD_ROOT%{oolib}/program/
%endif

cp -af $RPM_BUILD_ROOT%{oolib}/help/zh_CN/* $RPM_BUILD_ROOT%{oolib}/help/zh-CN
cp -af $RPM_BUILD_ROOT%{oolib}/help/zh_TW/* $RPM_BUILD_ROOT%{oolib}/help/zh-TW
rm -rf $RPM_BUILD_ROOT%{oolib}/help/{zh_CN,zh_TW}
mv $RPM_BUILD_ROOT%{oolib}/help/{zh-CN,zh_CN}
mv $RPM_BUILD_ROOT%{oolib}/help/{zh-TW,zh_TW}

# Remove unnecessary binaries
for app in %{apps}
do
    rm -f $RPM_BUILD_ROOT%{oolib}/program/s${app}
done

install -d $RPM_BUILD_ROOT%{_applnkdir}
gunzip -dc %{SOURCE6} | tar xf - -C $RPM_BUILD_ROOT%{_applnkdir}

# Remove stuff that should come from system libraries
rm -rf $RPM_BUILD_ROOT%{oolib}/program/libdb-*
rm -rf $RPM_BUILD_ROOT%{oolib}/program/libdb_*
rm -rf $RPM_BUILD_ROOT%{oolib}/program/filter/libfreetype*

# Fix GNOME & KDE
install -d $RPM_BUILD_ROOT%{_datadir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT%{oolib}/share/kde/net/share/mimelnk $RPM_BUILD_ROOT%{_datadir}
cp -rf $RPM_BUILD_ROOT%{oolib}/share/kde/net/share/icons/* $RPM_BUILD_ROOT%{_pixmapsdir}
cp -rf $RPM_BUILD_ROOT%{oolib}/share/icons/* $RPM_BUILD_ROOT%{_pixmapsdir}
rm -rf $RPM_BUILD_ROOT%{oolib}/share/kde
rm -rf $RPM_BUILD_ROOT%{oolib}/share/cde
rm -rf $RPM_BUILD_ROOT%{oolib}/share/gnome
rm -rf $RPM_BUILD_ROOT%{oolib}/share/icons

# Fixup instdb.ins to get rid of $RPM_BUILD_ROOT
perl -pi -e "s|$RPM_BUILD_ROOT||g" $RPM_BUILD_ROOT%{oolib}/program/instdb.ins
perl -pi -e "/^Installation gid_Installation/ .. /^End/ and s|(SourcePath.*)=.*|\1= \"%{oolib}/program\";|" \
  $RPM_BUILD_ROOT%{oolib}/program/instdb.ins

# Disable desktop (KDE, GNOME, CDE) integration for user installs
for module in GID_MODULE_OPTIONAL_GNOME gid_Module_Optional_Kde gid_Module_Optional_Cde; do
    perl -pi -e "/^Module $module/ .. /^End/ and s|(Installed.*)=.*|\1= NO;|" \
	$RPM_BUILD_ROOT%{oolib}/program/instdb.ins
done

# Fix setup and spadmin symlinks set by OO.org setup program
# (must have absolute symlinks)
ln -sf %{oolib}/program/setup $RPM_BUILD_ROOT%{oolib}/setup
ln -sf %{oolib}/program/soffice $RPM_BUILD_ROOT%{oolib}/spadmin
ln -sf %{oolib}/program/soffice $RPM_BUILD_ROOT%{oolib}/program/spadmin

# Install autoresponse file for user installation
install -d $RPM_BUILD_ROOT%{_sysconfdir}/openoffice
cat %{SOURCE3} > $RPM_BUILD_ROOT%{_sysconfdir}/openoffice/autoresponse.conf

# Install OpenOffice.org wrapper script
install -d $RPM_BUILD_ROOT%{_bindir}
cat %{SOURCE7} | sed -e "s/@OOVERSION@/%{subver}/" > \
    $RPM_BUILD_ROOT%{_bindir}/ooffice

# Install component wrapper scripts
install -d $RPM_BUILD_ROOT%{_bindir}
for app in %{apps}; do
    cat %{SOURCE8} | sed -e "s/@APP@/${app}/" \
	> $RPM_BUILD_ROOT%{_bindir}/oo${app}
done

echo 'UNO_WRITERDB=$SYSUSERCONFIG/.user60.rdb' \
    >> $RPM_BUILD_ROOT%{oolib}/program/unorc

# Build system in OO SUX
rm -f $RPM_BUILD_ROOT%{oolib}/program/libstdc++*
rm -f $RPM_BUILD_ROOT%{oolib}/program/libstlport_gcc.so
rm -f $RPM_BUILD_ROOT%{oolib}/program/libgcc_s.so.1

rm -rf $RPM_BUILD_ROOT%{oolib}/share/template/{internal,wizard}

# remove dictionaries
rm -rf $RPM_BUILD_ROOT%{oolib}/share/dict/ooo/*
cp %{SOURCE11} $RPM_BUILD_ROOT%{dictlst}-readme
touch $RPM_BUILD_ROOT%{dictlst}

# move to devel ???
for file in autodoc cppumaker idlc idlcpp javamaker rdbmaker regcomp \
    regmerge regview uno xml2cmp
do
    cp solver/%{subver}/%{_archbuilddir}/bin/$file $RPM_BUILD_ROOT%{_bindir}
done


AddFiles() {
    LOCALE=$1; shift
    OPTIONS=$1; shift
    ISDIR=$1; shift

    while [ $# -gt 0 ]
    do
	F=$1; shift
	if [ "$ISDIR" == "dir" ]; then
	    [ ! -d $RPM_BUILD_ROOT/$F ] && continue
	else
	    [ ! -f $RPM_BUILD_ROOT/$F ] && continue
	fi

	echo "$OPTIONS $F" >> "i18n-$LOCALE"
    done
}

Multiply() {
    PREFIX=$1; shift
    SUFIX=$1; shift
    while [ $# -gt 0 ]
    do
	echo "$PREFIX$1$SUFIX"
	shift
    done
}

# package files
for L in $LANGS; do
    lshort=`LangCode 3 $L 2`
    lno=`LangCode 3 $L 1`
    lname=`LangCode 3 $L 5`
    lres=`LangCode 3 $L 6`
    loth=`LangCode 3 $L 7`

    echo "%defattr(644,root,root,755)" > "i18n-$lshort"

    AddFiles $lshort "" dir %{oolib}/user/autotext/$lname
    AddFiles $lshort "" dir %{oolib}/share/autotext/$lname
    AddFiles $lshort "" dir %{oolib}/share/template/$lname
    AddFiles $lshort "" dir %{oolib}/help/$lshort
    AddFiles $lshort "" dir %{oolib}/share/wordbook/$lname

    PCKDIR=solver/%{subver}/%{_archbuilddir}/pck
    FILES=""
    [ -f "$PCKDIR/palettes$lno.zip" ] && FILES="`unzip -l $PCKDIR/palettes$lno.zip | awk '{ if (($lres != "")&&($lres != "----")&&($lres != "Name")) print $lres }'`"
    [ "$lshort" = "en" ] && FILES="$FILES autotbl.fmt `unzip -l $PCKDIR/palettes.zip | awk '{ if (($lres != "")&&($lres != "----")&&($lres != "Name")) print $lres }'`"
    AddFiles $lshort "" "" `Multiply %{oolib}/user/config/ "" $FILES`

    FILES=""
    [ -f "$PCKDIR/autocorr$lno.zip" ] && FILES="`unzip -l $PCKDIR/autocorr$lno.zip | awk '{ if (($lres != "")&&($lres != "----")&&($lres != "Name")) print $lres }'`"
    AddFiles $lshort "" "" `Multiply %{oolib}/share/autocorr/ "" $FILES`

    SUBF="abp analysis basctl bib cal cnt date dba dbi dbp dbu dbw dkt egi eme
    epb epg epn epp eps ept eur for frm gal imp iso jvm lgd oem ofa oic ooo pcr
    preload san sc sch sd set set_pp1 sfx sm spa stt svs svt svx sw tpl tplx uui
    vcl wwz com flash fwe pdffilter tk xsltdlg"
    SVER=%{subver}

    AddFiles $lshort "" "" `Multiply %{oolib}/program/resource/ $SVER$lno.res $SUBF`
    AddFiles $lshort "" dir `Multiply %{oolib}/share/registry/res/ "" $lshort $loth`
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc readlicense/source/license/unx/LICENSE
%doc %{oolib}/LICENSE*
%doc %{oolib}/*README*

%dir %{_sysconfdir}/openoffice
%config %{_sysconfdir}/openoffice/autoresponse.conf

%{_applnkdir}/Office
%{_pixmapsdir}/*.png
%{_pixmapsdir}/document-icons/*.png

%{_pixmapsdir}/locolor/16x16/apps/*.xpm
%{_pixmapsdir}/locolor/22x22/apps/*.xpm
%{_pixmapsdir}/locolor/32x32/apps/*.xpm
%{_pixmapsdir}/hicolor/16x16/apps/*.xpm
%{_pixmapsdir}/hicolor/22x22/apps/*.xpm
%{_pixmapsdir}/hicolor/32x32/apps/*.xpm
%{_pixmapsdir}/hicolor/48x48/apps/*.xpm



%{oolib}/program/*.rdb
%{oolib}/program/*.bmp
%{oolib}/program/user_registry.xsl

%{oolib}/program/sofficerc
%{oolib}/program/unorc
%{oolib}/program/bootstraprc
%{oolib}/program/configmgrrc
%{oolib}/program/instdb.ins

# dirs/trees
%{oolib}/program/classes

%dir %{oolib}/program/resource
%{oolib}/program/resource/bmp.res
#%{oolib}/program/resource/crash_dump.res
%{oolib}/program/resource/testtool.res

# mozilla
#%%{oolib}/program/defaults
#%%{oolib}/program/component.reg
#%%{oolib}/program/components/*.xpt
#%%{oolib}/program/components/*.dat

%dir %{oolib}/help
%{oolib}/help/en
%{oolib}/help/main_transform.xsl

%dir %{oolib}/share
%dir %{oolib}/share/autocorr
%dir %{oolib}/share/autotext
%{oolib}/share/basic
%{oolib}/share/config
%dir %{oolib}/share/dict
%dir %{oolib}/share/dict/ooo
%{oolib}/share/dtd
%{oolib}/share/fonts
%{oolib}/share/gallery
%{oolib}/share/psprint
%{oolib}/share/samples
%dir %{oolib}/share/template
%dir %{oolib}/share/wordbook
%{oolib}/share/readme
#%{oolib}/share/xslt

%dir %{oolib}/share/registry
%dir %{oolib}/share/registry/res
%{oolib}/share/registry/data
%{oolib}/share/registry/schema

%{oolib}/share/autotext/english
%{oolib}/share/template/english
%ghost %{oolib}/share/dict/ooo/dictionary.lst
%{oolib}/share/dict/ooo/dictionary.lst-readme

%dir %{oolib}/user
%dir %{oolib}/user/autotext
%{oolib}/user/basic
%{oolib}/user/database
%{oolib}/user/gallery
%{oolib}/user/psprint

%{oolib}/user/autotext/english

# Programs
%attr(755,root,root) %{_bindir}/oo*

%attr(755,root,root) %{oolib}/setup
%attr(755,root,root) %{oolib}/spadmin

%attr(755,root,root) %{oolib}/program/*.bin
#%attr(755,root,root) %{oolib}/program/crash_report
%attr(755,root,root) %{oolib}/program/fromtemplate
%attr(755,root,root) %{oolib}/program/gnomeint
%if %{with java}
%attr(755,root,root) %{oolib}/program/javaldx
%attr(755,root,root) %{oolib}/program/jvmsetup
%endif
%attr(755,root,root) %{oolib}/program/nswrapper
%attr(755,root,root) %{oolib}/program/pagein*
%attr(755,root,root) %{oolib}/program/setup
%attr(755,root,root) %{oolib}/program/soffice
%attr(755,root,root) %{oolib}/program/sopatchlevel.sh
%attr(755,root,root) %{oolib}/program/spadmin
%attr(755,root,root) %{oolib}/program/getstyle-gnome
%attr(755,root,root) %{oolib}/program/msgbox-gnome

# %files devel ?????????
%attr(755,root,root) %{_bindir}/autodoc
%attr(755,root,root) %{_bindir}/cppumaker
%attr(755,root,root) %{_bindir}/idlc
%attr(755,root,root) %{_bindir}/idlcpp
%attr(755,root,root) %{_bindir}/javamaker
%attr(755,root,root) %{_bindir}/rdbmaker
%attr(755,root,root) %{_bindir}/regcomp
%attr(755,root,root) %{_bindir}/regmerge
%attr(755,root,root) %{_bindir}/regview
%attr(755,root,root) %{_bindir}/uno
%attr(755,root,root) %{_bindir}/xml2cmp

%files libs
%defattr(644,root,root,755)
%dir %{oolib}
%dir %{oolib}/program
#%%dir %{oolib}/program/components   -- mozilla
%dir %{oolib}/program/filter

%attr(755,root,root) %{oolib}/program/*.so
%attr(755,root,root) %{oolib}/program/*.so.*
#%%attr(755,root,root) %{oolib}/program/components/*.so -- mozilla
%attr(755,root,root) %{oolib}/program/filter/*.so

%files mimelinks
%{_datadir}/mimelnk/application/*
