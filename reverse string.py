s1 = (input('enter string'))

l = 0

for ch in s1:
    l+=1

l = l-1

new_str = ""

while l>=0:

    new_str+=s1[l]
    l= l-1
print ('reverse string', new_str)



s2 = (input('enter your nmae'))

new_str2=""

for ch in s2:
    new_str2 = ch  + new_str2
print (new_str2)




