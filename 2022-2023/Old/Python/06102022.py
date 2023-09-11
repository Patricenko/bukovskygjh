import math
import functools
# sor ^ čisel - operacia, ak x sor x = 0, t.j a sor b sor c sor b sor c = a
# najvyssia mocnina - mame cislo v b. 111111110000 - teda / 10000 (prva jedna) a teda 4
# najvyssia mocnina vysledok = x & -x
# kolko moznosti ak n pocet schodov a mozem bud o 1 alebo 2
memo = {}
# @functools.cache #kesuje a zrychluje
def _sch(n):
    if n < 2 : return 1
    return sch(n-1) + sch(n-2)
def sch(*args):
    if args not in memo:
        memo[args] = _sch(*args)
    return memo[args]
def schfor(*args):
    __sch = [0,0,0,0]
    schfor(0) = 1
    schfor(1) = 1
    for i in range (2, n+1):
        __sch[i%4] = __sch((i-1)%4)+__sch((i-2)%4) # moze byt aj modulo 2, teda v [0,0] to da [1,1], potom [2,1], potom [2,3]....fibonnaci
n = input()
print(sch(int((n))))
print(sch[n%4])