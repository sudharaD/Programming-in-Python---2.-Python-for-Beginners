fruits = {"mango", "banana", "orange"}

print(fruits)

# can add multiple elements
fruits.update("A", "B")
print(fruits)

# can add single element
fruits.add("C")
print(fruits)

# remove an element, but the item not in the set will raise an error
fruits.remove("C")
print(fruits)

# remove an element but not raisi error eeven item not in the set
fruits.discard("A")
print(fruits)

# remove an random element
fruits.pop()
print(fruits)

# Set Union
A = {"1", "2", "5", "6"}
B = {"1", "3", "5", "6"}
print(A | B)

# Union() method
C = {"12", "13", "14", "15"}
D = {"12", "13", "20", "21"}
print(C.union(D))

# intersection
print(A & B)
print(C.intersection(D))

# Set Difference
print(A - B)
print(C.difference(D))

# Quiz problem
set1 = set([4, 5, (6, 7)])
set1.update([5, 2, 6])
print(set1)
check1 = 2 in set1
check2 = 6 in set1
print(check1 and check2)