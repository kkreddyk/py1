# Testing formatting
var="value"
print(f'Format:: {var}')

path="/Users/keerthikaliki/PycharmProjects/py1/"
filenam=path+"sampledata.txt"
f=open(filenam,"r")

print(f.read())
f.seek(10)
print("--------=--=-==-")
print(f.read())