P="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    arr=[str(i) for i in input().split()]
    k=int(arr[0])
    if k==0: break
    s=arr[1]
    tmp=""
    for i in s:
        tmp+=P[(P.find(i)+k)%28]
    res=list(tmp)
    res.reverse()
    for i in res:
        print(i,end='')
    print()