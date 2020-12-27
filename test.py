#!/usr/bin/env python3
import os
import os.path
import csv

csvdata = []

csv_file = os.path.join("template","icons.csv")
icon_path = os.path.join("template","image")

def Enquiry(lis1):
	if len(lis1) == 0:
		return 0
	else:
		return 1

def csv_reader(file_obj):
	with open(file_obj, "r") as csvfile:
		csv_data = csv.reader(csvfile)	
		for row in csv_data:
			# print(row) # Debug
			# csvdata.append(row)
			#print(str(' '.join(row)).split(' '))
			csvdata.append(str(' '.join(row)).split(' '))

def compare( value, listname = csvdata):
	_tmp = ""
	for i in range(len(listname)):
		for j in range(len(listname[i])):
			if str(listname[i][j]).lower() in str(value).lower(): _tmp = listname[i][0] + ".png"
	if Enquiry(_tmp): return _tmp
	else: return False

csv_reader(csv_file)

in_file = 'full.index.m4v'

def check_the_file(fname):
	root_name = os.path.splitext(fname)[0]
	root_ext = os.path.splitext(fname)[1]
	root_result = compare(root_ext)
	if root_result != False: return root_result
	else:
		return False

print(check_the_file(in_file))

