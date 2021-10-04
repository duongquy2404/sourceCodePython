s=input()
s1="6"; s2="68"; s3="688"
check=True
checkSix=False
tmp=""
for i in range(len(s)-1,-1,-1):
    if s[i]=='8':
        tmp=s[i]+tmp
    elif s[i]=='6':
        checkSix=True
        tmp=s[i]+tmp
        if tmp!='6' and tmp!='68' and tmp!='688':
            check=False
            break
        tmp=""
    else:
        check=False
        break

if check and checkSix:
    print("YES")
else:
    print("NO")