#write a python program to multiply all the item in the list..
b = [2, 3, 'a',4]
c = 1

for f in b:
    if isinstance(f,int) or f.isdigit():
        c *= int(f)


print('multiply=',c)



