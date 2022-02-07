#write a programme to remove duplicates from a list

a=[1,3,3,2,2,4,6,5,5,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)

print('after removing duplicates entry',b)
