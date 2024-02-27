import random
def jeparne(a):
    if a % 2 == 0:
        return True
    else:
        return False


for i in range (10):
    cislo = random.randint(0,20)
    print(f'cislo {cislo} je parne', jeparne(cislo))

jeparne(int(input())

