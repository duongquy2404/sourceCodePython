def xuatHien():
    dic={}
    n=int(input())
    lst=[int(i) for i in input().split()]
    check=False
    for i in lst:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in dic:
        if dic[i]>n//2:
            check=True
            print(i)
            break
    if check==False:
        print("NO")

for i in range(int(input())):
    xuatHien()
