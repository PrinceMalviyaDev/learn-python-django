import time

print("Hello")

time.sleep(1)

print("Prince")

a = time.time()
print(a)

b = time.ctime(a)
print(b)

c = time.localtime(10)
print(c)