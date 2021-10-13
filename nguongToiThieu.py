s=input()
dic=dict()
tmp=""
for i in range(0,len(s)-1,2):
    tmp=s[i]+s[i+1]
    if int(tmp) in dic:
        dic[int(tmp)]+=1
    else:
        dic[int(tmp)]=1
k=int(input())
check=False
for i in sorted(dic):
    if dic[i]>=k:
        print(i,dic[i])
        check=True

if not check:
    print("NOT FOUND")