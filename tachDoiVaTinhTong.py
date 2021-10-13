s=input()
while len(s)>1:
    a=s[:len(s)//2]
    b=s[len(s)//2:]
    s=str(int(a)+int(b))
    print(s)