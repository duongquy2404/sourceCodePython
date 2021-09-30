import math

n=int(input())
lst=[int(i) for i in input().split()]
lst.sort()
for i in range(0,len(lst)-1):
    for j in range(i+1,len(lst)):
        if math.gcd(lst[i],lst[j])==1:
            print(lst[i],lst[j])     