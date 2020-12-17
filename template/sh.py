#!/usr/bin/env python3

import csv

with open('icons.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		print(row)
		# print(' '.join(row))
