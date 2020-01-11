#!/usr/bin/env python3

#
# This is the 2nd simulation script example.
#

import sys
import os
import argparse


print("=" * 40)
print(' '.join(sys.argv))


# define args for simulation script
parser = argparse.ArgumentParser()
parser.add_argument("-dump", action="store_true", help="whether dump waveform")
parser.add_argument("-tc", type=str, help="specify testcase")
args = parser.parse_args()

# fixed simulation command
cmd = "irun -64bit -access rwc"

# handle variable options
if args.dump:
    cmd += " -define DUMP"

tc = 'tc_default'
if args.tc:
    tc = args.tc

cmd += ' +UVM_TESTNAME=' + tc

# add tb and dut file
cmd += ' -f tb.flist'
cmd += ' -f dut.flist'

# print and execute command
print('RUN: ' + cmd)
os.system(cmd)

