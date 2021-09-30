def changeArr(arr,n):
    if arr[0]==arr[1]==arr[2]==arr[3]:
        return n
    else:
        a=arr[0];b=arr[1];c=arr[2];d=arr[3]
        arr[0]=abs(a-b);arr[1]=abs(b-c);arr[2]=abs(c-d);arr[3]=abs(d-a)
        return changeArr(arr,n+1)

while True:
    arr=[int(i) for i in input().split()]
    if arr[0]==arr[1]==arr[2]==arr[3]==0:
        break
    else:
        print(changeArr(arr,0))
