def tichChuSo():
    s=str(input())
    res=1
    for i in range(0,len(s)):
        if int(s[i])!=0:
            res*=int(s[i])
    print(res)

for i in range(int(input())):
    tichChuSo()
