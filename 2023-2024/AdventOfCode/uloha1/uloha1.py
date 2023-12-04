import re
f = open("input.txt", "r")
l =  f.readline()
v = 0
while l != "":
    p=[]
    l = l.replace("zero", "0")
    l = l.replace("one", "1")
    l = l.replace("two", "2")
    l = l.replace("three", "3")
    l = l.replace("four", "4")
    l = l.replace("five", "5")
    l = l.replace("six", "6")
    l = l.replace("seven", "7")
    l = l.replace("eight", "8")
    l = l.replace("nine", "9")
    x = list(l)
    for i in x:
        if i.isnumeric():
            p.append(int(i))
    if len(p) == 1:
        v += p[0]
        print(x, p[0])
    else: v += 10*p[0]+p[-1]; print(x, 10*p[0]+p[-1])
    l = f.readline()
print(v)

f.close()