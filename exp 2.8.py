print('enter numbers')
sum=0
c=0

while 1:
    num=int(input())
    c=c+1
    sum=sum+num
    print("press q if you want to exit or y tooo continue")
    m = input()
    if m =='q':
        break

print ('average',avg/c)
print("sum",sum)
