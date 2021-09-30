while True:
    n=int(input())
    if n==0: break
    lst=[]
    for i in range(n):
        lst.append(int(input()))
    minLst=min(lst); maxLst=max(lst)
    if minLst!=maxLst:
        print(minLst,maxLst)
    else:
        print("BANG NHAU")