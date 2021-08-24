a={'a':10, 'b':40, 'c':15}
b={'k':20, 'j':14, 'p':5}
for i in b.keys():
    for j in b.values():
        a[i]=b[i]
print(a)



