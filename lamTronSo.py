import math

for i in range(int(input())):
    n=int(input())
    l=len(str(n))
    count=1
    while n>math.pow(10,count):
        if n%math.pow(10,count)<math.pow(10,count)/2:
            n-=n%math.pow(10,count)
        else:
            n+=math.pow(10,count)-n%math.pow(10,count)
        count+=1
    print(int(n))