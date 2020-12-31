#!/usr/bin/env python3

import os
import os.path
import sys
import math
import webbrowser
import platform

def main():
	file_dir = os.path.join(os.getcwd(), "dirs.html")
	directory = os.getcwd()
	cmd_command = "tree /A /F" + " " + directory + " " + ">>" + file_dir
	bash_three_dir = os.path.join(os.getcwd(), "modules","tree-1.8.0","tree")
	bash_str_one = bash_three_dir + " " + "-h -D --dirsfirst --sort=name -H" + " "
	bash_str_two = " " + ">" + " " + file_dir
	bash_command = bash_str_one + directory + bash_str_two
	html_str_one = "<html>\n\t<head>\n\t\t<title>Dirs</title>\n\t\t<style>"
	html_str_two = "\n\t\t\t* {\n\t\t\t\tfont-family: sans-serif;\n\t\t\t\tbackground-color: white;\n\t\t\t}"
	html_str_three = "\t\t</style>\n\t</head>\n<body>\n<pre>"
	html_str_for = "</pre>\n</body>\n</html>"
	if "Windows" in platform.system():
		file = open(file_dir, "w")
		file.write(html_str_one)
		file.write(html_str_two)
		file.write(html_str_three)
		file.close()
		os.system(cmd_command)
		file = open(file_dir, "a")
		file.write(html_str_for)
		file.close()
		webbrowser.open(os.path.realpath(file_dir))
	else:
		os.system(bash_command)
		webbrowser.open(os.path.realpath(file_dir))
	# tree -h -D --dirsfirst --sort=name -H . > index.html

if __name__=="__main__":
	main()

