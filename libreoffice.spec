
# Conditional build:
# _with_ra			- build in RA environment

# TODO:
# - finish localzation
# - czech patches from mandrake

Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	1.0.2
Release:	0.95.rc1
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp1.openoffice.pl/pub/OpenOffice.ORG/stable/%{version}/OOo_%{version}_source.tar.bz2
Source1:	ftp://ftp.cs.man.ac.uk/pub/toby/gpc/gpc231.tar.Z
Source2:	%{name}-rsfile.txt
Source3:	%{name}-rsfile-local.txt
Source4:	%{name}-xmlparse.sh
Source6:	%{name}-applnk.tar.gz
Source7:	%{name}-wrapper
Source8:	%{name}-wrapper-component
Source9:	%{name}-langs.txt
Source10:	%{name}-db3.jar
Source11:	%{name}-dictionary.lst.readme
Source12:	OOo_1.0.2beta_LinuxIntel_odk.tar.gz

Source101:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_01_unix.tgz
Source102:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_33_unix.tgz
Source103:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_34_unix.tgz
Source104:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_39_unix.tgz
Source105:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_46_unix.tgz
Source106:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_49_unix.tgz

# Localization scripts from Mandrake
Source302:	%{name}-dpack-lang.pl
Source303:	%{name}-transmute-help-errfile.pl
Source304:	%{name}-create-instdb.pl

Patch0:		%{name}-gcc.patch
#Patch2:		%{name}-mozilla.patch
# Start using some system libraries:
Patch4:		%{name}-system-stlport.patch
Patch5:		%{name}-system-freetype.patch
Patch6:		%{name}-system-getopt.patch
Patch7:		%{name}-freetype-2.1.patch
# Fix broken makefiles
Patch8:		%{name}-braindamage.patch
# Fix psprint /euro to /Euro
Patch10:	%{name}-psprint-euro.patch
# Fix config_office/configure
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
Patch22:	%{name}-system_ra-db.patch

Patch23:	%{name}-udm.patch
Patch24:	%{name}-autodoc.patch

Patch25:	%{name}-xmlsearch.patch
#Patch26:	%{name}-config-java.patch
Patch27:	%{name}-sj2-java.patch

Patch29:	%{name}-gcc2-95.patch
Patch30:	%{name}-system-zlib.patch
Patch31:	%{name}-system-mozilla.patch
Patch32:	%{name}-fix-errno.patch
Patch33:	%{name}-setup-localized-instdb.patch

URL:		http://www.openoffice.org/
%if %{?_with_ra:0}%{!?_with_ra:1}
BuildRequires:	db
BuildRequires:	db-devel
BuildRequires:	db-cxx
BuildRequires:	db-java
BuildRequires:	libstdc++-devel >= 3.2.1
%else
BuildRequires:	db3
BuildRequires:	db3-devel
BuildRequires:	db3-java
BuildRequires:	libstdc++-devel < 3.2.1
%endif
BuildRequires:	gcc
BuildRequires:	gcc-c++
#BuildRequires:	gcc-java

BuildRequires:	STLport-devel >= 4.5.3-3
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-fonts-PEX
BuildRequires:	XFree86-Xvfb
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	perl(XML::Twig)
BuildRequires:	tcsh
BuildRequires:	unzip
BuildRequires:	zip
BuildRequires:	zlib-devel
BuildRequires:	jar
BuildRequires:	jdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-i18n-en = %{version}-%{release}
Requires:	%{name}-dict-en
%if %{?_with_ra:0}%{!?_with_ra:1}
Requires:	libstdc++ >= 3.2.1
Requires:	db
%else
Requires:	libstdc++ < 3.2.1
Requires:	db3
%endif

%define sdkpath OpenOffice.org1.0.2_Beta_SDK

# Languages (English and German are always built)
# FIXME: split generation of language subpackages, otherwise rpm makes
# a broken pipe
%define languages1 ENUS,FREN,GERM,SPAN,ITAL,DTCH,PORT,SWED,POL,RUSS
%define languages2 DAN,GREEK,TURK,CHINSIM,CHINTRAD,JAPN,KOREAN,CZECH,CAT,FINN
%define languages3 ARAB,SLOVAK
%define languages  %{languages1},%{languages2},%{languages3}

# Supported languages for localized help files (others are not
# complete/advanced enough)
%define helplangs1 ENUS,FREN,GERM,SPAN,ITAL,SWED,RUSS,FINN,CZECH,JAPN
%define helplangs2 KOREAN,CHINSIM,CHINTRAD
%define helplangs  %{helplangs1},%{helplangs2}

%define	apps	agenda calc draw fax impress label letter math master memo vcard web writer

%define	_archbuilddir	unxlngi4.pro
%define	installpath	instsetoo/%{_archbuilddir}
%define	subver		641
%define	langinst	01

# Find a free display (resources generation requires X) and sets XDISPLAY
%define init_xdisplay XDISPLAY=0; while /bin/true; do if [ ! -f /tmp/.X$XDISPLAY-lock ]; then sleep 2s; ( /usr/X11R6/bin/Xvfb -ac :$XDISPLAY & 2>&1 > /dev/null); sleep 10s; if [ -f /tmp/.X$XDISPLAY-lock ]; then break; fi; fi; XDISPLAY=$(($XDISPLAY+1)); done

# The virtual X server PID
%define kill_xdisplay kill $(cat /tmp/.X$XDISPLAY-lock)

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

%package devel
Summary:	OpenOffice.org - header files and development documentation
Summary(pl):	OpenOffice.org - pliki nag³ówkowe i dokumentacja
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}

%description devel
OpenOffice.org productivity suite - header files and development
documentation.

%description devel -l pl
Pakiet biurowy OpenOffice.org - pliki nag³ówkowe i dokumentacja.

#
# Internationalization
#
%package i18n-ar
Summary:	OpenOffice.org - interface in Arabic language
Summary(pl):	OpenOffice.org - interfejs w jêzyku arabskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-ar
This package provides resources containing menus and dialogs in
Arabic language.

%description i18n-ar -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
arabskim.

%package i18n-ca
Summary:	OpenOffice.org - interface in Catalan language
Summary(pl):	OpenOffice.org - interfejs w jêzyku kataloñskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-ca
This package provides resources containing menus and dialogs in
Catalan language.

%description i18n-ca -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
kataloñskim.

%package i18n-da
Summary:	OpenOffice.org - interface in Danish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku duñskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-da
This package provides resources containing menus and dialogs in
Danish language.

%description i18n-da -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
duñskim.

%package i18n-de
Summary:	OpenOffice.org - interface in German language
Summary(pl):	OpenOffice.org - interfejs w jêzyku niemieckim
Group:		Applications/Office
Requires:	openoffice

%description i18n-de
This package provides resources containing menus and dialogs in
German language.

%description i18n-de -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
niemieckim.

%package i18n-el
Summary:	OpenOffice.org - interface in Greek language
Summary(pl):	OpenOffice.org - interfejs w jêzyku greckim
Group:		Applications/Office
Requires:	openoffice

%description i18n-el
This package provides resources containing menus and dialogs in
Greek language.

%description i18n-el -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
greckim.

%package i18n-en
Summary:	OpenOffice.org - interface in English language
Summary(pl):	OpenOffice.org - interfejs w jêzyku angielskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-en
This package provides resources containing menus and dialogs in
English language.

%description i18n-en -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
angielskim.

%package i18n-es
Summary:	OpenOffice.org - interface in Spanish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku hiszpañskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-es
This package provides resources containing menus and dialogs in
Spanish language.

%description i18n-es -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
hiszpañskim.

%package i18n-fi
Summary:	OpenOffice.org - interface in English language
Summary(pl):	OpenOffice.org - interfejs w jêzyku angielskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-fi
This package provides resources containing menus and dialogs in
Finnish language.

%description i18n-fi -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
fiñskim.

%package i18n-fr
Summary:	OpenOffice.org - interface in French language
Summary(pl):	OpenOffice.org - interfejs w jêzyku francuskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-fr
This package provides resources containing menus and dialogs in
French language.

%description i18n-fr -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
francuskim.

%package i18n-it
Summary:	OpenOffice.org - interface in Italian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku w³oskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-it
This package provides resources containing menus and dialogs in
Italian language.

%description i18n-it -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
w³oskim.

%package i18n-ja
Summary:	OpenOffice.org - interface in Japan language
Summary(pl):	OpenOffice.org - interfejs w jêzyku japoñskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-ja
This package provides resources containing menus and dialogs in
Japan language.

%description i18n-ja -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
japoñskim.

%package i18n-ko
Summary:	OpenOffice.org - interface in Korean language
Summary(pl):	OpenOffice.org - interfejs w jêzyku koreañskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-ko
This package provides resources containing menus and dialogs in
Korean language.

%description i18n-ko -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
koreañskim.

%package i18n-nl
Summary:	OpenOffice.org - interface in Dutch language
Summary(pl):	OpenOffice.org - interfejs w jêzyku holenderskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-nl
This package provides resources containing menus and dialogs in
Dutch language.

%description i18n-nl -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
holenderskim.

%package i18n-pl
Summary:	OpenOffice.org - interface in Polish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku polskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-pl
This package provides resources containing menus and dialogs in
Polish language.

%description i18n-pl -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
polskim.

%package i18n-pt
Summary:	OpenOffice.org - interface in Portuguese language
Summary(pl):	OpenOffice.org - interfejs w jêzyku portugalskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-pt
This package provides resources containing menus and dialogs in
Portuguese language.

%description i18n-pt -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
portugalskim.

%package i18n-ru
Summary:	OpenOffice.org - interface in Russian language
Summary(pl):	OpenOffice.org - interfejs w jêzyku rosyjskim
Group:		Applications/Office
Requires:	openoffice

%description i18n-ru
This package provides resources containing menus and dialogs in
Russian language.

%description i18n-ru -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
rosyjskim.

%package i18n-sv
Summary:	OpenOffice.org - interface in Swedish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku szwedzkim
Group:		Applications/Office
Requires:	openoffice

%description i18n-sv
This package provides resources containing menus and dialogs in
Swedish language.

%description i18n-sv -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
szwedzkim.

%package i18n-tr
Summary:	OpenOffice.org - interface in Turkish language
Summary(pl):	OpenOffice.org - interfejs w jêzyku tureckim
Group:		Applications/Office
Requires:	openoffice

%description i18n-tr
This package provides resources containing menus and dialogs in
Turkish language.

%description i18n-tr -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
tureckim.

%package i18n-zh_CN
Summary:	OpenOffice.org - interface in Chinese language for China
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim dla Chin
Group:		Applications/Office
Requires:	openoffice

%description i18n-zh_CN
This package provides resources containing menus and dialogs in
Chinese language for China.

%description i18n-zh_CN -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim dla Chin.

%package i18n-zh_TW
Summary:	OpenOffice.org - interface in Chinese language for Taiwan
Summary(pl):	OpenOffice.org - interfejs w jêzyku chiñskim dla Tajwanu
Group:		Applications/Office
Requires:	openoffice

%description i18n-zh_TW
This package provides resources containing menus and dialogs in
Chinese language for Taiwan.

%description i18n-zh_TW -l pl
Ten pakiet dostarcza zasoby zawieraj±ce menu i okna dialogowe w jêzyku
chiñskim dla Tajwanu.

%prep
%setup -q -n oo_%{version}_src
%patch0 -p1
#%patch2 -p1

%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%patch8 -p1
%patch10 -p1
#%patch11 -p1
#%patch13 -p1
%patch14 -p1
%patch16 -p1
%patch18 -p1

%patch19 -p1
%patch20 -p1
%if 0%{!?_with_ra:1}
%patch21 -p1
%else
%patch22 -p1
%endif

%patch23 -p1
%patch24 -p1
%patch25 -p1
#%patch26 -p1
%patch27 -p1

%patch29 -p1

%patch30 -p1

rm -f moz/prj/d.lst
%patch31 -p1
%patch32 -p1
%patch33 -p1

# gcc 2 include error hack:
rm -rf autodoc/source/inc/utility

install %{SOURCE1} external
cd external; tar fxz %{SOURCE1}; cp -fr gpc231/* gpc
cd ..

%if %{?_with_ra:0}%{!?_with_ra:1}
install -d solver/%{subver}/%{_archbuilddir}/lib
cp -f /lib/libgcc_s.so.1* solver/%{subver}/%{_archbuilddir}/lib
cp /usr/lib/libstdc++.so.5* solver/%{subver}/%{_archbuilddir}/lib
%endif

chmod +x solenv/bin/zipdep.pl

###################
## BUILD
###################
%build
CC=%{__cc}
CXX=%{__cxx}
GCJ=gcj
JAVA_HOME="/usr/lib/java"
export JAVA_HOME CC CXX GCJ

cd config_office
autoconf

%configure2_13 \
	--with-jdk-home=$JAVA_HOME \
	--with-stlport4-home=/usr \
	--with-lang="%{languages}" \
	--with-x

cd ..

cat <<EOF > prep
#!/bin/tcsh
./bootstrap
EOF
chmod u+rx prep
./prep

install -d solver/%{subver}/%{_archbuilddir}/bin
%if %{?_with_ra:0}%{!?_with_ra:1}
install /usr/lib/db.jar solver/%{subver}/%{_archbuilddir}/bin/db.jar
%else
install %{SOURCE10} solver/%{subver}/%{_archbuilddir}/bin/db.jar
%endif

cat <<EOF > compile
#!/bin/tcsh
source LinuxIntelEnv.Set
dmake -p -v
EOF
chmod u+rx compile
./compile


#########################
## INSTALL
#########################
%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{oolib}



#########################
# DEVEL STUFF
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

tar zxvf %{SOURCE12}

cat %{sdkpath}/setsdkenv_unix.in | \
    sed "s#@OO_SDK_HOME@#%{_datadir}/%{name}#" |\
    sed "s#@OFFICE_HOME@#%{_datadir}/openoffice#" |\
    sed "s#@OO_SDK_MAKE_HOME@#%{_bindir}#" |\
    sed "s#@OO_SDK_CPP_HOME@#%{_bindir}#" |\
    sed "s#@OO_SDK_CPP_HOME@#%{_includedir}/stlport#" |\
    sed "s#@OO_SDK_JAVA_HOME@#%{_libdir}/java#" |\
    sed "s#@OO_SDK_ANT_HOME@##" |\
    sed "s#@SDK_AUTO_DEPLOYMENT@#YES#" > $RPM_BUILD_ROOT%{_bindir}/oosdkenv

cp %{sdkpath}/linux/lib/libofficebean.so $RPM_BUILD_ROOT%{oolib}

cp solver/%{subver}/%{_archbuilddir}/lib/libjuh.so $RPM_BUILD_ROOT%{oolib}
cp solver/%{subver}/%{_archbuilddir}/lib/libprot_uno_uno.so $RPM_BUILD_ROOT%{oolib}
cp solver/%{subver}/%{_archbuilddir}/lib/librmcxt.so* $RPM_BUILD_ROOT%{oolib}

cp -rf %{sdkpath}/classes $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rf %{sdkpath}/settings $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rf %{sdkpath}/examples $RPM_BUILD_ROOT%{_datadir}/%{name}

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/xml

cp solver/%{subver}/%{_archbuilddir}/xml/acceptor.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/corefl.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/dynamicloader.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/invadp.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/module-description.dtd $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/rdbtdp.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/smgr.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/tdmgr.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/brdgfctr.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/cpld.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/impreg.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/inv.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/namingservice.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/remotebridge.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/stm.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/uuresolver.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/connectr.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/defreg.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/insp.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/jen.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/proxyfac.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/simreg.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml
cp solver/%{subver}/%{_archbuilddir}/xml/tcv.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/xml

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/include

cp -rf solver/%{subver}/%{_archbuilddir}/inc/bridges $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/com $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/cppu $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/cppuhelper $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/osl $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/rtl $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/sal $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/salhelper $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/store $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/typelib $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/uno $RPM_BUILD_ROOT%{_datadir}/%{name}/include
cp -rf solver/%{subver}/%{_archbuilddir}/inc/udkversion.mk $RPM_BUILD_ROOT%{_datadir}/%{name}/include

cp -rf solver/%{subver}/%{_archbuilddir}/idl $RPM_BUILD_ROOT%{_datadir}/%{name}
# END OF DEVEL STUFF
#########################

if [ -z "$DISPLAY" ]; then
	%{init_xdisplay}
fi
RESPONSE_FILE=$PWD/rsfile.ins
OLDPATH="`pwd`"
cd %{installpath}/%{langinst}/normal/
  # --short-circuit support
  if [ -f setup.ins.oorg ]; then
	cp -f setup.ins.oorg setup.ins
  else
	cp -f setup.ins setup.ins.oorg
  fi
  cat %{SOURCE2} | sed -e "s|@DESTDIR@|$RPM_BUILD_ROOT%{oolib}|" > $RESPONSE_FILE

  # Localize New and Wizard menus and OfficeObjects
  cp -p setup.ins setup.ins.localized
  (
  for i in `( cd ../../; echo [0-9][0-9] ) | sed 's/%{langinst} //'`; do
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
	| sed "s/^--//;/^ConfigurationItem/s/\(Name\|Titel\)/$i&/"
      echo
    fi
  done
  ) | awk ' $1 ~ /Value/ { l=$0; sub(/^.*= "/,"",l); sub(/";.*$/,"",l); sub(/%PRODUCTNAME/,"OpenOffice.org",l); sub(/%PRODUCTVERSION/,"%{version}",l); n=n+1; str="@@REPLACEME" n "@@"; s="\"" str "\""; sub(/".*"/,s); printf "s|%s|%s|\n", str, l > "Common.xml.sed" } { print } ' \
    >> setup.ins

if [ -z "$DISPLAY" ]; then
	DISPLAY=:$XDISPLAY ./setup -R:$RESPONSE_FILE
	%{kill_xdisplay}
else
	./setup -R:$RESPONSE_FILE
fi	

cd "$OLDPATH"

# Copy all localized resources to destination directory
install -d $RPM_BUILD_ROOT%{oolib}/program/resource
cp -f solver/%{subver}/%{_archbuilddir}/bin/*.res $RPM_BUILD_ROOT%{oolib}/program/resource

# don't care about main_transform.xsl, it looks safe to overwrite
for file in %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} %{SOURCE105} %{SOURCE106}
do
  tar zxvf $file
done
for file in s*.zip; do
  dir=`echo $file | sed -e "s/\(s[a-z]*\)[0-9]*.zip/\1/"`
  [[ "$dir" = "shared" ]] && dir="common"
  prefix=`echo $file | sed -e "s/s[a-z]*\([0-9]*\).zip/\1/"`
  langname=`cat %{SOURCE9} | grep ^$prefix | cut -d: -f2`
  install -d $RPM_BUILD_ROOT%{oolib}/help/$langname
  unzip -d $RPM_BUILD_ROOT%{oolib}/help/$langname -o $file
done
rm -f *.zip

#
# Extract language packs
#
(
    cd %{installpath}
    install -m 755 %{SOURCE302} oo_dpack_lang
    install -m 755 %{SOURCE303} oo_fixup_help
    install -m 755 %{SOURCE304} oo_gen_instdb
    
    LANGS=`echo "%{languages}" | sed -e "s/,/ /g"`
    for res in $LANGS
    do
	prefix=`cat %{SOURCE9} | grep ":$res:" | cut -d: -f1`
	isocode=`cat %{SOURCE9} | grep ":$res:" | cut -d: -f2`
	tempdir=$RPM_BUILD_ROOT%{oolib}-$isocode
	mkdir -p $tempdir

	# may extract help files, if known to be localized enough
	case ",%{helplangs}," in
	*,$res,*)
    	    ./oo_dpack_lang -d=$tempdir -i=$prefix/normal/setup.ins -h

# TODO: Check this oo_fixup_help thing
#      # fix permissions
#      find $tempdir/help/$isocode -type d | xargs chmod 755
#      find $tempdir/help/$isocode -type f | xargs chmod 644
#      # transmute error file to suggest installation of
#      # OpenOffice.org-help-* package
#      mv -f $tempdir/help/$isocode/err.html orig.err.html
#      # nuke broken <meta http-equiv="..."/> tag and entities in
#      # Finnish err.html
#      [[ "$isocode" = "fi" ]] && {
#        perl -pi -MEncode -MHTML::Entities -pi \
#             -e 's/<meta\s+http-equiv=[^>]+>//i;' \
#             -e '$_=Encode::encode_utf8 decode_entities $_' orig.err.html
#      }
#      ./oo_fixup_help $isocode orig.err.html >$tempdir/help/$isocode/err.html
#      rm -f orig.err.html
	    find $tempdir/help/$isocode "(" -type f -or -type l ")" -print | \
    		sed -e "s|$RPM_BUILD_ROOT%{oolib}-$isocode|%{oolib}|g" > $FILELIST.help.$isocode.in
	    find $tempdir/help/$isocode -type d -print | \
		sed -e "s|$RPM_BUILD_ROOT%{oolib}-$isocode|%dir %{oolib}|g" | sort -u >> $FILELIST.help.$isocode.in
	    # keep err.html and custom.css in main l10n package
#    	    grep -v "help/$isocode\(\|/\(err.html\|custom.css\)\)$" $FILELIST.help.$isocode.in > $FILELIST.help.$isocode
	    rm -f $FILELIST.help.$isocode.in
	    ;;
	*)
	    # default, create empty help directory
	    # NOTE: with Patch16 (help-fallback-en) we fallback to English help files
	    ./oo_dpack_lang -d=$tempdir -i=$prefix/normal/setup.ins
	    mkdir -p $tempdir/help/$isocode
	    ;;
	esac

	# link ooo resource files to iso files
	(
	    cd $tempdir/program/resource
            file1=`echo ooo*.res`
	    file2=`echo $file1 | sed "s|ooo|iso|"`
	    ln -sf $file1 $file2
	)

	# generate localized instdb.ins files, aka let the right files to
	# be installed for a user installation
	if [ "$isocode" != "en" ]; then
	    ./oo_gen_instdb -d $tempdir -i $prefix/normal/setup.ins \
		-o $tempdir/program/instdb.ins.$isocode -pv "%{version}"
	    perl -pi -e "s|$tempdir|%{oolib}|g" \
		$tempdir/program/instdb.ins.$isocode
	fi
	
	# build file list
	find $tempdir "(" -type f -or -type l ")" -print | \
	    sed -e "s|$tempdir|%{oolib}|g" > $FILELIST.$isocode
	find $tempdir -type d -print | \
	    sed -e "s|$tempdir|%dir %{oolib}|g" | sort -u >> $FILELIST.$isocode

	# remove duplicates from l10n-en package
	if [ "$isocode" != "en" ]; then
	    mv $FILELIST.$isocode $FILELIST.$isocode.in
	    perl -e "sub cat_ { local *F; open F, \$_[0] or return; my @l = <F>; wantarray() ? @l : join '', @l }; \
		sub difference2 { my %l; @l{@{\$_[1]}} = (); grep { !exists \$l{\$_} } @{\$_[0]} }; \
		print difference2([ cat_(\"$FILELIST.$isocode.in\") ], [ cat_(\"$FILELIST.en\") ])" \
		> $FILELIST.$isocode
	    rm -f $FILELIST.$isocode.in
	fi

	# move files here and there
	cp -af $tempdir/* $RPM_BUILD_ROOT%{oolib}/
	rm -rf $tempdir
    
	HOWMUCH=`ls $RPM_BUILD_ROOT%{oolib}/help/$isocode 2>/dev/null | wc -l`
	if [ $HOWMUCH -eq 0 ]; then rm -rf $RPM_BUILD_ROOT%{oolib}/help/$isocode; fi
    done
)

mv $RPM_BUILD_ROOT%{oolib}/help/{zh-CN,zh_CN}
mv $RPM_BUILD_ROOT%{oolib}/help/{zh-TW,zh_TW}
mv $RPM_BUILD_ROOT%{oolib}/program/instdb.ins.{zh-CN,zh_CN}
mv $RPM_BUILD_ROOT%{oolib}/program/instdb.ins.{zh-TW,zh_TW}

# Remove unnecessary binaries
for app in %{apps}
do
    rm -f $RPM_BUILD_ROOT%{oolib}/program/s${app}
done

install -d $RPM_BUILD_ROOT%{_applnkdir}
gunzip -dc %{SOURCE6} | tar xf - -C $RPM_BUILD_ROOT%{_applnkdir}

## Remove any fake classes
#rm -rf $RPM_BUILD_ROOT%{oolib}/program/classes

# Remove stuff that should come from system libraries
rm -rf $RPM_BUILD_ROOT%{oolib}/program/libdb-*
rm -rf $RPM_BUILD_ROOT%{oolib}/program/libdb_*

# Fix GNOME & KDE
install -d $RPM_BUILD_ROOT%{_datadir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT%{oolib}/share/kde/net/mimelnk/share/mimelnk $RPM_BUILD_ROOT%{_datadir}
cp -rf $RPM_BUILD_ROOT%{oolib}/share/kde/net/mimelnk/share/icons/* $RPM_BUILD_ROOT%{_pixmapsdir}
cp -rf $RPM_BUILD_ROOT%{oolib}/share/icons/* $RPM_BUILD_ROOT%{_pixmapsdir}
rm -rf $RPM_BUILD_ROOT%{oolib}/share/kde
rm -rf $RPM_BUILD_ROOT%{oolib}/share/cde
rm -rf $RPM_BUILD_ROOT%{oolib}/share/gnome
rm -rf $RPM_BUILD_ROOT%{oolib}/share/icons

# Now fixup Common.xml
COMMON_XML_SED=$PWD/%{installpath}/%{langinst}/normal/Common.xml.sed
OLDPATH="`pwd`"
cd $RPM_BUILD_ROOT%{oolib}/share/config/registry/instance/org/openoffice/Office/
  sed -e "s|<cfg:string cfg:type=\"string\" cfg:name=\"\([^\"]*\)\"\(>@@REPLACEME.*@@</cfg:\)string>|<cfg:value xml:lang=\"\1\"\2value>|" Common.xml > Common.xml.tmp
  sed -f $COMMON_XML_SED Common.xml.tmp > Common.xml
  rm -f Common.xml.tmp
cd "$OLDPATH"

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

# Fixup installation directory
perl -pi -e "s|$RPM_BUILD_ROOT||g" \
  $RPM_BUILD_ROOT%{oolib}/share/config/registry/instance/org/openoffice/Office/Common.xml

# Install autoresponse file for user installation
install -d $RPM_BUILD_ROOT%{_sysconfdir}/openoffice
cat %{SOURCE3} > $RPM_BUILD_ROOT%{_sysconfdir}/openoffice/autoresponse.conf

# Install OpenOffice.org wrapper script
install -d $RPM_BUILD_ROOT%{_bindir}
cat %{SOURCE7} | sed -e "s/@OOVERSION@/%{subver}/" > $RPM_BUILD_ROOT%{_bindir}/ooffice

# Install component wrapper scripts
install -d $RPM_BUILD_ROOT%{_bindir}
for app in %{apps}; do
  cat %{SOURCE8} | sed -e "s/@APP@/${app}/" > $RPM_BUILD_ROOT%{_bindir}/oo${app}
done

## Install new template and gallery content
#mkdir -p $RPM_BUILD_ROOT%{oolib}/share/template
#mkdir -p $RPM_BUILD_ROOT%{oolib}/share/gallery
#(cd $RPM_BUILD_ROOT%{oolib}/share;
#  tar fxvj %{SOURCE10}
#  tar fxvj %{SOURCE11}
#)

echo 'UNO_WRITERDB=$SYSUSERCONFIG/.user60.rdb
' >> $RPM_BUILD_ROOT%{oolib}/program/unorc

# Build system in OO SUX
rm -f $RPM_BUILD_ROOT%{oolib}/program/libstdc++*
rm -f $RPM_BUILD_ROOT%{oolib}/program/libstlport_gcc.so
rm -f $RPM_BUILD_ROOT%{oolib}/program/libgcc_s.so.1

rm -rf $RPM_BUILD_ROOT%{oolib}/share/template/{internal,wizard}

# package files
FindI18N() {
#    $1 - short language name	eg. pl
#    $2 - long language name	eg. polish
#    $3 - digit code		eg. 48
#    $4 - "strange" shortcut	eg. pol

    BUILDDIR=%(pwd)

    echo "%defattr(644,root,root,755)" > "i18n-$1"
    
    DIRS="%{oolib}/user/autotext/$2"
    DIRS="$DIRS %{oolib}/share/autotext/$2"
    DIRS="$DIRS %{oolib}/share/template/$2"
    DIRS="$DIRS %{oolib}/help/$1"
    DIRS="$DIRS	%{oolib}/share/wordbook/$2"
    
    for DIR in $DIRS
    do
	if [ -d "$RPM_BUILD_ROOT/$DIR" ]; then
	    echo "%lang($1) $DIR" >> "i18n-$1"
	fi
    done    
    
    if [ "$1" = "en" ]; then
        FILES=`(cd $RPM_BUILD_ROOT%{oolib}/user/config; ls 2>/dev/null | grep -v "_" | grep -v "registry" ||:)`
    elif [ ! "$1" = "" ]; then
	FILES=`(cd $RPM_BUILD_ROOT%{oolib}/user/config; ls 2>/dev/null | grep "_$4" ||:)`
    fi	
    for FILE in $FILES; do
        echo "%lang($1) %{oolib}/user/config/$FILE" >> "i18n-$1"
    done    

    SUBF="abp analysis basctl bib cal cnt date dba dbi dbp dbu"
    SUBF="$SUBF dbw dkt egi eme epb epg epn epp eps ept eur for"
    SUBF="$SUBF frm gal imp iso jvm lgd oem ofa oic ooo pcr preload"
    SUBF="$SUBF san sc sch sd set set_pp1 sfx sm spa stt svs svt"
    SUBF="$SUBF svx sw tpl tplx uui vcl wwz"
    SVER=%{subver}
    
    for FILE in $SUBF
    do
	F="%{oolib}/program/resource/$FILE$SVER$3.res"
	if [ -f "$RPM_BUILD_ROOT$F" ]; then
	    echo "%lang($1) $F" >> "i18n-$1"
	fi	
    done

    if [ -f $RPM_BUILD_ROOT/%{oolib}/program/instdb.ins.$1 ]
    then
	echo "%lang($1) %{oolib}/program/instdb.ins.$1" >> "i18n-$1"
    fi

    unzip -l solver/%{subver}/%{_archbuilddir}/pck/palletes$3.zip | sed "s/.* //" | awk '(flag==1)&&/----/{exit};(flag==1){print;};/----/{flag=1};' >> "i18n-$1"
    
    if [ ! -d "$RPM_BUILD_ROOT%{oolib}/help/$1" ]; then
	ln -sf %{oolib}/help/en $RPM_BUILD_ROOT%{oolib}/help/$1
	echo "%lang($1) %{oolib}/help/$1" >> "i18n-$1"
    fi
}

FindI18N ar arabic 96 ""
FindI18N ca catalan 37 ""
FindI18N da danish 45 ""
FindI18N de german 49 ""
FindI18N es spanish 34 ""
FindI18N el greek 30 ""
FindI18N en english 01 ""
FindI18N fi finnish 35 ""
FindI18N fr french 33 ""
FindI18N it italian 39 ""
FindI18N ja japanese 81 ""
FindI18N ko korean 82 ""
FindI18N nl dutch 31 ""
FindI18N pl polish 48 "pol"
FindI18N pt portuguese 03 ""
FindI18N ru russian 07 "rus"
FindI18N sv swedish 46 ""
FindI18N tr turkish 90 ""
FindI18N zh_CN chinese_simplified 86 ""
FindI18N zh_TW chinese_traditional 88 ""

cp %{SOURCE11} $RPM_BUILD_ROOT%{dictlst}-readme
rm -f $RPM_BUILD_ROOT%{dictlst}
touch $RPM_BUILD_ROOT%{dictlst}

# remove files which we know that were moved to openoffice-dict.spec
for file in en_US.aff en_US.dic hyph_da.dic hyph_de.dic hyph_en.dic \
    hyph_ru.dic th_en_US.dat th_en_US.idx
do
    rm -f $RPM_BUILD_ROOT%{oolib}/share/dict/ooo/$file
done


####################
## CLEAN
####################
%clean
#rm -rf $RPM_BUILD_ROOT

####################
## FILES
####################
%files
%defattr(644,root,root,755)
#%%doc readlicense/source/license/unx/LICENSE
%doc %{oolib}/LICENSE*
%doc %{oolib}/README*

%dir %{_sysconfdir}/openoffice
%config %{_sysconfdir}/openoffice/autoresponse.conf

%{_applnkdir}/Office
%{_pixmapsdir}/*.png

%{_pixmapsdir}/locolor/16x16/apps/*.xpm
%{_pixmapsdir}/locolor/32x32/apps/*.xpm
%{_pixmapsdir}/hicolor/32x32/apps/*.xpm
%{_pixmapsdir}/hicolor/48x48/apps/*.xpm

%{_datadir}/mimelnk/application/*

%{oolib}/program/*.rdb
%{oolib}/program/*.bmp

%{oolib}/program/sofficerc
%{oolib}/program/unorc
%{oolib}/program/bootstraprc
%{oolib}/program/configmgrrc
%{oolib}/program/instdb.ins

# dirs/trees
%{oolib}/program/classes
%{oolib}/program/addin

%dir %{oolib}/program/resource
%{oolib}/program/resource/bmp.res
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
%{oolib}/share/autocorr
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
%{oolib}/share/wordbook

%{oolib}/share/autotext/english
%{oolib}/share/template/english
%ghost %{oolib}/share/dict/ooo/dictionary.lst
%{oolib}/share/dict/ooo/dictionary.lst-readme

%dir %{oolib}/user
%dir %{oolib}/user/autotext
%{oolib}/user/basic
%dir %{oolib}/user/config
%{oolib}/user/config/registry
%{oolib}/user/database
%{oolib}/user/gallery
%{oolib}/user/psprint

%{oolib}/user/autotext/english

# Programs
%attr(755,root,root) %{_bindir}/oo*

%attr(755,root,root) %{oolib}/setup
%attr(755,root,root) %{oolib}/spadmin

%attr(755,root,root) %{oolib}/program/*.bin
%attr(755,root,root) %{oolib}/program/fromtemplate
%attr(755,root,root) %{oolib}/program/gnomeint
%attr(755,root,root) %{oolib}/program/javaldx
%attr(755,root,root) %{oolib}/program/jvmsetup
%attr(755,root,root) %{oolib}/program/nswrapper
%attr(755,root,root) %{oolib}/program/setup
%attr(755,root,root) %{oolib}/program/soffice
%attr(755,root,root) %{oolib}/program/sopatchlevel.sh
%attr(755,root,root) %{oolib}/program/spadmin


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

%files devel
%defattr(644,root,root,755)
%doc %{sdkpath}/docs/*
%attr(755,root,root) %{_bindir}/oosdkenv
%{_datadir}/%{name}

%files i18n-ar -f i18n-ar
%files i18n-ca -f i18n-ca
%files i18n-da -f i18n-da
%files i18n-de -f i18n-de
%files i18n-el -f i18n-el
%files i18n-en -f i18n-en
%files i18n-es -f i18n-es
%files i18n-fi -f i18n-fi
%files i18n-fr -f i18n-fr
%files i18n-it -f i18n-it
%files i18n-ja -f i18n-ja
%files i18n-ko -f i18n-ko
%files i18n-nl -f i18n-nl
%files i18n-pl -f i18n-pl
%files i18n-pt -f i18n-pt
%files i18n-ru -f i18n-ru
%files i18n-sv -f i18n-sv
%files i18n-tr -f i18n-tr
%files i18n-zh_CN -f i18n-zh_CN
%files i18n-zh_TW -f i18n-zh_TW
