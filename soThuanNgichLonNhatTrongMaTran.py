def checkTN(n):
    if len(str(n))>=2 and str(n)==str(n)[::-1]:
        return True
    return False

n,m=[int(i) for i in input().split()]
lst=list()
maxTN=-1
for i in range(n):
    lst_row=list(map(int,input().split()))
    for j in range(len(lst_row)):
        if checkTN(lst_row[j]):
            maxTN=max(maxTN,lst_row[j])
    lst.append(lst_row)

if maxTN==-1:
    print("NOT FOUND")
else:
    print(maxTN)
    for i in range(n):
        for j in range(m):
            if lst[i][j]==maxTN:
                print(f"Vi tri [{i}][{j}]")