# t = 5,5,4,3,2,1
# t1 = sorted(t)

# max = max(t1)
# i = len(t1)-1
# while(i > -1):
#     if t1[i] < max:
#         max = t1[i]
#         i = -1
#     i -= 1
# print(max)

t = (5,5,4,3,2,1)
p = max(t)
r = t[0]

for k in t:
    if(r < k and k != p):
        r = k
    elif r == p:
        r = k
print(r)
