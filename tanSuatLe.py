def tanSuatLe():
    n=int(input())
    lst=[int(i) for i in input().split()]
    dic={}
    for i in lst:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in dic:
        if dic[i]%2!=0:
            print(i)
            break

for i in range(int(input())):
    tanSuatLe()
    