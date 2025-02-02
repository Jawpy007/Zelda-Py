import pygame
from settings import *
from tile import Tile
from player import Player
from ui import UI
from support import *
from random import *
from os import listdir
class Level:
    def __init__(self):
        
        #Pour avoir la carte sur lequel le joueur ce déplace
        self.display_surface = pygame.display.get_surface()

        #Groupe de sprite 
        self.visible_sprites = YSortCameraGroup() #Sprite Visible par le joueur exemple texture
        self.obstacles_sprites = pygame.sprite.Group() #Sprite non Visible par le joueur exemple Hit-Box

        #Affiche les sprites
        self.create_map()

        # ui
        self.ui=UI()


    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('map/map_Grass.csv'),
            'object': import_csv_layout('map/map_LargeObjects.csv')
        
        
        
        }
        graphics= {
            'grass': import_folder('graphics/grass')
        }
        print(graphics)
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        if style == 'boundary':
                            Tile((x,y),[self.obstacles_sprites], 'invisible')
                        if style =="grass":
                            #créer de l'herbe
                            random_choice_grass = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacles_sprites],'grass' ,random_choice_grass )
                            


                        if style == "object":
                            #créer un objet
                            pass


                """if col == 'x':
                    Tile((x,y),[self.visible_sprites, self.obstacles_sprites])
                
                if col == "p":
                    self.player = Player((x,y),[self.visible_sprites], self.obstacles_sprites)"""
       
       
       
       
        self.player = Player((1430,2000),[self.visible_sprites], self.obstacles_sprites)

    def run(self):
        #Met a jour le jeu
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        #setup general
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_widht = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
   
        #création le sol
        self.floor_surf = pygame.image.load('graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):

        #obtenir le joueur quand il part
        self.offset.x = player.rect.centerx - self.half_widht
        self.offset.y = player.rect.centery - self.half_height
       
       #dessiner le sol
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

        