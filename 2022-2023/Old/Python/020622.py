import os
def menu():
    l = input('Continue?: ')
    if l == 'y':
        funkcia()
def funkcia():
    x = input('Zadaj vetu: ')
    clear = lambda: os.system('cls')
    clear()
    listx = ['i','I','y','Y','í']
    for i in listx:
        if i == 'i':
            veta = x.replace(i,'-')
        else:
            veta = veta.replace(i,'-')
    print(f'\nVeta: {veta}')
    y = input('Zadaj spravne: ')
    print ('Riesenie: ')
    chyba = 0
    for p in range (len(x)):
        if x[p] == y[p]:
            print(f'{x[p]}', end='')
        else:
            print('!', end='')
            chyba += 1
    print(f'\nPocet chyb: {chyba}')
    menu()
funkcia()
exit()
