
import pygame
import math
from pygame.draw import *
pygame.init()
FPS = 2
screen = pygame.display.set_mode((1200, 900))


# описание характеристик: положение центра, смещение центра, количество шариков
n = 6
x = []
y = []
v = []
dv = []
r = []
color = []
m = []
for i in range(n+1):
    x.append(i * 400)
    y.append(450)
    r.append(i * 50)
    dv.append(i * math.pi/4)
    v.append(2)
    m.append(r[i] ** 2)
    color.append(0)


color[1] = (255, 0, 0)
color[2] = (0, 0, 255)


var_ = True
while var_:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var_ = False

    for i in range(1, n+1):
        x[i] += v[i] * math.cos(dv[i])
        y[i] += v[i] * math.sin(dv[i])
        pygame.draw.circle(screen, color[i], (x[i], y[i]), r[i])

    pygame.time.delay(10)
    pygame.display.update()
pygame.quit()




