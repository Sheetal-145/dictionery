a={'a':10, 'b':40, 'c':15}
c={}
for i in a.keys():
    for j in a.values():
        if i!='b':
            c[i]=a[i]
print(c)
