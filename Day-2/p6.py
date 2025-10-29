a = " Srishti "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

b = "Prince"
c = "Indore"
print("i am {} and i am from {} ".format(b,c))

d = "hello sait, this college is sait, i am sait, you are sait, we are sait, everyone is sait, but srishti is not sait"

sub = "sait"
i = d.find(sub)
if i == -1:
    print("Substring is not present.")
while (i != -1):
    print("{} is present at {} position".format(sub,i))
    i = d.find(sub, i+len(sub), len(d))