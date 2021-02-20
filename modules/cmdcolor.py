#!/usr/bin/env python3

from ctypes import *

windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

def setCMDColor(colored):
    windll.Kernel32.SetConsoleTextAttribute(h, colored)
