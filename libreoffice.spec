
# Conditional build:
# _with_ibm_java	- uses IBM java instead SUN java
# _with_nest		- build for nest envinronment

# _with_us		- 01 US translation
# _with_pl		- 48 PL translation
# _with_de		- 49 DE translation

Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	1.0.1
Release:	0.4
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
#Source0:	ftp://ftp.openoffice.pl/%{version}/OOo_%{version}_source.tar.bz2
#Source0:	http://sf1.mirror.openoffice.org/%{version}/OOo_%{version}_source.tar.bz2
Source0:	ftp://ftp1.openoffice.pl/pub/OpenOffice.ORG/stable/%{version}/OOo_%{version}_source.tar.bz2
Source1:	ftp://ftp.cs.man.ac.uk/pub/toby/gpc/gpc231.tar.Z
Source2:	%{name}-db3.jar
Source3:	%{name}-rsfile.txt
Source4:	%{name}-xmlparse.sh
Source5:	%{name}-rsfile-local.txt
Source6:	%{name}-png48x48.tar.bz2
Source7:	%{name}-wrapper
Patch0:		%{name}-gcc.patch
Patch1:		%{name}-db3.patch
Patch2:		%{name}-mozilla.patch
Patch3:		%{name}-nest.patch
Patch4:		%{name}-perl.patch
# Start using some system libraries:
Patch5:		%{name}-system-freetype.patch
Patch6:		%{name}-system-getopt.patch
Patch7:		%{name}-freetype-2.1.patch
# Fix broken makefiles
Patch8:		%{name}-braindamage.patch
# Add jj patch for CLK_TCK -> CLOCKS_PER_SEC
Patch9:		%{name}-clockspersec.patch
# Fix psprint /euro to /Euro
Patch10:	%{name}-psprint-euro.patch
# Fix config_office/configure
Patch11:	%{name}-ac.patch

#Patch12:	%{name}-debug-keepsetup.patch
# Hackery around zipdep
Patch13:	%{name}-zipdep.patch
# Remove GPC from linking to GPL/LGPL OO.o code!
Patch14:	%{name}-remove-gpc.patch
# Disable stlport from being built
Patch16:	%{name}-no-stlport.patch

# Disable Java applet support
Patch17:	%{name}-no-java-vm.patch
# Fix broken inline assembly
Patch18:	%{name}-asm.patch

Patch19:	%{name}-nousrinclude.patch

Patch20:	%{name}-no-mozab.patch
Patch21:	%{name}-no-mozab2.patch

Patch22:	%{name}-system-db.patch

Patch23:	%{name}-udm.patch
Patch24:	%{name}-autodoc.patch

Patch25:	%{name}-xmlsearch.patch
Patch26:	%{name}-config-java.patch
Patch27:	%{name}-sj2-java.patch

URL:		http://www.openoffice.org/
BuildRequires:  db4
BuildRequires:  db4-devel
BuildRequires:  db4-cxx
BuildRequires:  db4-java
BuildRequires:	STLport-static
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-fonts-PEX
BuildRequires:	XFree86-Xvfb
#BuildRequires:	db3-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  bison
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	freetype-static
BuildRequires:	gcc
BuildRequires:	gcc-c++
#BuildRequires:	gcc-java
%{?_with_ibm_java:BuildRequires:	ibm-java-sdk}
%{?!_with_ibm_java:BuildRequires:	java-sun}
BuildRequires:	libstdc++-devel
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	tcsh
BuildRequires:	unzip
BuildRequires:	zip
BuildRequires:	jar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		langs		"ENUS,FREN,GERM,SPAN,ITAL,DTCH,PORT,DAN,GREEK,POL,SWED,TURK,RUSS"
%define		langs		"ENUS"


#%define		oo_ver	1.0

%define		_prefix		/usr/X11R6
%define		_archbuilddir	unxlngi3.pro
%define		installpath	instsetoo/%{_archbuilddir}
%define subver	641

# Find a free display (resources generation requires X) and sets XDISPLAY
%define init_xdisplay XDISPLAY=0; while /bin/true; do if [ ! -f /tmp/.X$XDISPLAY-lock ]; then sleep 2s; ( /usr/X11R6/bin/Xvfb -ac :$XDISPLAY & 2>&1 > /dev/null); sleep 10s; if [ -f /tmp/.X$XDISPLAY-lock ]; then break; fi; fi; XDISPLAY=$(($XDISPLAY+1)); done

# The virtual X server PID
%define kill_xdisplay kill $(cat /tmp/.X$XDISPLAY-lock)

#%{?_with_us:%define installpath instsetoo/unxlngi3.pro/01/normal}
#%{?_with_pl:%define installpath instsetoo/unxlngi3.pro/48/normal}
#%{?_with_de:%define installpath instsetoo/unxlngi3.pro/49/normal}

#%{?_with_us:%define langs ENUS}
#%{?_with_pl:%define langs POL}
#%{?_with_de:%define langs DTCH}

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

%prep
CC=%{__cc}
CXX=%{__cxx}
GCJ=gcj
export CC CXX GCJ

%setup -q -n oo_1.0.1_src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if%{?_with_nest:1}%{!?_with_nest:0}
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
#%patch9 -p1
%patch10 -p1
%patch11 -p1
#%patch12 -p0
%patch13 -p1
%patch14 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

%patch20 -p1
%patch21 -p1
%patch22 -p1

%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1

rm -rf autodoc/source/inc/utility

install %{SOURCE1} external
cd external; tar fxz %{SOURCE1}; cp -fr gpc231/* gpc
cd ..

chmod +x solenv/bin/zipdep.pl

##################
# Build fake JDK
mkdir -p fakejdk/bin fakejdk/include
cp -a %{SOURCE4} fakejdk/bin/xmlparse

# Create fakejdk/bin/java:
sed "s~@@~`pwd`~" > fakejdk/bin/java <<"EOF"
#!/bin/sh
if [ "$1" = "-version" ]; then
	echo 'java version "1.3.1_03"' 1>&2
	exit 0
fi
if [ "$4" = org.openoffice.configuration.XMLDefaultGenerator ]; then
	exec @@/fakejdk/bin/xmlparse "$@"
fi
echo "FIXME: Emulate java runtime using gcj here"
exit 1
EOF
chmod +x fakejdk/bin/java fakejdk/bin/xmlparse


# Create fakejdk/bin/javac
sed "s~@@~`pwd`~" > fakejdk/bin/javac <<"EOF"
#!/bin/sh
if [ "$1" = "-J-version" ]; then
	echo 'java version "1.3.1_03"' 1>&2
	exit 0
fi
TEMP=`mktemp -d fakejavac.XXXXXX` || exit 1
DEST=.
ANY=""
while [ $# != 0 ]; do
	if [ "$1" = "-classpath" ]; then
		shift
	elif [ "$1" = "-d" ]; then
		DEST=$2
		shift
	else
		case "$1" in
			*.java)
				C=`basename "$1" .java`
				grep '^[  ]*package[      ]*[^    ]*[     ]*;[    ]*$' $1 > $TEMP/$C.java
				echo "public class $C { }" >> $TEMP/$C.java
				ANY=1
			;;
			*)
				echo "unknown option passed to javac!" 1>&2
				exit 1
			;;
		esac
	fi
	shift
done
if [ -n "$ANY" ]; then
	gcj -C -d $DEST $TEMP/*.java
fi
rm -rf $TEMP
exit 0
EOF

chmod +x fakejdk/bin/javac
GCJHOME=`gcj -print-search-dirs | sed -n 's/^install:[         ]*//p'`
cp -f /usr/lib/java/include/linux/j* fakejdk/include
cp -f /usr/lib/java/include/j* fakejdk/include
cat fakejdk/include/jni.h | sed s/JDK1_1InitArgs/JDK1_1InitArgs2/ > fakejdk/include/jni2.h
rm -f fakejdk/include/jni.h
cat > fakejdk/include/jni.h <<EOF
#ifndef FAKEJDK_JNI_H
#define FAKEJDK_JNI_H 1
#include <jni2.h>
#include <stdio.h>
#include <stdarg.h>

#define JNIEXPORT
#define JNICALL

typedef struct JDK1_1InitArgs
{
	jint version;
	char ** properties;
	jint checkSource, nativeStackSize, javaStackSize, minHeapSize, maxHeapSize, verifyMode;
	char *classpath;
	jint (*vfprintf) (FILE *, const char *, va_list);
	void (*exit) (jint);
	void (*abort) (void);
	jint enableClassGC, enableVerboseGC, disableAsyncGC, verbose;
	jboolean debugging;
	jint debugPort;
} JDK1_1InitArgs;

#define JavaVM_ JavaVM
#endif
EOF

###################
## BUILD
###################
%build
JAVA_HOME=`pwd`/fakejdk
%{?!_with_ibm_java:JAVA_HOME="/usr/lib/jdk1.3.1_03"}
%{?_with_ibm_java:JAVA_HOME="/usr/lib/IBMJava2-13"}
JAVA_HOME="/usr/lib/java"
export JAVA_HOME

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

install -d solver/641/%{_archbuilddir}/bin
install /usr/lib/db.jar solver/641/%{_archbuilddir}/bin/db.jar

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
install -d $RPM_BUILD_ROOT%{_libdir}/openoffice

cp solver/641/%{_archbuilddir}/bin/setup_services.rdb solver/641/%{_archbuilddir}/bin/uno_writerdb.rdb
rm -f f0_061
zip -j -5 "f0_061" solver/641/%{_archbuilddir}/bin/uno_writerdb.rdb
mv f0_061.zip %{installpath}/01/normal/f0_061

%{init_xdisplay}
RESPONSE_FILE=$PWD/rsfile.ins
(cd %{installpath}/01/normal/;
  cat %{SOURCE3} | sed -e "s|@DESTDIR@|$RPM_BUILD_ROOT%{_libdir}/openoffice|" > $RESPONSE_FILE

  # Localize New and Wizard menus and OfficeObjects
  [[ ! -f setup.ins.localized ]] && {
  cp -p setup.ins setup.ins.localized
  (
  for i in `( cd ../../; echo [0-9][0-9] ) | sed 's/01 //'`; do
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
  ) | awk ' $1 ~ /Value/ { l=$0; sub(/^.*= "/,"",l); sub(/";.*$/,"",l); sub(/%PRODUCTNAME/,"OpenOffice.org",l); sub(/%PRODUCTVERSION/,"%{fullver}",l); n=n+1; str="@@REPLACEME" n "@@"; s="\"" str "\""; sub(/".*"/,s); printf "s|%s|%s|\n", str, l > "Common.xml.sed" } { print } ' \
    >> setup.ins
  }

  DISPLAY=:$XDISPLAY ./setup -R:$RESPONSE_FILE
  rm -f $RESPONSE_FILE
)
%{kill_xdisplay}

# Now fixup Common.xml
COMMON_XML_SED=$PWD/%{installpath}/01/normal/Common.xml.sed
(cd $RPM_BUILD_ROOT%{_libdir}/openoffice/share/config/registry/instance/org/openoffice/Office/;
  sed -e "s|<cfg:string cfg:type=\"string\" cfg:name=\"\([^\"]*\)\"\(>@@REPLACEME.*@@</cfg:\)string>|<cfg:value xml:lang=\"\1\"\2value>|" Common.xml > Common.xml.tmp
  sed -f $COMMON_XML_SED Common.xml.tmp > Common.xml
  rm -f Common.xml.tmp
)

# Fixup instdb.ins to get rid of $RPM_BUILD_ROOT
perl -pi -e "s|$RPM_BUILD_ROOT||g" \
  $RPM_BUILD_ROOT%{_libdir}/openoffice/program/instdb.ins
perl -pi -e "/^Installation gid_Installation/ .. /^End/ and s|(SourcePath.*)=.*|\1= \"%{_libdir}/openoffice/program\";|" \
  $RPM_BUILD_ROOT%{_libdir}/openoffice/program/instdb.ins

# Fix setup and spadmin symlinks set by OO.org setup program
# (must have absolute symlinks)
ln -sf %{_libdir}/openoffice/program/setup $RPM_BUILD_ROOT%{_libdir}/openoffice/setup
ln -sf %{_libdir}/openoffice/program/soffice $RPM_BUILD_ROOT%{_libdir}/openoffice/spadmin
ln -sf %{_libdir}/openoffice/program/soffice $RPM_BUILD_ROOT%{_libdir}/openoffice/program/spadmin

# Fixup installation directory
perl -pi -e "s|$RPM_BUILD_ROOT||g" \
  $RPM_BUILD_ROOT%{_libdir}/openoffice/share/config/registry/instance/org/openoffice/Office/Common.xml

# Recreate registry cache
#cat > ./build-create-cache.command << EOF
#\$CXXCOMP -g \$SOLARINC $RPM_OPT_FLAGS -fno-for-scope -fpermissive \
#	  -fexceptions -fno-enforce-eh-specs \$SOLARDEF %{SOURCE14} \
#	  -o ./createcache -L\$SOLARVER/\$UPD/\$INPATH/lib \
#	  -Wl,-rpath,\$SOLARVER/\$UPD/\$INPATH/lib -lcfgmgr2
#EOF
#/bin/tcsh -f -c "source %{build_env}; source build-create-cache.command"
#rm -rf %{buildroot}%{_libdir}/openoffice/share/config/registry/cache
#for arg in `cd %{buildroot}%{_libdir}/openoffice/share/config/registry/instance; \
#	    find . -name \*.xml | \
#	    sed 's~\.xml$~~;s~/~.~g;s~^\.\.~/~'`; do
#  ./createcache %{buildroot}%{_libdir}/openoffice/program/applicat.rdb \
#		%{buildroot}%{_libdir}/openoffice/share/config/registry $arg
#done

## FIXME: (gb) 6.0.41-3mdk: workaround for English wordbook, move them
## to share/ directory
#cp $RPM_BUILD_ROOT%{_libdir}/openoffice/user/wordbook/* $RPM_BUILD_ROOT%{_libdir}/openoffice/share/wordbook/english/

# Remove any fake classes
rm -rf $RPM_BUILD_ROOT%{_libdir}/openoffice/program/classes

# Remove stuff that should come from system libraries
rm -rf	$RPM_BUILD_ROOT%{_libdir}/openoffice/program/libdb-* \
	$RPM_BUILD_ROOT%{_libdir}/openoffice/program/libdb_cxx-* \
	$RPM_BUILD_ROOT%{_libdir}/openoffice/program/libdb_java-*

# Fix openoffice/share/kde/net/applnk paths
# mkdir -p %{buildroot}%{_libdir}/openoffice/share/kde/net/applnk/Office
mv "%{buildroot}%{_libdir}/openoffice/share/kde/net/applnk/OpenOffice.org 1.0.1" "%{buildroot}%{_libdir}/openoffice/share/kde/net/applnk/OpenOffice.org"
perl -pi -e "/^Module gid_Module_Optional_Kde/ .. /^End/ and s|YES|NO|g" %{buildroot}%{_libdir}/openoffice/program/instdb.ins
perl -pi -e "/^Installation gid_Installation/ .. /^End/ and s|%{buildroot}||g" %{buildroot}%{_libdir}/openoffice/program/instdb.ins
# perl -pi -e "/^/ .. /^/ and s|||g" %{buildroot}%{_libdir}/openoffice/program/instdb.ins
perl -pi -e "/^Directory GID_DIR_HOME_GNOME_APPS_STAR/ .. /^End/ and s|OpenOffice\.org\ 1\.0\.1|OpenOffice\.org|g" %{buildroot}%{_libdir}/openoffice/program/instdb.ins
perl -pi -e "/^Directory gid_Dir_Share_Kde_Net_Applnk_Star/ .. /^End/ and s|OpenOffice\.org\ 1\.0\.1|OpenOffice\.org|g" %{buildroot}%{_libdir}/openoffice/program/instdb.ins
perl -pi -e "/^Directory gid_Dir_Kde2_Share_Applnk_Star/ .. /^End/ and s|OpenOffice\.org\ 1\.0\.1|OpenOffice\.org|g" %{buildroot}%{_libdir}/openoffice/program/instdb.ins
perl -pi -e "/^Procedure GID_PROCEDURE_KDE_INST_FOR_REDHAT/ .. /^End/ and s|OpenOffice\.org\ 1\.0\.1|OpenOffice\.org|g" %{buildroot}%{_libdir}/openoffice/program/instdb.ins
perl -pi -e "/^Procedure GID_PROCEDURE_KDE_DEINSTALL_FOR_REDHAT/ .. /^End/ and s|OpenOffice\.org\ 1\.0\.1|OpenOffice\.org|g" %{buildroot}%{_libdir}/openoffice/program/instdb.ins
perl -pi -e "/^Procedure GID_PROCEDURE_GNOME_INSTALL/ .. /^End/ and s|OpenOffice\.org\ 1\.0\.1|OpenOffice\.org|g" %{buildroot}%{_libdir}/openoffice/program/instdb.ins

# Fix paths in GNOME and KDE .desktop files
for dir in %{buildroot}%{_libdir}/openoffice/share/gnome/net %{buildroot}%{_libdir}/openoffice/share/kde/net/applnk/OpenOffice.org; do
  for file in $(ls -1A ${dir}); do
    # fix all %{buildroot} occurances
    perl -pi -e "s|%{buildroot}||g" ${dir}/${file}
    # catch group calc draw impress math writer cases
    if [ "$file" == "drawing.desktop" ] || [ "$file" == "mathdoc.desktop" ] || [ "$file" == "presentation.desktop" ] || [ "$file" == "spreadsheet.desktop" ] || [ "$file" == "textdoc.desktop" ]; then
      perl -pi -e "s|%{_libdir}/openoffice/program/s|%{_bindir}/oo|" ${dir}/${file}
    fi
  done
done

# Install autoresponse file for user installation
mkdir -p %{buildroot}%{_sysconfdir}/openoffice
cat %{SOURCE5} > %{buildroot}%{_sysconfdir}/openoffice/autoresponse.conf
chmod 644 %{buildroot}%{_sysconfdir}/openoffice/autoresponse.conf

# Install OpenOffice.org wrapper script
mkdir -p %{buildroot}%{_bindir}
cat %{SOURCE7} | sed -e "s/<OOVERSION>/%{subver}/" > %{buildroot}%{_bindir}/ooffice
chmod 755 %{buildroot}%{_bindir}/ooffice

# Install component wrapper scripts
mkdir -p %{buildroot}%{_bindir}
for app in calc draw impress math writer; do
cat > %{buildroot}%{_bindir}/oo${app} << EOF
#!/bin/sh
if [ -z "\$1" ]; then
  exec %{_bindir}/ooffice private:factory/s${app}
else
  exec %{_bindir}/ooffice "\$@"
fi
EOF
chmod +x %{buildroot}%{_bindir}/oo${app}
done

# Unpack KDE applnk files, icons and MIME associations
mkdir -p %{buildroot}%{_datadir}/applnk/Office/OpenOffice.org
(cd ./solver/%{subver}/%{_archbuilddir}/pck/;
  for app in group calc draw impress math writer; do
    unzip -d %{buildroot}%{_datadir}/applnk/Office/OpenOffice.org ookdeapp${app}.zip
    if [ "$app" == "group" ]; then
      for file in $(unzip -l ookdeapp${app}.zip | awk -- ' /[a-z]*\.[a-y]+/ {print $4}'); do
        perl -pi -e "s|\<progpath\>|%{_libdir}/openoffice|" %{buildroot}%{_datadir}/applnk/Office/OpenOffice.org/$file
        perl -pi -e "s|\<singleproductname\>|OpenOffice\.org|" %{buildroot}%{_datadir}/applnk/Office/OpenOffice.org/$file
      done
    else
      for file in $(unzip -l ookdeapp${app}.zip | awk -- ' /[a-z]*\.[a-y]+/ {print $4}'); do
# DS!       perl -pi -e "s|Exec=.*s([a-z]*).|Exec=\"%{_bindir}/oo\1\"|" %{buildroot}%{_datadir}/applnk/Office/OpenOffice.org/$file
        perl -pi -e "s|\<progpath\>/program/s|%{_bindir}/oo|" %{buildroot}%{_datadir}/applnk/Office/OpenOffice.org/$file
        perl -pi -e "s|\<singleproductname\>|OpenOffice\.org|" %{buildroot}%{_datadir}/applnk/Office/OpenOffice.org/$file
      done
    fi
    unzip -d %{buildroot}%{_prefix} ookde${app}.zip
    for file in $(unzip -l ookde${app}.zip | awk -- ' /[a-z]+\.desktop/ {print $4}'); do
      perl -pi -e "s|\<singleproductname\>|OpenOffice\.org|" %{buildroot}%{_prefix}/$file
    done
  done
)

# Unpack GNOME files
mkdir -p %{buildroot}%{_datadir}/gnome/apps/Applications/OpenOffice.org
(cd ./solver/%{subver}/%{_archbuilddir}/pck/;
  for app in group calc draw impress math writer; do
    unzip -d %{buildroot}%{_datadir}/gnome/apps/Applications/OpenOffice.org oognomeapp${app}.zip
    if [ "$app" == "group" ]; then
      for file in $(unzip -l ookdeapp${app}.zip | awk -- ' /[a-z]*\.[a-y]+/ {print $4}'); do
        perl -pi -e "s|\<progpath\>|%{_libdir}/openoffice|" %{buildroot}%{_datadir}/gnome/apps/Applications/OpenOffice.org/$file
        perl -pi -e "s|\<singleproductname\>|OpenOffice\.org|" %{buildroot}%{_datadir}/gnome/apps/Applications/OpenOffice.org/$file
      done
    else
      for file in $(unzip -l ookdeapp${app}.zip | awk -- ' /[a-z]*\.[a-y]+/ {print $4}'); do
        perl -pi -e "s|\<progpath\>/program/s|%{_bindir}/oo|" %{buildroot}%{_datadir}/gnome/apps/Applications/OpenOffice.org/$file
        perl -pi -e "s|\<progpath\>|%{_libdir}/openoffice|" %{buildroot}%{_datadir}/gnome/apps/Applications/OpenOffice.org/$file
        perl -pi -e "s|\<singleproductname\>|OpenOffice\.org|" %{buildroot}%{_datadir}/gnome/apps/Applications/OpenOffice.org/$file
      done
    fi
  done
)

# Extract 48x48 PNGs for use by GNOME and Nautilus (Nautilus needs pngs under %{_datadir}/pixmaps)
mkdir -p %{buildroot}%{_datadir}/pixmaps
(cd %{buildroot}%{_datadir}/pixmaps/;
  tar fxvj %{SOURCE6}
)

## Install new template and gallery content
#mkdir -p %{buildroot}%{_libdir}/openoffice/share/template
#mkdir -p %{buildroot}%{_libdir}/openoffice/share/gallery
#(cd %{buildroot}%{_libdir}/openoffice/share;
#  tar fxvj %{SOURCE10}
#  tar fxvj %{SOURCE11}
#)


echo 'UNO_WRITERDB=$SYSUSERCONFIG/.user60.rdb
' >> $RPM_BUILD_ROOT%{_libdir}/openoffice/program/unorc





####################
## CLEAN
####################
%clean
rm -rf $RPM_BUILD_ROOT


####################
## FILES
####################
%files
%defattr(644,root,root,755)
%doc readlicense/source/license/unx/LICENSE
#%doc licenses/{README.gpc,COPYING,COPYING.LIB}
#
%attr(755,root,root) %{_bindir}/ooffice
%attr(755,root,root) %{_bindir}/oocalc
%attr(755,root,root) %{_bindir}/oodraw
%attr(755,root,root) %{_bindir}/ooimpress
%attr(755,root,root) %{_bindir}/oomath
%attr(755,root,root) %{_bindir}/oowriter
#
%dir %{_sysconfdir}/openoffice/
%config %{_sysconfdir}/openoffice/autoresponse.conf
#
%dir %{_datadir}/applnk/
%dir %{_datadir}/applnk/Office/
%dir %{_datadir}/applnk/Office/OpenOffice.org/
%{_datadir}/applnk/Office/OpenOffice.org/textdoc.desktop
%{_datadir}/applnk/Office/OpenOffice.org/spreadsheet.desktop
%{_datadir}/applnk/Office/OpenOffice.org/presentation.desktop
%{_datadir}/applnk/Office/OpenOffice.org/drawing.desktop
%{_datadir}/applnk/Office/OpenOffice.org/mathdoc.desktop
%{_datadir}/applnk/Office/OpenOffice.org/setup.desktop
%{_datadir}/applnk/Office/OpenOffice.org/printeradmin.desktop
%{_datadir}/applnk/Office/OpenOffice.org/.order
%{_datadir}/applnk/Office/OpenOffice.org/.directory
%dir %{_datadir}/mimelnk/
%dir %{_datadir}/mimelnk/application/
%{_datadir}/mimelnk/application/*.desktop
%dir %{_datadir}/icons/locolor/
%dir %{_datadir}/icons/locolor/16x16/
%dir %{_datadir}/icons/locolor/16x16/apps/
%{_datadir}/icons/locolor/16x16/apps/*.xpm
%dir %{_datadir}/icons/locolor/32x32/
%dir %{_datadir}/icons/locolor/32x32/apps/
%{_datadir}/icons/locolor/32x32/apps/*.xpm
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps/
%{_datadir}/icons/hicolor/32x32/apps/*.xpm
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/48x48/apps/
%{_datadir}/icons/hicolor/48x48/apps/*.xpm
%dir %{_datadir}/pixmaps/
%{_datadir}/pixmaps/*.png
#
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/apps/
%dir %{_datadir}/gnome/apps/Applications/
%dir %{_datadir}/gnome/apps/Applications/OpenOffice.org/
%{_datadir}/gnome/apps/Applications/OpenOffice.org/textdoc.desktop
%{_datadir}/gnome/apps/Applications/OpenOffice.org/spreadsheet.desktop
%{_datadir}/gnome/apps/Applications/OpenOffice.org/presentation.desktop
%{_datadir}/gnome/apps/Applications/OpenOffice.org/drawing.desktop
%{_datadir}/gnome/apps/Applications/OpenOffice.org/mathdoc.desktop
%{_datadir}/gnome/apps/Applications/OpenOffice.org/setup.desktop
%{_datadir}/gnome/apps/Applications/OpenOffice.org/printeradmin.desktop
%{_datadir}/gnome/apps/Applications/OpenOffice.org/.order
%{_datadir}/gnome/apps/Applications/OpenOffice.org/.directory
#

%attr(644,root,root) %{_libdir}/openoffice/LICENSE*
%attr(644,root,root) %{_libdir}/openoffice/README*
%attr(755,root,root) %{_libdir}/openoffice/setup
%attr(755,root,root) %{_libdir}/openoffice/spadmin

# Program
%attr(644,root,root) %{_libdir}/openoffice/program/*.bmp
%attr(644,root,root) %{_libdir}/openoffice/program/sofficerc
%attr(644,root,root) %{_libdir}/openoffice/program/unorc
%attr(644,root,root) %{_libdir}/openoffice/program/bootstraprc
%attr(644,root,root) %{_libdir}/openoffice/program/configmgrrc
%attr(644,root,root) %{_libdir}/openoffice/program/instdb.ins

%attr(644,root,root) %{_libdir}/openoffice/program/*.rdb

%attr(755,root,root) %{_libdir}/openoffice/program/*.so
%attr(755,root,root) %{_libdir}/openoffice/program/*.so.*
%attr(755,root,root) %{_libdir}/openoffice/program/fromtemplate
%attr(755,root,root) %{_libdir}/openoffice/program/gnomeint
%attr(755,root,root) %{_libdir}/openoffice/program/javaldx
%attr(755,root,root) %{_libdir}/openoffice/program/jvmsetup
%attr(755,root,root) %{_libdir}/openoffice/program/jvmsetup.bin
%attr(755,root,root) %{_libdir}/openoffice/program/nswrapper
%attr(755,root,root) %{_libdir}/openoffice/program/pluginapp.bin
%attr(755,root,root) %{_libdir}/openoffice/program/sagenda
%attr(755,root,root) %{_libdir}/openoffice/program/scalc
%attr(755,root,root) %{_libdir}/openoffice/program/sdraw
%attr(755,root,root) %{_libdir}/openoffice/program/setup
%attr(755,root,root) %{_libdir}/openoffice/program/setup.bin
%attr(755,root,root) %{_libdir}/openoffice/program/sfax
%attr(755,root,root) %{_libdir}/openoffice/program/simpress
%attr(755,root,root) %{_libdir}/openoffice/program/slabel
%attr(755,root,root) %{_libdir}/openoffice/program/sletter
%attr(755,root,root) %{_libdir}/openoffice/program/smaster
%attr(755,root,root) %{_libdir}/openoffice/program/smath
%attr(755,root,root) %{_libdir}/openoffice/program/smemo
%attr(755,root,root) %{_libdir}/openoffice/program/soffice
%attr(755,root,root) %{_libdir}/openoffice/program/soffice.bin
%attr(755,root,root) %{_libdir}/openoffice/program/sopatchlevel.sh
%attr(755,root,root) %{_libdir}/openoffice/program/spadmin
%attr(755,root,root) %{_libdir}/openoffice/program/spadmin.bin
%attr(755,root,root) %{_libdir}/openoffice/program/svcard
%attr(755,root,root) %{_libdir}/openoffice/program/sweb
%attr(755,root,root) %{_libdir}/openoffice/program/swriter

%attr(755,root,root) %{_libdir}/openoffice/program/filter/*.so
%attr(644,root,root) %{_libdir}/openoffice/program/addin/source
%attr(644,root,root) %{_libdir}/openoffice/program/resource/*

%{_libdir}/openoffice/help
%{_libdir}/openoffice/share
%{_libdir}/openoffice/user
