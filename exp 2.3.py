a = int (input("enter a number"))
print ("divisors of given number is")
for b in range(1,a+1):
    if (a%b==0):
        print(b)
