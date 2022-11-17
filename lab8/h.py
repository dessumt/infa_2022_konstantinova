import pygame

pygame.init()

screenWidth = 1200
screenHeight = 700

window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Atari Breakout')


class Circle():

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel_x = 1
        self.vel_y = 1


def check_hit():
    global hit
    if (((screenWidth - box.x) <= box.radius) or ((box.x) <= box.radius) or ((box.y) <= box.radius) or (
            (screenHeight - box.y) <= box.radius)):
        # meaning  hit either four walls
        if (((screenWidth - box.x) <= box.radius) or ((box.x) <= box.radius)):
            # hit right, left
            print('hit right, left')
            hit = True
        elif (((box.y) <= box.radius) or ((screenHeight - box.y) <= box.radius)):
            # hit top, bottom
            print('hit top, bottom')
            hit = True


# main loop
run = True
box = Circle(600, 300, 10)
hit = False
# (screenWidth-box.x)<=box.radius     hit right wall
while run:  # (box.x)<=box.radius                 hit left wall
    # (box.y)<=box.radius                 hit top wall
    pygame.time.Clock().tick(60)  # (screenHeight-box.y)<=box.radius    hit bottom wall

    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and (box.y) > box.radius:
        while True:
            box.y -= box.vel_y
            box.x += box.vel_x

            window.fill((0, 0, 0))
            pygame.draw.circle(window, (44, 176, 55), (box.x, box.y), box.radius)
            pygame.display.update()

            check_hit()
            if hit == False:
                continue
            elif hit == True:
                break

        if (box.y) <= box.radius or (screenHeight - box.y) <= box.radius:
            # hit top, bottom
            box.vel_x *= 1
            box.vel_y *= -1
            print('changed')

            if (box.y) <= box.radius:
                # hit top
                print('hi')
                while True:
                    box.x += box.vel_x  # <-- myguess is this is the problem
                    box.y += box.vel_y

                    window.fill((0, 0, 0))
                    pygame.draw.circle(window, (44, 176, 55), (box.x, box.y), box.radius)
                    pygame.display.update()




        elif (screenWidth - box.x) <= box.radius or (box.x) <= box.radius:
            # hit right, left
            box.vel_x *= -1
            box.vel_y *= 1

    window.fill((0, 0, 0))
    pygame.draw.circle(window, (44, 176, 55), (box.x, box.y), box.radius)
    pygame.display.update()

    print('Where are you going')

pygame.quit()