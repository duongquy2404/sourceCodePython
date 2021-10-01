import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

for i in range(int(input())):
    s=input()
    countNT=0
    check=True
    if checkNT(len(s)):
        for i in range(0,len(s)):
            if checkNT(int(s[i])):
                countNT+=1
        if countNT<=len(s)/2:
            check=False
    else:
        check=False
    if check:
        print("YES")
    else:
        print("NO")
