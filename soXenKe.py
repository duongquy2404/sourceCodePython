for i in range(int(input())):
    s=input()
    check=True
    if len(s)%2!=0:
        if s[0]!=s[1]:
            tmp=s[0]
            for i in range(2,len(s),2):
                if tmp!=s[i]:
                    check=False
        else:
            check=False
    else:
        check=False
    if check:
        print("YES")
    else:
        print("NO")