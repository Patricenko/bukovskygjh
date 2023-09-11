import tkinter
f = open('100102.txt','r')
c = tkinter.Canvas(width=701, height=701)
while f:
    l = f.readline()
    if l == '':
        break
    li = l.split(' ')
    kof = int(li[3])/10000
    c.create_oval(int(li[0]),int(li[1]),int(li[0])+kof,int(li[1])+kof,fill = 'yellow')
    c.create_text(int(li[0])+kof/2,int(li[1])-10,text = li[2], font = 'Arial 10 bold')
f.close()
c.pack()
c.mainloop()
