name = "Tony Shark"
print(name[2:8])
print(name.upper())
print(name.lower())
print(name.find('S'))
print(name.replace("Tony Shark", "Ironman"))
print("T" in name)     #shows true or false
print("shivani"+"Balla")
print("shivani"*2)

s = "abababababab"
s1 = s.replace("a","b")
print(s1)

t = "gayatri software"
l = t.split()
for x in l:
    print(x)
    
#joining of strings:
t = ('sunny', 'bunny', 'chinny')
s = '-'.join(t)
print(s)

l = ["lion","tiger"]
p = ':'.join(l)
print(p)
      

#Immutable data type
my_string = "hello"
new_string = my_string.upper()  # Creating a new string with modifications
print(new_string)

def fullName(first, last):
    print("Hello " + first + " " + last + "! Happy Learning Python")

if __name__ == '__main__':
    print("Please enter First Name")
    first = input()
    print("Please enter Last Name")
    last = input()
    fullName(first, last)
    
    
    
    
    
    
    
    
    
    
    



