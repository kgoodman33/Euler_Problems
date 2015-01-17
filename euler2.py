sequence = [1, 2]

i = 2
x = 0
sum = 2

while x < 4000000:
    sequence.append(sequence[i-1] + sequence[i-2])
    x = sequence[i]
    i += 1
    
    if x % 2 == 0:
        sum += x

print sum
   
    

