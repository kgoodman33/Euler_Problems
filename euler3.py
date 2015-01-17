



number = 600851475143
numbers = []

primes = []
i = 0

while i < (number - 1):
    i += 1
    if (number % i == 0):
        numbers.append(i)



testing = []

for x in numbers:
    z = 2
    while z < number:
              
        if (x % z == 0) and (x != z): 
            break
        z += 1
        
    else:
        primes.append(x)   
        
        
       
            
        
        
        
        
print primes.pop()