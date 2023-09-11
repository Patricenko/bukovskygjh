x = input('String or ascii(0/1): ')
p = input('Entry: ')
def string():
    global p
    for i in range (len(x)):
        print(ord(x[i]), end = ' ')
def ascii():
    global p
    for i in range (len(x)):
        print(chr(x[i]), end = ' ')
    
    
