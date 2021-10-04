def mulNumber(n):
    mul=1
    while n>0:
        mul*=n%10
        n//=10
    return mul

for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    lst.sort(key=mulNumber)
    for i in lst:
        print(i,end=" ")
    print()