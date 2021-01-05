#!/usr/bin/env python3

import csv
import os
# import os.path
import pathlib
import base64
import sys
# import math
import time
import random
import platform

Author = "maximalisimus"
Program_Name = "genindex"
License = "GPL"
About = "maximalis171091@mail.ru"
VERSION = "1.0"

# PREFIX = os.path.realpath(os.path.dirname(sys.argv[0]))
PREFIX = str(pathlib.Path(sys.argv[0]).resolve()).replace(pathlib.Path(sys.argv[0]).name,'')
# tmplate_dir = os.path.join(PREFIX,"template")
template_Dir = str(pathlib.Path(PREFIX).joinpath("template"))
modules_Dir = str(pathlib.Path(PREFIX).joinpath("modules"))
sys.path.append(modules_Dir)

if platform.system() == 'Windows':
	import cmdcolor
# csv_file = os.path.join(template_Dir,"icons.csv")
# icon_path = os.path.join(template_Dir,"image")
csv_file = str(pathlib.Path(template_Dir).joinpath("icons.csv"))
icon_path = str(pathlib.Path(template_Dir).joinpath("image"))

# html_header_file = os.path.join(template_Dir,"header.html")
# html_body_file = os.path.join(template_Dir,"body.html")
# html_footer_file = os.path.join(template_Dir,"footer.html")
html_Header_File = str(pathlib.Path(template_Dir).joinpath("header.html"))
html_Body_File = str(pathlib.Path(template_Dir).joinpath("body.html"))
html_Footer_File = str(pathlib.Path(template_Dir).joinpath("footer.html"))

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

def printUsage():
	usage_one = "\tUsage (genindex): \n\t\t[-dir directory] [-font font] [-bgcolor color]\n"
	usage_two = "\t\t[-exclude-dir dir] [-exclude-file file]\n"
	usage_three = "\t\t[-adi] [-genname] [-version] [-help]"
	usage_str = usage_one + usage_two + usage_three
	print(usage_str)

def printInfoApps():
	str_about = "Program: " + Program_Name + " , Version: v" + VERSION + "\n" + "License: " + License
	print(str_about)

def printAbout():
	str_fine = "About by: " + About
	print(str_fine)

def print_of_help():
	printInfoApps()
	printUsage()
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
	printAbout()

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

	@staticmethod
	def stripCurrentDir(paths):
		return paths.replace("./", "").replace("/.", "")

	@staticmethod
	def getPathIcon(fName, pathIcon = None):
		if pathIcon == None: return str(pathlib.Path(icon_path).joinpath(fName))
		else: return str(pathlib.Path(pathIcon).joinpath(fName))
		# if pathIcon == None: return os.path.join(icon_path,fName)
		# else: return os.path.join(pathIcon,fName)
	
	@staticmethod
	def getPathIndex(pathname):
		return str(pathlib.Path(pathname).resolve().joinpath("index.html"))
		# return os.path.join(os.path.realpath(pathname),"index.html")

	@staticmethod
	def getRealPath(pathname):
		return str(pathlib.Path(pathname).resolve())
		# return os.path.realpath(pathname)

	@staticmethod
	def readFile(fName):
		with open(str(pathlib.Path(fName)), "r") as files:
			data = files.read()
		return str(data)
	
	@staticmethod
	def writeFile(filePath, data, mode_ = False):
		if mode_:
			with open(str(pathlib.Path(filePath)), "a") as files:
				files.write(data)
		else:
			with open(str(pathlib.Path(filePath)), "w") as files:
				files.write(data)
	
	@staticmethod
	def readFileBase64(fName):
		with open(str(pathlib.Path(fName)), "rb") as files:
			data = files.read()
		return base64.b64encode(data).decode("ascii")

	@staticmethod
	def convertBytes(numeric):
		"""
		this function will convert bytes to MB.... GB... etc
		"""
		for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
			if numeric < 1024.0:
				return "{0:3.1f} {1}".format(numeric,x)
			numeric /= 1024.0

	@staticmethod
	def getFileSize(filePath):
		# fSize = str(math.floor(os.path.getsize(fName) / 1000)) + " kB"
		# return fSize
		"""
		this function will return the file size
		"""
		if pathlib.Path(filePath).is_file():
			file_Info = pathlib.Path(filePath).stat().st_size
			return Files.convertBytes(file_Info)
		# if os.path.isfile(filePath):
		#	file_info = os.stat(filePath)
		#	return Files.convertBytes(file_info.st_size)
	
	@staticmethod
	def getDataTime(fName):
		mod_Time = time.strftime('%d-%b-%Y %H:%M', time.localtime(pathlib.Path(fName).stat().st_mtime))
		return mod_Time
		# modifyTime = time.strftime('%d-%b-%Y %H:%M', time.localtime(os.path.getmtime(fName)))
		# return modifyTime

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

	csvdata = []
	
	def __init__(self):
		self.csv_reader()
	
	def getIconFolder(self):
		return self.icon_folder
	
	def getIconBack(self):
		return self.icon_back
	
	def csv_reader(self, file_obj = None):
		if file_obj == None: file_obj = csv_file
		with open(file_obj, "r") as csvFile:
			csv_data = csv.reader(csvFile)
			for row in csv_data:
				# print(row) # Debug
				# self.csvdata.append(row)
				#print(str(' '.join(row)).split(' '))
				self.csvdata.append(str(' '.join(row)).split(' '))
	
	def printCSV(self):
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

	def check_the_file(self, fName):
		root_name = pathlib.Path(fName).stem
		root_ext = pathlib.Path(fName).suffix
		# root_name = os.path.splitext(str(fName))[0]
		# root_ext = os.path.splitext(str(fName))[1]
		if self.str_make.lower() in str(root_name).lower(): return self.icon_make
		if self.str_cmake.lower() in str(root_name).lower(): return self.icon_cmake
		if self.str_shasums.lower() in str(root_name).lower(): return self.icon_sums
		if self.str_md5sums.lower() in str(root_name).lower(): return self.icon_sums
		root_result = self.compare(root_ext)
		if root_result != False: return root_result
		else: return self.icon_file

class htmlOgject:

	htmlHeader = Files.readFile(html_Header_File)
	htmlBody = Files.readFile(html_Body_File)
	htmlFooter = Files.readFile(html_Footer_File)

	def __init__(self, startPath, fonts = "sans-serif", bg_color = "white", addIndex = False):
		self.startPath = Files.getRealPath(startPath)
		self.fonts = fonts
		self.bgcolor = bg_color
		self.add_index = addIndex
		self.htmlHeader = self.htmlHeader.replace("#FONTS", fonts).replace("#BGCOLOR",bg_color)
		self.htmlFooter = self.htmlFooter.replace("#VERSION", VERSION)
		self.icons = IconFile()

	def setFonts(self, value):
		if Resources.Enquiry(value): self.fonts = value
		else: self.fonts = "sans-serif"
		
	def getFonts(self):
		return self.fonts
		
	def setBGColor(self, colors):
		if Resources.Enquiry(colors): self.bgcolor = colors
		else: self.bgcolor = "white"
	
	def getBGColor(self):
		return self.bgcolor
	
	def setAddIndex(self, value):
		self.add_index = value
	
	def getAddIndex(self):
		return self.add_index

class Arguments:

	_lng_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	def __init__(self, list_argv):
		self.args = list_argv
		self.directory = ""
		self.fonts = ""
		self.bgcolor = ""
		self.exclude_dir = []
		self.exclude_file = []
		self.add_index = False
		self.generate_name = False
		self.printOfVers = False
		self.printOfHelp = False
		self.checkArgs()

	def getFonts(self):
		return self.fonts

	def getBGCOLOR(self):
		return self.bgcolor

	def getDirectory(self):
		return self.directory

	def getGenName(self):
		return self.generate_name
	
	def getAddIndex(self):
		return self.add_index
	
	def getPrintVers(self):
		return self.printOfVers
	
	def getPrintHelp(self):
		return self.printOfHelp
	
	def isExcDir(self):
		if Resources.Enquiry(self.exclude_dir): return True
		else: return False
	
	def getExcDir(self):
		return self.exclude_dir
	
	def isExcFile(self):
		if Resources.Enquiry(self.exclude_file): return True
		else: return False
	
	def getExcFile(self):
		return self.exclude_file

	def genName(self):
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

	def generate_random_name(self):
		_list_tmplt = os.listdir(icon_path)
		_set_tmplt = set(_list_tmplt)
		_gen_name = ""
		while True:
			_gen_name = self.genName()
			if not _gen_name in _set_tmplt: break
		_image_name = _gen_name + ".png"
		return str(_image_name)

	def checkDirs(self, dirNames):
		if Resources.Enquiry(dirNames):
			if not pathlib.Path(dirNames).exists():
			# if not os.path.isdir(dirNames):
				if platform.system() == 'Windows':
					cmdcolor.setCMDColor(12)
					print("Parameter is not the directory <", dirNames, "> !!!")
					print("Please input the working directory !!!")
					cmdcolor.setCMDColor(15)
				else:
					print("\033[31m",end = "")
					print("Parameter is not the directory <", dirNames, "> !!!")
					print("Please input the working directory !!!")
					print("\033[0m", end = "")
				printInfoApps()
				printUsage()
				printAbout()
				exit(1)
			else: self.directory = Files.getRealPath(dirNames)
		else:
			if platform.system() == 'Windows':
				cmdcolor.setCMDColor(12)
				print("You have not input any working directory !!!")
				print("Please input the working directory !!!\n")
				cmdcolor.setCMDColor(15)
			else:
				print("\033[31m", end="")
				print("You have not input any working directory !!!")
				print("Please input the working directory !!!\n")
				print("\033[0m", end="")
			printInfoApps()
			printUsage()
			printAbout()
			exit(1)

	def checkArgs(self):
		if len(self.args) > 2:
			for count in range(len(self.args)):
				if switch(self.args[count]) == 1: self.checkDirs(self.args[count + 1])
				if switch(self.args[count]) == 2: self.fonts = self.args[count + 1]
				if switch(self.args[count]) == 3: self.bgcolor = self.args[count + 1]
				if switch(self.args[count]) == 4: self.exclude_dir.append(self.args[count + 1])
				if switch(self.args[count]) == 5: self.exclude_file.append(self.args[count + 1])
				if switch(self.args[count]) == 6: self.add_index = True
				if switch(self.args[count]) == 7: self.generate_name = True
				if switch(self.args[count]) == 8: self.printOfVers = True
				if switch(self.args[count]) == 9: self.printOfVers = True
				if switch(self.args[count]) == 10: self.printOfVers = True
				if switch(self.args[count]) == 11: self.printOfVers = True
				if switch(self.args[count]) == 12: self.printOfHelp = True
				if switch(self.args[count]) == 13: self.printOfHelp = True
				if switch(self.args[count]) == 14: self.printOfHelp = True
				if switch(self.args[count]) == 15: self.printOfHelp = True
		else:
			if switch(self.args[1]) == 7: self.generate_name = True
			if switch(self.args[1]) == 8: self.printOfVers = True
			if switch(self.args[1]) == 9: self.printOfVers = True
			if switch(self.args[1]) == 10: self.printOfVers = True
			if switch(self.args[1]) == 11: self.printOfVers = True
			if switch(self.args[1]) == 12: self.printOfHelp = True
			if switch(self.args[1]) == 13: self.printOfHelp = True
			if switch(self.args[1]) == 14: self.printOfHelp = True
			if switch(self.args[1]) == 15: self.printOfHelp = True
		if self.getGenName():
			print(self.generate_random_name())
			exit(0)
		if self.getPrintVers():
			print_of_version()
			exit(0)
		if self.getPrintHelp():
			print_of_help()
			exit(0)

def list_files(startPath):
	newPath = str(pathlib.Path(startPath).resolve())
	for root, dirs, files in os.walk(newPath, True, None, False):
		level = root.replace(newPath, '').count(os.sep)
		indent = ' ' * 2 * (level)
		subIndent = ' ' * 2 * (level + 1)
		print('{}{}/'.format(indent, pathlib.Path(root).stem))
		files.sort()
		for f in files:
			print('{}{}'.format(subIndent, f))

def main():
	any_args = Arguments(sys.argv)
	if len(any_args.args) > 2:
		html = htmlOgject(any_args.getDirectory())
		html.setFonts(any_args.getFonts())
		html.setBGColor(any_args.getBGCOLOR())
		html.setAddIndex(any_args.getAddIndex())
		# in_file = 'build.sh.tar.gz'
		# _str = Files.getPathIcon(html.icons.check_the_file(in_file))
		# print(_str)
		# print(Files.readFileBase64(_str))
		# _str = Files.getRealPath("/home/mikl/git_ssh/aur-packages/x86_64/apindex-2.2-1-any.pkg.tar.zst")
		# fileSize = Files.getFileSize(_str)
		# modifyTime = Files.getDataTime(_str)
		# print(_str, modifyTime, fileSize)
		# list_files("./")

if __name__=="__main__":
	main()

