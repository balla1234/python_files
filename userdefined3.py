#position argument
def sub(a,b):
        print(a-b)
sub(10,2) 

#keyword aargument
def wish(name,msg):
    print("Hello",name,msg)
wish(name ="durga",msg = "gm")      

#default argument
def wish(name="shivani"):
    print("Hello",name)
wish(name ="durga") 
wish()

#variable length argument
def sum(*n):
    total = 0
    for n1 in n:
        total = total + n1
    print("The sum =",total)
sum(10,20)
sum(10,20,30)        
