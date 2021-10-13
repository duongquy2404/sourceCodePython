for i in range(int(input())):
    n,p=[int(i) for i in input().split()]
    x=0
    while n:
        n//=p
        x+=n
    print(x)