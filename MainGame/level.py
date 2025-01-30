import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        
        #Pour avoir la carte sur lequel le joueur ce déplace
        self.display_surface = pygame.display.get_surface()

        #Groupe de sprite 
        self.visible_sprites = YSortCameraGroup() #Sprite Visible par le joueur exemple texture
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
                    self.player = Player((x,y),[self.visible_sprites], self.obstacles_sprites)


    def run(self):
        #Met a jour le jeu
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        #setup general
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_widht = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
   
    def custom_draw(self,player):

        #obtenir le joueur quand il part
        self.offset.x = player.rect.centerx - self.half_widht
        self.offset.y = player.rect.centery - self.half_height
       
       
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

        