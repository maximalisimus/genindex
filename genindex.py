#!/usr/bin/env python3

import csv
import os
import os.path
import sys
import math
from typing import Any

csvdata: list[Any] = []

directory = ""
_font = "sans-serif"
_bgcolor = "white"
_exclude_dir: list[Any] = []
_exclude_file: list[Any] = []

csv_file = "config/template/icons.csv"
icon_path = "config/template/image/"

def switch(case):
	return {
		"-font": 1,
		"-bgcolor": 2,
		"-exclude-dir": 3,
		"-exclude-file": 4,
		"-v": 5,
		"-h": 6
	}.get(case, None)

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
			if listname[i][j] == value: _tmp = listname[i][0]
	return _tmp

def printcsv(listname = csvdata):
	for i in range(len(listname)):
		# print(listname[i][0], end = '\n')
		for j in range(len(listname[i])):
			print(listname[i][j], end = '\n')

def main():
	global _font, _bgcolor
	if len(sys.argv) <= 1:
		print("Error! You did not specify a destination directory!")
		exit(1)
	elif len(sys.argv) == 1:
		if not os.path.isdir(sys.argv[1]):
			print("The specified parameter {0} is not a directory!".format(sys.argv[1]))
			exit(2)
		else:
			directory = sys.argv[1]
	else:
		if not os.path.isdir(sys.argv[1]):
			print("The specified parameter {0} is not a directory!".format(sys.argv[1]))
			exit(2)
		else:
			directory = sys.argv[1]
		for count in range(len(sys.argv)):
			if switch(sys.argv[count]) == 1: _font = sys.argv[count+1]
			if switch(sys.argv[count]) == 2: _bgcolor = sys.argv[count + 1]
			if switch(sys.argv[count]) == 3: _exclude_dir.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 4: _exclude_file.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 5: print("Versions")
			if switch(sys.argv[count]) == 6: print("Help!")
	print("Font = " + _font)
	print("BGColor = " + _bgcolor)
	# print("\nExclude dir:")
	# print(_exclude_dir)
	# print("\nExclude files: ")
	# print(_exclude_file)
	csv_reader(csv_file)
	# print(csvdata)
	# printcsv()
	# _file = compare("rar")
	# if _file != "": _str = icon_path + _file + ".png"

if __name__=="__main__":
	main()
