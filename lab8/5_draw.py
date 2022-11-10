# Игра поймай шарик. Успеваешь кликнуть - зарабатываешь очки
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

# набор цветов шаров
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
color = COLORS[randint(0, 5)]
balls = []
# описание характеристик: количество шариков
n = randint(3, 10)


# характеристики шарика, описываются координаты, радиус, цвет
def new_ball():
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    balls.append([color, (x, y), r])
    return (x, y, r, color)


# создание n штук шариков с координатами '''
def create_ball(n):
        c = []
        for i in range(n):
            c.append((new_ball()))
        return c


# шарики появляются
def click():
    print(x, y, r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
E = []
points = 0
c = create_ball(n)
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # проверка на попадание
            E = pygame.mouse.get_pos()
            x1 = E[0]
            y1 = E[1]
            if ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5 <= r:
                print('попал')
                points += 1
                print('Количество очков', points)
            else:
                print('не попал')
                print('Количество очков', points)

    c = create_ball(n)
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
