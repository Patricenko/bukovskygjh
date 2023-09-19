from random import *
import time
def generuj_zamiesane_1(od, do): # O(2n)
    z = []
    for i in range(od, do + 1):
        z.append(i)
    for i in range(len(z)):
        j = randrange(len(z))
        z[i], z[j] = z[j], z[i]
    return z

def generuj_zamiesane_2(od, do): # O(nekonecno)
    z = []
    cislo = randrange(od, do + 1)
    for i in range(od, do + 1):
        while cislo in z:
            cislo = randrange(od, do + 1)
        z.append(cislo)
    return z

def zamiesaj_3(zoznam):
    if zoznam == []:
        return []
    return [zoznam.pop(randrange(len(zoznam)))] + zamiesaj_3(zoznam)

def generuj_zamiesane_3(od, do): # O(n2)
    z = []
    for i in range(od, do + 1):
        z.append(i)
    return zamiesaj_3(z)

def vyzrebuj_4(od, do, zoznam):
    cislo = randrange(od, do + 1)
    if cislo in zoznam:
        return vyzrebuj_4(od, do, zoznam)
    return cislo

def generuj_zamiesane_4(od, do):
    z = []
    cislo = randrange(od, do + 1)
    for i in range(od, do + 1):
        z.append(vyzrebuj_4(od, do, z))
    return z

def zamiesaj_5(zoznam):
    if len(zoznam) <= 1:
        return zoznam
    polovica = len(zoznam) // 2
    if randrange(2) == 0:
        return zamiesaj_5(zoznam[:polovica]) + zamiesaj_5(zoznam[polovica:])
    else :
        return zamiesaj_5(zoznam[polovica:]) + zamiesaj_5(zoznam[:polovica])

def generuj_zamiesane_5(od, do):
    z = []
    for i in range(od, do + 1):
        z.append(i)
    return zamiesaj_5(z)

start_time = time.time()
z1 = generuj_zamiesane_1(10, 990)
print("1. --- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
z2 = generuj_zamiesane_2(10, 990)
print("2. --- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
z3 = generuj_zamiesane_3(10, 990)
print("3. --- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
z4 = generuj_zamiesane_4(10, 990)
print("4. --- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
z5 = generuj_zamiesane_5(10, 990)
print("5. --- %s seconds ---" % (time.time() - start_time))
