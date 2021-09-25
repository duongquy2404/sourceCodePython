test=int(input())

while test>0:
    str=input()
    checkNum=True
    for i in range(1,len(str)):
        if str[i]<str[i-1]:
            checkNum=False
    if checkNum==True:
        print("YES")
    else:
        print("NO")
    test-=1
