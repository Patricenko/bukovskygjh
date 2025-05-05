import tkinter
import random

root = tkinter.Canvas(width=500, height = 500)

def checkCollision(s):
    global enemies, character, x0, y0, score, scoreboard, enemiesRec
    changedEnemies = []
    for enemy in enemies:
        curcoords = root.coords(enemy)
        xe0 = curcoords[0] - 5
        ye0 = curcoords[1] - 5
        xe1 = curcoords[0] + 5
        ye1 = curcoords[1] + 5
        xp0 = x0 - 5
        yp0 = y0 - 5
        xp1 = x0 + 5
        yp1 = y0 + 5
        if xp0 < xe1 and xp1 > xe0 and yp0 < ye1 and yp1 > ye0:
            root.delete(enemiesRec[enemy])
            root.delete(enemy)
            changedEnemies.append(enemy)
            score += 1
            root.itemconfig(scoreboard, text = f"Score: {score}")
    for enemy in changedEnemies:
        enemiesRec.pop(enemy)
        enemies.pop(enemy)
def moveForward(s):
    global x0, y0
    y0 -= 10
    checkCollision(s)
    root.move('char', 0, -10)
def moveLeft(s):
    global x0, y0
    x0 -= 0
    checkCollision(s)
    root.move('char', -10, 0)
def moveBack(s):
    global x0, y0
    y0 += 10
    checkCollision(s)
    root.move('char', 0, 10)
def moveRight(s):
    global x0, y0
    x0 += 10
    checkCollision(s)
    root.move('char', 10, 0)

def spawnEnemy():
    x = random.randint(10, 490)
    y = random.randint(10, 490)
    newenemy = root.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill="yellow")
    newenemytext = root.create_text(x, y, text = f"5")
    return newenemytext, newenemy
def mainMove():
    global x0, y0, timer_food, timer_new, scoreboard, enemiesRec
    if timer_food / 1000 >= 1:
        print(enemies)
        timer_food = 0
        for enemy in enemies:
            enemies[enemy] -= 1
            root.itemconfig(enemy, text=f"{enemies[enemy]}")
            if int(enemies[enemy]) <= 0:
                root.itemconfig(scoreboard, text = "Game Over")
                root.pack()
                return

    if timer_new / 3000 >= 1:
        x = random.randint(10,490)
        y = random.randint(10, 490)
        newenemytext, newenemy = spawnEnemy()
        enemies[newenemytext] = 5
        enemiesRec[newenemytext] = newenemy
        timer_new = 0
    timer_food += 50
    timer_new += 50
    root.after(50, mainMove)


def startGame():
    global character, score, scoreboard, enemies, direction, x0, y0, timer_new, timer_food, enemiesRec
    x0 = 240
    y0 = 240
    character = root.create_rectangle(230,230,250,250, fill="red", outline="black", width=2, tags='char')
    score = 0
    scoreboard = root.create_text(250,50, text=f"Score: {score}")
    enemies = {}
    enemiesRec = {}
    timer_new, timer_food = 0, 0
    direction = "W"

startGame()
root.focus_set()
root.bind_all("<w>", moveForward)
root.bind_all("<a>", moveLeft)
root.bind_all("<s>", moveBack)
root.bind_all("<d>", moveRight)
mainMove()

root.pack()
root.mainloop()
tkinter.mainloop()