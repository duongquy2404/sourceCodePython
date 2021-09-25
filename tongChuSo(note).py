n=int(input())
count=0

def sum_number(n):
    sum=0
    while n!=0:
        sum+=n%10
        n//=10
    return sum

while n>9:
    n=sum_number(n)
    count+=1

print(count)
