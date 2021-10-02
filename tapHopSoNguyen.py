n,m=[int(i) for i in input().split()]
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
arr=set(arr)
brr=set(brr)
lst=list()
for i in arr:
    if i in brr:
        lst.append(i)
lst.sort()
for i in lst:
    print(i,end=" ")
print()
lst1=list()
for i in arr:
    if i not in brr:
        lst1.append(i)
lst1.sort()
for i in lst1:
    print(i,end=" ")
print()
lst2=list()
for i in brr:
    if i not in arr:
        lst2.append(i)
lst2.sort()
for i in lst2:
    print(i,end=" ")