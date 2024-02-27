import front_stack as fs
import re
priority = {"=": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
def vyhodnot(entry):
    def oddel(entry):
        if entry[0] == "-": entry = "0" + entry
        elif entry[0] == "+": entry = "0" + entry
        if "(" and ")" in entry:
            x1 = entry.find("(")
            x2 = entry.find(")")
            r = vyhodnot(entry[x1 + 1:x2] + "=")
            if r == None: pass
            else: entry = entry[:x1] + r + entry[(x2 + 1):]
        pairs = []
        npairs = 0
        h = ""
        #pairs = [[item for item in group] for group in re.findall(fr'([0-9]+)([{priority}])', entry)]
        for i in range(len(entry)):
            if entry[i].isdigit(): h += entry[i]
            elif entry[i] in priority:
                pairs.append([h])
                h = ""
                pairs[npairs].append(entry[i])
                npairs += 1
        #print(pairs)
        stack.push(pairs[0])
        for i in range(1, len(pairs)):
            x = (vypocitaj(pairs[i]))
            if x != None: return (x)
    def medzikrok(x1, x2, first, second):
        if first == "+": return (vypocitaj([str(x1 + x2), second]))
        if first == "-": return (vypocitaj([str(x1 - x2), second]))
        if first == "*": return (vypocitaj([str(x1 * x2), second]))
        if first == "/": return (vypocitaj([str(x1 // x2), second]))
        if first == "^": return (vypocitaj([str(x1 ** x2), second]))
    def vypocitaj(Num):
        stack.push(Num)
        cislo2 = stack.pop()
        if cislo2[1] == "=":
            if stack.is_empty() == False:
                cislo1 = stack.pop()
                if cislo1 != None:
                    if priority[cislo1[1]] >= priority[cislo2[1]]:
                        return ((medzikrok(int(cislo1[0]), int(cislo2[0]), cislo1[1], cislo2[1])))
                else: stack.push(cislo2)
            else: return (cislo2[0])
        else:
            cislo1 = stack.pop()
            if cislo1 != None:
                if priority[cislo1[1]] >= priority[cislo2[1]]:
                    return (medzikrok(int(cislo1[0]), int(cislo2[0]), cislo1[1], cislo2[1]))
                else: stack.push(cislo1); stack.push(cislo2)
            else: stack.push(cislo2)
    return (oddel(entry))
def calc(entry):
    stack = fs.Tstack()
    return vyhodnot(entry)