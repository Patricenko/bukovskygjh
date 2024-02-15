p1 = open("seedtosoil", "r")
p2 = open("soiltofer", "r")
p3 = open("fertowater", "r")
p4 = open("watertolight", "r")
p5 = open("lighttotemp", "r")
p6 = open("temptohum", "r")
p7 = open("humtoloc", "r")
p1x = []
p2x = []
p3x = []
p4x = []
p5x = []
p6x = []
p7x = []
seeds = [432986705,28073546,1364097901,88338513,2733524843,234912494,3151642679,224376393,485709676,344068331,1560394266,911616092,3819746175,87998136,892394515,435690182,4218056486,23868437,848725444,8940450]
l = p1.readline()
while l != "": p1x.append(l.strip().split()); l = p1.readline()
l = p2.readline()
while l != "": p2x.append(l.strip().split()); l = p2.readline()
l = p3.readline()
while l != "": p3x.append(l.strip().split()); l = p3.readline()
l = p4.readline()
while l != "": p4x.append(l.strip().split()); l = p4.readline()
l = p5.readline()
while l != "": p5x.append(l.strip().split()); l = p5.readline()
l = p6.readline()
while l != "": p6x.append(l.strip().split()); l = p6.readline()
l = p7.readline()
while l != "": p7x.append(l.strip().split()); l = p7.readline()
p1.close();p2.close();p3.close();p4.close();p5.close();p6.close();p7.close()
soil = []
fer = []
water = []
light = []
temp = []
hum = []
loc = []
for a in range (len(seeds)):
    for b in range(len(p1x)):
        if p1x[b][0] <= seeds[a] < p1x[b][0]+p1x[b][2]:
            cursoil = int(p1x[b][1])+int(p1x[b][2])+(int(p1x[b][1]) - int(p1x[b][0]))
        else: break
        for c in range(len(p2x)):
            if p2x[c][0] <= cursoil < p2x[c][0] + p2x[c][2]:
                curfer = int(p2x[c][1]) + int(p2x[c][2]) + (int(p2x[c][1]) - int(p2x[c][0]))
            else:
                break
            for d in range(len(p3x)):
                if p3x[d][0] <= curfer < p3x[d][0] + p3x[d][2]:
                    curwater = int(p3x[d][1]) + int(p3x[d][2]) + (int(p3x[d][1]) - int(p3x[d][0]))
                else:
                    break
                for e in range(len(p4x)):
                    if p4x[e][0] <= curwater < p4x[e][0] + p4x[e][2]:
                        curlight = int(p4x[e][1]) + int(p4x[e][2]) + (int(p4x[e][1]) - int(p4x[e][0]))
                    else:
                        break
                    for f in range(len(p5x)):
                        if p5x[f][0] <= curlight < p5x[f][0] + p5x[f][2]:
                            curtemp = int(p5x[f][1]) + int(p5x[f][2]) + (int(p5x[f][1]) - int(p5x[f][0]))
                        else:
                            break
                        for g in range(len(p6x)):
                            if p6x[g][0] <= cursoil < p6x[g][0] + p6x[g][2]:
                                curhum = int(p6x[g][1]) + int(p6x[g][2]) + (int(p6x[g][1]) - int(p6x[g][0]))
                            else:
                                break
                            for h in range(len(p7x)):
                                if p7x[h][0] <= curhum < p7x[h][0] + p7x[h][2]:
                                    curloc = int(p7x[h][1]) + int(p7x[h][2]) + (int(p7x[h][1]) - int(p7x[h][0]))
                                    loc.append(curloc)
                                else:
                                    break

print(min(loc))
