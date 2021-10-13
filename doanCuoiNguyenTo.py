import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

for i in range(int(input())):
    s=input()
    tmp=s[len(s)-4:]
    n=int(tmp)
    if checkNT(n):
        print("YES")
    else:
        print("NO")