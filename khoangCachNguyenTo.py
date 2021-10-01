import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

n,x=[int(i) for i in input().split()]
m=1
print(x,end=" ")
for i in range(n):
    m+=1
    while not checkNT(m):
        m+=1
    x+=m
    print(x,end=" ")
