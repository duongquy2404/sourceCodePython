test=(int)(input())

while test>0:
    sum=0
    s=input()
    for i in s:
        sum+=int(i)
    if sum%3==0:
        print("YES")
    else:
        print("NO")
    test-=1
