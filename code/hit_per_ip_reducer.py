#!/usr/bin/env python3

import sys


total = 0
prev = None

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 2:
		continue

	k, v = data
	if prev and prev != k:
		print('{0}\t{1}'.format(prev, total))
		total = 0

	prev = k
	total += int(v)

if prev:
	print('{0}\t{1}'.format(prev, total))
