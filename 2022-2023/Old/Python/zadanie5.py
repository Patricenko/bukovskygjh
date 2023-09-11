import time
f = open('zadanie5.txt','r')
l = f.readline().replace('move ','').replace('from ','').replace('to ','').replace('[','').replace('] ','').replace('move ','').replace('    ',' ')
boxes = [[],[],[],[],[],[],[],[],[]]
while l  != '':
    if l[0] == '.':
        for i in range (1,len(l)-1):
            if l[i] != ' ':
                boxes[i-1].append(l[i])
    elif l[0] == "&":
        for i in range (len(boxes)):
            boxes[i].reverse()
    else:
        #print(boxes)
        listicek = l.replace('\n','').split(' ')
        for i in range (int(listicek[0]),0,-1):
            boxes[int(listicek[2])-1].append(boxes[int(listicek[1])-1][len(boxes[int(listicek[1])-1])-i])
            boxes[int(listicek[1])-1].pop(len(boxes[int(listicek[1])-1])-i)
        #print(boxes)
        #for i in range (int(listicek[0])):
        #    boxes[int(listicek[2])-1].append(boxes[int(listicek[1])-1][len(boxes[int(listicek[1])-1])-1])
        #    boxes[int(listicek[1])-1].pop()
    l = f.readline().replace('move ','').replace('from ','').replace('to ','').replace('[','').replace('] ','').replace('move ','').replace('    ',' ')
for i in range(len(boxes)):
    print(boxes[i][len(boxes[i])-1], end = '')