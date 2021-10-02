n,m=[int(i) for i in input().split()]
lst=list(map(int,input().split()))
dic=dict()
count=0; countMax=0
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
    countMax=max(countMax,dic[i])
for i in dic:
    if count<=dic[i] and dic[i]<countMax:
        count=dic[i]
man=11
for i in lst:
    if count==dic[i]:
        man=min(man,i)
if man<11:
    print(man)
else:
    print("NONE")