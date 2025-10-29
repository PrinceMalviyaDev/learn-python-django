def calc(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    floor = a//b
    rem = a%b
    power = a**b

    return sum,sub,mul,div,floor,rem,power

# sum,sub,mul,div,floor,rem,power = calc(20,2)

# print("sum = ", sum)
# print("sub = ", sub)
# print("mul = ", mul)
# print("div = ", div)
# print("floor = ", floor)
# print("rem = ", rem)
# print("power = ", power)

t = calc(20,2)

for i in t:
    print(i)