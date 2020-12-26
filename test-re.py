import re

text = "The ants go marching one by one"

strings = ['the', 'one']

def Enquiry(lis1):
	if len(lis1) == 0:
		return 0
	else:
		return 1

def search_re(str_, words):
	_tmp = []
	for word in words:
		match = re.findall(word, str_)
		if match: _tmp.append(word)
	if Enquiry(_tmp): return _tmp
	else: return False

_str = search_re(text,strings)
print(_str)
