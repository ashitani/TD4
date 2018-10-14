#/usr/bin/env python
# -*- coding: utf-8 -*-

from td4lib import *
import sys

argn=len(sys.argv)
if argn!=2 and argn!=3:
    print("Usage python %s asm_file [clock frequency(Hz)]" % sys.argv[0])
    print("default clock frequency=10[Hz]")
    exit()

if argn==3:
    freq=sys.argv[2]
else:
    freq=10

file = sys.argv[1]

td4=TD4()
td4.load_asm(file)
td4.run(freq=freq)
