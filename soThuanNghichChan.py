def checkNumber(n):
    check=True
    s=str(n)
    if s!=s[::-1] or len(s)%2!=0:
        check=False
    else:
        while(n>0):
            if (n%10)%2!=0:
                check=False
                break
            n//=10
    return check

for i in range(int(input())):
    n=int(input())
    for i in range(22,n):
        if checkNumber(i):
            print(i,end=" ")
    print()