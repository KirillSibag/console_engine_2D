import keyboard
from time import sleep
from random import randint as r

from main import *


def move(x, y):
    if x <= 0:
        x = 120 - x
    elif x >= 120:
        x -= 120

    if y <= 0:
        y = 30 - y
    elif y >= 30:
        y -= 30
    
    line = "asdw"
    res = [0,0,0,0]
    
    for i in range(4):
        if keyboard.is_pressed(line[i]):
            res[i] = 1

    n = 2
    return x + res[2]*n - res[0]*n, y + res[1] - res[3], int(x + res[2]*n - res[0]*n), int(y + res[1] - res[3])



def game_main():
    px = 60.0
    py = 15.0

    score = 0
    eat = []
    enemies = []
    built = []
    builts = 10
    lbu = []
    
    while True:
        px, py, x, y = move(px, py)
        
        
        for i in lbu:
            if abs(i[0] - x) < 2 and abs(i[1] - y) < 2:
                builts += r(1, 10)
                lbu.remove(i)
        
        for i in enemies:
            if x >= i[0]:
                i[0] += 1
            else:
                i[0] -= 1

            if y >= i[1]:
                i[1] += 1/2
            else:
                i[1] -= 1/2


        for i in built:
            ens = [[],[]]
            for j in enemies:
                ens[1].append([int(j[0]), int(j[1])])
                ens[0].append(abs(j[0]-i[0]) + abs(j[1]-i[1]))

            xe = ens[1][ens[0].index(min(ens[0]))][0]
            ye = ens[1][ens[0].index(min(ens[0]))][1]
            
            if xe >= i[0]:
                i[0] += 1.5
            else:
                i[0] -= 1.5

            if ye >= i[1]:
                i[1] += 2/3
            else:
                i[1] -= 2/3
                
        
        for i in enemies:
            if abs(i[0] - x) < 2 and abs(i[1] - y) < 2:
                score -= 10
                enemies.remove(i)
                
            else:
                for j in built: 
                    if  abs(i[0] - j[0]) < 2 and abs(i[1] - j[1]) < 2:
                        try: 
                            eat.append([i[0] + r(0,4)-2, i[1] + r(0,4)-2])
                            lbu.append([i[0] + r(0,4)-2, i[1] + r(0,4)-2])
                            enemies.remove(i)
                            built.remove(j)
                            score += 3
                            break
                        except Exception:
                            a = 0

        for i in eat:
            if abs(i[0] - x) < 2 and abs(i[1] - y) < 2:
                score += 1
                eat.remove(i)

        if keyboard.is_pressed("SPACE") and builts > 0:
            built.append([x, y])
            builts -= 1

        if len(enemies) < 2 or r(0, 100) > 90:
            enemies.append([r(2, 120-2), r(2, 30-2)])

        for i in enemies:
            points(int(i[0]), int(i[1]), 9)

        for i in eat:
            points(int(i[0]), int(i[1]), 11)

        for i in built:
            points(int(i[0]), int(i[1]), 8)

        for i in lbu:
            points(int(i[0]), int(i[1]), 10)


        points(x, y, 0)
            
        stri = "очков: " + str(score)
        stri1 = " пуль: " + str(builts)
        fin = main()
        
        print(stri + fin[len(stri)-1:119] + stri1 + fin[120 + len(stri):])
        sleep(0.1)
        
        if keyboard.is_pressed("p"):
            break


line =        "   ____ ___  _   _ ____   ___  _     _____         _____ _   _  ____ ___ _   _ _____ \n"
line +=       "  / ___/ _ \| \ | / ___| / _ \| |   | ____|       | ____| \ | |/ ___|_ _| \ | | ____|\n"
line +=       " | |  | | | |  \| \___ \| | | | |   |  _|         |  _| |  \| | |  _ | ||  \| |  _|  \n"
line +=       " | |__| |_| | |\  |___) | |_| | |___| |___        | |___| |\  | |_| || || |\  | |___ \n"
line +=       "  \____\___/|_|_\_|____/_\___/|_____|_____|  ___ _|_____|_| \_|\____|___|_| \_|_____|\n"
line +=       " | '_ \| '__/ _ \/ __/ __| / __| '_ \ / _` |/ __/ _ \                                \n"
line +=       " | |_) | | |  __/\__ \__ \ \__ \ |_) | (_| | (_|  __/                                \n"
line +=       " | .__/|_|  \___||___/___/ |___/ .__/ \__,_|\___\___|                                \n"
line +=       " |_|                           |_|                                                   \n"
            
while True:
    print(line)
    while not keyboard.is_pressed("SPACE"):
        sleep(0.01)

    print("нажмите 'ctrl + c' для завершения")
    sleep(2)

    
    game_main()

        
