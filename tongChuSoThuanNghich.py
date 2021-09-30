def sumNumber(s):
    sum=0
    for i in s:
        sum+=int(i)
    return sum

def checkReverse(s):
    if s==s[::-1]:
        return True
    return False

for i in range(int(input())):
    s=input()
    if sumNumber(s)>9 and checkReverse(str(sumNumber(s)))==True:
        print("YES")
    else:
        print("NO")   