d1 = {'a': 300, 'b': 200, 'c':300}
d2 = {'a': 200, 'b': 200, 'd':400}
d={}
for i in d1:
    for x in d2:
        if x in d1:
            d[i]=d1[i]+d2[x]
        elif i not in d2:
            d[i]=d1[i]
            d[x]=d2[x]
print(d)
