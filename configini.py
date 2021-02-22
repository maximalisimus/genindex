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
	
	def __init__(self, configFile = "None"):
		if configFile == "None":
			self.iniFile = "settings.ini"
		else:
			self.iniFile = str(pathlib.Path(configFile).resolve())
		self.iniDict = {}
		self.iniConfig = configparser.ConfigParser()
	
	def __del__(self):
		del self
	
	def setINIFile(self, configFile):
		self.iniFile = str(pathlib.Path(configFile).resolve())
	
	def getINIFile(self):
		return self.iniFile
	
	def writeConfig(self):
		self.iniConfig.read_dict(self.iniDict)
		with open(str(pathlib.Path(self.iniFile)), "w") as cf:
			self.iniConfig.write(cf)
	
	def readConfig(self):
		if pathlib.Path(self.iniFile).exists():
			self.iniDict.clear()
			dict_sample = {}
			with open(str(pathlib.Path(self.iniFile)), "r") as cf:
				self.iniConfig.read_file(cf)
			for keys in self.iniConfig.sections():
				self.iniDict.setdefault(keys,"None")
				dict_sample.clear()
				for opt in self.iniConfig.options(keys):
					dict_sample.setdefault(opt,self.iniConfig.get(keys,opt))
				self.iniDict[keys] = dict_sample.copy()
			dict_sample.clear()
			del dict_sample
	
	def resetAllDict(self):
		self.iniDict.clear()
	
	def setDictParamValues(self, onsection, onkeys, onvalue):
		if onsection in self.iniDict:
			if onkeys in self.iniDict[onsection]:
				self.iniDict[onsection][onkeys] = str(onvalue)
	
	def getDictParam(self, onsection, onkeys):
		return str(self.iniDict.get(str(onsection),{}).get(str(onkeys)))
	
	def delDictParam(self, onsection, onkeys):
		if onsection in self.iniDict:
			if onkeys in self.iniDict[onsection]:
				self.iniDict[onsection].pop(onkeys,"Error! There's not in key the dict.")
	
	def addDictParam(self, onsection, onkeys, onvalue = "None"):
		if onsection in self.iniDict:
			if onvalue == "None":
				self.iniDict[onsection].setdefault(str(onkeys),"None")
			else:
				self.iniDict[onsection].setdefault(str(onkeys),str(onvalue))
	
	def addSectionDict(self, onsection, listparam = "None", listvalue = "None"):
		dict_sample = {}
		dict_sample.clear()
		self.iniDict.setdefault(str(onsection), "None")
		if listparam != "None":
			if listvalue != "None":
				count = len(listvalue)
				for keys in range(len(listparam)):
					if keys < count:
						dict_sample.setdefault(str(listparam[keys]),str(listvalue[keys]))
					else:
						dict_sample.setdefault(str(listparam[keys]),"None")
				self.iniDict[onsection] = dict_sample.copy()
			else:
				for keys in range(len(listparam)):
					dict_sample.setdefault(str(listparam[keys]),"None")
				self.iniDict[onsection] = dict_sample.copy()
		dict_sample.clear()
		del dict_sample
		
	
	def delSectionDict(self, onsection):
		if onsection in self.iniDict:
			self.iniDict.pop(str(onsection), "Error! There's not in section the dict.")
	
	def getSectionOnList(self, onsection):
		if onsection in self.iniDict:
			tmplst = []
			rezlst = []
			for keys in self.iniDict[onsection]:
				tmplst.clear()
				tmplst.append(keys)
				tmplst.append(self.iniDict[onsection][keys])
				rezlst.append(list(tuple(tmplst)))
			return rezlst

def retStrOnPathIni(onlist):
	return ';'.join(onlist)

def retListOnStrIni(onstr):
	return onstr.split(';')

if __name__ == "__main__":
	#config_file = "settings.ini"
	#ini_conf = InIConfig(config_file)
	#ini_conf.readConfig()
	#print(ini_conf.iniDict)
	#print("-------------------------------")
	#ini_conf.addSectionDict("Global")#,["main","about"])#,["True","False"])
	#print(ini_conf.iniDict)
	##ini_conf.getSectionOnList("Settings")
	#tmp_lst = ini_conf.getSectionOnList("Settings")
	#print(tmp_lst)
	#print("-------------------------------")
	#tmp_lst[1][1] = "black"
	#print(tmp_lst)
	
