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

csv_file = os.path.join("template","icons.csv")
icon_path = os.path.join("template","image")
# csv_file = "template/icons.csv"
# icon_path = "template/image/"

def switch(case):
	return {
		"-dir": 1,
		"-font": 2,
		"-bgcolor": 3,
		"-exclude-dir": 4,
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
			if str(listname[i][j]).lower() in str(value).lower(): _tmp = listname[i][0] + ".png"
	return _tmp

def stripCurrentDir(path):
	return path.replace("./", "").replace("/.", "")

def printcsv(listname = csvdata):
	for i in range(len(listname)):
		# print(listname[i][0], end = '\n')
		for j in range(len(listname[i])):
			print(listname[i][j], end = '\n')

def Enquiry(lis1):
	if len(lis1) == 0:
		return 0
	else:
		return 1

def is_part_in_list(str_, words):
	for word in words:
		if word.lower() in str_.lower():
			return True
	return False

def work_in_dir(value_dir):
	for dirpath, dirnames, filenames in os.walk(value_dir, True, None, False):
		_real_dir = str(dirpath).replace(value_dir, "")
		if Enquiry(_exclude_dir):
			if not is_part_in_list(_real_dir, _exclude_dir):
				for a in _exclude_dir:
					if str(a).lower() in dirnames: dirnames.remove(a)
				print("Каталог:", _real_dir)
				if Enquiry(dirnames):
					dirnames.sort()
					for dirname in dirnames:
						print("Direcory:", dirname)
				else:
					print("Directory is found!")
				if Enquiry(filenames):
					filenames.sort()
					for filename in filenames:
						print("Filename:", filename)
		else:
			print("Каталог:", _real_dir)
			if Enquiry(dirnames):
				dirnames.sort()
				for dirname in dirnames:
					print("Direcory:", dirname)
			else:
				print("Directory is found!")
			if Enquiry(filenames):
				filenames.sort()
				for filename in filenames:
					print("Filename:", filename)

def main():
	if len(sys.argv) > 2:
		for count in range(len(sys.argv)):
			if switch(sys.argv[count]) == 1: directory = sys.argv[count + 1]
			if switch(sys.argv[count]) == 2: _font = sys.argv[count + 1]
			if switch(sys.argv[count]) == 3: _bgcolor = sys.argv[count + 1]
			if switch(sys.argv[count]) == 4: _exclude_dir.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 5: print("Versions")
			if switch(sys.argv[count]) == 6: print("Help!")
		if not os.path.isdir(directory):
			print("Parameter is not the directory", directory)
			exit(1)
		# print("Font = " + _font)
		# print("BGColor = " + _bgcolor)
		# print("\nExclude dir:")
		# print(_exclude_dir)
		# print("\nExclude files: ")
		# print(_exclude_file)
		csv_reader(csv_file)
		# print(csvdata)
		# printcsv()
		# _file = compare(".exe")
		# if _file != "":
		#	print(_file)
		#	_str = os.path.join(icon_path,_file)
		#	# _str = icon_path + _file
		#	print(_str)
		# work_in_dir(directory)

if __name__=="__main__":
	main()
