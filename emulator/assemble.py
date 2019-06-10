#/usr/bin/env python
# -*- coding: utf-8 -*-

from td4lib import *
import sys

if len(sys.argv)!=2:
    print("Usage python %s asm_file" % sys.argv[0])
    exit()
file = sys.argv[1]

td4=TD4()
td4.load_asm(file)
td4.dump_rom2()