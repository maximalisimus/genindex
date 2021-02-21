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
		elif not pathlib.Path(configFile).exists():
			self.iniFile = str(pathlib.Path(configFile).resolve())
		else:
			self.iniFile = str(pathlib.Path(configFile).resolve())
		self.ini_config = {}
		self.cnf = configparser.ConfigParser()
	
	def __del__(self):
		del self
	
	def writeConfig(self):
		self.cnf.read_dict(self.ini_config)
		with open(str(pathlib.Path(self.iniFile)), "w") as cf:
			self.cnf.write(cf)
	
	def readConfig(self):
		self.ini_config.clear()
		dict_sample = {}
		with open(str(pathlib.Path(self.iniFile)), "r") as cf:
			self.cnf.read_file(cf)
		for keys in self.cnf.sections():
			self.ini_config.setdefault(keys)
			dict_sample.clear()
			for opt in self.cnf.options(keys):
				dict_sample.setdefault(opt,self.cnf.get(keys,opt))
			self.ini_config[keys] = dict_sample.copy()
		dict_sample.clear()
		del dict_sample
	
	def resetAllDict(self):
		self.ini_config.clear()
	
	def setDictParam(self, onsection, onkeys, onvalue):
		if onsection in self.ini_config:
			if onkeys in self.ini_config[onsection]:
				self.ini_config[onsection][onkeys] = str(onvalue)
				self.cnf.read_dict(self.ini_config)
	
	def setSectionDict(self, onsection, listparam, listvalue):
		dict_sample = {}
		dict_sample.clear()
		self.ini_config.setdefault(str(onsection))
		count = len(listvalue)
		for keys in range(len(listparam)):
			if keys < count:
				dict_sample.setdefault(str(listparam[keys]),str(listvalue[keys]))
			else:
				dict_sample.setdefault(str(listparam[keys]),"None")
		#print(dict_sample)
		self.ini_config[onsection] = dict_sample.copy()
		dict_sample.clear()
		del dict_sample

if __name__ == "__main__":
	#config_file = "settings3.ini"
	#ini_conf = InIConfig(config_file)
	#ini_conf.readConfig()
	#print(ini_conf.ini_config)
	#ini_conf.setDictParam("Settings","bgcolor","white")
	#print("-------------------------------")
	#ini_conf.writeConfig()
	#ini_conf.readConfig()
	#print(ini_conf.ini_config)
