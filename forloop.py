

for x in "somename":
    print(x)

print(f'======')

for x in [1,2,3,4]:
    print(x)
print(f'======')

for x in [1,2,3,4,5,6,7,8,9]:
    print(x)
    if x == 7:
        print("breaking at x==",x,"----",type(x))
        break

s='hello'
print("s[2]=",s[2])

a={1,2,3,3,4,5,5,6}
print("a=",a)
print(type(a))