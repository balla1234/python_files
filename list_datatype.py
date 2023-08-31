#append
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)
  
#clear
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  

#copy
original = [1, 2, 3]
new_copy = original.copy()
new_copy.append(4)
print(original)  
print(new_copy)  

#count
numbers = [1, 2, 2, 3, 2, 4]
count_of_2 = numbers.count(2)
print(count_of_2) 


#extend
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1) 


fruits = ['apple', 'banana', 'cherry']
index_of_banana = fruits.index('banana')
print(index_of_banana)  

fruits = ['apple', 'banana', 'cherry']
removed_fruit = fruits.pop()
print(removed_fruit) 
print(fruits) 

colors = ['red', 'green', 'blue', 'green']
colors.pop(-1)
print(colors)  

numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)  

numbers1 = [3, 1, 4, 1, 5, 9, 2]
numbers1.sort()
print(numbers1)  

# Creating an empty list
my_list = []

# Appending elements to the list
my_list.append(5)       # Appends the integer 5
my_list.append("Hello") # Appends the string "Hello"
my_list.append(True)    # Appends the boolean True
my_list.append([1, 2, 3])  # Appends a nested list [1, 2, 3]

print(my_list)  

# Appending elements of the same data type
int_list = []
for i in range(1, 6):
    int_list.append(i)

print(int_list) 


# Generating a list of multiples of 2
multiples_of_2 = [num * 2 for num in range(1, 11)]

# Printing the list
print(multiples_of_2)
 

        








