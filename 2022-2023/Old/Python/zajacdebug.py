x = input()
od = do = active = -1
zajac = control = l = 0   
def funkcia():
    global x, zajac, control, l, active
    for i in range(0,len(x)):
        if x[i] == 'U' and i == control+l and active == 1:
            zajac += 1
            active = -1
        elif x[i] == 'U' and i != control+l and active == 1:
            zajac = -1
            break
        elif x[i] == 'U':
            active = 1
            control = i
    print (zajac)
for i in range(0,len(x)):
    if x[i] == 'U' and od >= 0:
        do = i
        l = do-od
        funkcia()
        break
    elif x[i] == 'U':
        od = i
        
