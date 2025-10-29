from collections import deque   # For Queue

# Stack using list:
lst = [1,2,3,4,5,6,7]
print(lst)
print(lst.pop())
print(lst)

# Queue using list
queue = deque([1,2,3,4,5,6])
queue.append(7)
print(queue.popleft())

sqr = [x*x for x in range(1,11)]
print(sqr)

sqrs = list(map(lambda x:x**2, [x for x in range(1, 11)]))
print(sqrs)