f = open('zadanie4.txt','r')
l = f.readline()
win = riadok = 0
struct1 = []
struct2 = []
while l != '':
    struct1 = []
    struct2 = []
    riadok += 1
    l = l.replace('-',' ')
    l = l.replace(',',' ')
    line = l.split(' ')
    for i in range (int(line[0]),int(line[1])+1):
        struct1.append(i)
    for i in range (int(line[2]),int(line[3])+1):
        struct2.append(i)
    for i in struct1:
        if i in struct2:
            win += 1
            print(win)
            break
    l = f.readline()
print(win)
