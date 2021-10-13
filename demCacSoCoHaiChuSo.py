s=input()
dic=dict()
tmp=""
for i in range(0,len(s)-1,2):
    tmp=s[i]
    tmp+=s[i+1]
    if tmp in dic:
        dic[tmp]+=1
    else:
        dic[tmp]=1
for i in dic:
    print(i,dic[i])