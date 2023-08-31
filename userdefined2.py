def wish(name):
    print("Hello", name, "Good morning")
wish("Durga")  

def squareit(num):
    print("The square of",num,"is", num*num)
squareit(4)  
squareit(5)

def even_odd(num):
    if num%2 == 0:
        print(num,"is even num")
    else:
        print(num, "is odd num")  
even_odd(10)
even_odd(15)   

def fact(num):
    result = 1
    while num >= 1: 
        result = result * num
        num = num - 1
    return result  # Moved the return statement out of the loop

for i in range(1, 5):
    print("The factorial of", i, "is:", fact(i))
    
def calc(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div
t = calc(100,50)  
print("The result are")
for i in t:
    print(i)  
     