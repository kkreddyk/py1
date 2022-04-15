# Test Python program

print("Printing...",end="")
print("2nd line",end="\n")
print("3rd line")

v1 = "value-1"
v2="value-2"
v3="value-3"

print(v1,v2,v3)
print(v1+v2+v3)
print("-----------------")
path="/Users/keerthikaliki/PycharmProjects/py1"
filenam="sampledata.txt"
f = open(filenam,"rt")
print(f.read(10))
print("-----------------")
print(f.read())
print("-----------------")
print("-----------------")
