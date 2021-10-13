import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

n=int(input())
arr=list(map(int,input().split()))
lst=list()
count=0
for i in range(0,10001):
    if checkNT(i) or i in arr:
        lst.append(i)

for i in range(len(lst)):
    if checkNT(lst[i])==False:
        j=i-1; k=i+1
        while not checkNT(lst[j]):
            j-=1
        while not checkNT(lst[k]):
            k+=1
        if lst[i]>2:
            count=max(count,min(lst[i]-lst[j],lst[k]-lst[i]))
        else:
            count=max(count,lst[k]-lst[i])
        if lst[i]==max(arr):
            break
print(count)
