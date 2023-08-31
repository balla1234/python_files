#len
t = (10,20,30,40,10)
print(len(t))

#count
print(t.count(10))

#index
print(t.index(30))

#sorted
t1 = sorted(t)
print(t1)

#min() and max()
print(min(t))
print(max(t))

t = (x**2 for x in range(1,6))
print(type(t))
for x in t:
    print(x)   #getting generator object
    
t = eval(input("Enter tuple of nums:"))
l = len(t)    
sum = 0
for x in t:
    sum = sum + x
print("the sum =",sum)
print("the average =", sum/l)    