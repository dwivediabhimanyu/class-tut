# Find the ABS value
def abs(n):
	if n<0:
		return(-n)
	else:
		return(n)

# Calculate the FACTORIAL
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Check if a number is EVEN or NOT
def even(n):
	if n % 2 == 0:
		return True
	else:
		return False


# Temperature Conversion
def cf(n):
	return (n*1.8)+32
def fc(n):
	return (n-32)/1.8

# Check Prime
def prime(num):
    if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               return False    
               break  
       else:  
           return True 
         
    else:  
       return False
