x = (input('Word: '))
k = int(input('Koeficient: '))
p = ('Code/Uncode(0/1): ')
for i in range(len(x)):
    if p == 0:
        print(chr(ord(x[i])+k), end='')
    else:
        print(chr(ord(x[i])-k), end='')    
    
