import math
n=int(input())
countSum=0
arrRow=[0]*n; arrCol=[0]*n
for i in range(n):
    s=input()
    for j in range(len(s)):
        if s[j]=='C':
            arrRow[i]+=1
            arrCol[j]+=1
for i in arrRow:
    if i>=2:countSum+=math.comb(i,2)
for i in arrCol:
    if i>=2: countSum+=math.comb(i,2)

print(countSum)