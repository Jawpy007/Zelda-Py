import pygame
from settings import *

class UI:
    def __init__(self,level_type,game):

        #general
        self.game=game
        self.level_type=level_type
        self.display_surface = pygame.display.get_surface()
        self.font =pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        if self.level_type=="world":
            #bar setup
            self.dico_bar={} #contient : [self.XXX_bar_rect, [Nom, posx, posy, taille x, taille y], color]
                #health
            self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,HEALTH_BAR_HEIGHT)
            self.dico_bar["health"]=[self.health_bar_rect, ["health",10,10,HEALTH_BAR_WIDTH,HEALTH_BAR_HEIGHT], GREEN]
                #energy
            self.energy_bar_rect = pygame.Rect(10,10+HEALTH_BAR_HEIGHT,ENERGY_BAR_WIDTH,ENERGY_BAR_HEIGHT)
            self.dico_bar["energy"]=[self.energy_bar_rect, ["energy",10,10+HEALTH_BAR_HEIGHT,ENERGY_BAR_WIDTH,ENERGY_BAR_HEIGHT], YELLOW]
                #xp
            self.xp_bar_rect = pygame.Rect(10,10+HEALTH_BAR_HEIGHT*2,XP_BAR_WIDTH,XP_BAR_HEIGHT)
            self.dico_bar["xp"]=[self.xp_bar_rect, ["xp",10,10+HEALTH_BAR_HEIGHT*2,XP_BAR_WIDTH,XP_BAR_HEIGHT], BLUEXP]

        if self.level_type=="main_menu":
            self.play_but = pygame.Rect(WIDTH//2-PLAY_BUT_SIZE["x"]//2,HEIGTH//2-PLAY_BUT_SIZE["y"]//2,PLAY_BUT_SIZE["x"],PLAY_BUT_SIZE["y"])

    def draw_bar(self,elem_de_bar):

        stats=self.player.stats[elem_de_bar[1][0]]
        max_stats=stats[1]
        min_stats=stats[0]

        bar_len_x=(min_stats*100)/max_stats

        bar_len_x=bar_len_x*(elem_de_bar[1][3]-4)/100

        inside_bar=pygame.Rect(elem_de_bar[1][1]+2,elem_de_bar[1][2]+2,bar_len_x,elem_de_bar[1][4]-4)

        bar_color=elem_de_bar[-1] #prend la couleur de la bar
        bar=elem_de_bar[0]
        pygame.draw.rect(self.display_surface,bar_color,bar)
        pygame.draw.rect(self.display_surface,(101,100,222),inside_bar)

    def input(self):
        mouse=pygame.mouse.get_pressed()
        cliquedroit=mouse[0]

        if self.level_type=="main_menu":
            if cliquedroit:
                mouse_cord=pygame.mouse.get_pos()
                
                if self.play_but.collidepoint(mouse_cord):
                    self.game.change_level("world")


    def display(self,player=None):

        if self.level_type=="world":
            self.player=player


            for elem_de_bar in self.dico_bar.keys():
                self.draw_bar(self.dico_bar[elem_de_bar])
        elif self.level_type=="main_menu":
            pygame.draw.rect(self.display_surface,"white",self.play_but)
            self.input()
        


