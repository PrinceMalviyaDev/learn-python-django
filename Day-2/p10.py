# List is the collection of heterogeneous objects.
# List is mutable
# Insertion order is preserved
# All the elements are indexed

list = [1, 2, "Srishti", 18.9, True]
print(list)


# Difference between append and extend method:

lst = [10,20,30,40,50]
l = [100,200,300,400]
l2 = [1000, 2000, 3000]

print(lst)
lst.append(l)
print(lst)

print(lst[5][2]) # output = 300

lst.extend(l2)
print(lst)