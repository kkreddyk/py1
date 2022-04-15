# Test Python program
import os
print("Printing...",end="")
print("2nd line",end="\n")
print("3rd line")

v1 = "value-1"
v2="value-2"
v3="value-3"

print(v1,v2,v3)
print(v1+v2+v3)
print("-----------------")
path="/Users/keerthikaliki/PycharmProjects/py1/"
filenam=path+"sampledata.txt"
f = open(filenam,"rt")
print("Reading 10 Characters="+f.read(10))
print("-----------------")
print("Reading a Line="+f.readline())
print("-----------------")
print("Read the full file from previous cursor="+f.read())
print("-----------------")


f2=open(filenam,"rt")
for x in f2:
    print(x)
print("Closing the file::"+path+"/"+filenam)
f2.close()
print("-----------------")

f3=open(filenam,"a")
f3.write("\nThis is a new Line")
f3.close()

f4=open(filenam,"r")
for x in f4:
    print(x)
f4.close()
print("-----------------")


filenam1=path+"sampledata1.txt"

if os.path.exists(filenam1):
    os.remove(filenam1)
else:
    print("File:: "+filenam1+" doesn't exist")

f5=open(filenam1,"x")


filenam2=path+"sampledata1.txt"
f6=open(filenam2,"w")
f6.write("Writing a new line")
f6.close()
print("--------f7---------")

f7=open(filenam2,"r")
for x in f7:
    print(x)
f7.close()

