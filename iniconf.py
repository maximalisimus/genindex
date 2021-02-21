#!/usr/bin/env python3

import pathlib
import sys

PREFIX = str(pathlib.Path(sys.argv[0]).resolve()).replace(pathlib.Path(sys.argv[0]).name,'')
# modules_Dir = str(pathlib.Path(PREFIX).joinpath("modules"))

config_file = "settings.ini"
# settings_file = str(pathlib.Path(modules_Dir).joinpath(config_file))
settings_file = str(pathlib.Path(PREFIX).joinpath(config_file))

try:
	import configparser
except ImportError:
	import ConfigParser as configparser
	
iniFile = "./settings.ini"

cnf = configparser.ConfigParser()
cf = open(iniFile, "r")
cnf.read_file(cf)
cf.close()

ini_config = {}
dict_sample = {}
for keys in cnf.sections():
	ini_config.setdefault(keys)
	dict_sample.clear()
	for opt in cnf.options(keys):
		dict_sample.setdefault(opt,cnf.get(keys,opt))
	ini_config[keys] = dict_sample.copy()
	dict_sample.clear()
del dict_sample
print(ini_config)
print("-----------------------")
#for dct in ini_config:
#	print(dct)
#	for param in ini_config[dct]:
#		print("\t", param,"=",ini_config[dct][param])
ini_config['Settings']['bgcolor'] = "black"
cnf.read_dict(ini_config)
print(cnf.get("Settings","bgcolor"))



