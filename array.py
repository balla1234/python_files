from array import array

int_array = array('i', [1, 2, 3, 4, 5])

int_array.append(6)         #append
int_array.extend([7, 8, 9])   #extend
int_array.insert(3, 10)    #insert
int_array.pop(2)     #pop
int_array.remove(5)  #remove
int_array.index(4)
count = int_array.count(9)
reverse = int_array.reverse()
bytes_data = int_array.tobytes()

new_array = array('i')
new_array.frombytes(bytes_data)


print(int_array)
print(count)
print(reverse)
print(bytes_data)
print(new_array)
