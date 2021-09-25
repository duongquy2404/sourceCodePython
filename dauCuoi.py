test=int(input())

while test>0:
    s=input()
    if s[0]==s[-2] and s[1]==s[-1]:
        print("YES")
    else:
        print("NO")
    test-=1