a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
n={}
for i in range(0, len(b)):
    for j in range(0, len(c)):
        n[b[i]]=c[j]
print(n)

