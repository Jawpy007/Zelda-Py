import pygame  # Importation de la bibliothèque pygame
from settings import *  # Importation des constantes et paramètres du jeu

# Définition de la classe Player qui hérite de pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)  # Initialisation de la classe parent

        self.image = pygame.image.load('graphics/test/player.png')  # Chargement de l'image du joueur
        self.rect = self.image.get_rect(topleft=pos)  # Définition de la position initiale du joueur

        # Définition des variables de mouvement
        self.direction = pygame.math.Vector2()
        self.speed = PLAYERSPEED  # Vitesse du joueur
        self.injump = False  # Indique si le joueur est en saut
        self.jumping_time = pygame.time.get_ticks()  # Temps du début du saut
        self.current_time = pygame.time.get_ticks()  # Temps actuel pour gérer le saut
        self.nbjump = JUMPMAX  # Nombre de sauts restants
        self.player_running = False  # Indique si le joueur court

        self.obstacle_sprites = obstacle_sprites  # Liste des obstacles

    # Fonction de gestion des entrées utilisateur
    def input(self):
        keys = pygame.key.get_pressed()  # Récupération des touches pressées
        
        # Gestion du saut
        if not self.injump and self.nbjump > 0:
            if keys[pygame.K_SPACE]:
                self.injump = True
                self.nbjump -= 1
                self.jumping_time = pygame.time.get_ticks()
            else:
                self.direction.y = 1  # Gravité appliquée au joueur
        elif not (self.current_time - self.jumping_time <= JUMPTIME):
            self.direction.y = 1  # Gravité après fin du saut
        
        # Gestion de la course
        self.player_running = keys[pygame.K_LSHIFT]

        # Déplacement horizontal
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    # Fonction de déplacement du joueur
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # Mouvement horizontal avec gestion de la course
        self.rect.x += self.direction.x * (speed * 2 if self.player_running else speed)
        self.collision('horizontal')
        
        # Mouvement vertical avec gestion de la gravité et du saut
        if self.direction.y > 0:
            self.rect.y += self.direction.y * speed * 2
        elif self.direction.y < 0:
            self.rect.y += self.direction.y * speed * 2
        self.collision('vertical')

    # Fonction de gestion des collisions avec les obstacles
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:  # Collision à droite
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # Collision à gauche
                        self.rect.left = sprite.rect.right
        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # Collision en bas
                        self.rect.bottom = sprite.rect.top
                        if self.current_time - self.jumping_time >= JUMPTIME:
                            self.injump = False
                            self.nbjump = JUMPMAX
                    if self.direction.y < 0:  # Collision en haut
                        self.rect.top = sprite.rect.bottom

    # Fonction de gestion du saut
    def jumping(self):
        if self.injump:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.jumping_time <= JUMPTIME:
                self.direction.y = -1
            else:
                self.injump = False

    # Mise à jour du joueur à chaque frame
    def update(self):
        self.input()  # Gestion des entrées utilisateur
        self.jumping()  # Gestion du saut
        self.move(self.speed)  # Déplacement du joueur
