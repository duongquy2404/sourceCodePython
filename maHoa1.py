def maHoa():
    s=input()
    count=1
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            print(count,s[i],sep='',end='')
            count=1
    print(count,s[len(s)-1],sep='',end='')
    print()

for i in range(int(input())):
    maHoa()