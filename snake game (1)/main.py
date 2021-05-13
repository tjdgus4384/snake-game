from turtle import *
from random import randrange
from util import square, vector, triangle, circle, line, squarenum, rectangle
import time
import stages
from copy import deepcopy

# snake의 방향을 바꾸는 함수
def change(x, y):
    aim.x = x
    aim.y = y

L=0
def nextstage():
    global L
    if L == len(stages.stage)-1:
        up(), goto(-80, -10), down(), color("black")
        write("YOU WIN!", font=("Arial", 20, "normal"))
        return
    time.sleep(1)
    clear()
    print("df")
    up(), goto(-110, -10), down(), color("black")
    write("STAGE %d CLEAR!" %(L+1), font=("Arial", 20, "normal"))
    L += 1
    time.sleep(1)
    clear()
    startf(0, -90, L)

def timer():
    global T
    up(), goto(-200, -200), down(), color("black")
    T = time.time() - startT
    write("%.2fs"%T, font=("Arial", 16, "normal"))

def again():
    global L
    print("df")
    time.sleep(1)
    clear()
    up(), goto(-90, -10), down(), color("black")
    write("STAGE %d FAIL" %(L+1), font=("Arial", 20, "normal"))
    time.sleep(1)
    clear()
    startf(0, -90, L)

# snake의 head가 게임 창의 내부에 있으면 True를 리턴
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# snake를 1개 포인트만큼 이동
def move():
    global T
    global cnt
    head = snake[-1].copy()
    head.move(aim)
    if head in walls:
        rectangle(-200, -195, 60, 20, 'white') f
        timer()
        ontimer(move, 100)
        return
    if head in pwalls:
        if pwalls.get(head) != None:
            pwalls[head] -= 1
            if pwalls[head] == 0:
                pwalls.pop(head)
                walls.add(head)
    if head in thorns:
        again()
        return
    for body in snake:
            for i in range(len(lasers)):
                if cnt > 0 and lasers[i][0].x <= body.x <= lasers[i][1].x and lasers[i][0].y <= body.y <= lasers[i][1].y:
                    again()
                    return
    if len(foods) == 0:
        nextstage()
        return
    if head in teledict:
        head = teledict[head]
    if head in foods:
        foods.remove(head)
    else:
        snake.pop(0)

    snake.append(head)
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')
    for telep in teledict:
        square(telep.x, telep.y, 9, 'magenta')
        square(teledict[telep].x, teledict[telep].y, 9, 'purple')
    for food in foods:
        square(food.x, food.y, 9, 'green')
    for i in range(len(lasers)):
        if cnt > 0 : line(lasers[i][0].x, lasers[i][0].y+4.5, lasers[i][1].x, lasers[i][1].y+4.5)
        cnt += 1
        if cnt == 10: cnt = -5

    for wall in walls:
        square(wall.x, wall.y, 9, 'gray')
    for pwall in pwalls:
        squarenum(pwall.x, pwall.y, 9, 'blue', pwalls[pwall])
    for thorn in thorns:
        triangle(thorn.x, thorn.y, 9, 'red')
    timer()
    update()
    ontimer(move, 100)

def startf(x, y, i=0):
    global startT
    global snake, walls, pwalls, thorns, lasers, teledict, foods, aim, cnt
    if x < 25 and x > -25 and y < -80 and y > -100 and i < len(stages.stage):
        clear()
        up(), goto(-40, -10), down(), color("black")
        write("STAGE %d"%(i+1), font=("Arial", 16, "normal"))
        time.sleep(2)
        clear()
        cnt = 0
        aim = vector(0, 0)
        snake = deepcopy(stages.stage[i])[0]
        walls = deepcopy(stages.stage[i])[1]
        pwalls = deepcopy(stages.stage[i])[2]
        thorns = deepcopy(stages.stage[i])[3]
        lasers = deepcopy(stages.stage[i])[4]
        teledict = deepcopy(stages.stage[i])[5]
        foods = deepcopy(stages.stage[i])[6]
        startT = time.time()
        move()
        done()

setup(600, 600)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
up(), goto(-175, 30), down(), color("black")
write("SNAKE GAME", font=("Arial", 40, "normal"))
up(), goto(-25, -100), down(), color("black")
write("PLAY", font=("Arial", 16, "normal"))
onscreenclick(startf, 1, add=False)
done()