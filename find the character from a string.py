a = input("enter your name")
b = input("enter character")

res = None
for i in range(0, len(a)):
    if a[i] == b:
        res = i + 1
        break
     
if res == None:
    print ("No such character available in string")
else:
    print ("Character {} is present at {}".format(b, str(res)))
