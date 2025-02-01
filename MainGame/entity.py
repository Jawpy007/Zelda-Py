import pygame
from settings import JUMPMAX,JUMPTIME
class Entity(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move(self,speed):
        if self.direction.magnitude() != 0:
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
                    if self.current_time-self.jumping_time >= JUMPTIME:
                        self.injump=False
                        self.nbjump=JUMPMAX
                    if self.direction.y < 0: # bouger en haut
                        self.rect.top = sprite.rect.bottom
        
    def jumping(self):
        if self.injump:
            self.current_time=pygame.time.get_ticks()
        if self.current_time-self.jumping_time <= JUMPTIME:
            self.direction.y= -1
        else:
            self.injump=False
