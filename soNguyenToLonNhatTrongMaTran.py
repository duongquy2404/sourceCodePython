import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

n,m=[int(i) for i in input().split()]
lst=list()
maxNT=-1
for i in range(n):
    lst_row=list(map(int,input().split()))
    for j in range(len(lst_row)):
        if checkNT(lst_row[j]):
            maxNT=max(maxNT,lst_row[j])
    lst.append(lst_row)

if maxNT==-1:
    print("NOT FOUND")
else:
    print(maxNT)
    for i in range(n):
        for j in range(m):
            if lst[i][j]==maxNT:
                print(f"Vi tri [{i}][{j}]")