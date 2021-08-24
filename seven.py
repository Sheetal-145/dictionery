# n= [ {"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# new=[]
# for i in n:
#     for value in i.values():
#         if value not in new:
#             new.append(value)
# print(new)


d=[{1:20, 2:30}]
d1=[{2:40, 5:50}]

n={}

for i in d:
    for j in d1:
        for x,y in i.items():
            for k,l in j.items():
                if x==k:
                    n[x]=i[x]+j[k]
                    break
                else:
                    n[x]=i[x]
                    n[k]=j[k]
print(n)

