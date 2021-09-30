import math

for i in range(int(input())):
    n=int(input())
    s=int(str(n)[::-1])
    if math.gcd(n,s)==1:
        print("YES")
    else:
        print("NO")