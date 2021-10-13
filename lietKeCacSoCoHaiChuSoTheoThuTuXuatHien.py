s=input()
st=set()
tmp=""
for i in range(0,len(s)-1,2):
    tmp=s[i]+s[i+1]
    if tmp not in st:
        print(tmp,end=" ")
    st.add(tmp)