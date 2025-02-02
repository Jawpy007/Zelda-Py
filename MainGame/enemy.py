import pygame  # Importation de la bibliothèque Pygame
from settings import *  # Importation des paramètres du jeu
from entity import Entity  # Importation de la classe de base Entity
from support import *  # Importation des fonctions de support pour le jeu

# Définition de la classe Enemy, qui hérite de Entity
class Enemy(Entity):
    def __init__(self, monster_name, pos, groups):
        # Initialisation de la classe parente
        super().__init__(groups)
        self.sprite_type = 'enemy'  # Définit ce sprite comme un ennemi

        # Partie Graphique : Chargement des animations
        self.import_graphics(monster_name)
        self.image = pygame.Surface((64,64))  # Création d'une surface temporaire pour le sprite
        self.rect = self.image.get_rect(topleft=pos)  # Positionnement initial de l'ennemi
    
    # Fonction pour importer les animations de l'ennemi
    def import_graphics(self, name):
        self.animation = {'idle': [], 'move': [], 'attack': []}  # Dictionnaire contenant les animations
        main_path = f'/graphics/monsters/{name}/'  # Chemin du dossier contenant les animations
        for animation in self.animation.keys():  # Parcours des types d'animations
            self.animation[animation] = import_folder(main_path + animation)  # Importation des images

