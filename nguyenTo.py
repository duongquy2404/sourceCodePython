import math

def checkNT(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def checkCountK():
    n=int(input())
    count=0
    for i in range(n):
        if math.gcd(i,n)==1:
            count+=1
    if checkNT(count):
        print("YES")
    else:
        print("NO")

for i in range(int(input())):
    checkCountK()        