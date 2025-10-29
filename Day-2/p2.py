import random

list = []
for i in range(1,11):
    num = random.randint(1,10)
    list.append(num)

for i in list:
    print(i)

for i in range(10):
    print(random.uniform(1,10))