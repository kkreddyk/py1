# Trying Exception Handling example

import sys

path = "/Users/keerthikaliki/PycharmProjects/py1/"
file1 = path+"sampledata.txt"
try:
    f = open(file1)
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("Testing OSError for file open::: {0}".format(err))
    raise