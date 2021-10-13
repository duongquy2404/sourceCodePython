for i in range(int(input())):
    s1=input()
    s2=input()
    count=0
    i=0
    while i<=len(s1)-len(s2)+1:
        if s1[i:len(s2)+i]==s2:
            count+=1
            i+=len(s2)
        else:
            i+=1
    print(count)
