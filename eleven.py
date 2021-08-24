my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
a=[]
for value in my_dict.values():
    a.append(value)
i=0
e=[]
while i<len(a):
    j=0
    while j<len(a):
        if a[j]>a[i]:
            if a[j] not in e:
                e.append(a[j])
        j+=1
    break    
    i+=1
print(e)


        
