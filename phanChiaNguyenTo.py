import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

n=int(input())
tmp=list(map(int,input().split()))
lst=list()
for i in tmp:
    if i not in lst:
        lst.append(i)
sumFirst=0
sumLast=sum(lst)
location=-1
for i in range(0,len(lst)):
    sumFirst+=lst[i]
    sumLast-=lst[i]
    if checkNT(sumFirst) and checkNT(sumLast):
        location=i
        break
if location==-1:
    print("NOT FOUND")
else:
    print(location)