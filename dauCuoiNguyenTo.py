import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

for i in range(int(input())):
    s=input()
    tmp1=s[len(s)-3:]
    n1=int(tmp1)
    tmp2=s[:3]
    n2=int(tmp2)
    if checkNT(n1) and checkNT(n2):
        print("YES")
    else:
        print("NO")