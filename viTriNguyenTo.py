import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

for i in range(int(input())):
    s=input()
    check=True
    for i in range(0,len(s)):
        if (checkNT(i) and not checkNT(int(s[i]))) or (not checkNT(i) and checkNT(int(s[i]))):
            check=False
    if check:
        print("YES")
    else:
        print("NO")