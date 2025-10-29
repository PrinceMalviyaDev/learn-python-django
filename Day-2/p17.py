# i % 2 != 0 and t % 3 != 0 then it is prime

def isPrime(num):
    flag = 0
    for i in range(1, num+1):
        if(num % i == 0):
            flag += 1
    if flag <= 2:
        print(num, "is Prime.")
    else:
        print(num, "is not Prime")
    

list = [1,2,3,4,5,6,7,8,9,10,11]

for i in list:
    isPrime(i)