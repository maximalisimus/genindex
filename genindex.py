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
_exclude: list[Any] = []

csv_file = "config/template/icons.csv"
icon_path = "config/template/image/"

def switch(case):
	return {
		"-font": 1,
		"-bgcolor": 2,
		"-exclude": 3,
		"-v": 4,
		"-h": 5
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
			if switch(sys.argv[count]) == 3: _exclude.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 4: print("Versions")
			if switch(sys.argv[count]) == 5: print("Help!")
	# print("Font = " + _font)
	# print("BGColor = " + _bgcolor)
	# print("\nExclude dir:")
	# print(_exclude_dir)
	# print("\nExclude files: ")
	# print(_exclude_file)
	# csv_reader(csv_file)
	# print(csvdata)
	# printcsv()
	# _file = compare("rar")
	# if _file != "": _str = icon_path + _file + ".png"

	for dirpath, dirnames, filenames in os.walk(directory, True, None, False):
		_real_dir = str(dirpath).replace(directory,"")
		if Enquiry(_exclude):
			if not is_part_in_list(_real_dir,_exclude):
				for a in _exclude:
					if a in dirnames: dirnames.remove(a)
				print("Каталог:",_real_dir)
				if Enquiry(dirnames):
					dirnames.sort()
					for dirname in dirnames:
						print("Direcory:", dirname)
				else:
					print("Directory is found!")
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
			filenames.sort()
			for filename in filenames:
				print("Filename:", filename)

if __name__=="__main__":
	main()
