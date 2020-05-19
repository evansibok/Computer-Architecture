#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

if len(sys.argv) < 2:
    print("usage: ls8.py <filename>.ls8")
    sys.exit(1)

cpu.load(sys.argv[1])
# # alu(self, op, reg_a, reg_b)
# cpu.alu(opCode, reg_a, reg_b)
cpu.run()
