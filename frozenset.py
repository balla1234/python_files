#frozenset
numbers = [1, 2, 3, 4, 5]
frozen_numbers = frozenset(numbers)
print(frozen_numbers)

#copy
original_frozen = frozenset([1, 2, 3])
copy_frozen = original_frozen.copy()
print(copy_frozen)

#isdisjoint
set1 = frozenset([1, 2, 3])   #Returns True if the frozenset has no elements in common with the other iterable
set2 = frozenset([4, 5, 6])
disjoint = set1.isdisjoint(set2)
print(disjoint)

#issubset
set1 = frozenset([1, 2])       
set2 = frozenset([1, 2, 3, 4])
subset = set1.issubset(set2)
print(subset)

#issuperset
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([1, 2])
superset = set1.issuperset(set2)
print(superset)

#union
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])
union = set1.union(set2)
print(union)

#intersection
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])
intersection = set1.intersection(set2)

#difference
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])
difference = set1.difference(set2)
print(difference)

#symmetric_difference
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)
