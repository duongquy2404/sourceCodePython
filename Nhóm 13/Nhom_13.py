import re

filename1 = "Student_code_N07.csv"
with open(filename1) as file1:
    reader = file1.readlines()
l1=[]
for line in reader:
    l1.append(line[0:10:1])
list_students = dict()
with open("meeting_saved_chat_13.txt", encoding= "UTF-8") as read_text:
    for i in read_text:
        i=i.upper()
        line=re.split("\s", i)
        tmp = re.findall("B[0-9]{2}[A-Z]{4}[0-9]{3}",i)
        if len(tmp)==2 and len(set(tmp))==1:
            list_students[tmp[0]]= line[0]
listmsv = []
for k in list_students.keys():
    listmsv.append(k)
listtime = []
for v in list_students.values():
    listtime.append(v)
with open("VANG.csv", 'w') as file3:
    for i in range(1, len(l1)):
        if l1[i] not in listmsv:
            file3.write(l1[i]+"\n")
with open("MUON.txt", 'w') as file4:
    for i in range(0, len(listtime)):
        if listtime[i] > "14:50:00":
            file4.write(listmsv[i]+"\n")