f1=open("assets/myData","r")
f2=open("assets/copiedData","w")
line=f1.readline()
while line:
    line=f1.readline()
    f2.write(line)

f1.close()
f2.close()

