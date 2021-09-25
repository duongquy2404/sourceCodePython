a,k,n=list(map(int,input().split()))

lst=[]
for i in range(1,n-a+1):
    if (a+i)%k==0:
        lst.append(str(i))

if len(lst)==0:
    print(-1)
else:
    print(" ".join(lst))