
list1 = [1, 2, 3, 4]
list2 = [5, 6]
nested = [list1, list2]
print("Nested List:", nested)
print("Length:", len(list1))
print("Concatenation:", list1 + list2)
print("Membership (3 in list1):", 3 in list1)
print("Iteration:")
for i in list1:
    print(i, end=' ')
print("\nIndexing:", list1[2])
print("Slicing:", list1[1:3])
