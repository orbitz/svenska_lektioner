#!/usr/bin/env python

import sys

column = int(sys.argv[1])
infile = sys.argv[2]

for line in open(infile):
    sline = line.strip().split('\t')
    print sline[column]
    sys.stdin.readline()
    print ' | '.join(sline)
    print

