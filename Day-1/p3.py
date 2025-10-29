# Exchange the value of two variables without using third value.

a = 10 
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)