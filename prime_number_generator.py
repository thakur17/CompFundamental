#This is the pyhton code editor
# find primes using a for-else construct
x=input("Enter number to check for the prime ")
n=int(x)
flag=0
for y in range (2, n):
    flag=0
    x_range = range(2, int(y/2))
    for z in x_range:
        if y % z == 0:
            break
        
        # loop fell through without finding a factor
    #if(flag==1):
    else:
        print(str(y)+" is a prime number")
 #   print(str(n)+" is a prime number")
#else:
 #   print(str(n)+" is not a prime number")
 #To understand how the code works is called TRACING.
