n=int(input())
arr=list()
sumUpper=0
sumLower=0
for i in range(0,n):
    arr_row=list(map(int,input().split()))
    arr.append(arr_row)
k=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i<j:
            sumUpper+=arr[i][j]
        elif i>j:
            sumLower+=arr[i][j]
if abs(sumUpper-sumLower)<=k:
    print("YES")
else:
    print("NO")
print(abs(sumUpper-sumLower))