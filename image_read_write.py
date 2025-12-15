i1=open("assets/image.png","rb")
i2=open("assets/image_new1.png","wb")

for line in i1:
    i2.write(line)
i1.close()
i2.close()