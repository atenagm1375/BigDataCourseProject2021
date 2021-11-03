#!/usr/bin/env python3

import sys


for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	print('{0}\t{1}'.format(data[1], data[0]))
