import math

def checkNT(n):
    if n<2: return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0: return False
    return True

n,m=[int(i) for i in input().split()]
arr=list()

for i in range(0,n):
    arr_row=list(map(int,input().split()))
    arr.append(arr_row)

for i in range(0,n):
    for j in range(0,m):
        if checkNT(arr[i][j]):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()

