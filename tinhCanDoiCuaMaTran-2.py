n=int(input())
arr=list()
for i in range(0,n):
    arr_row=list(map(int,input().split()))
    arr.append(arr_row)
k=int(input())
sumUpper=0; sumLower=0
for i in range(0,n):
    for j in range(0,n):
        if i+j<n-1:
            sumUpper+=arr[i][j]
        if i+j>n-1:
            sumLower+=arr[i][j]
if abs(sumUpper-sumLower)<=k:
    print("YES")
else:
    print("NO")
print(abs(sumUpper-sumLower))