#!/usr/bin/env python3

import subprocess

cmd = "tree /F"
returned_output = subprocess.check_output(cmd)
print(returned_output.decode("utf-8"))
