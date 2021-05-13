from util import square, vector, triangle, circle, line, squarenum
from turtle import *

setup(600, 600, 370, 0)
hideturtle()
tracer(False)
listen()

#stage setting
snake = [vector(20, 20)]
walls = {vector(100, 0), vector(-100, 0)}
pwalls = {vector(150, 0) : 5}
thorns = {vector(10, 10)}
lasers = [[vector(-100, 0), vector(100, 0)]]
teledict = {vector(0, 100) : vector(0, -100)}
foods = {vector(0, 0), vector(50, 50)}

for body in snake:
    square(body.x, body.y, 9, 'black')
for telep in teledict:
    square(telep.x, telep.y, 9, 'magenta')
    square(teledict[telep].x, teledict[telep].y, 9, 'purple')
for food in foods:
    square(food.x, food.y, 9, 'green')
for i in range(len(lasers)):
    line(lasers[i][0].x, lasers[i][0].y + 4.5, lasers[i][1].x, lasers[i][1].y + 4.5)
for wall in walls:
    square(wall.x, wall.y, 9, 'gray')
for pwall in pwalls:
    squarenum(pwall.x, pwall.y, 9, 'blue', pwalls[pwall])
for thorn in thorns:
    triangle(thorn.x, thorn.y, 9, 'red')
done()