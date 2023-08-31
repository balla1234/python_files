# Creating an empty list
my_list = []

# Appending elements to the list
my_list.append(5)       # Appends the integer 5
my_list.append("Hello") # Appends the string "Hello"
my_list.append(True)    # Appends the boolean True
my_list.append([1, 2, 3])  # Appends a nested list [1, 2, 3]

print(my_list)  # Output: [5, 'Hello', True, [1, 2, 3]]

# Appending elements of the same data type
int_list = []
for i in range(1, 6):
    int_list.append(i)

print(int_list)  # Output: [1, 2, 3, 4, 5]

list = [10, 20, 30]
list.append("durga")
list.remove(20)
list3 = list*2
print(list)
print(list3)
