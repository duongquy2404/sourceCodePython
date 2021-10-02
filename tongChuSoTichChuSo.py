for i in range(int(input())):
    s=input()
    sum=0; mul=1; check=False
    for i in range(0,len(s)):
        if i%2==0:
            sum+=int(s[i])
        else:
            if int(s[i])!=0:
                check=True
                mul*=int(s[i])
    if not check: mul=0
    print(sum,mul)
