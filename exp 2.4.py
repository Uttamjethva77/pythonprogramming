a = int(input("Enter a number: "))  
  
if a > 1:  
   for b in range(2,a):  
       if (a % b) == 0:  
           print(a,"is not a prime number")  
           print(b,"times",a//b,"is",a)  
           break  
   else:  
       print(a,"is a prime number")  
         
else:  
   print(b,"is not a prime number")  
