test=int(input())
f1=1
f2=1

lst=[]
lst.append(f1)
lst.append(f2)

for i in range(2,93):
    lst.append(lst[i-1]+lst[i-2])

while test>0:
    a,b=list(map(int,input().split()))
    s=""
    for i in range(a-1,b):
        s=s+str(lst[i])+" "
    print(s)
    test-=1