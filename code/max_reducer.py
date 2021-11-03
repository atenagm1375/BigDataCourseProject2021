#!/usr/bin/env python3

import sys


maxval = 0
maxfile = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	k, v = data
	if maxval < int(k):
		maxval = int(k)
		maxfile = v

if maxfile:
	print('{0}\t{1}'.format(maxfile, maxval))
