import pygame
from pygame.locals import *
from pygame.time import Clock
pygame.init()

class Virus:
    def __init__(self, image, position,vitesse) -> None:
        self.img = pygame.image.load(image)
        self.pos = self.img.get_rect().move(position)
        self.vit = vitesse
    
    def bouger(self):
            self.pos = self.pos.move(self.vit,0)
            if self.pos.right > 480:
                self.vit= -self.vit
            elif self.pos.left < 0:
                self.vit = -self.vit

    def __del__(self):
        print("réussi, UN DE MOINS !!!!!")

# Fenetre
taille = largeur, hauteur = 480, 320        
blanc=0xFFFFFF
ecran = pygame.display.set_mode(taille)

virus = Virus("virus1.png", [199, 100], 1)

continuer = 1                                     # On défini continuer à 1
clock = pygame.time.Clock()
clock_cpt = 0

while continuer:                                  # Tant que continuer n'est pas nul
    for event in pygame.event.get():              # 
        if event.type == pygame.QUIT:             
            continuer=0
        if event.type == MOUSEBUTTONDOWN:
            coordX = event.pos[0]
            coordY = event.pos[1]
            try:
                if coordY > virus.pos.top and coordY < virus.pos.bottom and coordX < virus.pos.right and coordX > virus.pos.left:
                    del virus
                else:
                    print("Raté HIHIHIHIHIHHI")
            except:
                pass
    
    ecran.fill(blanc)
    try:
        ecran.blit(virus.img,virus.pos)
        tick = clock.tick()
        clock_cpt += tick
        if clock_cpt >=4:
            clock_cpt = 0
            virus.bouger()
    except:
        pass
    pygame.display.flip()