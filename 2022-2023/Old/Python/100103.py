import tkinter
f = open('100102.txt', 'r')
c = tkinter.Canvas(width=701, height=701)
while f:
    l = f.readline()
    if l == '':
        break
    li = l.split(' ')
    match li[0]:
        case 'o':
            c.create_oval(int(li[1]),int(li[2]),int(li[3]),int(li[1=4]),fill = li[5])
            pass
        case 'r':
            c.create_recatngle(int(li[1]),int(li[2]),int(li[3]),int(li[4]),fill = li[5])
            pass
        case 'p':
            pass
        case 'l':
            c.create_line(int(li[1]),int(li[2]),font = 'Arial 10 bold')
            pass
f.close()
c.pack()
c.mainloop()
