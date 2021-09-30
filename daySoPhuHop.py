def phuHop():
    n=int(input())
    arr=[int(i) for i in input().split()]
    brr=[int(i) for i in input().split()]
    arr.sort()
    brr.sort()
    res="YES"
    for i in range(n):
        if arr[i]>brr[i]:
            res="NO"
    print(res)

for i in range(int(input())):
    phuHop()
