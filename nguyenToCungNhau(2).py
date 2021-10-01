import math

n,k=[int(i) for i in input().split()]
count=1
for i in range(int(math.pow(10,k-1)),int(math.pow(10,k))):
    if math.gcd(n,i)==1:
        if count<10:
            print(i,end=" ")
            count+=1
        else:
            count=1
            print(i)