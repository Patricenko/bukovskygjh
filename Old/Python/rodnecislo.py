from datetime import date
def neplatny():
    print('Rodne cislo je neplatne')
dnes = date.today()
d1 = dnes.strftime("%d/%m/%Y")
print("Dnesny datum: ", d1)
x = input('Rodne cislo: ')
rok = int('20'+x[0:2])
mesiac = int(x[2:4])
dnesmesiac = int(d1[3:5])
vek = 2022-rok
if mesiac > dnesmesiac:
    vek = vek-1
den = int(x[4:6])
if den > 31 or rok > 2022:
    neplatny()
elif 12 < mesiac < 50:
    neplatny()
elif mesiac > 72:
    neplatny()
else:
    pohlavie = 'error'
    if mesiac <= 12:
        pohlavie = 'muz'
    else:
        mesiac = mesiac-50
        pohlavie = 'zena'
    print(f'Datum narodenia: {den}.0{mesiac}.20{x[0:2]}')
    print (f'Pohlavie: {pohlavie}')
    print (f'Vek: {vek}')
