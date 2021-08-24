# dic = {'Alex': [1, 2, 3], 'David': [2, 2]}
# c=0
# sum=0
# for key in dic:
#     i=0
#     while i<len(dic[key]):
#         sum+=(dic[key][i])
#         i+=1
#         c+=1
# print(sum)
# print(c)

dic = {'Alex': [1, 2, 3], 'David': [2, 2]}
c=0
for i in dic.values():
    for j in i:
        c+=1
print(c)
