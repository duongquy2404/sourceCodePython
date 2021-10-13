n=int(input())
lst=list(map(int,input().split()))
stepMin=2000000
step=0
value=-1
for i in range(len(lst)):
    step=0
    for j in range(len(lst)):
        if i!=j:
            step+=abs(lst[i]-lst[j])
    if step<stepMin:
        stepMin=step
        value=lst[i]

print(stepMin,value)