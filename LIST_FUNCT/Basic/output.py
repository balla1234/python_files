print("Hello \n World")
print("Hello \t World")
print("Hello"*10)
print("Hello"+"world")
print("hello","india")

a,b,c = 10,20,30
print("the values are:", a,b,c)

print(a,b,c,sep=',')
print(a,b,c,sep=':')

print("Namaste")
print("India")

print("Namaste", end = '')

print("India", end = '')

s = "gayatri"
a = 8
s1 = "java"
s2 = "python"
print("hello",s,"your age",a)
print("you are teaching",s1,"and",s2)

a = 10
b = 20
c = 30
print("a value is %i" %a)
print("b value is %d and c value is %d" %(b,c))

s = "shivani"
list = [1,2,3,4]
print("Hello %s...The list of items are %s" %(s,list))




name = "gayatri"
salary = 10000
gf = "sunny"

# Using the .format() method to insert values into the string
message = "hello {0} your salary is {1} and your friend {2} is waiting".format(name, salary, gf)
print(message)
