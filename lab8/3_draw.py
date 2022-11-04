import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
bg_color = (230, 230, 230)
screen.fill(bg_color)

circle(screen, (255, 255, 0), (200, 200), 150)

circle(screen, (255, 0, 0), (130, 150), 30)
circle(screen, (255, 0, 0), (265, 150), 20)

circle(screen, (0, 0, 0), (130, 150), 15)
circle(screen, (0, 0, 0), (265, 150), 10)

polygon(screen, (0, 0, 0), [(150, 120), (100, 110),
                            (35, 70), (130, 100)])
polygon(screen, (0, 0, 0), [(240, 120), (300, 110),
                            (355, 70), (270, 100)])

rect(screen, (0, 0, 0), (130, 240, 140, 19))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
