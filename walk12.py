import os
resp =os.walk("C:\\Ravana\\Test")
d1 ={}
i = 0
for r,d,f in resp:
    for file in r:
        if file in d1:
            file = file +"|"+str(i)
            i = i+1
        d1[file] =r
print(d1)
file_name = input("Enter the file name ")
for k,v in d1.items():
    if file_name.lower() in k.lower() :
        print (k.split("|")[0],":", v)
