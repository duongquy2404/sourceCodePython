for j in range(1,int(input())+1):
    s1=input(); s2=input()
    if len(s1)==len(s2):
        dic1=dict(); dic2=dict()
        for i in range(0,len(s1)):
            if s1[i] in dic1:
                dic1[s1[i]]+=1
            else:
                dic1[s1[i]]=1
            if s2[i] in dic2:
                dic2[s2[i]]+=1
            else:
                dic2[s2[i]]=1
        check=True
        for i in dic1:
            if i not in dic2:
                check=False
                break
            if dic1[i]!=dic2[i]:
                check=False
                break
        print(f"Test {j}:",end=" ")
        if check:
            print("YES")
        else:
            print("NO")
    else:
        print(f"Test {j}:",end=" ")
        print("NO")