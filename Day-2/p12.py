lst = [1,2,3,4,6]

# lst.insert(index, element)
lst.insert(4,5)
print(lst)

print(lst.pop())

print(lst.remove(4))
print(lst)

lst.reverse()
print(lst)

lst.sort()
print(lst)

a = [[3,4],[1,2],[5,6]]
a.sort(key = lambda x:x[0])
print(a)