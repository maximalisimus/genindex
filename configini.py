#!/usr/bin/env python3

import pathlib
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
	
	def __init__(self, configFile = "None", on_fonts = "sans-serif", on_bgcolor = "white", is_addindex = False):
		self.sections = "Settings"
		self.param_fonts = "fonts"
		self.param_bgcolor = "bgcolor"
		self.param_addindex = "addindex"
		self.param_exdirs = "exclude_dir"
		self.param_exfls = "exclude_files"
		self.data_fonts = on_fonts
		self.data_bgcolor = on_bgcolor
		self.data_addindex = is_addindex
		self.data_exdirs = "None"
		self.data_exfls = "None"
		if configFile == "None":
			self.iniFile = "settings.ini"
		elif not pathlib.Path(configFile).exists():
			self.iniFile = str(pathlib.Path(configFile).resolve())
			self.writeconfig()
		else:
			self.iniFile = str(pathlib.Path(configFile).resolve())
	
	def __del__(self):
		del self
	
	def ResetConfig(self):
		self.sections = "Settings"
		self.param_fonts = "fonts"
		self.param_bgcolor = "bgcolor"
		self.param_addindex = "addindex"
		self.param_exdirs = "exclude_dir"
		self.param_exfls = "exclude_files"
		self.data_fonts = "sans-serif"
		self.data_bgcolor = "white"
		self.data_addindex = False
		self.data_exdirs = "None"
		self.data_exfls = "None"
		self.writeconfig()
	
	def setINIFile(self,config_files):
		if pathlib.Path(config_files).exists():
			self.iniFile = str(pathlib.Path(config_files).resolve())
	
	def getINIFile(self):
		return self.iniFile
	
	def setDataFonts(self, on_fonts):
		self.data_fonts = on_fonts
	
	def getDataFonts(self):
		return self.data_fonts
		
	def setDataBGColor(self,on_bgcolor):
		self.data_bgcolor = on_bgcolor
		
	def getDataBGCOLOR(self):
		return self.data_bgcolor
		
	def setDataAddindex(self, is_index):
		self.data_addindex = is_index
		
	def getDataAddindex(self):
		return self.data_addindex
	
	def setExdir(self,on_exdirs):
		self.data_exdirs = ';'.join(on_exdirs)
	
	def getDataExdir(self):
		return self.data_exdirs.split(';')
	
	def setDataExFls(self,on_exfls):
		self.data_exfls = ';'.join(on_exfls)
	
	def getDataExfls(self):
		return self.data_exfls.split(';')
	
	def writeconfig(self):
		cnf = configparser.ConfigParser()
		cnf.add_section(self.sections)
		cnf.set(self.sections,self.param_fonts,self.data_fonts)
		cnf.set(self.sections,self.param_bgcolor,self.data_bgcolor)
		cnf.set(self.sections,self.param_addindex,self.data_addindex)
		cnf.set(self.sections,self.param_exdirs,self.data_exdirs)
		cnf.set(self.sections,self.param_exfls,self.data_exfls)
		# cnf.remove_option(,)
		# cnf.remove_section()
		cf = open(self.iniFile, "w")
		cnf.write(cf)
		cf.close()
	
	def readconfig(self):
		cnf = configparser.ConfigParser()
		cf = open(self.iniFile, "r")
		cnf.read_file(cf)
		self.data_fonts = cnf.get(self.sections,self.param_fonts)
		self.data_bgcolor = cnf.get(self.sections,self.param_bgcolor)
		self.data_addindex = cnf.get(self.sections,self.param_addindex)
		self.data_exdirs = cnf.get(self.sections,self.param_exdirs)
		self.data_exfls = cnf.get(self.sections,self.param_exfls)
		cf.close()

	def printconfig(self):
		print("#",self.iniFile)
		print("[Settings]")
		print(self.param_fonts,"=",self.data_fonts)
		print(self.param_bgcolor,"=",self.data_bgcolor)
		print(self.param_addindex,"=",self.data_addindex)
		print(self.param_exdirs,"=",self.data_exdirs)
		print(self.param_exfls,"=",self.data_exfls)

if __name__ == "__main__":
	ini_conf = InIConfig(settings_file)
	ini_conf.readconfig()
	#ini_conf.printconfig()
	#ini_conf.writeconfig()
	del ini_conf
