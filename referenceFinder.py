f = open("word.txt", encoding='utf-8')
content = f.read()
#print(content)
found = False
temp =""
set = {"REFERENCIAS"}
for a in content:
    if(a=="("):
        found=True
        temp=temp+a
        #print(a)
    elif(a==")"):
        found=False
        temp=temp+a
        set.add(temp)
        temp=""
        #print(a+"\n")
    elif(found):
        temp = temp +a
        #print(a)

#print(set)
f2 = open("result.txt", "w")
for a in set:
    f2.write(a+"\n")
    