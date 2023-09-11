x = input()
active = phase = stop = zajac = 0
i0 = check = -1
def funkcia():
    global active, phase, i0, check, zajac, stop
    for i in range (0, len(x)):
        if x[i] == "U" and phase == 0 and active == 0:
            active = 1
            i0 = i
        elif x[i] == "U" and phase == 0 and active == 1:
            check = i-i0
            phase = 1
            active = 0
            funkcia()
            break
        elif x[i] == "U" and phase == 1 and active == 1 and i == stop+check:
            zajac += 1
            active = 0
            stop = 0
        elif x[i] == "U" and phase == 1 and active == 0:
            active = 1
            stop = i
        elif x[i] == "U" and phase == 1 and active == 1 and i != stop+check:
            zajac = -1
            break
funkcia()
print (zajac)
