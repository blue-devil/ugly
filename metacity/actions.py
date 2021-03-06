#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	#pisitools.cflags.remove("-O2")
	autotools.configure("--enable-debug=yes --disable-static \
                         --disable-canberra \
                         --disable-schemas-compile \
                         --disable-startup-notification")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
	pisitools.removeDir("/usr/share/gnome-control-center")

