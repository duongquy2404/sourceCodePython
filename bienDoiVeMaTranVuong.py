n,m=[int(i) for i in input().split()]
arr=list()

for i in range(n):
    arr_row=list(map(int,input().split()))
    arr.append(arr_row)

if n>m:
    count=n-m
    for i in range(n):
        if count>0 and i%2==0:
            count-=1
            continue
        for j in range(m):
            print(arr[i][j],end=" ")
        print()
elif n<m:
    count=m-n
    for i in range(n):
        for j in range(m):
            if j%2!=0 and j<count*2:
                continue
            print(arr[i][j],end=" ")
        print()
else:
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end=" ")
        print()