n,m=[int(i) for i in input().split()]
lst=list()
minLst=1000000
maxLst=-1000000
check=False
for i in range(n):
    lst_row=list(map(int,input().split()))
    minLst=min(minLst,min(lst_row))
    maxLst=max(maxLst,max(lst_row))
    lst.append(lst_row)

luckyLst=maxLst-minLst
for i in range(n):
        for j in range(m):
            if lst[i][j]==luckyLst:
                check=True
if not check:
    print("NOT FOUND")
else:
    print(luckyLst)
    for i in range(n):
        for j in range(m):
            if lst[i][j]==luckyLst:
                check=True
                print(f"Vi tri [{i}][{j}]")