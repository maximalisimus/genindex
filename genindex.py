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

csv_file = os.path.join("template","icons.csv")
icon_path = os.path.join("template","image")

icon_make = "r3i1s.png"
icon_cmake = "w9c4z.png"
icon_folder = "folder.png"
icon_file = "file.png"
icon_sums = "q6f3z.png"

str_make = "Makefile"
str_cmake = "Cmakelist"
str_shasums = "sha"
str_md5sums = "md5sums"

def switch(case):
	return {
		"-tree": 1,
		"-dir": 2,
		"-font": 3,
		"-bgcolor": 4,
		"-exclude-dir": 5,
		"-exclude-file": 6,
		"-genname": 7,
		"-v": 8,
		"-h": 9
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

def stripCurrentDir(path):
	return path.replace("./", "").replace("/.", "")

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

def list_files(startpath):
	prefix_start = '┌'
	prefix_middle = '├──'
	prefix_fine = '└──'
	prefix_last = '│'
	_start_files = []
	_count_cnt = 0
	_count_len = 0
	_cnt = 0
	for root, dirs, files in os.walk(startpath):
		_real_dir = str(root).replace(startpath, "")
		if Enquiry(_exclude_dir):
			if not is_part_in_list(_real_dir, _exclude_dir):
				level = root.replace(startpath, '').count(os.sep)
				indent = '─' * 2 * (level)
				subindent = ' ' * 2 * (level + 1)
				_start_dir = root.replace(startpath, '')
				if len(_start_dir) == 0:
					print(prefix_start,startpath)
				else:
					if level == 0:
						print(prefix_middle,os.path.basename(root))
					else:
						_line = prefix_middle + indent
						print(_line,os.path.basename(root))
				if _cnt == 0:
					for f in files:
						_start_files.append(f)
				else:
					files.sort()
					_count_len = len(files) -1
					_count_cnt = 0
					for f in files:
						if _count_cnt == _count_len:
							print(prefix_last,subindent,prefix_fine,f)
						else:
							print(prefix_last,subindent,prefix_middle,f)
						_count_cnt +=1
				_cnt+=1		
		else:
			level = root.replace(startpath, '').count(os.sep)
			indent = '─' * 2 * (level)
			subindent = ' ' * 2 * (level + 1)
			_start_dir = root.replace(startpath, '')
			if len(_start_dir) == 0:
				print(prefix_start,startpath)
			else:
				if level == 0:
					print(prefix_middle,os.path.basename(root))
				else:
					_line = prefix_middle + indent
					print(_line,os.path.basename(root))
			if _cnt == 0:
				for f in files:
					_start_files.append(f)
			else:
				files.sort()
				_count_len = len(files) -1
				_count_cnt = 0
				for f in files:
					if _count_cnt == _count_len:
						print(prefix_last,subindent,prefix_fine,f)
					else:
						print(prefix_last,subindent,prefix_middle,f)
					_count_cnt +=1
			_cnt+=1
	_start_files.sort()
	_count_cnt = 0
	_count_len = len(_start_files) -1
	if Enquiry(_exclude_file):
		_str_one = set(_start_files)
		_str_two = set(_exclude_file)
		_new_filename = []
		_new_filename.clear()
		for key1 in _str_one:
			if not is_part_in_list(str(key1),_str_two): _new_filename.append(key1)
		_new_filename.sort()
		_count_len = len(_new_filename) -1
		for _file in _new_filename:
			if _count_cnt == _count_len:
				print(prefix_fine,_file)
			else:
				print(prefix_middle,_file)
			_count_cnt +=1
	else:
		for _file in _start_files:
			if _count_cnt == _count_len:
				print(prefix_fine,_file)
			else:
				print(prefix_middle,_file)
			_count_cnt +=1

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
		_trees = False
		for count in range(len(sys.argv)):
			if switch(sys.argv[count]) == 1:
				directory = sys.argv[count + 1]
				if not os.path.isdir(directory):
					print("Parameter is not the directory", directory, "\nHelp")
					exit(1)
				else:
					list_files(directory)
					exit(0)
			if switch(sys.argv[count]) == 2: directory = sys.argv[count + 1]
			if switch(sys.argv[count]) == 3: _font = sys.argv[count + 1]
			if switch(sys.argv[count]) == 4: _bgcolor = sys.argv[count + 1]
			if switch(sys.argv[count]) == 5: _exclude_dir.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 6: _exclude_file.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 7: print(generate_random_name(icon_path))
			if switch(sys.argv[count]) == 8: print("Versions")
			if switch(sys.argv[count]) == 9: print("Help!")
		if not os.path.isdir(directory):
			print("Parameter is not the directory", directory, "\nHelp")
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
		# _file = compare(".mui")
		# if _file != "":
		#	print(_file)
		#	_str = os.path.join(icon_path,_file)
		#	# _str = icon_path + _file
		#	fileSize = str(math.floor(os.path.getsize(_str) / 1000)) + " kB"
		#	modifyTime = time.strftime('%d-%b-%Y %H:%M', time.localtime(os.path.getmtime(_str)))
		#	print(_str, modifyTime, fileSize)
		# work_in_dir(directory)
		# in_file = 'sha256sums.txt'
		# print(check_the_file(in_file))

if __name__=="__main__":
	main()
