import math
from random import choice
from random import randint

import pygame


FPS = 33

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F

GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WIDTH = 799
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.y + self.r >= 600:
            self.vy = self.vy/4
            self.vx *= 0.7
        if self.x + self.r >= 799:
            self.vx *= -1
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (obj.x-self.x)**2+(obj.y - self.y)**2 <= (obj.r-self.r)**2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 20
        self.y = 700

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
    # FIXIT don't know how to do it
        pygame.draw.polygon(screen, self.color, [[50, 490],
                                                 [30, 400],
        [40+self.f2_power * math.cos(self.an), 440 + self.f2_power * math.sin(self.an)],
        [50 + self.f2_power * math.cos(self.an), 490 + self.f2_power * math.sin(self.an)]])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def new_target(self, screen, type):
        self.points = 0
        self.live = 1
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.screen = screen
        self.color = RED
        if type == 1:
            self.vx = randint(-5, 5)
            self.vy = randint(-5, 5)
            self.r = randint(25, 50)
        if type == 2:
            self.r = randint(5, 10)
            self.vx = randint(-5, 5)
            self.vy = randint(-5, 5)
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()

    def move(self):
        if (self.x + self.vx + self.r > 799) or (self.x + self.vx - self.r < 0.3*799):
            self.vx *= (-1)
            self.vy *= (-1)
        if (self.y + self.vy + self.r > 0.8*600) or (self.y + self.vy - self.r < 20):
            self.vx *= (-1)
            self.vy *= (-1)
        self.y += self.vy
        self.x += self.vx



    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        self.move()




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
type = randint(1, 2)
target.new_target(screen, type)
finished = False
points = 0

while not finished:
    screen.fill(WHITE)
    type = randint(1, 2)
    gun.draw()
    target.draw()
    for b in balls:
        if abs(b.vx)>=0.2:
            b.draw()
        else:
            pygame.draw.circle(screen, WHITE, (b.x, b.y), b.r)
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target(screen, type)
    gun.power_up()

pygame.quit()
