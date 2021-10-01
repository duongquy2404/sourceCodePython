for i in range(int(input())):
    n,m,k=[int(i) for i in input().split()]
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    crr=list(map(int,input().split()))
    lst=list()
    i=0; j=0; k=0
    while i<len(arr) and j<len(brr) and k<len(crr):
        if arr[i]<brr[j] or arr[i]<crr[k]:
            i+=1
        elif brr[j]<arr[i] or brr[j]<crr[k]:
            j+=1
        elif crr[k]<arr[i] or crr[k]<brr[j]:
            k+=1
        elif arr[i]==brr[j]==crr[k]:
            lst.append(arr[i])
            i+=1; j+=1; k+=1
    if len(lst)>0:
        for i in lst:
            print(i,end=" ")
        print()
    else:
        print("NO")


