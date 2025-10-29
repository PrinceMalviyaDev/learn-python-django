# Types of arguments:

# 1. Positional arguments
def posfunc(a,b):
    print(a + b)
posfunc(3,4)


# 2. Keyword arguments
def keyfunc(name,msg):
    print("Welcome",name,msg)
keyfunc(msg="How are you?", name="Prince")


# 3. Default arguments
def deffunc(name="User",msg="How are you?"):
    print("Hello",name,msg)
deffunc("Prince")


# 4. Variable length arguments
def varfunc(*a):
    for i in a:
        print(i)
varfunc(1,2,3,4,5)