cart = [10,20,500,700,50,60]
for item in cart:
    if item>=500:
        print("we cannot process this item:",item)
        continue
    print(item)
    
cart = [10,20,500,700,50,60]
for item in cart:
    if item>=500:
        print("we cannot process this order")
        break
    print(item)  
else:
    print("congrats..")  
  