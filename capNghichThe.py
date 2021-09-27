n=(int)(input())
count=0
lst=list(map(int,input().split()))

for i in range(0,n-1):
    for j in range(i+1,n):
        if lst[i]>lst[j]:
            count+=1

print(count)
