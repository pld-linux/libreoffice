
# Conditional build:
# _with_ibm_java	- uses IBM java instead SUN java
# _with_nest		- build for nest envinronment

# _with_us		- 01 US translation
# _with_pl		- 48 PL translation
# _with_de		- 49 DE translation

#%define		oo_ver	1.0
Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	1.0.0
Release:	0.6
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
#Source0:	http://sf1.mirror.openoffice.org/%{version}/oo_%{version}_source.tar.bz2
Source0:	http://sf1.mirror.openoffice.org/%{version}/OOo_%{version}_source.tar.bz2
Source1:	ftp://ftp.cs.man.ac.uk/pub/toby/gpc/gpc231.tar.Z
Source2:	%{name}-db3.jar
Source3:	%{name}-rsfile.txt
Source4:	%{name}-xmlparse.sh
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

Patch12:	%{name}-debug-keepsetup.patch
# Hackery around zipdep
Patch13:	%{name}-zipdep.patch
# Remove GPC from linking to GPL/LGPL OO.o code!
Patch14:	%{name}-remove-gpc.patch
Patch15:	%{name}-fontcache-1.5.patch
# Disable stlport from being built
Patch16:	%{name}-no-stlport.patch
URL:		http://www.openoffice.org/
BuildRequires:	STLport-static
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-fonts-PEX
BuildRequires:	XFree86-Xvfb
BuildRequires:	db3-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  bison
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	freetype-static
%{?!_with_nest:BuildRequires:	gcc <= 3.0.0}
%{?_with_nest:BuildRequires:	gcc2}
%{?!_with_nest:BuildRequires:	gcc-c++ <= 3.0.0}
%{?_with_nest:BuildRequires:	gcc2-c++}
#%{?_with_ibm_java:BuildRequires:	ibm-java-sdk}
#%{?!_with_ibm_java:BuildRequires:	jdk = 1.3.1_03}
%{?!_with_nest:BuildRequires:	libstdc++-devel <= 3.0.0}
%{?_with_nest:BuildRequires:	libstdc++2-devel}
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	tcsh
BuildRequires:	unzip
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%{?_with_us:%define installpath instsetoo/unxlngi3.pro/01/normal}
%{?_with_pl:%define installpath instsetoo/unxlngi3.pro/48/normal}
%{?_with_de:%define installpath instsetoo/unxlngi3.pro/49/normal}

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
%setup -q -n oo_1.0_src
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
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p0
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

install %{SOURCE1} external
cd external; tar fxz %{SOURCE1}; cp -fr gpc231/* gpc

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
	$GCJ -C -d $DEST $TEMP/*.java
fi
rm -rf $TEMP
exit 0
EOF

chmod +x fakejdk/bin/javac
GCJHOME=`$GCJ -print-search-dirs | sed -n 's/^install:[         ]*//p'`
ln -sf $GCJHOME/include/j* fakejdk/include/
rm -f fakejdk/include/jni.h
cat > fakejdk/include/jni.h <<EOF
#ifndef FAKEJDK_JNI_H
#define FAKEJDK_JNI_H 1
#include_next <jni.h>
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

%build
JAVA_HOME=`pwd`/fakejdk
export $JAVA_HOME

cd config_office
autoconf

#%{?!_with_ibm_java:JAVA_HOME="/usr/lib/jdk1.3.1_03"}
#%{?_with_ibm_java:JAVA_HOME="/usr/lib/IBMJava2-13"}
%configure2_13 \
	--with-jdk-home=$JAVA_HOME \
	--with-stlport4-home=/usr \
	--with-lang=ALL \
	--with-x

cd ..

cat <<EOF > prep
#!/bin/tcsh
./bootstrap
EOF
chmod u+rx prep
./prep

install -d solver/641/unxlngi3.pro/bin
install %{SOURCE2} solver/641/unxlngi3.pro/bin/db.jar

cat <<EOF > compile
#!/bin/tcsh
source LinuxIntelEnv.Set
dmake -p -v
EOF
chmod u+rx compile
./compile

%install
rm -rf $RPM_BUILD_ROOT

#cat <<EOF > install
#!/bin/tcsh
#source LinuxIntelEnv.Set
#dmake install
#EOF
#
#chmod u+rx install
#./install

# starting Xvfb
i=0
while [ -f /tmp/.X$i-lock ]; do
	i=$(($i+1))
done

/usr/X11R6/bin/Xvfb :$i & 
PID=$!
sleep 5

# preparing to start installator
cp -f %{SOURCE3} $RPM_BUILD_DIR/oo_%{oo_ver}_src/install.rs.in
sed -e "s,@DESTDIR@,$RPM_BUILD_ROOT/usr/X11R6/lib/openoffice," \
	-e "s,@LOGFILE@,$RPM_BUILD_DIR/oo_%{oo_ver}_src/install.log," \
	install.rs.in > install.rs

cp solver/641/unxlngi3.pro/bin/setup_services.rdb solver/641/unxlngi3.pro/bin/uno_writerdb.rdb
rm -f f0_062
zip -j -5 "f0_062" solver/641/unxlngi3.pro/bin/uno_writerdb.rdb
mv f0_062.zip %{installpath}/f0_062

for FileID in Lib_gcc Lib_Stdc Lib_Mozab_2 Lib_Mozabdrv Mozilla_Runtime; do
  perl -ni -e "/^(File|Shortcut) gid_(File|Shortcut)_${FileID}/ .. /^End/ or print" %{installpath}/setup.ins
  perl -pi -e "s/gid_File_${FileID},//g" %{installpath}/setup.ins
done

# starting installator
DISPLAY=":$i" %{installpath}/setup -R:$RPM_BUILD_DIR/oo_%{oo_ver}_src/install.rs

# stopping Xvfb
#kill $PID

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
