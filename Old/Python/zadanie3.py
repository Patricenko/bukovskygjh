f = open('zadanie3.txt','r')
l = f.readline()
win = 0
points = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
while list != "":
    half = int((len(l)-1)/2)
    for i in range (half):
        if l[i] in l[half:len(l)]:
            print (points[points.index(l[i])])
            win += int(points.index(l[i]))+1
            print(win)
    l = f.readline()
print(win)
