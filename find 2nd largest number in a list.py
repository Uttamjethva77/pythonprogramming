#find 2nd largest number in a list

l = [10, 20, 4, 45, 99]
  
l.sort()
  
print("2nd largest is:", l[-2])

#2nd trick

a = []

b = int(input("Please enter the Total Number you Want in list "))
for i in range(1, b + 1):
    c = int(input("Please enter the Value of %d Element : " %i))
    a.append(c)

for i in range (b):
    for j in range(i + 1, b):
        if(a[i] > a[j]):
            d = a[i]
            a[i] = a[j]
            a[j] = d


print("2nd largest is ", a[-2])
