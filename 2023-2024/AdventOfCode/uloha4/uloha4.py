f = open("input.txt","r")
l = f.readline()
# cast1
v = 0
c = 1
while l != "":
    v0 = -1
    x = l.split(":")
    my = x[1].strip().split("|")[1].split(" ")
    while ("" in my):
        my.remove("")
    win = x[1].strip().split("|")[0].split(" ")
    while ("" in win):
        win.remove("")
    print(my, win)
    for i in range(len(my)):
        if my[i] in win: v0 += 1
    if v0 != -1:
        v += 2**v0
        c += v0
    l = f.readline()
    print(v,c)