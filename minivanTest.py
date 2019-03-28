import urllib.request
import urllib.parse
import sys
import re
import operator
import collections
import csv
from task1_module2 import doorTest

def help():
    """
    This is the help function
    """
    print("Usage is ./matthew_bybee_group3_hw7.py <file input>")
    return

def parseArg(argument):
    """
    This file accepts a CSV file location and checks it
    """
    
    with open(argument) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            if (line == 0):
                line += 1
                continue
            else:
                doorTest(row)
                continue
    return

#main
try: #do try/catch for portability
    parseArg(sys.argv[1])
except IndexError:
    help()
