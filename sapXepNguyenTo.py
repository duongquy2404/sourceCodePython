import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

n=int(input())
lst=list(map(int,input().split()))
tmp=list()
for i in lst:
    if checkNT(i):
        tmp.append(i)
tmp.sort()
for i in range(0,len(lst)):
    if checkNT(lst[i]):
        lst[i]=tmp.pop(0)
for i in lst:
    print(i,end=" ")