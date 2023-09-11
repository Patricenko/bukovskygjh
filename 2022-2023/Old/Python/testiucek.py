def nasobenie():
    global x, a
    print(x*a)



x = int(input())
a = int(input())
if x == a:
    print('Su rovnake')
elif x > a:
    print('Prve je vacsie')
elif x < a:
    print('Druhe je vacsie')
nasobenie()
