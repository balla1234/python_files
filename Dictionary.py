#clear
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  

#get
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')
print(value)  

#item
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)]) in tuple 

#keys
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b', 'c'])

#values
my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)  # Output: dict_values([1, 2, 3])

#pop
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}

value = my_dict.pop('d', 0)
print(value)  # Output: 0

#pop items
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.popitem()
print(my_dict)  # Output: {'a': 1, 'b': 2}

#update
my_dict = {'a': 1, 'b': 2}
new_dict = {'c': 3, 'd': 4}
my_dict.update(new_dict)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}







marks = {"english" : 95, "chemistry" : 92, } 
print(marks["chemistry"])  
marks["physics"] = 96
print(marks)

car = dict(colour = 'Black', brand = "Ford", model = "Mustang", year = 2021)
print(car)
print(car['colour'])
print(car['brand'])

car = dict(colour = 'Black', brand = "Ford", model = "Mustang", year = 2021)
p = car['city'] = 'Hyderabad'

print(p)

car = dict(colour = 'Black', brand = "Ford", model = "Mustang", year = 2021)
del car['brand']
print(car)

# clear()
dict1 = {'a': 100, 'b': 200, 'c': 300}
print(dict1)
print("Perform Clear on Dict")
dict1.clear()
print(dict1)

# get()
dict1 = {'a': 100, 'b': 200, 'c': 300}
print("\n")
print(dict1)
print("Get value of the key b")
val = dict1.get('b')
print(val)

print("\n Get value of the key b")
print(dict1.get('z'))

# returned default instead of None.
print("\n Get value of the key z")
print(dict1.get('z', -1))

# items()
print("\n All items in dict1")
print(list(dict1.items()))
print(list(dict1.items())[1][0])
print(list(dict1.items())[1][1])

# keys()
# Returns a iterable object of all keys in dict1
print("\n keys in dict1")
print(dict1.keys())

# values()
#Returns a iterable object of values in dict1
print("\n Values in dict1")
print(dict1.values())

# pop()
# Removes a key from a dictionary.
value = dict1.pop('b')
print(value)
print("\n Items after pop")
print(dict1)

# popitem()
dict1 = {'a': 100, 'b': 200, 'c': 300}
#Removes the last key-value pair added from dict1 and returns it as a tuple
value = dict1.popitem()
print(value)
print("\n Items after popitem")
print(dict1)
print(dict1.popitem())


# update
dict1 = {'a': 100, 'b': 200, 'c': 300}
#To update an entry, you can just assign a new value to an existing key
dict1['b'] = 101
print("\n Items after update")
print(dict1)

dic1 = {10: 100, 20: 200}
dic2 = {30: 300, 40: 400}
dic3 = {50: 500, 60: 600}

new_dict1 = {**dic1, **dic2, **dic3}

print(new_dict1)

n = 3
new_dict1 = {}

# Generate keys and values in the format (n, nnn)
for i in range(1, n + 1):
    key = i
    value = int(str(n) * 3)
    new_dict1[key] = value

print(new_dict1)

d = {101:'durga', 102:'ravi', 103: 'shiva'}
d[101] = 'sunny'
print(d)

f = {}
f['a'] = "apple"
f['b'] = "banana"
print(f)

d = eval(input({"Enter dictionary :"}))
s = sum(d.values())
print("sum=",s)