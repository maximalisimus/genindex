#!/usr/bin/env python3

import pathlib
import os
import sys

PREFIX = str(pathlib.Path(sys.argv[0]).resolve()).replace(pathlib.Path(sys.argv[0]).name,'')
modules_Dir = str(pathlib.Path(PREFIX).joinpath("modules"))

config_file = "settings.ini"
settings_file = str(pathlib.Path(modules_Dir).joinpath(config_file))

try:
	import configparser
except ImportError:
	import ConfigParser as configparser
	
class InIConfig():
	
	def __init__(self, exdir = "None", exfls = "None",fonts = "sans-serif", bgcolor = "white", addindex = False):
		self.sections = "Settings"
		self.parameter_1 = "fonts"
		self.parameter_2 = "bgcolor"
		self.parameter_3 = "addindex"
		self.parameter_4 = "exclude_dir"
		self.parameter_5 = "exclude_files"
		self.data_1 = fonts
		self.data_2 = bgcolor
		self.data_3 = addindex
		self.data_4 = exdir
		self.data_5 = exfls
	
	def setFonts(self,fnt):
		self.data_1 = fnt
	
	def getFonts(self):
		return self.data_1
		
	def setBGColor(self,bg_color):
		self.data_2 = bg_color
		
	def getBGCOLOR(self):
		return self.data_2
		
	def setAddindex(self, isindex):
		self.data_3 = isindex
		
	def getAddindex(self):
		return self.data_3
	
	def setExdir(self,ex_dir):
		self.data_4 = ';'.join(ex_dir)
	
	def getExdir(self):
		return self.data_4.split(';')
	
	def setExFls(self,ex_fls):
		self.data_4 = ';'.join(ex_fls)
	
	def getExfls(self):
		return self.data_5.split(';')
	
	def writeconfig(self):
		cnf = configparser.ConfigParser()
		cnf.add_section(self.sections)
		cnf.set(self.sections,self.parameter_1,self.data_1)
		cnf.set(self.sections,self.parameter_2,self.data_2)
		cnf.set(self.sections,self.parameter_3,self.data_3)
		cnf.set(self.sections,self.parameter_4,self.data_4)
		cnf.set(self.sections,self.parameter_5,self.data_5)
		# cnf.remove_option(,)
		# cnf.remove_section()
		cf = open(settings_file, "w")
		cnf.write(cf)
		cf.close()
	
	def readconfig(self):
		cnf = configparser.ConfigParser()
		cf = open(settings_file, "r")
		cnf.read_file(cf)
		self.data_1 = cnf.get(self.sections,self.parameter_1)
		self.data_2 = cnf.get(self.sections,self.parameter_2)
		self.data_3 = cnf.get(self.sections,self.parameter_3)
		self.data_4 = cnf.get(self.sections,self.parameter_4)
		self.data_5 = cnf.get(self.sections,self.parameter_5)
		cf.close()

	def printconfig(self):
		print(self.parameter_1,"=",self.data_1)
		print(self.parameter_2,"=",self.data_2)
		print(self.parameter_3,"=",self.data_3)
		print(self.parameter_4,"=",self.data_4)
		print(self.parameter_5,"=",self.data_5)

if __name__ == "__main__":
	ini_conf = InIConfig()
	ini_conf.readconfig()
	#ini_conf.printconfig()
	#tmp = ["./git", "./build", "./__pycache__"]
	#a = ' '.join(tmp)
	#print(a)
	print(str(' '.join(ini_conf.getExdir())))
	#print("-----------------")
	#ini_conf.setExdir("./git")
	#ini_conf.writeconfig()
	#ini_conf.readconfig()
	#ini_conf.printconfig()
