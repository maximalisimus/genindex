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
		if len(str(configFile)) != 0:
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
				self.iniDict.setdefault(str(keys),"None")
				dict_sample.clear()
				for opt in self.iniConfig.options(keys):
					dict_sample.setdefault(str(opt),str(self.iniConfig.get(keys,opt)))
				self.iniDict[str(keys)] = dict_sample.copy()
			dict_sample.clear()
			del dict_sample
	
	def resetAllDict(self):
		self.iniDict.clear()
	
	def setDictParamValues(self, onsection, onkeys, onvalue):
		if onsection in self.iniDict:
			if onkeys in self.iniDict[str(onsection)]:
				self.iniDict[str(onsection)][str(onkeys)] = str(onvalue)
	
	def getDictParam(self, onsection, onkeys):
		return str(self.iniDict.get(str(onsection),{}).get(str(onkeys)))
	
	def delDictParam(self, onsection, onkeys):
		if onsection in self.iniDict:
			if onkeys in self.iniDict[str(onsection)]:
				self.iniDict[str(onsection)].pop(str(onkeys),"Error! There's not in key the dict.")
	
	def addDictParam(self, onsection, onkeys, onvalue = "None"):
		if onsection in self.iniDict:
			if onvalue == "None":
				self.iniDict[str(onsection)].setdefault(str(onkeys),"None")
			else:
				self.iniDict[str(onsection)].setdefault(str(onkeys),str(onvalue))
	
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
				self.iniDict[str(onsection)] = dict_sample.copy()
			else:
				for keys in range(len(listparam)):
					dict_sample.setdefault(str(listparam[keys]),"None")
				self.iniDict[str(onsection)] = dict_sample.copy()
		dict_sample.clear()
		del dict_sample
	
	def updateSectionPara(self, onsection, listPara, nestedListPara = False):
		dict_sample = {}
		dict_sample.clear()
		dict_backup = {}
		dict_backup.clear()
		self.iniDict.setdefault(str(onsection), "None")
		if str(self.iniDict[str(onsection)]) != "None":
			for keys in self.iniDict[str(onsection)]:
				if str(self.iniDict[str(onsection)][str(keys)]) != "None":
					dict_backup.setdefault(str(keys), str(self.iniDict[str(onsection)][str(keys)]))
				else:
					dict_backup.setdefault(str(keys),"None")
		if len(listPara) != 0:
			if nestedListPara:
				for count in range(len(listPara)):
					if len(listPara[count]) > 1:
						dict_sample.setdefault(str(listPara[count][0]), str(listPara[count][1]))
					else:
						#print(str(listPara[count][0]),"None")
						dict_sample.setdefault(str(listPara[count][0]), "None")
			else:
				if len(listPara) > 1:
					dict_sample.setdefault(str(listPara[0]), str(listPara[1]))
				else:
					#print(str(listPara[0]),"None")
					dict_sample.setdefault(str(listPara[0]), "None")
		dict_backup.update(dict_sample.copy())
		self.iniDict[str(onsection)] = dict_backup.copy()
		dict_sample.clear()
		del dict_sample
		dict_backup.clear()
		del dict_backup
	
	def delSectionDict(self, onsection):
		if onsection in self.iniDict:
			self.iniDict.pop(str(onsection), "Error! There's not in section the dict.")
	
	def getSectionListPara(self, onsection, onkeys):
		if onsection in self.iniDict:
			if onkeys in self.iniDict[str(onsection)]:
				rez = []
				rez.clear()
				rez.append(str(onkeys))
				rez.append(str(self.iniDict[str(onsection)][str(onkeys)]))
				return rez
			else:
				rez = []
				rez.clear()
				rez.append(str(onkeys))
				rez.append("None")
				return rez
		else:
			rez = []
			rez.clear()
			rez.append("None")
			rez.append("None")
			return rez
	
	def getSectionList(self, onsection):
		if onsection in self.iniDict:
			tmplst = []
			rezlst = []
			for keys in self.iniDict[str(onsection)]:
				tmplst.clear()
				tmplst.append(str(keys))
				tmplst.append(self.iniDict[str(onsection)][str(keys)])
				rezlst.append(list(tuple(tmplst)))
			return rezlst
	
	def getSectionParamList(self, onsection):
		if onsection in self.iniDict:
			rezlst = []
			for keys in self.iniDict[str(onsection)]:
				rezlst.append(str(keys))
			return rezlst
	
	def getSectionValueList(self, onsection):
		if onsection in self.iniDict:
			rezlst = []
			for keys in self.iniDict[str(onsection)]:
				rezlst.append(self.iniDict[str(onsection)][str(keys)])
			return rezlst

	def returnStr(self, onlist, onsepparate = ";"):
		return onsepparate.join(onlist)

	def returnList(self, onstr, onsepparate = ";"):
		return onstr.split(onsepparate)
	
	def printConfigDict(self, istab = False):
		for sections in self.iniDict:
			strsection = "[" + sections + "]"
			print(strsection)
			for keys in self.iniDict[str(sections)]:
				if istab: print("\t",keys,"=",self.iniDict[str(sections)][str(keys)])
				else: print(keys,"=",self.iniDict[str(sections)][str(keys)])
			print("")

if __name__ == "__main__":
	#config_file = "settings.ini"
	#ini_conf = InIConfig(config_file)
	#ini_conf.readConfig()
	#ini_conf.printConfigDict()
	#print(ini_conf.getSectionListPara("Settings","bgcolor"))
	#print(ini_conf.iniDict)
	#print("-------------------------------")
	#newlist = ini_conf.getSectionList("Settings")
	#newlist[1][1] = "black"
	#newlist = [["Mein","True"],["Dynamic","False"]]
	#newlist = ["bgcolor","black"]
	# newlist = [["bgcolor","black"]]
	#ini_conf.delSectionDict("Settings")
	#ini_conf.updateSectionPara("Settings", newlist)
	# ini_conf.updateSectionPara("Settings", newlist, True)
	#ini_conf.printConfigDict()
	#print(ini_conf.iniDict)
	#print("-------------------------------")
	#newlist = [["Mein","True"],["Dynamic","False"]]
	#ini_conf.addSectionPara("Types", newlist)
	#print(ini_conf.iniDict)
