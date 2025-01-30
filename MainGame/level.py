import pygame

class Level:
    def __init__(self):
        
        #Groupe de sprite 

        self.visible_sprites = pygame.sprite.Group() #Sprite Visible par le joueur exemple texture

        self.obstacles_sprites = pygame.sprite.Group() #Sprite non Visible par le joueur exemple Hit-Box

    def run(self):
        #Met a jour le jeu
        pass
    

