import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        
        #Pour avoir la carte sur lequel le joueur ce déplace
        self.display_surface = pygame.display.get_surface()

        #Groupe de sprite 
        self.visible_sprites = pygame.sprite.Group() #Sprite Visible par le joueur exemple texture
        self.obstacles_sprites = pygame.sprite.Group() #Sprite non Visible par le joueur exemple Hit-Box

        #Affiche les sprites
        self.create_map()


    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == 'x':
                    Tile((x,y),[self.visible_sprites, self.obstacles_sprites])
                
                if col == "p":
                    Player((x,y),[self.visible_sprites], self.obstacles_sprites)


    def run(self):
        #Met a jour le jeu
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()


