f = open('1001_1.txt','r')
x = 0
while f:
    l = f.readline()
    if l == '':
        break
    li = l.split(' ')
    meno = li[0]
    for i in range(1,len(li)):
        x += int(li[i])
    print(meno,x/int(len(li)-1))
    x = 0
f.close()
