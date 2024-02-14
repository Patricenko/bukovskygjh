import math
def toBinary(num):
    return bin(num)

def binary():
    f = open("sifra.txt","r")
    w = open("vysledok.txt", "a")
    l = f.readlines()
    for i in l:
        i = i.strip()
        w.write(toBinary(int(i)).strip("b") + "\n")
    w.close()
    return w

def find_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

number = int(input("Enter a number: "))
prime_factors = find_prime_factors(number)
print(f"The prime factors of {number} are {prime_factors}.")
