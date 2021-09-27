a,k,n=[int(i) for i in input().split()]
result=False
n=int(n/k)
for i in range(1,n+1):
    if i*k-a>0:
        result=True
        print(i*k-a,end=' ')

if result==False: print(-1)