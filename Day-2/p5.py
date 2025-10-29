c = '''indore is a "cool" city
        indore is a big city'''

sec = c[12:18]

print(sec)

for i in range(-1,-7, -1):
    print(sec[i],end="")

print("")
print(sec[::-1])

print(c[::])
print(c[::-1])
print(c[:13])
print(c[13:])