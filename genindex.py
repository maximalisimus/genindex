#!/usr/bin/env python3

import csv
import os
import os.path
import sys
import math
import time
import random

_lng_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

csvdata = []

directory = ""
_font = "sans-serif"
_bgcolor = "white"
_exclude_dir = []
_exclude_file = []

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

VERSION = "1.0"
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
		"-genname": 6,
		"-v": 7,
		"-h": 8
	}.get(case, None)

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

def generate_random_name(_dirs):
	_list_tmplt = os.listdir(_dirs)
	_set_tmplt = set(_list_tmplt)
	_gen_name = ""
	while True:
		_gen_name = genname()
		if not _gen_name in _set_tmplt: break
	_image_name = _gen_name + ".png"
	return str(_image_name)

def getPathIcon(filename):
	return os.path.join(icon_path,filename)

def readFile(fileName):
	with open(fileName, "r") as file:
		data = file.read()
	return str(data)

def writeFile(filePath, data):
	with open(filePath, "w") as files:
		files.write(data)

def readFileBase64(fileName):
	with open(ResourceManager.getFile(fileName), "rb") as files:
		data = files.read()
	return base64.b64encode(data).decode("ascii")

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
					if Enquiry(_exclude_file):
						_str_one = set(filenames)
						_str_two = set(_exclude_file)
						_new_filename = []
						_new_filename.clear()
						for key1 in _str_one:
							if not is_part_in_list(str(key1),_str_two): _new_filename.append(key1)
						_new_filename.sort()
						for filename in _new_filename:
							print("Filename:", filename)
					else:
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
				if Enquiry(_exclude_file):
					_str_one = set(filenames)
					_str_two = set(_exclude_file)
					_new_filename = []
					_new_filename.clear()
					for key1 in _str_one:
						if not is_part_in_list(str(key1), _str_two): _new_filename.append(key1)
					_new_filename.sort()
					for filename in _new_filename:
						print("Filename:", filename)
				else:
					filenames.sort()
					for filename in filenames:
						print("Filename:", filename)

def main():
	if len(sys.argv) > 2:
		_generate_name = False
		for count in range(len(sys.argv)):
			if switch(sys.argv[count]) == 1: directory = sys.argv[count + 1]
			if switch(sys.argv[count]) == 2: _font = sys.argv[count + 1]
			if switch(sys.argv[count]) == 3: _bgcolor = sys.argv[count + 1]
			if switch(sys.argv[count]) == 4: _exclude_dir.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 5: _exclude_file.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 6: _generate_name = True
			if switch(sys.argv[count]) == 7: print("Versions")
			if switch(sys.argv[count]) == 8: print("Help!")
		if _generate_name == True:
			print(generate_random_name(icon_path))
			exit(0)
		if not os.path.isdir(directory):
			print("Parameter is not the directory", directory, "\nHelp")
			exit(1)
		csv_reader(csv_file)
		# print(csvdata)
		# printcsv()
		# in_file = 'build.sh'
		# _str = os.path.join(icon_path,check_the_file(in_file))
		# _str = icon_path + _file
		# fileSize = str(math.floor(os.path.getsize(_str) / 1000)) + " kB"
		# modifyTime = time.strftime('%d-%b-%Y %H:%M', time.localtime(os.path.getmtime(_str)))
		# print(_str, modifyTime, fileSize)
		# work_in_dir(directory)

if __name__=="__main__":
	main()

