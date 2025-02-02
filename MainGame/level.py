import pygame  # Importation de la bibliothèque Pygame
from settings import *  # Importation des constantes du jeu
from tile import Tile  # Importation de la classe Tile pour gérer les obstacles
from player import Player  # Importation de la classe Player pour gérer le joueur
from ui import UI  # Importation de l'interface utilisateur

# Définition de la classe Level, qui gère la carte du jeu et les entités
class Level:
    def __init__(self):
        
        # Récupération de la surface d'affichage du jeu
        self.display_surface = pygame.display.get_surface()

        # Groupes de sprites
        self.visible_sprites = YSortCameraGroup()  # Sprites visibles (ex: textures, joueur)
        self.obstacles_sprites = pygame.sprite.Group()  # Sprites obstacles (ex: hit-box, murs)

        # Génération de la carte
        self.create_map()

        # Interface utilisateur
        self.ui = UI()

    # Création de la carte du jeu
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):  # Parcours des lignes de la carte
            for col_index, col in enumerate(row):  # Parcours des colonnes de la carte
                x = col_index * TILESIZE  # Conversion des indices en coordonnées
                y = row_index * TILESIZE

                if col == 'x':  # Si on trouve un mur
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                
                if col == "p":  # Si on trouve le joueur
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)

    # Mise à jour et affichage du niveau
    def run(self):
        self.visible_sprites.custom_draw(self.player)  # Dessine les sprites visibles
        self.visible_sprites.update()  # Met à jour les sprites
        self.ui.display(self.player)  # Affiche l'interface utilisateur

# Gestion de l'affichage et du tri des sprites (ex: effet de profondeur)
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        # Initialisation du groupe de sprites
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2  # Moitié de la largeur de l'écran
        self.half_height = self.display_surface.get_size()[1] // 2  # Moitié de la hauteur de l'écran
        self.offset = pygame.math.Vector2()  # Décalage pour le suivi du joueur
   
    # Dessin des sprites en tenant compte du suivi caméra
    def custom_draw(self, player):
        
        # Calcul du décalage en fonction de la position du joueur
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
       
        # Dessine chaque sprite en appliquant le décalage
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)