
# Conditional build:
# _with_ra			- build in RA environment

# TODO:
# - finish localzation
# - split into language packages
# - czech patches from mandrake
# - correct mirrors
# - add missing dictionaries

Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	1.0.2
Release:	0.88
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

Source101:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_01_unix.tgz
Source102:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_33_unix.tgz
Source103:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_34_unix.tgz
Source104:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_39_unix.tgz
Source105:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_46_unix.tgz
Source106:	ftp://ftp.task.gda.pl/mirror/ftp.openoffice.org/contrib/helpfiles/helpcontent_49_unix.tgz

# Wordbooks: http://whiteboard.openoffice.org/lingucomponent/download_dictionary.html
# renamed sources from:
# ftp://ftp.openoffice.pl/OpenOffice.ORG/contrib/dictionaries
Source201:	%{name}-bg_BG.zip
Source202:	%{name}-ca_ES.zip
Source203:	%{name}-cs_CZ.zip
Source204:	%{name}-da_DK.zip
Source205:	%{name}-de_CH.zip
Source206:	%{name}-de_DE.zip
Source207:	%{name}-el_GR.zip
Source208:	%{name}-en_CA.zip
Source209:	%{name}-en_GB.zip
Source210:	%{name}-en_US.zip
Source211:	%{name}-es_ES.zip
Source212:	%{name}-fr_FR.zip
Source213:	%{name}-ga_IE.zip
Source214:	%{name}-gl_ES.zip
Source215:	%{name}-hr_HR.zip
Source216:	%{name}-hu_HU.zip
Source217:	%{name}-it_IT.zip
Source218:	%{name}-lt_LT.zip
Source219:	%{name}-nb_NO.zip
Source220:	%{name}-nl_NL.zip
Source221:	%{name}-nn_NO.zip
Source222:	%{name}-pl_PL.zip
Source223:	%{name}-pt_BR.zip
Source224:	%{name}-pt_PT.zip
Source225:	%{name}-sk_SK.zip
Source226:	%{name}-sl_SI.zip
Source227:	%{name}-sv_SE.zip
Source228:	%{name}-uk_UA.zip
Source229:	%{name}-ru_RU.zip
# This one is special, as there is no country associated with Latin,
# nor should it be %lang(la).
Source230:	%{name}-la.zip

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
BuildRequires:	tcsh
BuildRequires:	unzip
BuildRequires:	zip
BuildRequires:	zlib-devel
BuildRequires:	jar
BuildRequires:	jdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-i18n-en = %{version}-%{release}
%if %{?_with_ra:0}%{!?_with_ra:1}
Requires:	libstdc++ >= 3.2.1
Requires:	db
%else
Requires:	libstdc++ < 3.2.1
Requires:	db3
%endif


%define	langs	"ENUS,FREN,GERM,SPAN,ITAL,DTCH,PORT,DAN,GREEK,POL,SWED,TURK,RUSS,CZECH"
%define	apps	agenda calc draw fax impress label letter math master memo vcard web writer
%define	wordbooks1	%{SOURCE201} %{SOURCE202} %{SOURCE203} %{SOURCE204} %{SOURCE205}
%define wordbooks2	%{SOURCE206} %{SOURCE207} %{SOURCE208} %{SOURCE209} %{SOURCE210}
%define wordbooks3	%{SOURCE211} %{SOURCE212} %{SOURCE213} %{SOURCE214} %{SOURCE215}
%define wordbooks4	%{SOURCE216} %{SOURCE217} %{SOURCE218} %{SOURCE219} %{SOURCE220}
%define wordbooks5	%{SOURCE221} %{SOURCE222} %{SOURCE223} %{SOURCE224} %{SOURCE225}
%define wordbooks6	%{SOURCE226} %{SOURCE227} %{SOURCE228} %{SOURCE229} %{SOURCE230}
%define wordbooks	%wordbooks1 %wordbooks2 %wordbooks3 %wordbooks4 %wordbooks5 %wordbooks6

%define	_archbuilddir	unxlngi4.pro
%define	installpath	instsetoo/%{_archbuilddir}
%define	subver		641
%define	langinst	01

# Find a free display (resources generation requires X) and sets XDISPLAY
%define init_xdisplay XDISPLAY=0; while /bin/true; do if [ ! -f /tmp/.X$XDISPLAY-lock ]; then sleep 2s; ( /usr/X11R6/bin/Xvfb -ac :$XDISPLAY & 2>&1 > /dev/null); sleep 10s; if [ -f /tmp/.X$XDISPLAY-lock ]; then break; fi; fi; XDISPLAY=$(($XDISPLAY+1)); done

# The virtual X server PID
%define kill_xdisplay kill $(cat /tmp/.X$XDISPLAY-lock)

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

#
# Internationalization
#
%package i18n-ar
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-ar
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-ca
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-ca
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-da
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-da
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-de
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-de
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-es
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-es
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-el
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-el
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-en
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-en
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-fi
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-fi
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-fr
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-fr
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-it
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-it
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-ja
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-ja
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-ko
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-ko
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-nl
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-nl
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-pl
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-pl
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-pt
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-pt
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-ru
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-ru
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-sv
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-sv
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-tr
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-tr
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-zh_CN
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-zh_CN
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

%package i18n-zh_TW
Summary:	OpenOffice.org internationalization
Group:		Applications/Office
Requires:	openoffice

%description i18n-zh_TW
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides resources containing
menus and dialogs for various languages.

#
# Dictionaries
#
%package dict-bg
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-bg
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-ca
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-ca
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-cs
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-cs
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-da
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-da
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-de
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-de
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-el
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-el
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-en
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-en
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-es
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-es
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-fr
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-fr
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-ga
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-ga
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-gl
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-gl
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-hr
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-hr
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-hu
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-hu
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-it
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-it
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-la
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-la
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-lt
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-lt
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-nb
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-nb
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-nl
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-nl
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-nn
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-nn
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-pl
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-pl
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-pt
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-pt
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-ru
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-ru
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-sk
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-sk
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-sl
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-sl
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-sv
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-sv
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

%package dict-uk
Summary:	OpenOffice.org dictionary
Group:		Applications/Office
Requires:	openoffice

%description dict-uk
OpenOffice.org is an Open Source, community-developed, multi-platform
office productivity suite.  This package provides spell checker dictionaries.

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
	--with-lang=%{langs} \
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

# think: f0_061 should contains uui641%{langinst}.res file!
#cp solver/%{subver}/%{_archbuilddir}/bin/setup_services.rdb solver/%{subver}/%{_archbuilddir}/bin/uno_writerdb.rdb
#rm -f f0_061
#zip -j -5 "f0_061" solver/%{subver}/%{_archbuilddir}/bin/uno_writerdb.rdb
#mv f0_061.zip %{installpath}/%{langinst}/normal/f0_061

install -d $RPM_BUILD_ROOT%{_libdir}/openoffice

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
  cat %{SOURCE2} | sed -e "s|@DESTDIR@|$RPM_BUILD_ROOT%{_libdir}/openoffice|" > $RESPONSE_FILE

  # Add additional wordbooks

  for dict in %{wordbooks} # somepath/de_AT.zip %{SOURCE50}
   do
    loc=`echo $dict | sed 's~^.*/%{name}-\([a-zA-Z_]*\).zip$~\1~'`
###########################
    perl -ni -e "/^ConfigurationItem gid_Configurationitem_Oo_${loc}_Spellchecker/ .. /^End/ or print" setup.ins
#	awk "BEGIN { o=1} /^End$/ { if(o==0){o=1}} u^ConfigurationItem gid_Configurationitem_Oo_${loc}_Spellchecker$/ { if (o==1) { o=0} } { if(o==1) { print } }" setup.ins
    cat >> setup.ins <<EOF
ConfigurationItem gid_Configurationitem_Oo_${loc}_Spellchecker
        ModuleID         = gid_Module_Root;
        Path             = "org.openoffice.Office.Linguistic/ServiceManager/SpellCheckerList";
        Key                      = "`echo $loc | sed 's/_/-/'`";
        Value            = "org.openoffice.lingu.MySpellSpellChecker";
        Styles           = (CFG_STRINGLIST, CREATE);
End

EOF
###########################
  done

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
install -d $RPM_BUILD_ROOT%{_libdir}/openoffice/program/resource
cp -f solver/%{subver}/%{_archbuilddir}/bin/*.res $RPM_BUILD_ROOT%{_libdir}/openoffice/program/resource

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
  install -d $RPM_BUILD_ROOT%{_libdir}/openoffice/help/$langname
  unzip -d $RPM_BUILD_ROOT%{_libdir}/openoffice/help/$langname -o $file
done
rm -f *.zip

for file in solver/%{subver}/%{_archbuilddir}/pck/autocorr*.zip
do
  [[ -n `echo "$file" | grep "01"` ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/autocorr $file
done

for prefix in `(cd solver/%{subver}/%{_archbuilddir}/bin/ ; echo [0-9][0-9] ) | sed s@solver/%{subver}/%{_archbuilddir}/bin/@@ | sed s/01//`
do
  language=`cat %{SOURCE9} | grep ^$prefix | cut -d: -f5`
  lang=`cat %{SOURCE9} | grep ^$prefix | cut -d: -f6`

  install -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language/wizard/styles
  install -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language/wizard/web
  install -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language/internal

# WRITEME:
#  unzip solver/%{subver}/%{_archbuilddir}/pck/palletes$prefix.zip
#  for p in *.so?
#  do
#    mv $p `echo $p | sed s@\\.@_\\.@`
#  done

  install -d $RPM_BUILD_ROOT%{_libdir}/openoffice/user/autotext/$language
  install -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/autotext/$language
  for file in solver/%{subver}/%{_archbuilddir}/pck/*$prefix.zip
  do
    pf=`echo $file | sed s@solver/%{subver}/%{_archbuilddir}/pck/@@ | sed -e 's/[0-9]\+\.zip$//'`
    if [ -f $file ]
    then
    [[ ! "$pf" = "autotextuser" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/user/autotext/$language $file
    [[ ! "$pf" = "autotextshare" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/autotext/$language $file
# WRITEME:
#    [[ ! "$pf" = "tpllayoutimpr" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language $file
#    [[ ! "$pf" = "tplpresntimpr" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template $file
    [[ ! "$pf" = "tplwizagenda" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language/wizard $file
    [[ ! "$pf" = "tplwizdesktop" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language/internal $file
    [[ ! "$pf" = "tplwizfax" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language/wizard $file
    [[ ! "$pf" = "tplwizhomepage" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language/wizard/web $file
    [[ ! "$pf" = "tplwizletter" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language/wizard $file
    [[ ! "$pf" = "tplwizmemo" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language/wizard $file
    [[ ! "$pf" = "tplwizstyles" ]] || unzip -o -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/$language/wizard/styles $file
    fi
# FINDME:
# /openoffice/share/templates/samples

# CHECKME:
#??    [[ "$pf" = "wordbook" ]] unzip -d $RPM_BUILD_ROOT%{_libdir}/openoffice/
  done
done

# Remove unnecessary binaries
for app in %{apps} ; do
  rm -f $RPM_BUILD_ROOT%{_libdir}/openoffice/program/s${app}
done

install -d $RPM_BUILD_ROOT%{_applnkdir}
gunzip -dc %{SOURCE6} | tar xf - -C $RPM_BUILD_ROOT%{_applnkdir}

## Remove any fake classes
#rm -rf $RPM_BUILD_ROOT%{_libdir}/openoffice/program/classes

# Remove stuff that should come from system libraries
rm -rf $RPM_BUILD_ROOT%{_libdir}/openoffice/program/libdb-*
rm -rf $RPM_BUILD_ROOT%{_libdir}/openoffice/program/libdb_*

# Fix GNOME & KDE
install -d $RPM_BUILD_ROOT%{_datadir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT%{_libdir}/openoffice/share/kde/net/mimelnk/share/mimelnk $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_libdir}/openoffice/share/kde/net/mimelnk/share/icons/* $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT%{_libdir}/openoffice/share/icons/* $RPM_BUILD_ROOT%{_pixmapsdir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/openoffice/share/kde
rm -rf $RPM_BUILD_ROOT%{_libdir}/openoffice/share/cde
rm -rf $RPM_BUILD_ROOT%{_libdir}/openoffice/share/gnome
rm -rf $RPM_BUILD_ROOT%{_libdir}/openoffice/share/icons

# Now fixup Common.xml
COMMON_XML_SED=$PWD/%{installpath}/%{langinst}/normal/Common.xml.sed
OLDPATH="`pwd`"
cd $RPM_BUILD_ROOT%{_libdir}/openoffice/share/config/registry/instance/org/openoffice/Office/
  sed -e "s|<cfg:string cfg:type=\"string\" cfg:name=\"\([^\"]*\)\"\(>@@REPLACEME.*@@</cfg:\)string>|<cfg:value xml:lang=\"\1\"\2value>|" Common.xml > Common.xml.tmp
  sed -f $COMMON_XML_SED Common.xml.tmp > Common.xml
  rm -f Common.xml.tmp
cd "$OLDPATH"

# Fixup instdb.ins to get rid of $RPM_BUILD_ROOT
perl -pi -e "s|$RPM_BUILD_ROOT||g" $RPM_BUILD_ROOT%{_libdir}/openoffice/program/instdb.ins
perl -pi -e "/^Installation gid_Installation/ .. /^End/ and s|(SourcePath.*)=.*|\1= \"%{_libdir}/openoffice/program\";|" \
  $RPM_BUILD_ROOT%{_libdir}/openoffice/program/instdb.ins

# Disable desktop (KDE, GNOME, CDE) integration for user installs
for module in GID_MODULE_OPTIONAL_GNOME gid_Module_Optional_Kde gid_Module_Optional_Cde; do
  perl -pi -e "/^Module $module/ .. /^End/ and s|(Installed.*)=.*|\1= NO;|" \
    $RPM_BUILD_ROOT%{_libdir}/openoffice/program/instdb.ins
done

# Fix setup and spadmin symlinks set by OO.org setup program
# (must have absolute symlinks)
ln -sf %{_libdir}/openoffice/program/setup $RPM_BUILD_ROOT%{_libdir}/openoffice/setup
ln -sf %{_libdir}/openoffice/program/soffice $RPM_BUILD_ROOT%{_libdir}/openoffice/spadmin
ln -sf %{_libdir}/openoffice/program/soffice $RPM_BUILD_ROOT%{_libdir}/openoffice/program/spadmin

# Fixup installation directory
perl -pi -e "s|$RPM_BUILD_ROOT||g" \
  $RPM_BUILD_ROOT%{_libdir}/openoffice/share/config/registry/instance/org/openoffice/Office/Common.xml

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
#mkdir -p $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template
#mkdir -p $RPM_BUILD_ROOT%{_libdir}/openoffice/share/gallery
#(cd $RPM_BUILD_ROOT%{_libdir}/openoffice/share;
#  tar fxvj %{SOURCE10}
#  tar fxvj %{SOURCE11}
#)

echo 'UNO_WRITERDB=$SYSUSERCONFIG/.user60.rdb
' >> $RPM_BUILD_ROOT%{_libdir}/openoffice/program/unorc

# Install additional dictionaries
rm -rf a8ldict
install -d a8ldict
install -d $RPM_BUILD_ROOT%{_libdir}/openoffice/share/dict/ooo
for dict in %{wordbooks}; do
  loc=`echo $dict | sed 's~^.*/%{name}-\([a-zA-Z_]*\).zip$~\1~'`
  lang=`echo $loc | sed 's~_.*$~~'`
  mkdir a8ldict/$loc
  unzip -j $dict -d a8ldict/$loc/
  rm -f a8ldict/$loc/hyph_en.dic a8ldict/$loc/standard.dic
  mv -f a8ldict/$loc/*.aff a8ldict/$loc/*.dic $RPM_BUILD_ROOT%{_libdir}/openoffice/share/dict/ooo/
  echo DICT `echo $loc | tr _ ' '` $loc >> $RPM_BUILD_ROOT%{_libdir}/openoffice/share/dict/ooo/dictionary.lst
done
## Special case - Latin
#mkdir a8ldict/la
#unzip %{SOURCE50} -d a8ldict/la/
#mv -f a8ldict/la/*.aff a8ldict/la/*.dic $RPM_BUILD_ROOT%{_libdir}/openoffice/share/dict/ooo/
echo DICT la ANY la >> $RPM_BUILD_ROOT%{_libdir}/openoffice/share/dict/ooo/dictionary.lst
# Special case - Austrian German
echo DICT de AT de_AT >> $RPM_BUILD_ROOT%{_libdir}/openoffice/share/dict/ooo/dictionary.lst
echo DICT de AT de_DE >> $RPM_BUILD_ROOT%{_libdir}/openoffice/share/dict/ooo/dictionary.lst


# Build system in OO SUX
rm -f $RPM_BUILD_ROOT%{_libdir}/openoffice/program/libstdc++*
rm -f $RPM_BUILD_ROOT%{_libdir}/openoffice/program/libstlport_gcc.so
rm -f $RPM_BUILD_ROOT%{_libdir}/openoffice/program/libgcc_s.so.1

rm -rf $RPM_BUILD_ROOT%{_libdir}/openoffice/share/template/{internal,wizard}

# package files
FindI18N() {
#    $1 - short language name	eg. pl
#    $2 - long language name	eg. polish
#    $3 - digit code		eg. 48

    BUILDDIR=%(pwd)

    echo "%defattr(644,root,root,755)" > "i18n-$1"
    
    DIRS="%{_libdir}/openoffice/user/autotext/$2"
    DIRS="$DIRS %{_libdir}/openoffice/share/autotext/$2"
    DIRS="$DIRS %{_libdir}/openoffice/share/template/$2"
    DIRS="$DIRS %{_libdir}/openoffice/help/$1"
    
    for DIR in $DIRS
    do
	if [ -d "$RPM_BUILD_ROOT/$DIR" ]; then
	    echo "%lang($1) $DIR" >> "i18n-$1"
	fi
    done    
    
    SUBF="abp analysis basctl bib cal cnt date dba dbi dbp dbu"
    SUBF="$SUBF dbw dkt egi eme epb epg epn epp eps ept eur for"
    SUBF="$SUBF frm gal imp iso jvm lgd oem ofa oic ooo pcr preload"
    SUBF="$SUBF san sc sch sd set set_pp1 sfx sm spa stt svs svt"
    SUBF="$SUBF svx sw tpl tplx uui vcl wwz"
    SVER=%{subver}
    
    for FILE in $SUBF
    do
	F="%{_libdir}/openoffice/program/resource/$FILE$SVER$3.res"
	if [ -f "$RPM_BUILD_ROOT$F" ]; then
	    echo "%lang($1) $F" >> "i18n-$1"
	fi	
    done
}

FindDict() {
#    $1 - short language name	eg. pl
#    $2 - long language name	eg. polish
#    $3... - locale name (?)	eg. pl_PL

    BUILDDIR=%(pwd)
    LANG="$1"

    echo "%defattr(644,root,root,755)" > "dict-$LANG"

    FILES="%{_libdir}/openoffice/share/dict/ooo/hyph_$LANG.dic"    
    shift; shift
    while test $# -gt 0; do
	FILES="$FILES %{_libdir}/openoffice/share/dict/ooo/$1.dic"
        FILES="$FILES %{_libdir}/openoffice/share/dict/ooo/$1.aff"
        FILES="$FILES %{_libdir}/openoffice/share/dict/ooo/th_$1.dat"
	FILES="$FILES %{_libdir}/openoffice/share/dict/ooo/th_$1.idx"
	shift
    done    
    
    for FILE in $FILES
    do
	if [ -f "$RPM_BUILD_ROOT/$FILE" ]; then
	    echo "%lang($LANG) $FILE" >> "dict-$LANG"
	fi
    done    
}

FindI18N ar arabic 96
FindI18N ca catalan 37
FindI18N da danish 45
FindI18N de german 49
FindI18N es spanish 34
FindI18N el greek 30
FindI18N en english 01
FindI18N fi finnish 35
FindI18N fr french 33
FindI18N it italian 39
FindI18N ja japanese 81
FindI18N ko korean 82
FindI18N nl dutch 31
FindI18N pl polish 48
FindI18N pt portuguese 03
FindI18N ru russian 07
FindI18N sv swedish 46
FindI18N tr turkish 90
FindI18N zh_CN chinese_simplified 86
FindI18N zh_TW chinese_traditional 88

FindDict bg bulgarian bg_BG
FindDict ca catalan ca_ES
FindDict cs czech cs_CZ
FindDict da danish da_DK
FindDict de german de_AT de_CH de_DE
FindDict el greek el_GR
FindDict en english en_CA en_GB en_US en_ES
FindDict es spanish es_ES
FindDict fr french fr_FR
FindDict ga irish ga_IE
FindDict gl galician gl_ES
FindDict hr croatian hr_HR
FindDict hu hungarian hu_HU
FindDict it italian it_IT
FindDict la latin la
FindDict lt lithuanian lt_LT
FindDict nb norwegian_bokmaal nb_NO
FindDict nl dutch nl_NL
FindDict nn norwegian_nynorsk nn_NO
FindDict pl polish pl_PL
FindDict pt portuguese pt_BR pt_PT
FindDict ru russian ru_RU
FindDict sk slovak sk_SK
FindDict sl slovenian sl_SI
FindDict sv swedish sv_SE
FindDict uk ukrainian uk_UA

%post

# Fixup user language to the system set
lang=$(echo "$LC_MESSAGES" | sed -n "s/\([a-z]*_[A-Z]*\).*/\1/p")
if [ -n "$lang" -a -e "%{_libdir}/openoffice/help/${lang%%%%_*}" ]; then
  for item in Linguistic_General_Default_Locale User_User_Language; do
    perl -pi -e "/^ConfigurationItem gid_Configurationitem_${item}/ .. /^End/ and s|en-US|${lang/_/-}|" \
      %{_libdir}/openoffice/program/instdb.ins
  done
fi

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
%doc %{_libdir}/openoffice/LICENSE*
%doc %{_libdir}/openoffice/README*

%dir %{_sysconfdir}/openoffice
%config %{_sysconfdir}/openoffice/autoresponse.conf

%{_applnkdir}/Office
%{_pixmapsdir}/*.png

%{_pixmapsdir}/locolor/16x16/apps/*.xpm
%{_pixmapsdir}/locolor/32x32/apps/*.xpm
%{_pixmapsdir}/hicolor/32x32/apps/*.xpm
%{_pixmapsdir}/hicolor/48x48/apps/*.xpm

%{_datadir}/mimelnk/application/*

%{_libdir}/openoffice/program/*.rdb
%{_libdir}/openoffice/program/*.bmp

%{_libdir}/openoffice/program/sofficerc
%{_libdir}/openoffice/program/unorc
%{_libdir}/openoffice/program/bootstraprc
%{_libdir}/openoffice/program/configmgrrc
%{_libdir}/openoffice/program/instdb.ins

# dirs/trees
%{_libdir}/openoffice/program/classes
%{_libdir}/openoffice/program/addin

%dir %{_libdir}/openoffice/program/resource
%{_libdir}/openoffice/program/resource/bmp.res
%{_libdir}/openoffice/program/resource/testtool.res

# mozilla
#%%{_libdir}/openoffice/program/defaults
#%%{_libdir}/openoffice/program/component.reg
#%%{_libdir}/openoffice/program/components/*.xpt
#%%{_libdir}/openoffice/program/components/*.dat

%dir %{_libdir}/openoffice/help
%{_libdir}/openoffice/help/en
%{_libdir}/openoffice/help/main_transform.xsl

%dir %{_libdir}/openoffice/share
%{_libdir}/openoffice/share/autocorr
%dir %{_libdir}/openoffice/share/autotext
%{_libdir}/openoffice/share/basic
%{_libdir}/openoffice/share/config
%dir %{_libdir}/openoffice/share/dict
%dir %{_libdir}/openoffice/share/dict/ooo
%{_libdir}/openoffice/share/dtd
%{_libdir}/openoffice/share/fonts
%{_libdir}/openoffice/share/gallery
%{_libdir}/openoffice/share/psprint
%{_libdir}/openoffice/share/samples
%dir %{_libdir}/openoffice/share/template
%{_libdir}/openoffice/share/wordbook

%{_libdir}/openoffice/share/autotext/english
%{_libdir}/openoffice/share/template/english
%{_libdir}/openoffice/share/dict/ooo/*en*
%{_libdir}/openoffice/share/dict/ooo/dictionary.lst

%dir %{_libdir}/openoffice/user
%dir %{_libdir}/openoffice/user/autotext
%{_libdir}/openoffice/user/basic
%{_libdir}/openoffice/user/config
%{_libdir}/openoffice/user/database
%{_libdir}/openoffice/user/gallery
%{_libdir}/openoffice/user/psprint

%{_libdir}/openoffice/user/autotext/english

# Programs
%attr(755,root,root) %{_bindir}/*

%attr(755,root,root) %{_libdir}/openoffice/setup
%attr(755,root,root) %{_libdir}/openoffice/spadmin

%attr(755,root,root) %{_libdir}/openoffice/program/*.bin
%attr(755,root,root) %{_libdir}/openoffice/program/fromtemplate
%attr(755,root,root) %{_libdir}/openoffice/program/gnomeint
%attr(755,root,root) %{_libdir}/openoffice/program/javaldx
%attr(755,root,root) %{_libdir}/openoffice/program/jvmsetup
%attr(755,root,root) %{_libdir}/openoffice/program/nswrapper
%attr(755,root,root) %{_libdir}/openoffice/program/setup
%attr(755,root,root) %{_libdir}/openoffice/program/soffice
%attr(755,root,root) %{_libdir}/openoffice/program/sopatchlevel.sh
%attr(755,root,root) %{_libdir}/openoffice/program/spadmin


%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/openoffice
%dir %{_libdir}/openoffice/program
#%%dir %{_libdir}/openoffice/program/components   -- mozilla
%dir %{_libdir}/openoffice/program/filter

%attr(755,root,root) %{_libdir}/openoffice/program/*.so
%attr(755,root,root) %{_libdir}/openoffice/program/*.so.*
#%%attr(755,root,root) %{_libdir}/openoffice/program/components/*.so -- mozilla
%attr(755,root,root) %{_libdir}/openoffice/program/filter/*.so

%files i18n-ar -f i18n-ar
%files i18n-ca -f i18n-ca
%files i18n-da -f i18n-da
%files i18n-de -f i18n-de
%files i18n-es -f i18n-es
%files i18n-el -f i18n-el
%files i18n-en -f i18n-en
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

%files dict-bg -f dict-bg
%files dict-ca -f dict-ca
%files dict-cs -f dict-cs
%files dict-da -f dict-da
%files dict-de -f dict-de
%files dict-el -f dict-el
%files dict-en -f dict-en
%files dict-es -f dict-es
%files dict-fr -f dict-fr
%files dict-ga -f dict-ga
%files dict-gl -f dict-gl
%files dict-hr -f dict-hr
%files dict-hu -f dict-hu
%files dict-it -f dict-it
%files dict-la -f dict-la
%files dict-lt -f dict-lt
%files dict-nb -f dict-nb
%files dict-nl -f dict-nl
%files dict-nn -f dict-nn
%files dict-pl -f dict-pl
%files dict-pt -f dict-pt
%files dict-ru -f dict-ru
%files dict-sk -f dict-sk
%files dict-sl -f dict-sl
%files dict-sv -f dict-sv
%files dict-uk -f dict-uk
