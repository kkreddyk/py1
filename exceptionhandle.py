# Trying Exception Handling example

import sys

"""
path = "/Users/keerthikaliki/PycharmProjects/py1/"
file1 = path+"sampledata.txt"
try:
    f = open(file1)
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("Testing OSError for file open::: {0}".format(err))
    raise
"""


"""try:
    print("Trying...")
    #print("Trying..."+1/0)
    #print("Trying..."+a)
except ZeroDivisionError:
    print("Except..ZeroDivisionError...")
except NameError:
    print("Except..NameError..")
except:
    print("Generic Errors")
else:
    print("in else")
finally:
    print("finally...")
"""

try:
    print("Trying..")
    raise NameError("h")
except NameError:
    print("Except NameError")

finally:
    print("finally")