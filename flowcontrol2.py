s = "hello world"
for x in s:
    print(x)
    
s = input("enter some string:")
i = 0
for x in s:
    print("the character present at", i, "index is:", x)
    i = i + 1
    
#to  print hello ten times
for x in range(10):
  print("hello")  
  
#to display num 0 to 10
for x in range(11):
    print(x)   

#to display odd num from 0 to 20
for x in range(21):
    if(x%2!=0):
        print(x)
        
#to display num from 10 to 1 in descending order
for x in range(10,0,-1):
    print(x)  

list = eval(input("Enter list:"))
sum = 0;  # Use a single equal sign to assign a value, not double equal signs
for x in list:
    sum = sum + x;
    print("The sum =", sum)  # Make sure to put a space around the equals sign
    
for i in range(10):
    if i%2 == 0:
        continue
    print(i)    
    
#infinite loop
i = 0
while True:
   i = i + 1
    print("Hello", i)
    
 #Nested loop
for i in range(4):
    for j in range(4):
        print("i=", i, "j=", j)

    


        
    