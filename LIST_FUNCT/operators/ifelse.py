a = 10
b = 20
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
    
a = int(input("Enter first num"))
b = int(input("Enter sec num"))
c = int(input("Enter third num"))

max_value = a if a > b and a > c else b if b > c else c
print("Maximum value:", max_value)
print("both numbers are equal" if a==b else "first num is less than sec num" if a<b else "first num greater then sec num")
    
