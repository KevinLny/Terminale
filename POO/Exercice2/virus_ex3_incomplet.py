import pygame
from pygame.locals import *
pygame.init()

taille = largeur, hauteur = 480, 320
blanc=0xFFFFFF
ecran = pygame.display.set_mode(taille)

images=["virus1.png","virus2.png","virus3.png"]

class Virus:
    def __init__(self,image,position,vitesse):
        # Compléter dans l'exercice 2
        
        
# Instantiation des 3 objets Virus
v1=Virus(images[0],[0,0],1)
v2=Virus(images[1],[0,100],2)
v3=Virus(images[2],[0,200],3)

# Gestion du temps pour les déplacements
clock = pygame.time.Clock()
clock_cpt = 0

continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer=0
    ecran.fill(blanc)
    
    # Affichage des 3 objets virus
    # à compléter
    
    # Gestion de la vitesse des déplacements : si 4 clock.tick() => virus.bouge()
    # à compléter (voir exercice 2)
    
    pygame.display.flip()