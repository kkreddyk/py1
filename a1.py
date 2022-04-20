
import datetime
path = "/Users/keerthikaliki/PycharmProjects/py1/"
filen = path + "sampledata.txt"

f=open(filen)
#print(f.read())

for x in f.readlines():
    print("***=",x)
    break

print(datetime.date.year)
print(datetime.time)
print(datetime.date)
print(datetime.date)
print(datetime.date)
