##OP{'red': 3, 'green': 5, 'black': 5, 'white': 5}

d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
n={}
for i in d.values():
    c=0
    for j in i:
        c+=1
    n[i]=c
print(n)
    


