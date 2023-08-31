original_list = [1, 2, 3]
copied_list = original_list.copy()

copied_list.append(4)
print(original_list)  # Output: [1, 2, 3]
print(copied_list)    # Output: [1, 2, 3, 4]

#Copying a List of Objects:

class MyClass:
    def __init__(self, value):
        self.value = value

obj_list = [MyClass(1), MyClass(2), MyClass(3)]
copied_obj_list = obj_list.copy()

copied_obj_list[0].value = 100
print(obj_list[0].value)       # Output: 100
print(copied_obj_list[0].value) # Output: 100

