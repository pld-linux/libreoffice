#!/bin/sh
# ------------------------------------------------------------------------
# Red Hat replacement for org.openoffice.configuration.XMLDefaultGenerator
# XSLT processor using xsltproc
# ------------------------------------------------------------------------
if [ "x$1" = x-Xmx128m ]; then
  shift
else
  echo First argument not -Xmx128m
  exit 1
fi
if [ "x$1" = x-classpath ]; then
  shift
else
  echo First argument not -classpath
  exit 1
fi
shift
if [ "$1" != org.openoffice.configuration.XMLDefaultGenerator ]; then
  echo Only org.openoffice.configuration.XMLDefaultGenerator emulated
  exit 1
fi
shift
xcd=$1
xml="`dirname $1`/`basename $1 .xcd`.xml"
if echo "$xcd" | grep -qv ^/; then
  xcd="`pwd`/$xcd"
fi
util=$2
misc=$3
data=$4
dtd=`grep 'schema:component SYSTEM' $xcd | cut -d\" -f2`
if echo "$dtd" | grep -qv ^/; then
  dtd="`dirname $xcd`/$dtd"
fi
if echo "$util" | grep -qv ^/; then
  util="`pwd`/$util"
fi
# Someone XML aware tell me how XML parser finds out it wants to load
# instance{,2}.xsl from the .xcd and .dtd files
if echo "$dtd" | grep -q description2; then
  xsl="$util/instance2.xsl"
else
  xsl="$util/instance.xsl"
fi
xmli="$misc/instance/$xml"
xmlt="$misc/template/$xml"
mkdir -p `dirname $xmli`
mkdir -p `dirname $xmlt`
echo "** Start validating: file:$xcd"
tmpd=`mktemp -d /tmp/ooxmlparse.XXXXXX` || exit 1
gcc -xc - -o $tmpd/utf8filter <<"EOF"
#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>

int main (void)
{
  char *buf = NULL, *p, *q, b[8];
  size_t bufsize = 0;

  while (getline (&buf, &bufsize, stdin) >= 0)
    {
      p = buf;
      while ((q = strstr (p, "&#x")) != NULL)
	{
	  wchar_t w;
	  int i;

	  *q = '\0';
	  fputs (p, stdout);
	  w = strtoul (q + 3, &p, 16);
	  if (*p++ != ';')
	    abort ();
	  if (w < 0x80)
	    b[0] = w, b[1] = '\0';
	  else if (w >= 0x7fffffff)
	    abort ();
	  else
	    {
	      for (i = 2; i < 6; i++)
		if ((w & (0xffffffff << (5 * i + 1))) == 0)
		  break;
	      b[0] = 0xffffff00 >> i;
	      b[i--] = '\0';
	      do
		{
		  b[i] = 0x80 | (w & 0x3f); w >>= 6;
		}
	      while (--i > 0);
	      b[0] |= w;
	    }
	  fputs (b, stdout);
	}
      fputs (p, stdout);
    }
  exit (0);
}
EOF
cp -a $dtd $tmpd/foo.dtd
sed 's~^\(.*<xsl:attribute name="\)xml:lang\(".*\)$~&\
\1cfg:xmllang\2~' $xsl > $tmpd/foo.xsl
needs="`sed -n -e 's~^.*cfg:component="\([^"]*\)".*$~\1~p' $xcd | sort -u`"
sedcmd=""
for np in $needs; do
  n=`echo $np | sed -e 's~\.~/~g'`
  na=`basename $n`
  sed -e '/schema:component SYSTEM/s~^\([^"]*"\)[^"]*\(".*\)$~\1foo.dtd\2~' $n.xcd > $tmpd/$na.xcd
  ln -sf $na.xcd $tmpd/$na.xml
  sedcmd="$sedcmd;s@cfg:component=\"$np\"@cfg:component=\"$na\"@g"
done
sed -e '/schema:component SYSTEM/s~^\([^"]*"\)[^"]*\(".*\)$~\1foo.dtd\2~' -e "$sedcmd" $xcd > $tmpd/foo.xcd
cat > $tmpd/postprocess.sed <<"EOF"
s~xmlns:cfg="" ~~g
s~xmlns:cfg\(="[^"]*"\)[ 	]*\(cfg:package="[^"]*"\)~\2 xmlns:xcfg\1~
s~[ 	]*xmlns:cfg="[^"]>~~g
s~xmlns:cfg="[^"]*"[ 	]*~~g
s~xmlns:xcfg~xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance" xmlns:cfg~
s~^\(<?xml.*\)?>~\1 encoding="utf-8"?>~
s~<\([a-zA-Z0-9_:]*\)\([ 	][^>]*\)></\1>~<\1\2/>~g
s~&quot;~"~g
s~[ 	]name=~ cfg:name=~g
s~[ 	]type=~ cfg:type=~g
s~xmllang=~xml:lang=~g
s~xmlns:xsi=""[ 	]*~~g
s~\(<ooInetSuffix[^>]*\)[ 	]cfg:null="true"~\1~g
s~cfg:null=~xsi:null=~g
EOF
pushd $tmpd >/dev/null 2>&1
xsltproc foo.xsl foo.xcd 2>/dev/null \
  | sed -f postprocess.sed | ./utf8filter > instance
# For some reason cfg:instance-of from different component doesn't work for template
# generation. Work around it.
if grep -q 'schema:instance cfg:instance-of="Font" cfg:name="Font" cfg:component="Common"' foo.xcd; then
  sed -n '/schema:group[ 	]*cfg:name="Font"/,/\/schema:group/p;/\/schema:templates/q' Common.xcd > Font.xcd
  sed '/<schema:templates>/r Font.xcd' foo.xcd > foo.xcd.new
  sed '/schema:instance cfg:instance-of="Font" cfg:name="Font"/s~[ 	]*cfg:component="Common"~~' foo.xcd.new > foo.xcd
fi
xsltproc --stringparam templates true foo.xsl foo.xcd 2>/dev/null \
  | sed -f postprocess.sed | ./utf8filter > template
if [ -f foo.xcd.new ]; then
  # Finish the workaround.
  awk '/<Font>/ { if (!a) { b=1; next; }
		  sub(/<Font>/,"<Font xmlns:xsi=\"http://www.w3.org/1999/XMLSchema-instance\">"); }
       /<\/Font>/ { if (!a) { a=1; b=0; next; } }
       { if (b) next; print; }' template > template.new
  mv -f template.new template
fi
popd >/dev/null 2>&1
cat $tmpd/instance > $xmli
cat $tmpd/template > $xmlt
rm -rf $tmpd
echo "** Document is valid!"
exit 0
