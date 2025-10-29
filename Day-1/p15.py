s = lambda n:n*n
print("The square of 4 is",s(4))
print("The square of 5 is",s(5))

s = lambda a,b:a+b
print("The sum of 2 and 3 is",s(2,3))
print("The sum of 4 and 5 is",s(4,5))

s = lambda a,b:a if a>b else b
print("The biggest among 10 and 20 is", s(10,20))
print("The biggest among 30 and 15 is", s(30,15))