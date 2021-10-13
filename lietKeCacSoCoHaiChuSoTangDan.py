s=input()
st=set()
tmp=""
for i in range(0,len(s)-1,2):
    tmp=s[i]+s[i+1]
    st.add(int(tmp))
st=sorted(st)
for i in st:
    print(i,end=" ")