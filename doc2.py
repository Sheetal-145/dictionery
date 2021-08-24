a='w3resource'
d={}
i=0
while i<len(a):
    c=0
    j=0
    while j<len(a):
        if a[i]==a[j]:
            c+=1
        j+=1
    if a[i] not in d:
        d[a[i]]=c
    i+=1
print(d)


    