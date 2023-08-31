# to find square
s = lambda n:n*n
print("The square of 4 is:",s(4))
print("The square of 5 is:",s(5))


s = lambda a,b:a+b
print("the sum of 10,20 is:",s(10,20))

#filter function without lambda 
def even(x):
    if x%2 == 0:
        return True
    else:
        return False
l = [0,5,10,15,20,25,30]
l1 = list(filter(even,l))
print(l1)

#filter function with lambda function
l = [0,5,10,15,20,25]
l1 = list(filter(lambda x:x%2 == 0,l))
print(l1)
l2 = list(filter(lambda x:x%2 != 0,l))
print(l2)

#Map function without lambda
l = [1,2,3,4,5]
def double(x):
    return 2*x
l1 = list(map(double,l))
print(l1)

#Map function without lambda
l = [1,2,3,4,5]
l1 = list(map(lambda x:2*x,l))
print(l1)

l2 = list(map(lambda x:x*x,l))
print(l2)

#Reduce() function
from functools import reduce

l = [10, 20, 30, 40, 50]
result = reduce(lambda x, y: x + y,l)
res1 = reduce(lambda x,y:x*y,l)
print(result)
print(res1)

def wish(name):
    print("Good morning:",name)
wish('Durga')    
