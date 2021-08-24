##Ek program likho jo ki dictionaries ki values ko sort(ascending or descending) kar de

d={'bijender':45,'deepak':60,'param':20, 'anjili':30,'roshini':50}
empty={}
a=[]
for i in d.values():
    a.append(i)
for j in range(0,len(a)):
    for x in range(0, len(a)):
        if a[j]<a[x]:
            a[j],a[x]=a[x],a[j]
for y in a:
    for z in d.keys():
        if d[z]==y:
            empty[z]=y
print(empty)

