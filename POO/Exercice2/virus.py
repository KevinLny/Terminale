import pygame
from pygame.locals import *
pygame.init()

# Fenetre
taille = largeur, hauteur = 480, 320        
blanc=0xFFFFFF
ecran = pygame.display.set_mode(taille)

#------------------------------------------

virus=pygame.image.load("virus1.png")             # Charge l'image virus en object pygame
virusrect=virus.get_rect()                        #On récupere le rectangle pris par l'image
print(virusrect)                                  #
print(ecran.get_rect().center)                    #
virusrect.center=ecran.get_rect().center          # On met l'image virus au centre
print(virusrect)                                  # 
print(virusrect[0])                               #
print(virusrect[1])                               #

continuer = 1                                     # On défini continuer à 1

while continuer:                                  # Tant que continuer n'est pas nul
    for event in pygame.event.get():              # 
        if event.type == pygame.QUIT:             
            continuer=0
    ecran.fill(blanc)
    ecran.blit(virus, (virusrect[0],virusrect[1]))
    pygame.display.flip()