# input = a5b6c7d3
# output = aaaaabbbbbbcccccccddd

s = "a5b6c7d3"

cur, prev = "", ""
for i in s:
    if i.isalpha():
        cur = cur+i
        prev = i
    else:
        cur = cur + prev*(int(i)-1)

print(cur)
