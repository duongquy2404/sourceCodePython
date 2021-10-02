for i in range(int(input())):
    n=int(input())
    dic=dict()
    count=0
    res=0
    for i in range(n):
        x=int(input())
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
        if count<dic[x]:
            count=dic[x]
            res=x
    for i in dic:
        if dic[i]==count:
            res=min(res,i)
    print(res)
            