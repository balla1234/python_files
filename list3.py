list = [10,20,30]
print(list[-1])
print(type(list))

#list = eval(input("Enter list"))
#print(list)
#print(type(list))

int_list = []
for i in range(0,10,2):
    int_list.append(i)

print(int_list)

s = "learning python is easy"
l = s.split()
print(l)

n = [1,2,3]
n[1] = 5
print(n)

p = [1,2,3,4,5,6,7,8]
for p1 in p:
    if p1%2 == 0:
     print(p1)
     
n = [1,1,2,2,2,2,3,3,4]    
print(n.count(1)) 
print(n.count(2))

a = [10,20,30]
b = [40,50,60]
c = a+b
d = c*3
print(c)
print(d)

s = [x*x for x in range(1,11)]
print(s)

t = [t*2 for t in range(1,10)]
print(t)

n = [20,"B",10, "A"]
n.sort()
print(n)