#add
s = {10,20,30}
s.add(40)
print(s)

#update
l = [2,3,4]
s.update(l)
print(s)

t = {x*x for x in range(5)}
print(t)

w = input("Enter word to search for vowels: ")
s = set(w)
v = {'a','e','i','o','u'}
d = s.intersection(v)
print("The different vowel present in",w,"are",d)