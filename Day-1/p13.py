def add(*n):
    sum = 0
    for i in n:
        sum += i
    return sum

print(add())
print(add(10))
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
print(add(10,20,30,40,50))
