import math

def sumNumber(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

for i in range(int(input())):
    a,b=[int(i) for i in input().split()]
    if checkNT(sumNumber(math.gcd(a,b))):
        print("YES")
    else:
        print("NO")
