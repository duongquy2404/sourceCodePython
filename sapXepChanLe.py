n=int(input())
lst=list()
while len(lst)<n:
    lst.extend(list(map(int,input().strip().split())))
even=list()
odd=list()
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort(reverse=True)
e=0; o=0
arr=list()
for i in lst:
    if i%2==0:
        arr.append(even[e])
        e+=1
    else:
        arr.append(odd[o])
        o+=1

for i in arr:
    print(i,end=' ')