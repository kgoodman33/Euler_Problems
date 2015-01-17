sequence = [1, 2]

i = 2
x = 0
sum = 2

while len(str(x)) <= 1000:
    sequence.append(sequence[i-1] + sequence[i-2])
    x = sequence[i]
    
    i += 1
    


print i - 1
   
    