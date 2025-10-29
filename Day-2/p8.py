# input = a5b2c9
# output = afbdcl
# USE  :   ord("a") = 97      char(65) = A

s = "a5b3c9"

result = ""
for i in s:
    if i.isalpha():
        result = result+i
        previous = i
    else:
        result = result+chr(ord(previous)+int(i))
        
print(result)
        
