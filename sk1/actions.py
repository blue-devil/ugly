#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

def setup():
	shelltools.export("LANG", "en_US.UTF-8")
	shelltools.system("ln -s setup-sk1.py setup.py")

def build():
	pythonmodules.compile()

def install():
	pythonmodules.install()
