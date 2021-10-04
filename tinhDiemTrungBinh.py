import math
n=int(input())
lst=list(map(float,input().split()))
lst.sort()
count=0
sum=0
for i in range(1,len(lst)-1):
    if lst[i]!=lst[0] and lst[i]!=lst[len(lst)-1]:
        sum+=lst[i]
        count+=1
print(round(sum/count,2))