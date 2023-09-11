# dostaneme pole kompotov a ze kolko najviac kompotov vieme zjest - tak aby sme nezjedli dva susedne + vypis tie cisla
final = []
def fucking():
    pole = list(map(int,input().split()))
    for i in range (len(pole)):
        if i == 0 and pole[i+1] != pole[i]:
            final.append2 (pole[i])
            print(f'Appended {pole[i]} and start')
            continue
        elif i == len(pole) and pole[i-1] != pole[i]:
            final.append(pole[i])
            print(f'Appended {pole[i]} and final')
            continue
        else:
            try:
                if pole[i] != pole[i-1] and pole[i] != pole[i+1]:
                    final.append(pole[i])
                    print(f'Appended {pole[i]}')
            except:
                print('You muderfuker es ist outta range')
pole = list(map(int,input().split()))
for i in pole:
print (final)
