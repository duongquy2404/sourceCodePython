import math

for i in range(int(input())):
    n,x,m=[float(i) for i in input().split()]
    print(math.ceil(math.log(m/n,x/100+1)))