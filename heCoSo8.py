s=input()
if len(s)%3==1: s="00"+s
if len(s)%3==2: s="0"+s
res=""; tmp=""
for i in range(len(s)):
    if i%3==2:
        tmp+=s[i]
        if tmp=="000": res+='0'
        elif tmp=="001": res+='1'
        elif tmp=="010": res+='2'
        elif tmp=="011": res+='3'
        elif tmp=="100": res+='4'
        elif tmp=="101": res+='5'
        elif tmp=="110": res+='6'
        elif tmp=="111": res+='7'
        tmp=""
    else:
        tmp+=s[i]
print(res)