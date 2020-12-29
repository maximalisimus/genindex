#!/usr/bin/env python3

import os
import os.path
import sys
import math

_exclude_dir = []
_exclude_file = []

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

def list_files(startpath):
	count = 0
	old_count = 0
	old_list = []
	old_list.clear()
	one_list = []
	one_list.clear()
	old_subindent = 0
	for root, dirs, files in os.walk(startpath):
		_real_dir = str(root).replace(startpath, "")
		if Enquiry(_exclude_dir):
			if not is_part_in_list(_real_dir, _exclude_dir):
				level = root.replace(startpath, '').count(os.sep)
				indent = ' ' * 2 * (level)
				subindent = ' ' * 2 * (level + 1)
				if Enquiry(old_list):
					old_list.sort()
					for key in old_list:
						print('{}{}'.format(old_subindent, key))
				print('{}{}/'.format(indent, os.path.basename(root)))
				if count == 0:
					if Enquiry(_exclude_file):
						_str_one = set(files)
						_str_two = set(_exclude_file)
						for key1 in _str_one:
							if not is_part_in_list(str(key1),_str_two): one_list.append(key1)
					else:
						for f in files:
							one_list.append(f)
					count+=1
					old_count+=1
					continue
				if Enquiry(_exclude_file):
					_str_one = set(files)
					_str_two = set(_exclude_file)
					old_list.clear()
					for key1 in _str_one:
						if not is_part_in_list(str(key1),_str_two): old_list.append(key1)
				else:
					old_list.clear()
					for f in files:
						old_list.append(f)
				old_subindent = subindent
				count+=1
	one_list.sort()
	for f in one_list:
		print(f)

_exclude_dir.append(".git")
_exclude_file.append("gitattributes")

list_files("../abif-master")



