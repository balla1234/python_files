# Defining a simple function
def greet(name):
    return "Hello, " + name + "!"

# Calling the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!

# Function with multiple arguments
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# Calling a function with keyword arguments
def power(base, exponent):
    return base ** exponent

result = power(exponent=4, base=2)
print(result)  # Output: 8

# Function that returns a value
def multiply(a, b):
    return a * b

product = multiply(4, 7)
print(product)  # Output: 28


# Function with default argument
def greet(name="Guest"):
    return "Hello, " + name + "!"

message = greet()
print(message)  # Output: Hello, Guest!

def print_sum(first,second):
    return first + second

add = print_sum(1,5)
print(add)

def is_even(num):
    return num % 2 == 0

for i in range(1, 6):
    if is_even(i):
        print(i, "is even")
    else:
        print(i, "is odd")
        
        
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Even numbers:")
for num in number_list:
    if num % 2 == 0:
        print(num)

print("Odd numbers:")
for num in number_list:
    if num % 2 != 0:
        print(num)
        
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Multiples of 3:")
for num in number_list:
    if num % 3 == 0:
        
        print(num)
      
for i in range(1, 20):
    if i % 4 == 0:
        print(i)
        
        

    
