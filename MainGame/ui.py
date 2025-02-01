import pygame
from settings import *

class UI:
    def __init__(self):
        
        #general
        self.display_surface = pygame.display.get_surface()
        self.font =pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        #bar setup
        self.dico_bar={} #contient : [self.XXX_bar_rect, [Nom, posx, posy, taille x, taille y], color]
            #health
        self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,HEALTH_BAR_HEIGHT)
        self.dico_bar["Health"]=[self.health_bar_rect, [10,10,HEALTH_BAR_WIDTH,HEALTH_BAR_HEIGHT], GREEN]
            #energy
        self.energy_bar_rect = pygame.Rect(10,10+HEALTH_BAR_HEIGHT,ENERGY_BAR_WIDTH,ENERGY_BAR_HEIGHT)
        self.dico_bar["Energie"]=[self.energy_bar_rect, [10,10+HEALTH_BAR_HEIGHT,ENERGY_BAR_WIDTH,ENERGY_BAR_HEIGHT], YELLOW]
            #xp
        self.xp_bar_rect = pygame.Rect(10,10+HEALTH_BAR_HEIGHT*2,XP_BAR_WIDTH,XP_BAR_HEIGHT)
        self.dico_bar["Xp"]=[self.xp_bar_rect, [10,10+HEALTH_BAR_HEIGHT*2,XP_BAR_WIDTH,XP_BAR_HEIGHT], BLUEXP]

    def draw_bar(self,elem_de_bar):
        bar_color=elem_de_bar[-1] #prend la couleur de la bar
        bar=elem_de_bar[0]
        pygame.draw.rect(self.display_surface,bar_color,bar)



    def display(self,player):
        for elem_de_bar in self.dico_bar.keys():
            self.draw_bar(self.dico_bar[elem_de_bar])


