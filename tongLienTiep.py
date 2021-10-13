for i in range(int(input())):
    n=int(input())
    count=0; l=1
    while l*(l+1)<2*n:
        a = (n - l * (l + 1) / 2) / (l + 1)
        if a - int(a) == 0.0:
            count+=1
        l+=1
    print(count)