test=int(input())

while test>0:
    n=int(input())
    if n%10==6 and (n//10)%10==8:
        print("YES")
    else:
        print("NO")
    test-=1