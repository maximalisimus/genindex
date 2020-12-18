#!/usr/bin/env python3

import csv

with open('icons.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')	
	results = []
	for row in spamreader:
		results.append(row)
	for i in range(len(results)):
		# print(results[i][0], end = '\n')
		for j in range(len(results[i])):
			print(results[i][j], end = '\n')
		# print(' '.join(row))
