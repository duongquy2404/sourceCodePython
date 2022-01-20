def rotate(s):
    sum=0
    for i in range(len(s)):
        sum+=int(ord(s[i])-ord('A'))
    sum%=26
    res=""
    for i in range(len(s)):
        n=int(sum+ord(s[i])-ord('A'))%26
        n+=65
        res+=chr(n)
    return res

def merge(s1,s2):
    res=""
    for i in range(len(s1)):
        n=int(ord(s1[i])+ord(s2[i])-2*ord('A'))%26
        n+=65
        res+=chr(n)
    return res

for i in range(int(input())):
    s=input()
    s1=s[0:len(s)//2]
    s2=s[len(s)//2:]
    print(merge(rotate(s1),rotate(s2)))