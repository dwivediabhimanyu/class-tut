# Find HCF
def hcf(x, y):  
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i  
   return hcf  


# Find LCM
def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm