import time
f = open('zadanie6.txt','r')
listicek = []
fl = []
x = 0
l = list(f.readline())
#for i in range(len(l)-3):
#    if not l[i] in fl:
#        fl.append(l[i])
#    else:
#        fl = []
#    if len(fl) == 4:
#        print(fl)
#        print(i)
#        break
for x in range(14, len(l)):
    if len(set(l[x - 14:x])) == 14:
        print(x)
        exit(0)
    



    
                

