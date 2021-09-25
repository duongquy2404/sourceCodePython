test=int(input())

while test>0:
    s=input()
    s1=""
    sum=0
    for i in range(0,len(s)):
        if s[i]>='0' and s[i]<='9':
            sum+=int(s[i])
        else:
            s1=s1+s[i]
    lst=sorted(s1)
    temp=""
    for i in lst:
        temp=temp+i
    temp=temp+str(sum)
    print(temp)
    test-=1