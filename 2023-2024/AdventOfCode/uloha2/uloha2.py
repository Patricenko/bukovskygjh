def cast1():
    f = open("input.txt", "r")
    l = f.readline()
    v = 0
    v2 = 0
    while l != "":
        active = 0
        sets = []
        set = []
        red = []
        green = []
        blue = []
        l = l.strip()
        l = l.replace(" ","")
        l = l.replace("green", "*g")
        l = l.replace("red", "*r")
        l = l.replace("blue", "*b")
        list = l.split(":")
        id = int(list[0][4:])
        sets = list[1].split(";")
        for i in sets:
            set.append(i.split(","))
        for k in set:
            for j in k:
                j = j.split("*")
                if j[1] == "r" and int(j[0]) > 12: active = 1
                elif j[1] == "g" and int(j[0]) > 13: active = 1
                elif j[1] == "b" and int(j[0]) > 14: active = 1
                if j[1] == "r": red.append(int(j[0]))
                elif j[1] == "g": green.append(int(j[0]))
                elif j[1] == "b": blue.append(int(j[0]))
        print(id, set, active)
        if active == 0:
            v += id
        print(red, green, blue, max(red)*max(green)*max(blue))
        v2 += max(red)*max(green)*max(blue)
        l = f.readline()
    f.close()
    print(v, v2)
cast1()