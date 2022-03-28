import pygame
from pygame.locals import *
pygame.init()

size = width, height = 480, 320
speed = [2, 2]

screen = pygame.display.set_mode(size)
bg = pygame.image.load("pelouse.jpg").convert()
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

continuer = 1
pygame.key.set_repeat(100, 5)

#Boucle infinie
while continuer:

    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
            continuer=0      #On arrête la boucle
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                ballrect = ballrect.move(speed)
                if ballrect.left < 0 or ballrect.right > width:
                    speed[0] = -speed[0]
                if ballrect.top < 0 or ballrect.bottom > height:
                    speed[1] = -speed[1]
    screen.blit(bg, (0,0))
    screen.blit(ball, ballrect)
    pygame.display.flip()