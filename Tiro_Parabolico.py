import random
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-300, -300)
speed = vector(0, 0)
targets = []


def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 300) / 25
        speed.y = (y + 300) / 25


def inside(xy):
    "Return True if xy within screen."
    return -300 < xy.x < 300 and -300 < xy.y < 300


def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, "blue")

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, "red")

    update()


def move():
    "Move ball and targets."
    if randrange(30) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
    # Hace que el movimiento de los balones sea más rápido
    for target in targets:
        target.x -= 0.5*4
    # Hace que la velocidad de los proyectiles vaya más rápido
    if inside(ball):
        speed.y -= 0.35*1.5
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    # Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionan.

    for target in targets:
        if not inside(target):
            target.x = 300

    ontimer(move, 10)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()