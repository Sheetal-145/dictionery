# Python program to get the maximum and minimum value in a dictionary

my_dict={'a':90,'b':5,'c':560,'d':40,'e':10,'f':20}
max=0
for i in my_dict.values():
    if i>max:
        max=i
min=i
for j in my_dict.values():
    if j<min:
        min=j
print(min)
print(max)




    

