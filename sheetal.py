d={2:'red',1:'deepak',4:'param', 3:'anjili',5:'roshini'}
empty={}
a=[]
for i in d.values():
    a.append(i)
for j in range(0,len(a)):
    for x in range(0, len(a)):
        if a[j]<a[x]:
            a[j],a[x]=a[x],a[j]
for y in a:
    for z,l in d.items():
        if l==y:
            empty[z]=y
print(empty)
