s=input()
count=0
while len(s)!=1:
    n=0
    if s[0]=='-':
        n+=ord('-')-ord('0')
    else:
        n+=int(s[0])
    for i in range(1,len(s)):
            n+=int(s[i])
    s=str(n)
    count+=1

print(count)