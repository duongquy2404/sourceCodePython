import math

def sumNumber(s):
    sum=0
    for i in s:
        sum+=int(i)
    return sum

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

for i in range(int(input())):
    check=True
    s=input()
    for i in s:
        if int(i)%2==0:
            if s.index(i)%2!=0:
                check=False
                break
        else:
            if s.index(i)%2==0:
                check=False
                break
    if check and checkNT(sumNumber(s)):
        print("YES")
    else:
        print("NO")