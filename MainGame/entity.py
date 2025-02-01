import pygame  # Importation de la bibliothèque Pygame
from settings import JUMPMAX, JUMPTIME  # Importation de constantes depuis un fichier externe

# Définition d'une classe de base pour les entités du jeu
class Entity(pygame.sprite.Sprite):  # Hérite de pygame.sprite.Sprite pour la gestion des sprites
    def __init__(self, groups):
        super().__init__(groups)  # Initialise le sprite avec les groupes passés en paramètre
        self.frame_index = 0  # Indice pour l'animation
        self.animation_speed = 0.15  # Vitesse d'animation
        self.direction = pygame.math.Vector2()  # Vecteur de direction de l'entité

    # Méthode pour déplacer l'entité
    def move(self, speed):
        if self.direction.magnitude() != 0:  # Vérifie que la direction n'est pas un vecteur nul
            self.direction = self.direction.normalize()  # Normalisation pour garder une vitesse constante
        
        # Déplacement horizontal
        self.rect.x += self.direction.x * speed  # Modifie la position en x en fonction de la direction
        self.collision('horizontal')  # Vérifie et gère les collisions horizontales
        
        # Déplacement vertical
        self.rect.y += self.direction.y * speed  # Modifie la position en y en fonction de la direction
        self.collision('vertical')  # Vérifie et gère les collisions verticales

    # Gestion des collisions
    def collision(self, direction):
        if direction == 'horizontal':  # Gestion des collisions horizontales
            for sprite in self.obstacle_sprites:  # Parcours des objets pouvant être des obstacles
                if sprite.rect.colliderect(self.rect):  # Vérifie si l'entité entre en collision avec un obstacle
                    if self.direction.x > 0:  # Si elle va vers la droite
                        self.rect.right = sprite.rect.left  # Empêche de traverser en fixant la position
                    if self.direction.x < 0:  # Si elle va vers la gauche
                        self.rect.left = sprite.rect.right  # Bloque le mouvement
        
        if direction == 'vertical':  # Gestion des collisions verticales
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # Si l'entité tombe
                        self.rect.bottom = sprite.rect.top  # Bloque la chute sur l'obstacle
                        if self.current_time - self.jumping_time >= JUMPTIME:  # Vérifie le temps de saut
                            self.injump = False  # Termine le saut
                            self.nbjump = JUMPMAX  # Réinitialise le nombre de sauts
                    if self.direction.y < 0:  # Si l'entité saute et touche un plafond
                        self.rect.top = sprite.rect.bottom  # Bloque le mouvement vers le haut
    
    # Gestion du saut
    def jumping(self):
        if self.injump:
            self.current_time = pygame.time.get_ticks()  # Obtient le temps actuel
        if self.current_time - self.jumping_time <= JUMPTIME:  # Vérifie si le temps de saut n'a pas expiré
            self.direction.y = -1  # Applique une force vers le haut
        else:
            self.injump = False  # Termine le saut une fois le temps écoulé

