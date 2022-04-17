
for x in range(5):
    print(x)

print("----------------")
c=0
while c<7:
    print(c)
    c+=1
    if c==4:
        continue
    else:
        break
print("----------------")

for x in range(10):
    if x % 2 == 0:
        print("Even:",x)
        continue
    print(x)
