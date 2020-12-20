#!/usr/bin/env python3

import os
import os.path
import base64
import csv
import sys
from typing import List, Any

csvdata: list[Any] = []

csv_file = "icons.csv"


def csv_reader(file_obj):
    with open(file_obj, "r") as csvfile:
        csv_data = csv.reader(csvfile)
        for row in csv_data:
            # print(row) # Debug
            # csvdata.append(row)
            # print(str(' '.join(row)).split(' '))
            csvdata.append(str(' '.join(row)).split(' '))


def printcsv(listname=None):
    if listname is None:
        listname = csvdata
    for i in range(len(listname)):
        # print(listname[i][0], end = '\n')
        for j in range(len(listname[i])):
            print(listname[i][j], end='\n')


def main():
    # Debug
    # if len(sys.argv) <= 1:
    #    print("No root directory specified!")
    #    exit(1)
    # Debug
    # print("Work")
    csv_reader(csv_file)
    # print(csvdata)
    printcsv()


if __name__ == "__main__":
    main()
