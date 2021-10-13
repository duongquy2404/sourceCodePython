lst=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(int(input())):
    n,b=[int(i) for i in input().split()]
    res=""
    while(n>0):
        res=lst[n%b]+res
        n//=b
    print(res)