import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n=int(input())
lst=[int(i) for i in input().split()]
dic={}

for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

for i in lst:
    if checkNT(i) and dic[i]!=0:
        print(i,dic[i])
        dic[i]=0
