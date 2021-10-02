n,m=[int(i) for i in input().split()]
arr=set(map(int,input().split()))
brr=set(map(int,input().split()))
check=True
if len(arr)==len(brr):
    for i in arr:
        if i not in brr:
            check=False
            break
else:
    check=False

if check:
    print("YES")
else:
    print("NO")