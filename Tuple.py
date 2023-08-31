marks = (95,98,97,97,97)
print(marks.count(97))
print(marks.index(97))
 
person = "ram", "sham", "abhi"
print(person)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concatenated_tuple = tuple1 + tuple2

print(concatenated_tuple)


t = (10,20,30,40)
print(type(t))
print(t.count(10))

r = range(10)
for i in r: print(i)

t = range(10,20)
for i in t : print(i)

s = range(10,20,2)
for i in s : print(i)
#s[0]=15
#print(s)   #'range' object does not support item assignment

l = list(range(10))
print(l)

t = 10,
print(t)

list = [10,20,30] 
t = tuple(list)
print(t)

t = tuple(range(10,20,2))
print(t)
