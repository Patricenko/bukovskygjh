import random
def plus():
    global x, malep, velkep, symbolyp, male, velke, symboly, cisla, cislap
    if 97 <= x <= 122:
        malep += 1
    elif 65 <= x <= 90:
        velkep += 1
    elif 32 <= x <= 46 or 58 <= x <= 64 or 91 <= x <= 96 or 123 <= x <= 126:
        symbolyp += 1
    elif 48 <= x <= 57:
        cislap += 1
    print(chr(x), end='')
def loop():
    global x, malep, velkep, symbolyp, male, velke, symboly, cisla, cislap
    x = random.randint(32,127)
    if velkep == velke and 65 <= x <= 90:
        loop()
    elif malep == male and 97 <= x <= 122:
        loop()
    elif symbolyp == symboly and 32 <= x <= 47:
        loop()
    elif symbolyp == symboly and 58 <= x <= 64:
        loop()
    elif symbolyp == symboly and 91 <= x <= 96:
        loop()
    elif symbolyp == symboly and 123 <= x <= 126:
        loop()
    elif cislap == cisla and 48 <= x <= 57:
        loop()
    else:
        plus()
def volitelne():
    global x, malep, velkep, symbolyp, male, velke, symboly, cisla, cislap
    velke = int(input('Pocet velkych pismen: '))
    male = int(input('Pocet malych pismen: '))
    symboly = int(input('Pocet symbolov: '))
    cisla = int(input('Pocet cisiel: '))
    velkep = malep = symbolyp = cislap = x = 0
    for i in range (0,velke+male+symboly+cisla,1):
        loop()
def generuj():
    pocet = int(input('Pocet znakov hesla: '))
    for i in range (0,pocet,1):
        p = random.randint(32,127)
        print(chr(p), end='')
otazka = int(input('Podla poctu znakov: 0\nVolitelny pocet znakov: 1\nVyber: '))
if otazka == 1:
    volitelne()
else:
    generuj()
