n=int(input())
count=0
lst=list(map(int,input().split()))

for i in range(0,n-1):
    if lst[i]!=lst[i+1]:
        count+=1
        i+=1

print(count)