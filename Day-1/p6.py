# Take a number input and tell whether it is even or odd without using /,//,% operators and loops

num = int(input("Enter a Number: "))

if num & 1:
    print("Odd")
else:
    print("Even")
