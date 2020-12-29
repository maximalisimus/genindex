#!/usr/bin/env python3

import os
import os.path
import sys
import math

_exclude_dir = []
_exclude_file = []

def switch(case):
	return {
		"-dir": 1,
		"-exclude-dir": 2,
		"-exclude-file": 3
	}.get(case, None)

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

def on_trees(startpath,editpath = None):
	if editpath == None: editpath = startpath
	basedir = str(editpath).replace(startpath, '')
	level = editpath.replace(startpath, '').count(os.sep)
	indent = ' ' * 2 * (level)
	subindent = ' ' * 2 * (level + 1)
	dirlist = []
	filelist = []
	for key in os.listdir(editpath):
		paths = os.path.join(editpath,key)
		if os.path.isdir(paths):
			if Enquiry(_exclude_dir):
				if not is_part_in_list(key, _exclude_dir): dirlist.append(key)
			else: dirlist.append(key)
		else:
			if Enquiry(_exclude_file):
				if not is_part_in_list(key, _exclude_file): filelist.append(key)
			else:
				filelist.append(key)
	if Enquiry(dirlist):
		dirlist.sort()
		for key1 in dirlist:
			paths = os.path.join(editpath,key1)
			level = paths.replace(startpath, '').count(os.sep)
			indent = ' ' * 2 * (level)
			print('{}{}/'.format(indent, key1))
			on_trees(startpath,paths)
	if Enquiry(filelist):
		filelist.sort()
		for key2 in filelist:
			print('{}{}'.format(subindent, key2))

def main():
	if len(sys.argv) > 2:
		for count in range(len(sys.argv)):
			if switch(sys.argv[count]) == 1: directory = sys.argv[count + 1]
			if switch(sys.argv[count]) == 2: _exclude_dir.append(sys.argv[count + 1])
			if switch(sys.argv[count]) == 3: _exclude_file.append(sys.argv[count + 1])
		if not os.path.isdir(directory):
			print("Parameter is not the directory", directory)
			print("Help")
			exit(1)
		on_trees(directory)

if __name__=="__main__":
	main()

