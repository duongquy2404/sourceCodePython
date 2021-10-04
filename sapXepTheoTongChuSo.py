def sumNumber(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum

for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    lst.sort(key=sumNumber)
    for i in lst:
        print(i,end=" ")
    print()