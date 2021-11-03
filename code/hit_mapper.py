#!/usr/bin/env python3

import sys


for line in sys.stdin:
	data = line.strip().split("GET ")
	if len(data) > 1:
		filename = data[1].split()[0]
		print('{0}\t{1}'.format(filename, 1))
