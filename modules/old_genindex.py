#!/usr/bin/env python3

import csv
import os
import os.path
import base64
import sys
import math
import time
import random

Author = "maximalisimus"
Program_Name = "genindex"
License = "GPL"
About = "maximalis171091@mail.ru"
VERSION = "1.0"

_lng_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

csvdata = []

directory = ""
_font = "sans-serif"
_bgcolor = "white"
_exclude_dir = []
_exclude_file = []
add_index = False

icon_make = "r3i1s.png"
icon_cmake = "w9c4z.png"
icon_folder = "folder.png"
icon_file = "file.png"
icon_back = "back.png"
icon_sums = "q6f3z.png"

str_make = "Makefile"
str_cmake = "Cmakelist"
str_shasums = "sha"
str_md5sums = "md5sums"

PREFIX = os.path.realpath(os.path.dirname(sys.argv[0]))
tmplate_dir = os.path.join(PREFIX,"template")
html_header_file = os.path.join(tmplate_dir,"header.html")
html_body_file = os.path.join(tmplate_dir,"body.html")
html_footer_file = os.path.join(tmplate_dir,"footer.html")

csv_file = os.path.join(tmplate_dir,"icons.csv")
icon_path = os.path.join(tmplate_dir,"image")

def switch(case):
	return {
		"-dir": 1,
		"-font": 2,
		"-bgcolor": 3,
		"-exclude-dir": 4,
		"-exclude-file": 5,
		"-adi": 6,
		"-genname": 7,
		"-v": 8,
		"--v": 9,
		"--version": 10,
		"-version": 11,
		"-h": 12,
		"--h": 13,
		"--help": 14,
		"-help": 15
	}.get(case, None)

def print_of_help():
	str_about = "Program: " + Program_Name + " , Version: v" + VERSION + "\n" + "License: " + License
	str_fine = "About by: " + About
	usage_one = "\tUsage genindex: \n\t\t[-dir directory] [-font font] [-bgcolor color]\n"
	usage_two = "\t\t[exclude-dir dir] [-exclude-file file]\n"
	usage_three = "\t\t[-adi] [-genname] [--version] [--help]"
	usage_str = usage_one + usage_two + usage_three
	print(str_about)
	print(usage_str)
	print("Options:")
	print("\t-dir           - Working directory")
	print("\t-font          - Font to index.html")
	print("\t-bgcolor       - Background color to index.html")
	print("\t-exclude-dir   - Excluding the specified directory")
	print("\t                 from the destination file list index.html")
	print("\t-exclude-file  - Excluding the specified file from the")
	print("\t                 destination file list index.html")
	print("\t-adi           - Adding a transition file \"/index.html\"")
	print("\t                 to the folders")
	print("\t-genname       - Generate a unique name for your icon image file")
	print("\t                 that is not in the icon image templates folder")
	print("\t-version       - Print the program version and exit")
	print("\t-help          - Help")
	print(str_fine)

def print_of_version():
	out_str = "Author: " + Author + "\n"
	out_str_two = out_str + "Program: " + Program_Name + "\n"
	out_str_free = out_str_two + "Version: v" + VERSION + "\n"
	out_str_four = out_str_free + "License: " + License + "\n"
	# About
	out_str_full = out_str_four + "About by: " + About
	print(out_str_full)

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
			if str(listname[i][j]).lower() == str(value)[1:].lower(): _tmp = listname[i][0] + ".png"
	if Enquiry(_tmp): return _tmp
	else: return False

def printcsv(listname = csvdata):
	for i in range(len(listname)):
		# print(listname[i][0], end = '\n')
		for j in range(len(listname[i])):
			print(listname[i][j], end = '\n')

def is_part_in_list(str_, words):
	for word in words:
		if word.lower() in str_.lower():
			return True
	return False

def genname():
	_fine_str = ""
	counter = 0
	_tmp_str = random.choice(_lng_str)
	_fine_str += _tmp_str
	counter = random.randint(0, 9)
	_fine_str += str(counter)
	_tmp_str = random.choice(_lng_str)
	_fine_str += _tmp_str
	counter = random.randint(0, 9)
	_fine_str += str(counter)
	_tmp_str = random.choice(_lng_str)
	_fine_str += _tmp_str
	return str(_fine_str)

def generate_random_name(_dirs):
	_list_tmplt = os.listdir(_dirs)
	_set_tmplt = set(_list_tmplt)
	_gen_name = ""
	while True:
		_gen_name = genname()
		if not _gen_name in _set_tmplt: break
	_image_name = _gen_name + ".png"
	return str(_image_name)

def check_the_file(fname):
	root_name = os.path.splitext(fname)[0]
	root_ext = os.path.splitext(fname)[1]
	if str_make.lower() in str(root_name).lower(): return icon_make
	if str_cmake.lower() in str(root_name).lower(): return icon_cmake
	if str_shasums.lower() in str(root_name).lower(): return icon_sums
	if str_md5sums.lower() in str(root_name).lower(): return icon_sums
	root_result = compare(root_ext)
	if root_result != False: return root_result
	else:
		return icon_file

def getPathIcon(fName):
	return os.path.join(icon_path,fName)

def getPathIndex(pathname):
	return os.path.join(os.path.realpath(pathname),"index.html")

def readFile(fName):
	with open(fName, "r") as files:
		data = files.read()
	return str(data)

def writeFile(filePath, data, mode_ = False):
	if mode_:
		with open(filePath, "a") as files:
			files.write(data)
	else:
		with open(filePath, "w") as files:
			files.write(data)

def readFileBase64(fName):
	with open(fName, "rb") as files:
		data = files.read()
	return base64.b64encode(data).decode("ascii")

def main():
	if len(sys.argv) > 2:
		_generate_name = False
		print_vers = False
		print_help = False
		for count in range(len(sys.argv)):
			if switch(sys.argv[count]) == 1: directory = sys.argv[count + 1]
			if switch(sys.argv[count]) == 2: _font = sys.argv[count + 1]
			if switch(sys.argv[count]) == 3: _bgcolor = sys.argv[count + 1]
			if switch(sys.argv[count]) == 4: _exclude_dir.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 5: _exclude_file.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 6: add_index = True
			if switch(sys.argv[count]) == 7: _generate_name = True
			if switch(sys.argv[count]) == 8: print_vers = True
			if switch(sys.argv[count]) == 9: print_vers = True
			if switch(sys.argv[count]) == 10: print_vers = True
			if switch(sys.argv[count]) == 11: print_vers = True
			if switch(sys.argv[count]) == 12: print_help = True
			if switch(sys.argv[count]) == 13: print_help = True
			if switch(sys.argv[count]) == 14: print_help = True
			if switch(sys.argv[count]) == 15: print_help = True
		if _generate_name == True:
			print(generate_random_name(icon_path))
			exit(0)
		if print_vers == True:
			print_of_version()
			exit(0)
		if print_help == True:
			print_of_help()
			exit(0)
		if not os.path.isdir(directory):
			print("Parameter is not the directory", directory, "\nHelp")
			exit(1)
		csv_reader(csv_file)
		# print(csvdata)
		# printcsv()
		# in_file = 'build.sh'
		# _str = getPathIcon(check_the_file(in_file))
		# print(readFileBase64(_str))
		# fileSize = str(math.floor(os.path.getsize(_str) / 1000)) + " kB"
		# modifyTime = time.strftime('%d-%b-%Y %H:%M', time.localtime(os.path.getmtime(_str)))
		# print(_str, modifyTime, fileSize)
	else:
		_generate_name = False
		print_vers = False
		print_help = False
		for count in range(len(sys.argv)):
			if switch(sys.argv[count]) == 7: _generate_name = True
			if switch(sys.argv[count]) == 8: print_vers = True
			if switch(sys.argv[count]) == 9: print_vers = True
			if switch(sys.argv[count]) == 10: print_vers = True
			if switch(sys.argv[count]) == 11: print_vers = True
			if switch(sys.argv[count]) == 12: print_help = True
			if switch(sys.argv[count]) == 13: print_help = True
			if switch(sys.argv[count]) == 14: print_help = True
			if switch(sys.argv[count]) == 15: print_help = True
		if _generate_name == True:
			print(generate_random_name(icon_path))
		if print_vers == True:
			print_of_version()
		if print_help == True:
			print_of_help()
		exit(0)

if __name__=="__main__":
	main()

