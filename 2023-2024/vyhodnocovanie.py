import front_stack as fs
import re
priority = {'=' : 0, "+" : 1, "-" : 1, "x" : 2, "/" : 2, "^" : 3, "[" : 3}
def vyhodnot(entry):
    def hodnota(stackitem):
        if stackitem[1] == "=":
            return stackitem[0]
        if stackitem[1] in priority:
            return priority[stackitem[1]]
    def medzivypocet(a,b,value):
        if value == "^":
            return a**b
        if value == "/":
            return int(a/b)
        if value == "x":
            return a*b
        if value == "+":
            return a+b
        if value == "-":
            return a-b
    def vypocet(dvojice):
        if dvojice != None:
            stack = fs.TStack()
            stack.push(dvojice[0])
            for i in range(1,len(dvojice)):
                stack.push(dvojice[i])
                hodnota(dvojice[i])
                while stack.begin.next != None and hodnota(stack.begin.info[1]) <= hodnota(stack.begin.next.info[1]):
                    p1 = stack.pop()
                    p2 = stack.pop()
                    v = medzivypocet(int(p2[0]),int(p1[0]),p1[1])
                    stack.push((v,p1[1]))
    vypocet(re.findall(fr"([0-9]+)([{priority}])", entry))
    prvok = stack.pop()
    return prvok[0]

#print(vyhodnot(input()))
print(re.findall(fr"([0-9]+)([{priority}])", input()))

