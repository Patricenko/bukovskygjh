import tkinter
c = tkinter.Canvas(width=1000, height=1000)
c.pack()

l = []
overall_score = 0
with open('input.txt','r') as f:
    count = int(f.readline())
    for i in range(count):
        score = int(f.readline().split()[1])
        overall_score += score
        l.append(score)
l.sort()
print("Počet súťažiacich:", count)
print("Celkový počet bodov:", overall_score)
print("Poradie:")
c.create_text(200, 10, text=f"Poradie:", anchor='w')
for i in range(count+1):
    if i == count-1: break
    print(f"Medzi {count-i}. a {count-i-1}. miestom: {l[i+1]-l[i]} bodov")
    c.create_text(200, 50+20*i, text=f"Medzi {count-i}. a {count-i-1}. miestom: {l[i+1]-l[i]} bodov", anchor='w')
c.create_text(200, 50+20*count, text=f"Celkový počet bodov: {overall_score}", anchor='w')

c.mainloop()