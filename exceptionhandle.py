# Trying Exception Handling example

import sys
import traceback

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

"""
try:
    print("Trying..")
    raise NameError("h")
except NameError:
    print("Except NameError")
finally:
    print("finally..")
"""


try:
    print("Trying")
    #print(1/0)
    #print(var)
    path = "/Users/keerthikaliki/PycharmProjects/py1/"
    filenam = path + "sampledata.txt"
    f=open("/Users/keerthikaliki/PycharmProjects/py")
    f.read()
except Exception as e:
    print(e)
    traceback.print_exc()
finally:
    print("finally")



