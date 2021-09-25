n=int(input())
lst=list(map(int,input().split()))

lst.sort()
x=lst[0]
for i in lst:
    if i==x:
        x+=1
    else:
        break

print(x)