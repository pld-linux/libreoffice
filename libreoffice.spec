# TODO:
# 	- everything
#	- PLD vendor list of patches to apply in patches/*/appply?
#	- drop requirement on XFree86-static
#	- --with-system-myspell + myspell package as in Debian
#	- --with-system-neon - check compilation

# Conditional build:
%bcond_with	java		# Java support
%bcond_without	kde		# do not use KDE framework, use GNOME

%define		ver		1.1
%define		rel		1
%define		ooobver		1.1.54
%define		subver		645
%define		fullver		%{ver}.%{rel}
%define		dfullver	%(echo %{fullver} | tr . _)
%define		specflags	-fno-strict-aliasing

Summary:	OpenOffice - powerful office suite
Summary(pl):	OpenOffice - potê¿ny pakiet biurowy
Name:		openoffice
Version:	%{fullver}
Release:	1.1
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://ooo.ximian.com/packages/OOO_%{dfullver}/ooo-build-%{ooobver}.tar.gz
# Source0-md5:	22a459b68c2534c2213805d1445d947d
Source1:	http://ooo.ximian.com/packages/OOO_%{dfullver}/OOO_%{dfullver}.tar.bz2
# Source1-md5:	550381bc429fbbda54cb84758f14e010
Source2:	http://ooo.ximian.com/packages/ooo-icons-OOO_1_1-9.tar.gz
# Source2-md5:	32a0e62f89ef36a91437fc705fbe6440
Source3:	http://kde.openoffice.org/files/documents/159/1785/ooo-KDE_icons-OOO_1_1-0.1.tar.gz
# Source3-md5:	5157d4453d17cae586ce24989d34357a
Source10:	http://ep09.pld-linux.org/~adgor/pld/%{name}-desktopfiles-0.2.tar.bz2

# PLD splash screen
Source20:	%{name}-about.bmp
Source21:	%{name}-intro.bmp

%define		cftp	http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib

# Dictionaries
Source100:	%{cftp}/dictionaries/af_ZA.zip
# Source100-md5:	f05f0cf5ffcdb4ceab933bca1596ce34
Source101:	%{cftp}/dictionaries/bg_BG.zip
# Source101-md5:	0619620e36b1a9a45995f939d765fd3e
Source102:      %{cftp}/dictionaries/ca_ES.zip
# Source102-md5:	6cea81b3e1101fb277062e7eef4ff720
Source103:      %{cftp}/dictionaries/cs_CZ.zip
# Source103-md5:	b8d4a6943ec18300a9b0047d2540209e
Source104:      %{cftp}/dictionaries/cy_GB.zip
# Source104-md5:	accdb94f38555af45a54494e046a88f3
Source105:      %{cftp}/dictionaries/da_DK.zip
# Source105-md5:	c46cd29fb20190f944b5893825b30243
Source106:      %{cftp}/dictionaries/de_AT.zip
# Source106-md5:	fdee257cc4e9d49968048a6e3edec91a
Source107:      %{cftp}/dictionaries/de_CH.zip
# Source107-md5:	2da60dd02b5a62f1a5c8b9e4a3a7fe4d
Source108:      %{cftp}/dictionaries/de_DE_comb.zip
# Source108-md5:	7bc797d02c2a9f6a6af13bf2d1f813e8
Source109:      %{cftp}/dictionaries/de_DE_neu.zip
# Source109-md5:	53d898fcad816feb23777e426de58f5e
Source110:      %{cftp}/dictionaries/de_DE.zip
# Source110-md5:	9eb02aad372bcd12209e761762ffb10a
Source111:      %{cftp}/dictionaries/el_GR.zip
# Source111-md5:	86e612d5cc243bdd0f09c919c9487c64
Source112:      %{cftp}/dictionaries/en_AU.zip
# Source112-md5:	c39f529173d8bb0e15b1fade11dfe780
Source113:      %{cftp}/dictionaries/en_CA.zip
# Source113-md5:	c14942ea471a5182f376802c68933880
Source114:      %{cftp}/dictionaries/en_EN.zip
# Source114-md5:	500a057f13d2a4aa9a4f0d8e2de92fa0
Source115:      %{cftp}/dictionaries/en_GB.zip
# Source115-md5:	31736e7e88a2cc94e17ac7d9b1ad580f
Source116:      %{cftp}/dictionaries/en_NZ.zip
# Source116-md5:	8ac9e6640d132de29571f81d33012bb8
Source117:      %{cftp}/dictionaries/en_US.zip
# Source117-md5:	523914f52e4040f51d804df4fb449544
Source118:      %{cftp}/dictionaries/es_ES.zip
# Source118-md5:	09da802fdc3361ef46fdbf7da661e08f
Source119:      %{cftp}/dictionaries/es_MX.zip
# Source119-md5:	1a8b2d34033f3d4c8e51892084e9d6fa
Source120:      %{cftp}/dictionaries/fi_FI.zip
# Source120-md5:	7925825d1a344755858ae9b69366303b
Source121:      %{cftp}/dictionaries/fo_FO.zip
# Source121-md5:	647b7b31d02fbdb33f4f309a5da4b838
Source122:      %{cftp}/dictionaries/fr_BE.zip
# Source122-md5:	63a9d20757795b157136999075ff599a
Source123:      %{cftp}/dictionaries/fr_FR.zip
# Source123-md5:	904d799ab36df32cc598a8dc7990649f
Source124:      %{cftp}/dictionaries/ga_IE.zip
# Source124-md5:	f9bb3343d14fab214cffff654586d7d1
Source125:      %{cftp}/dictionaries/gl_ES.zip
# Source125-md5:	7270162479a5efc8e6acdc61d625fa26
Source126:      %{cftp}/dictionaries/hr_HR.zip
# Source126-md5:	5c5d0479b0fb7e7d2b5e0533cc2e370b
Source127:      %{cftp}/dictionaries/hu_HU.zip
# Source127-md5:	e697bbd1025a7f11716d7988fcfba778
Source128:      %{cftp}/dictionaries/ia.zip
# Source128-md5:	b7b91df66071a5761054a5e5337b5aa9
Source129:      %{cftp}/dictionaries/id_ID.zip
# Source129-md5:	4151dd63aa18c487fc58b4f6435afe69
Source130:      %{cftp}/dictionaries/is_IS.zip
# Source130-md5:	bef105aec65714d13517415bff58c0b9
Source131:      %{cftp}/dictionaries/it_IT.zip
# Source131-md5:	0d21eeea237108d70430cb5a7e1ce61a
Source132:      %{cftp}/dictionaries/la.zip
# Source132-md5:	52ab1f91dbf6ae75c509f0dc995e20de
Source133:      %{cftp}/dictionaries/lt_LT.zip
# Source133-md5:	3590ba02288c9092340101dca3ddc132
Source134:      %{cftp}/dictionaries/Math_es_ES.zip
# Source134-md5:	07a0341691647b312ba11b2ba34c18ce
Source135:      %{cftp}/dictionaries/mi_NZ.zip
# Source135-md5:	f691ca67df4570821f931574295715b5
Source136:      %{cftp}/dictionaries/ms_MY.zip
# Source136-md5:	f1db7ff9dd8be247e1bca30042dba115
Source137:      %{cftp}/dictionaries/nb_NO.zip
# Source137-md5:	8868ade2fae74e7c07f6f30479e654d1
Source138:      %{cftp}/dictionaries/nl_med.zip
# Source138-md5:	c5acbe50d9fcfc575295fa6f12b0bf00
Source139:      %{cftp}/dictionaries/nl_NL.zip
# Source139-md5:	caab73fe1aaf03a59860765e0b7637f8
Source140:      %{cftp}/dictionaries/nn_NO.zip
# Source140-md5:	9a2826b88207e25135caa8481bebf5ad
Source141:      %{cftp}/dictionaries/no_NO.zip
# Source141-md5:	4af191480fa97dba2b9e996436531f10
Source142:      %{cftp}/dictionaries/pl_PL.zip
# Source142-md5:	92639866d223e19b6469678e12dffe12
Source143:      %{cftp}/dictionaries/pt_BR.zip
# Source143-md5:	83aa4540283c0049c27271576890fd88
Source144:      %{cftp}/dictionaries/pt_PT.zip
# Source144-md5:	6f44ed7caf6846dca9d539bb390719c4
Source145:      %{cftp}/dictionaries/ro_RO.zip
# Source145-md5:	c8a56b8d79450dcb3ca68c6987da1930
Source146:      %{cftp}/dictionaries/ru_RU_0.zip
# Source146-md5:	a5d5be04dd6180072a27090ed586427f
Source147:      %{cftp}/dictionaries/ru_RU_ie.zip
# Source147-md5:	f1e43d1d398a08761ac9a995b408ae22
Source148:      %{cftp}/dictionaries/ru_RU_io.zip
# Source148-md5:	23b346fae3b118fcb93ba9acb83d906a
Source149:      %{cftp}/dictionaries/ru_RU_ye.zip
# Source149-md5:	f166fb2b195cc3c6581fc84a6591eb59
Source150:      %{cftp}/dictionaries/ru_RU_yo.zip
# Source150-md5:	0eed06136f9beffa21f2d5406c54b10e
Source151:      %{cftp}/dictionaries/ru_RU.zip
# Source151-md5:	67da1e4d594de554a9184568235ab301
Source152:      %{cftp}/dictionaries/sk_SK.zip
# Source152-md5:	572a5674c6f1777de2eacaae60110266
Source153:      %{cftp}/dictionaries/sl_SI.zip
# Source153-md5:	a79c19d16bc26349bbded16b410616a8
Source154:      %{cftp}/dictionaries/sv_SE.zip
# Source154-md5:	8d9c49a43bfbecec6962c1344914dc8d
Source155:      %{cftp}/dictionaries/uk_UA.zip
# Source155-md5:	a0ae3b331ae5566a330d1bccc4a95791

# Hypenation Dictionaries
Source200:	%{cftp}/dictionaries/hyph_bg_BG.zip
# Source200-md5:	c9a456317214bc336d764e9d94bdd3d2
Source201:      %{cftp}/dictionaries/hyph_cs_CZ.zip
# Source201-md5:	7dc7192fb3c141db6518c54781df6846
Source202:      %{cftp}/dictionaries/hyph_da_DK.zip
# Source202-md5:	c398f568793bc62982f1179f2db0c119
Source203:      %{cftp}/dictionaries/hyph_de_CH.zip
# Source203-md5:	d8c4f525869c46cc52185356271121ab
Source204:      %{cftp}/dictionaries/hyph_de_DE.zip
# Source204-md5:	b58540aed1323894242c9c2ff9c51913
Source205:      %{cftp}/dictionaries/hyph_el_GR.zip
# Source205-md5:	6fde4ac4ec263432b0cc45e6ad4fdec5
Source206:      %{cftp}/dictionaries/hyph_en_AU.zip
# Source206-md5:	54e447e19a8ed73331afee93415ffaab
Source207:      %{cftp}/dictionaries/hyph_en_CA.zip
# Source207-md5:	2f03411f2a8335a84b64a0d7255518de
Source208:      %{cftp}/dictionaries/hyph_en_GB.zip
# Source208-md5:	1c9bda9ce2b52246ecdb7107998cbeec
Source209:      %{cftp}/dictionaries/hyph_en_NZ.zip
# Source209-md5:	54e447e19a8ed73331afee93415ffaab
Source210:      %{cftp}/dictionaries/hyph_en_US.zip
# Source210-md5:	54e447e19a8ed73331afee93415ffaab
Source211:      %{cftp}/dictionaries/hyph_es_ES.zip
# Source211-md5:	7fc4be41cf7b6cdadd7dfbf56c701551
Source212:      %{cftp}/dictionaries/hyph_es_MX.zip
# Source212-md5:	f0e308d132801b593925b14bb5905bb8
Source213:      %{cftp}/dictionaries/hyph_fi_FI.zip
# Source213-md5:	1fc88b865f919a9323d72843e860e266
Source214:      %{cftp}/dictionaries/hyph_fr_BE.zip
# Source214-md5:	4548b4c184377148109538892b5e6dea
Source215:      %{cftp}/dictionaries/hyph_fr_FR.zip
# Source215-md5:	eb13ba5b369e72bc45f5762745ca4471
Source216:      %{cftp}/dictionaries/hyph_ga_IE.zip
# Source216-md5:	bd410dd925853de0dc7e5e117ac2555d
Source217:      %{cftp}/dictionaries/hyph_hu_HU.zip
# Source217-md5:	09fde61c70a7b1c53e22d08b763a5b80
Source218:      %{cftp}/dictionaries/hyph_id_ID.zip
# Source218-md5:	41b1f922c4d5b3d02987074e0d6bb6ee
Source219:      %{cftp}/dictionaries/hyph_is_IS.zip
# Source219-md5:	448230e966bdf68d5f8abffd18480402
Source220:      %{cftp}/dictionaries/hyph_it_IT.zip
# Source220-md5:	db546e7bb7cf72fc3c751e70f83ed659
Source221:      %{cftp}/dictionaries/hyph_lt_LT.zip
# Source221-md5:	6d90a1e831f639137077879dacb596cb
Source222:      %{cftp}/dictionaries/hyph_nl_NL.zip
# Source222-md5:	ba5c271337479a8f8ddc2a3d6a99b37b
Source223:      %{cftp}/dictionaries/hyph_pl_PL.zip
# Source223-md5:	2f81a155d8aa7479c912ae019eb5bae0
Source224:      %{cftp}/dictionaries/hyph_pt_BR.zip
# Source224-md5:	aec223b5efc1e231015ebd2ae9c359e6
Source225:      %{cftp}/dictionaries/hyph_pt_PT.zip
# Source225-md5:	327989bbbfc9f9d56eb772427a344eb3
Source226:      %{cftp}/dictionaries/hyph_ru_RU.zip
# Source226-md5:	f8a8b8a368bc7394b5a4060082c44bb4
Source227:      %{cftp}/dictionaries/hyph_sk_SK.zip
# Source227-md5:	89ad655afadb78f6ceb87d9e1e3a675f
Source228:      %{cftp}/dictionaries/hyph_sl_SI.zip
# Source228-md5:	1a9ae1d95f0f12a7909c1d4e2c5fd8e1
Source229:      %{cftp}/dictionaries/hyph_sv_SE.zip
# Source229-md5:	a1c31b48cbf570bb05f22e98dacb9e17
Source230:      %{cftp}/dictionaries/hyph_uk_UA.zip
# Source230-md5:	b87fc9d4668dac5b5bd7b943aee85efd

# Thesaurus Dictionaries
Source300:	%{cftp}/dictionaries/thes_bg_BG.zip
# Source300-md5:	630ec215fcf655b99429ca7c97667b8d
Source301:      %{cftp}/dictionaries/thes_de_DE.zip
# Source301-md5:	ffe02a241bbe6acfb9992f49b40360b9
Source302:      %{cftp}/dictionaries/thes_en_US.zip
# Source302-md5:	6262581a06eacc011ec4d87534721b0e
Source303:      %{cftp}/dictionaries/thes_fr_FR.zip
# Source303-md5:	061d832c6a6537a61770d3e065e0b1bb
Source304:      %{cftp}/dictionaries/thes_hu_HU.zip
# Source304-md5:	20e4bfe680999629270e1e8b7e2534e5

# Help content
Source400:      %{cftp}/helpcontent/helpcontent_01_unix.tgz
# Source400-md5:	7da2aff674c2c84aba8b21ac2ab16bb6
Source401:      %{cftp}/helpcontent/helpcontent_31_unix.tgz
# Source401-md5:	c7e618e2d9b8bd25cae12954ef2548c9
Source402:      %{cftp}/helpcontent/helpcontent_33_unix.tgz
# Source402-md5:	68d58bc30b485a77c0a0fba08af3aee3
Source403:      %{cftp}/helpcontent/helpcontent_34_unix.tgz
# Source403-md5:	8696bbee3dc4d5b6fd60218123016e29
Source404:      %{cftp}/helpcontent/helpcontent_39_unix.tgz
# Source404-md5:	c2ae86d02f462d2b663d621190f5ef34
Source405:      %{cftp}/helpcontent/helpcontent_46_unix.tgz
# Source405-md5:	7b013981edce2fabe4a8751ff64a8d58
Source406:      %{cftp}/helpcontent/helpcontent_49_unix.tgz
# Source406-md5:	a39f44ec40f452c963a4a187f31d1acb
Source407:      %{cftp}/helpcontent/helpcontent_81_unix.tgz
# Source407-md5:	81b705057a0e14ebcbf02fac4762781a
Source408:      %{cftp}/helpcontent/helpcontent_82_unix.tgz
# Source408-md5:	3121fbd251176d7c7b6e33ecec744c65
Source409:      %{cftp}/helpcontent/helpcontent_86_unix.tgz
# Source409-md5:	aee37935139c5ccd4b6d8abdd2037c66
Source410:      %{cftp}/helpcontent/helpcontent_88_unix.tgz
# Source410-md5:	3b00571318e45965dee0545d86306d65

Source499:	%{name}-additional-dictionaries.txt

Patch0:		%{name}-rh-disable-spellcheck-all-langs.patch
Patch1:		%{name}-pld-stlport.patch
Patch2:		%{name}-pld-ximian-is-pld.patch
Patch3:		%{name}-pld-copy-all-bmp.patch
Patch4:		%{name}-pld-ooo-build-ldver.patch
Patch5:		%{name}-pld-nptl.patch
Patch6:		%{name}-pld-do-not-overwrite-configopt.patch
Patch7:		%{name}-pld-package-lang.patch

URL:		http://www.openoffice.org/
BuildRequires:	ImageMagick
BuildRequires:	STLport-devel >= 4.5.3-6
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison >= 1.875-4
BuildRequires:	cups-devel
BuildRequires:	db-devel
BuildRequires:	db-cxx-devel
BuildRequires:	/usr/bin/getopt
%if %{with java}
BuildRequires:	db-java
BuildRequires:	jar
BuildRequires:	jdk
%else
BuildRequires:	libxslt-progs
%endif
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	libstdc++-devel >= 3.2.1
BuildRequires:	curl-devel
BuildRequires:	unixODBC-devel
BuildRequires:	sane-backends-devel
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	tcsh
BuildRequires:	unzip
BuildRequires:	zip
BuildRequires:	zlib-devel
# more and more...
BuildRequires:  pkgconfig
BuildRequires:  startup-notification-devel
BuildRequires:  libart_lgpl-devel
%if %{with kde}
BuildRequires:	qt-devel
BuildRequires:	kdelibs-devel
%else
BuildRequires:	gtk+2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:  libbonobo-devel
BuildRequires:	libgnomecups-devel
%endif
BuildConflicts:	java-sun = 1.4.2
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n-en = %{epoch}:%{version}-%{release}
Requires:	%{name}-dict-en
Requires:	libstdc++ >= 3.2.1
Requires:	cups-lib
Requires:	db
Requires:	db-cxx
Requires:	startup-notification
%if ! %{with kde}
Requires:	libgnomecups
Requires:	gnome-vfs2
%endif
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

%description libs
OpenOffice.org productivity suite - shared libraries.

%description libs -l pl
Pakiet biurowy OpenOffice.org - biblioteki.

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

#%files i18n-ar -f i18n-ar
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

#%files i18n-ca -f i18n-ca
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

#%files i18n-cs -f i18n-cs
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

#%files i18n-da -f i18n-da
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

#%files i18n-de -f i18n-de
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

#%files i18n-el -f i18n-el
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

#%files i18n-en -f i18n-en
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

#%files i18n-es -f i18n-es
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

#%files i18n-fi -f i18n-fi
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

#%files i18n-fr -f i18n-fr
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

#%files i18n-it -f i18n-it
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

#%files i18n-ja -f i18n-ja
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

#%files i18n-ko -f i18n-ko
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

#%files i18n-nl -f i18n-nl
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

#%files i18n-pl -f i18n-pl
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

#%files i18n-pt -f i18n-pt
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

#%files i18n-pt_BR -f i18n-pt_BR
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

#%files i18n-ru -f i18n-ru
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

#%files i18n-sk -f i18n-sk
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

#%files i18n-sv -f i18n-sv
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

#%files i18n-tr -f i18n-tr
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

#%files i18n-zh_CN -f i18n-zh_CN
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

#%files i18n-zh_TW -f i18n-zh_TW
%endif

%prep
%setup -q -n ooo-build-%{ooobver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

install -d src
ln -s %{SOURCE1} src/
ln -s %{SOURCE2} src/
ln -s %{SOURCE3} src/

ln -s %{SOURCE20} src/openabout_pld.bmp
ln -s %{SOURCE21} src/openintro_pld.bmp

%build
# Make sure we have /proc mounted - otherwise idlc will fail later.
[ -r /proc/version ] || exit 1

CC=%{__cc}
CXX=%{__cxx}
GCJ=gcj
JAVA_HOME="/usr/lib/java"
ENVCFLAGS="%{rpmcflags}"
ENVCFLAGSCXX="%{rpmcflags}"
DESTDIR=$RPM_BUILD_ROOT
IGNORE_MANIFEST_CHANGES=1
export JAVA_HOME CC CXX GCJ ENVCFLAGS ENVCFLAGSCXX DESTDIR IGNORE_MANIFEST_CHANGES

if [ -z "$RPM_BUILD_NCPUS" ] ; then
	if [ -x /usr/bin/getconf ] ; then
		RPM_BUILD_NCPUS=$(/usr/bin/getconf _NPROCESSORS_ONLN)
		if [ $RPM_BUILD_NCPUS -eq 0 ] ; then 
			RPM_BUILD_NCPUS=1
		fi
	else 
		RPM_BUILD_NCPUS=1
	fi
fi

# parallel build is broken
RPM_BUILD_NCPUS=1

CONFOPTS=" \
	--with-system-gcc \
	--with-system-zlib \
	--with-system-sane-headers \
	--with-system-x11-extensions-headers \
	--with-system-unixodbc-headers \
	--with-system-db \
	--with-system-curl \
	--with-system-freetype \
	--with-vendor="PLD" \
	--with-distro="Ximian" \
%if %{with kde}
	--with-icons="KDE" \
	--with-widgetset=kde \
%else
	--with-icons="Ximian" \
	--with-widgetset=gtk \
%endif
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
	--enable-crashdump \
	--enable-libsn \
	--enable-libart \
	--disable-rpath \
	--disable-symbols \
	--with-num-cpus=$RPM_BUILD_NCPUS
"

# for cvs snaps
[ -x ./autogen.sh ] && ./autogen.sh $CONFOPTS

# build-ooo script will pickup these
CONFIGURE_OPTIONS="$CONFOPTS"; export CONFIGURE_OPTIONS

# main build
%configure $CONFOPTS

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT; export DESTDIR

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for file in \
	%{SOURCE100} %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} %{SOURCE105} \
	%{SOURCE106} %{SOURCE107} %{SOURCE108} %{SOURCE109} %{SOURCE110} %{SOURCE111} \
	%{SOURCE112} %{SOURCE113} %{SOURCE114} %{SOURCE115} %{SOURCE116} %{SOURCE117} \
	%{SOURCE118} %{SOURCE119} %{SOURCE120} %{SOURCE121} %{SOURCE122} %{SOURCE123} \
	%{SOURCE124} %{SOURCE125} %{SOURCE126} %{SOURCE127} %{SOURCE128} %{SOURCE129} \
	%{SOURCE130} %{SOURCE131} %{SOURCE132} %{SOURCE133} %{SOURCE134} %{SOURCE135} \
	%{SOURCE136} %{SOURCE137} %{SOURCE138} %{SOURCE139} %{SOURCE110} %{SOURCE141} \
	%{SOURCE142} %{SOURCE143} %{SOURCE144} %{SOURCE145} %{SOURCE146} %{SOURCE147} \
	%{SOURCE148} %{SOURCE149} %{SOURCE150} %{SOURCE151} %{SOURCE152} %{SOURCE153} \
	%{SOURCE154} %{SOURCE155} \
	%{SOURCE200} %{SOURCE201} %{SOURCE202} %{SOURCE203} %{SOURCE204} %{SOURCE205} \
	%{SOURCE206} %{SOURCE207} %{SOURCE208} %{SOURCE209} %{SOURCE210} %{SOURCE211} \
	%{SOURCE212} %{SOURCE213} %{SOURCE214} %{SOURCE215} %{SOURCE216} %{SOURCE217} \
	%{SOURCE218} %{SOURCE219} %{SOURCE220} %{SOURCE221} %{SOURCE222} %{SOURCE223} \
	%{SOURCE224} %{SOURCE225} %{SOURCE226} %{SOURCE227} %{SOURCE228} %{SOURCE229} \
	%{SOURCE230} \
	%{SOURCE300} %{SOURCE301} %{SOURCE302} %{SOURCE303} %{SOURCE304}; do
		unzip -o -d $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo $file
done
cat %{SOURCE499} >> $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo/dictionary.lst

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

install -d $RPM_BUILD_ROOT%{_desktopdir}
bzip2 -dc %{SOURCE10} | tar xf - -C $RPM_BUILD_ROOT%{_desktopdir}

# Add in the regcomp tool since some people need it for 3rd party add-ons
cp -f build/OOO_%{dfullver}/solver/%{subver}/unxlng*.pro/bin/regcomp $RPM_BUILD_ROOT%{_libdir}/%{name}/program

# OOo should not install the Vera fonts, they are Required: now
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/fonts/truetype/*

# Copy fixed OpenSymbol to correct location
install -d $RPM_BUILD_ROOT%{_datadir}/fonts/openoffice
cp fonts/opens___.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/openoffice
# %%ghost the fonts.cache-1 file
touch $RPM_BUILD_ROOT%{_datadir}/fonts/openoffice/fonts.cache-1

# We don't need spadmin or the setup application
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/setup
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/spadmin
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/spadmin
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/openoffice-setup.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/openoffice-printeradmin.desktop

# Remove some python cruft
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/program/python-core-*/lib/test

rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/kde
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/gnome
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/share/cde

#rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/program/gnomeint

# Freetype creeps in somehow
rm -f %{_libdir}/%{name}/program/filter/libfreetype.so*

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
# Take list from dictionaries
for lang in $RPM_BUILD_ROOT%{_libdir}/%{name}/share/dict/ooo/*.aff; do
	eval `echo "$lang" | sed -e 's#.*/\(.*\)\.aff#\1#g' | awk -F_ ' { print "FLANG=\"" $1 "\"\nSLANG=\"" $2 "\"\nTLANG=\"" $3; "\""; } '`
	# we take only first code ie xx_YY -> we take xx
	nlang="$FLANG"
	# nlonglang=$(../bin/openoffice-xlate-lang -l "$nlang" 2> /dev/null)
	echo "%%defattr(644,root,root,755)" > ${nlang}.lang
	[ -f build/lang_${nlang}_list.txt ] && sed -e "s#$RPM_BUILD_ROOT#%%lang(${nlang}) #g" build/lang_${nlang}_list.txt >> ${nlang}.lang
	find $RPM_BUILD_ROOT -type d | sed -e "s#$RPM_BUILD_ROOT##g" -e "s#\(.*/${nlang}\)\$#%%lang(${nlang}) \1#g" | grep -E '^%%lang' >> ${nlang}.lang
	if [ -n "$nlonglang" ]; then
		find $RPM_BUILD_ROOT -type d | sed -e "s#$RPM_BUILD_ROOT##g" -e "s#\(.*/${nlonglang}\)\$#%%lang(${nlang}) \1#g" | grep -E '^%%lang' >> ${nlang}.lang
	fi
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc readlicense/source/license/unx/LICENSE
%doc %{_libdir}/%{name}/LICENSE*
%doc %{_libdir}/%{name}/*README*

%dir %{_sysconfdir}/openoffice
#%config %{_sysconfdir}/openoffice/autoresponse.conf

%{_desktopdir}/*.desktop
#%{_pixmapsdir}/*.png
#%{_pixmapsdir}/document-icons/*.png

%{_libdir}/%{name}/program/*.rdb
%{_libdir}/%{name}/program/*.bmp
%{_libdir}/%{name}/program/user_registry.xsl

%{_libdir}/%{name}/program/sofficerc
%{_libdir}/%{name}/program/unorc
%{_libdir}/%{name}/program/bootstraprc
%{_libdir}/%{name}/program/configmgrrc
%{_libdir}/%{name}/program/instdb.ins

# dirs/trees
#%{_libdir}/%{name}/program/classes

%dir %{_libdir}/%{name}/program/resource
#%{_libdir}/%{name}/program/resource/bmp.res
#%{_libdir}/%{name}/program/resource/crash_dump.res

# mozilla
#%%{_libdir}/%{name}/program/defaults
#%%{_libdir}/%{name}/program/component.reg
#%%{_libdir}/%{name}/program/components/*.xpt
#%%{_libdir}/%{name}/program/components/*.dat

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
#%{_libdir}/%{name}/share/xslt

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
%{_libdir}/%{name}/user/database
%{_libdir}/%{name}/user/gallery
%{_libdir}/%{name}/user/psprint

%{_libdir}/%{name}/user/autotext/english

# Programs
%attr(755,root,root) %{_bindir}/oo*

#%attr(755,root,root) %{_libdir}/%{name}/setup
#%attr(755,root,root) %{_libdir}/%{name}/spadmin

%attr(755,root,root) %{_libdir}/%{name}/program/*.bin
#%attr(755,root,root) %{_libdir}/%{name}/program/crash_report
#%attr(755,root,root) %{_libdir}/%{name}/program/fromtemplate
#%attr(755,root,root) %{_libdir}/%{name}/program/gnomeint
%if %{with java}
%attr(755,root,root) %{_libdir}/%{name}/program/javaldx
%attr(755,root,root) %{_libdir}/%{name}/program/jvmsetup
%endif
%attr(755,root,root) %{_libdir}/%{name}/program/nswrapper
%attr(755,root,root) %{_libdir}/%{name}/program/pagein*
%attr(755,root,root) %{_libdir}/%{name}/program/setup
%attr(755,root,root) %{_libdir}/%{name}/program/soffice
#%attr(755,root,root) %{_libdir}/%{name}/program/sopatchlevel.sh
#%attr(755,root,root) %{_libdir}/%{name}/program/spadmin
%attr(755,root,root) %{_libdir}/%{name}/program/getstyle-gnome
%attr(755,root,root) %{_libdir}/%{name}/program/msgbox-gnome

# %files devel ?????????
#%attr(755,root,root) %{_bindir}/autodoc
#%attr(755,root,root) %{_bindir}/cppumaker
#%attr(755,root,root) %{_bindir}/idlc
#%attr(755,root,root) %{_bindir}/idlcpp
#%attr(755,root,root) %{_bindir}/javamaker
#%attr(755,root,root) %{_bindir}/rdbmaker
#%attr(755,root,root) %{_bindir}/regcomp
#%attr(755,root,root) %{_bindir}/regmerge
#%attr(755,root,root) %{_bindir}/regview
#%attr(755,root,root) %{_bindir}/uno
#%attr(755,root,root) %{_bindir}/xml2cmp

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/program
#%%dir %{_libdir}/%{name}/program/components -- mozilla
%dir %{_libdir}/%{name}/program/filter

%attr(755,root,root) %{_libdir}/%{name}/program/*.so
%attr(755,root,root) %{_libdir}/%{name}/program/*.so.*
#%%attr(755,root,root) %{_libdir}/%{name}/program/components/*.so -- mozilla
%attr(755,root,root) %{_libdir}/%{name}/program/filter/*.so

%files mimelinks
%defattr(644,root,root,755)
#%{_datadir}/mimelnk/application/*
