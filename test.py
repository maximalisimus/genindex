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

PREFIX = os.path.realpath(os.path.dirname(sys.argv[0]))
tmplate_dir = os.path.join(PREFIX,"template")

csv_file = os.path.join(tmplate_dir,"icons.csv")
icon_path = os.path.join(tmplate_dir,"image")

html_header_file = os.path.join(tmplate_dir,"header.html")
html_body_file = os.path.join(tmplate_dir,"body.html")
html_footer_file = os.path.join(tmplate_dir,"footer.html")

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
	usage_one = "\tUsage: \n\t\t[-dir directory] [-font font] [-bgcolor color]\n"
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
	out_str_full = out_str_four + "About by: " + About
	print(out_str_full)

class Resources:
	
	@staticmethod
	def Enquiry(lis1):
		if len(lis1) == 0:
			return 0
		else:
			return 1
	
	@staticmethod
	def is_part_in_list(str_, words):
		for word in words:
			if word.lower() in str_.lower():
				return True
		return False

class Files:
	
	def __init__(self,value):
		self.directory = str(value)
	
	def getDirectory(self):
		return self.directory
	
	@staticmethod
	def getPathIcon(fName, pathicon):
		return os.path.join(pathicon,fName)
	
	@staticmethod
	def getPathIndex(pathname):
		return os.path.join(os.path.realpath(pathname),"index.html")
	
	@staticmethod
	def readFile(fName):
		with open(fName, "r") as files:
			data = files.read()
		return str(data)
	
	@staticmethod
	def writeFile(filePath, data, mode_ = False):
		if mode_:
			with open(filePath, "a") as files:
				files.write(data)
		else:
			with open(filePath, "w") as files:
				files.write(data)
	
	@staticmethod
	def readFileBase64(fName):
		with open(fName, "rb") as files:
			data = files.read()
		return base64.b64encode(data).decode("ascii")
	
	@staticmethod
	def getFileSize(fName):
		fSize = str(math.floor(os.path.getsize(fName) / 1000)) + " kB"
		return fSize
	
	@staticmethod
	def getDataTime(fName):
		modifyTime = time.strftime('%d-%b-%Y %H:%M', time.localtime(os.path.getmtime(fName)))
		return modifyTime
		

class IconFile:
	
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
	
	_lng_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	csvdata = []
	
	def __init__(self, dirs = None):
		if dirs == None: self.dirs = icon_path
		else: self.dirs = dirs
	
	def getIconFolder(self):
		return self.icon_folder
	
	def getIconBack(self):
		return self.icon_back
	
	def csv_reader(self):
		file_obj = csv_file
		with open(file_obj, "r") as csvfile:
			csv_data = csv.reader(csvfile)	
			for row in csv_data:
				# print(row) # Debug
				# self.csvdata.append(row)
				#print(str(' '.join(row)).split(' '))
				self.csvdata.append(str(' '.join(row)).split(' '))
	
	def printcsv(self):
		for i in range(len(self.csvdata)):
			# print(self.csvdata[i][0], end = '\n')
			for j in range(len(self.csvdata[i])):
				print(self.csvdata[i][j], end = '\n')
	
	def compare(self, value):
		_tmp = ""
		for i in range(len(self.csvdata)):
			for j in range(len(self.csvdata[i])):
				if str(self.csvdata[i][j]).lower() == str(value)[1:].lower(): _tmp = self.csvdata[i][0] + ".png"
		if Resources.Enquiry(_tmp): return _tmp
		else: return False

	def check_the_file(self, fname):
		root_name = os.path.splitext(fname)[0]
		root_ext = os.path.splitext(fname)[1]
		if self.str_make.lower() in str(root_name).lower(): return self.icon_make
		if self.str_cmake.lower() in str(root_name).lower(): return self.icon_cmake
		if self.str_shasums.lower() in str(root_name).lower(): return self.icon_sums
		if self.str_md5sums.lower() in str(root_name).lower(): return self.icon_sums
		root_result = self.compare(root_ext)
		if root_result != False: return root_result
		else: return self.icon_file

	def genname(self):
		_fine_str = ""
		counter = 0
		_tmp_str = random.choice(self._lng_str)
		_fine_str += _tmp_str
		counter = random.randint(0, 9)
		_fine_str += str(counter)
		_tmp_str = random.choice(self._lng_str)
		_fine_str += _tmp_str
		counter = random.randint(0, 9)
		_fine_str += str(counter)
		_tmp_str = random.choice(self._lng_str)
		_fine_str += _tmp_str
		return str(_fine_str)

	def generate_random_name(self, _dirs = None):
		if _dirs == None: _list_tmplt = os.listdir(icon_path)
		else: _list_tmplt = os.listdir(_dirs)
		_set_tmplt = set(_list_tmplt)
		_gen_name = ""
		while True:
			_gen_name = self.genname()
			if not _gen_name in _set_tmplt: break
		_image_name = _gen_name + ".png"
		return str(_image_name)

class htmlOgject(Files):
	
	def __init__(self, startpath, fonts = "sans-serif", bg_color = "white", addindex = False):
		super().__init__(self,startpath)
		self.fonts = fonts
		self.bgcolor = bg_color
		self.add_index = addindex
	
	def setFonts(self, value):
		self.fonts = value
		
	def getFonts(self):
		return self.fonts
		
	def setBGColor(self, colors):
		self.bgcolor = colors
	
	def getBGColor(self):
		return self.bgcolor
	
	def setAddIndex(self, value):
		self.add_index = value
	
	def getAddIndex(self):
		return self.add_index

class Arguments:
	
	def __init__(self, list_argv):
		self.args = list_argv
		self.directory = ""
		self.fonts = ""
		self.bgcolor = ""
		self.exclude_dir = []
		self.exclude_file = []
		self.add_index = False
		self.generate_name = False
		self.print_vers = False
		self.print_help = False
	
	def getDirectory(self):
		return self.directory
	
	def isDirectory(self):
		if Resources.Enquiry(self.directory): return True
		else: return False
	
	def getGenName(self):
		return self.generate_name
	
	def getAddIndex(self):
		return self.add_index
	
	def getPrintVers(self):
		return self.print_vers
	
	def getPrintHelp(self):
		return self.print_help
	
	def isExcDir(self):
		if Resources.Enquiry(self.exclude_dir): return True
		else: return False
		
	def isExcFile(self):
		if Resources.Enquiry(self.exclude_file): return True
		else: return False
	
	def checkArgs(self):
		for count in range(len(self.args)):
			if switch(self.args[count]) == 1: self.directory = self.args[count + 1]
			if switch(self.args[count]) == 2: self.fonts = self.args[count + 1]
			if switch(self.args[count]) == 3: self.bgcolor = self.args[count + 1]
			if switch(self.args[count]) == 4: self.exclude_dir.append(self.args[count + 1])
			if switch(self.args[count]) == 5: self.exclude_file.append(self.args[count + 1])
			if switch(self.args[count]) == 6: self.add_index = True
			if switch(self.args[count]) == 7: self.generate_name = True
			if switch(self.args[count]) == 8: self.print_vers = True
			if switch(self.args[count]) == 9: self.print_vers = True
			if switch(self.args[count]) == 10: self.print_vers = True
			if switch(self.args[count]) == 11: self.print_vers = True
			if switch(self.args[count]) == 12: self.print_help = True
			if switch(self.args[count]) == 13: self.print_help = True
			if switch(self.args[count]) == 14: self.print_help = True
			if switch(self.args[count]) == 15: self.print_help = True
	
def main():
	if len(sys.argv) > 2:
		any_args = Arguments(sys.argv)
		any_args.checkArgs()
		icons = IconFile()
		icons.csv_reader()
		if any_args.getGenName() == True:
			print(icons.generate_random_name())
			exit(0)
		if any_args.getPrintVers() == True:
			print_of_version()
			exit(0)
		if any_args.getPrintHelp() == True:
			print_of_help()
			exit(0)
		if not os.path.isdir(any_args.getDirectory()):
			print("Parameter is not the directory", any_args.getDirectory(), "\n")
			print_of_help()
			exit(1)
		# in_file = 'build.sh'
		# _str = Files.getPathIcon(icons.check_the_file(in_file),icon_path)
		# print(Files.readFileBase64(_str))
		# fileSize = Files.getFileSize(_str)
		# modifyTime = Files.getDataTime(_str)
		# print(_str, modifyTime, fileSize)
	else:
		any_args = Arguments(sys.argv)
		any_args.checkArgs()
		if any_args.getGenName() == True:
			print(icons.generate_random_name())
		if any_args.getPrintVers() == True:
			print_of_version()
		if any_args.getPrintHelp() == True:
			print_of_help()
		exit(0)

if __name__=="__main__":
	main()

