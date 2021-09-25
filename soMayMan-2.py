test=int(input())

while test>0:
    str=input()
    checkLucky=True

    for i in str:
        if i!='4' and i!='7':
            checkLucky=False

    if checkLucky==True:
        print("YES")
    else:
        print("NO")
    test-=1