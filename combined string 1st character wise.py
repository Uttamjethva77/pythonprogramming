a1=0
a2=0
b=input('enter 1st string')
for ch in b:
    a1+=1
c=input('enter 2nd string')
for ch in c:
    a2+=1

i=0
final=""

mi = a1
if a2 < a1:
    mi = a2

while i < mi:
    final = final + b[i] + c[i]
    i = i+1

if a1>a2:
    while i < a1:
        final = final + b[i]
        i = i+1

else:
    while i < a2:
        final = final + c[i]
        i = i+1
    
print("combined string is",final)
