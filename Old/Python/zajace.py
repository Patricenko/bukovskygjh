x = input()
zajac = control = l = 0
od = do = -1
for i in range(0,len(x)):
    if x[i] == 'U' and od >= 0:
        do = i
        l = do-od
    elif x[i] == 'U':
        od = i
for i in range(0,len(x)):
    if x[i] == 'U' and i == control+l:
        zajac += 1
    elif x[i] == 'U':
        control = i
print (zajac)

    
