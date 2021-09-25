test=int(input())

while test>0:
    s=input()
    check=True
    sum=int(s[0])
    for i in range(1,len(s)):
        sum+=int(s[i])
        if abs(int(s[i-1])-int(s[i]))!=2:
            check=False
    if check==True and sum%10==0:
        print("YES")
    else:
        print("NO")
    test-=1