n=int(input())
brr=list()
for i in range(n):
    brr_row=list(map(int,input().split()))
    brr.append(brr_row)
arr=list()
arr.append(int((brr[0][1]+brr[0][2]-brr[1][2])/2))
for i in range(1,n):
    arr.append(brr[0][i]-arr[0])
for i in arr:
    print(i,end=" ")