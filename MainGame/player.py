import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, obstacle_sprites):
        super().__init__(groups) #Initialisation de la classe parent

        self.image = pygame.image.load('graphics/test/player.png')
        self.rect = self.image.get_rect(topleft = pos)

		# movement 
        self.direction = pygame.math.Vector2()
        self.speed = PLAYERSPEED

        self.obstacle_sprites = obstacle_sprites

    
    def input(self): #récupération des input du joueur
        keys = pygame.key.get_pressed()

        # movement input
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def move(self,speed):
        if self.direction.magnitude() != 0: #obligatoire car un vecteur de 0 ne peut pas etre normalize()
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        #self.rect.center = self.direction * speed
    
    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # bouger a droite
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # bouger a gauche
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # bouger en bas
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # bouger en haut
                        self.rect.top = sprite.rect.bottom
						
    def update(self):
        self.input()
        self.move(self.speed)