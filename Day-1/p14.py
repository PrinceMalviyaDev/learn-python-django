a = 9000
print("Initial Value: ",a)

def sum(*n):
    global a 
    a = 12000
    print("Global variable is modified by sum function.")

sum()
print("After Modification:",a)