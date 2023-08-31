#add

fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

#clear
numbers = {1, 2, 3, 4, 5}
numbers.clear()
print(numbers)  # Output: set()

#copy
original = {1, 2, 3}
new_copy = original.copy()
new_copy.add(4)
print(original)  # Output: {1, 2, 3}
print(new_copy)  # Output: {1, 2, 3, 4}

#difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference = set1.difference(set2)
print(difference)  # Output: {1, 2}

#difference_update
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}

#discard
fruits = {'apple', 'banana', 'cherry'}
fruits.discard('banana')
print(fruits)  # Output: {'apple', 'cherry'}

#intersection
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection = set1.intersection(set2)
print(intersection)  # Output: {2, 3}

#intersection_update
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)  # Output: {2, 3}

#isdisjoint
set1 = {1, 2, 3}
set2 = {4, 5, 6}
disjoint = set1.isdisjoint(set2)
print(disjoint)  # Output: True

#issubset
set1 = {1, 2}
set2 = {1, 2, 3, 4}
subset = set1.issubset(set2)
print(subset)  # Output: True

#issuperset
set1 = {1, 2, 3, 4}
set2 = {1, 2}
superset = set1.issuperset(set2)
print(superset)  # Output: True

#pop
numbers = {1, 2, 3, 4}
popped = numbers.pop()
print(popped)  # Output: 1 or another arbitrary element
print(numbers)  # Output: {2, 3, 4}

#remove
fruits = {'apple', 'banana', 'cherry'}
fruits.remove('banana')
print(fruits)  # Output: {'apple', 'cherry'}

#symmetric_difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)  # Output: {1, 2, 4, 5}

#symmetric_difference_update
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 4, 5}

#union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
print(union)  # Output: {1, 2, 3, 4, 5}

#update
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}


marks = {95,98,97,97,97}

for score in marks:
    print(score)
    
# Create a Set
print("Create a Set s")
s = {"red", "blue", "green"}
print(s)    

print("\n Add Method")
print("Add a new color Orange")
s.add("orange")
print(s)

# Copy 
print("\n Copy Method")
print("A new Set s1 is created")
s1 = s.copy()
print(s1)

# Remove
print("\n Remove Method")
print("Remove Orange from s1")
s1.remove("orange")
print(s1)

# Discard
print("\n Discard Method")
print("Discard is similar to remove, but does not throw any error if element does not exist")
s1.discard("elephant")


s = {"red", "blue", "green", "orange"}
s1 = {"red", "blue", "green"}

print(s1.issubset(s))
print(s.issuperset(s1))

##
def intersection(a, b):
    s1 = set(a)
    s2 = set(b)
    return s1.intersection(s2)

if __name__ == "__main__":
    # Create two lists of your choice.
    a = [10, 12, 31, 44, 56]
    b = [16, 71, 98, 91, 10]
    s3 = intersection(a, b)

    if len(s3) > 0:
        print("True")
    else:
        print("False")
        
z = {100, 0, 10, 100, 10, "durga"} 
print(z)  
#z[0]=20 
print(z)   #'set' object does not support item assignment
z.add(60)
z.remove("durga")
print(z)

f = frozenset(z)
print(type(f))
for i in f: print(i)
#cannot use add and remove function in frozenset
