a = 10
b = 10
print(a is b)

x = [10, 20 , 30 ,24]
b = bytes(x)
type(b)
print(b[0])
print(b[-1])
for i in b: print(i)

#b[0] = 100 #bytes' object does not support item assignment

c = bytearray(x)

c[0]=100
for i in c : print(i)


