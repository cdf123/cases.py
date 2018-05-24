#!/usr/bin/python
import sys
import itertools

for str in map(''.join, itertools.product(*((c.upper(), c.lower()) for c in sys.argv[1]))):
    print str
