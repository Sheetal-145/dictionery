name=input("enter a name: ")
d={}
i=0
while i<len(name):
    d[name[i]]=i
    i+=1
print(d)
