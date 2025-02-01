import pygame
from settings import * 
from entity import Entity
from support import * 

class Enemy(Entity):
    def __init__(self, monster_name,pos,groups):
        #Setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #Partie Graphique
        self.import_graphics(monster_name)
        self.image = pygame.Surface((64,64)) #A completer avec les animations lorsqu'on les auras , 4:21:48
        self.rect = self.image.get_rect(topleft = pos)
    
    def import_graphics(self,name):

        self.animation = {'idle':[],'move':[],'attack':[]}
        main_path = f'/graphics/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

