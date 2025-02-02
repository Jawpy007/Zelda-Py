import pygame
from settings import *

# Définition de la classe Player qui hérite de pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups, obstacle_sprites):
		super().__init__(groups) #Initialisation de la classe parent

		self.image = pygame.image.load('graphics/test/player.png')
		self.rect = self.image.get_rect(topleft = pos)

		# movement 
		self.direction = pygame.math.Vector2()
		self.speed = PLAYERSPEED
		self.injump=False
		self.jumping_time=pygame.time.get_ticks()
		self.current_time=pygame.time.get_ticks()
		self.nbjump=JUMPMAX
		self.player_running=False


		self.obstacle_sprites = obstacle_sprites

		self.player_xp_level=1
		self.stats={"health": [BASE_PLAYER_HEALTH, BASE_PLAYER_HEALTH], "xp": [BASE_PLAYER_XP,100], "energy": [BASE_PLAYER_ENERGY,BASE_PLAYER_ENERGY]} #[min,max]

	#	print(self.stats_updates("health", -10))
	#	print(self.stats_updates("energy", 10))
	#	print(self.stats_updates("xp", -10))

	
	def input(self): 
		#récupération des input du joueur
		keys = pygame.key.get_pressed()
		
		# movement input
		if not(self.injump) and self.nbjump>0:
			if keys[pygame.K_SPACE]:
				self.injump=True
				self.nbjump-=1
				self.jumping_time=pygame.time.get_ticks()
			else:
				self.direction.y = 1
		elif not(self.current_time-self.jumping_time <= JUMPTIME):
			self.direction.y = 1
		
		if keys[pygame.K_LSHIFT]:
			self.player_running=True
		else:
			self.player_running=False

		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT] or keys[pygame.K_q]:
			self.direction.x = -1
		else:
			self.direction.x = 0





	
	def move(self,speed):
		if self.direction.magnitude() != 0: #obligatoire car un vecteur de 0 ne peut pas etre normalize()
			self.direction = self.direction.normalize()

		self.rect.x += self.direction.x * speed*2 if self.player_running else self.direction.x * speed
		self.collision('horizontal')
		if self.direction.y>0:
			self.rect.y += self.direction.y * speed*2
		if self.direction.y<0:
			self.rect.y += self.direction.y * (speed*2)
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

			
	def stats_updates(self,stats_name,value_update, max_value=None): #si max value none on change pas le max
		if max_value!=None:
			self.stats[stats_name][1]=max_value
		
		if value_update+self.stats[stats_name][0]>self.stats[stats_name][1]:
			if stats_name=="health":
				self.stats[stats_name][0]=self.stats[stats_name][1]
			if stats_name=="energy":
				self.stats[stats_name][0]=self.stats[stats_name][1]
			if stats_name=="xp":
				self.stats[stats_name][0]=0
				self.player_level_up()

		elif value_update+self.stats[stats_name][0]<=0:
			if stats_name=="health":
				self.stats[stats_name][0]=0
				self.player_death()
			if stats_name=="energy":
				return(False)
			if stats_name=="xp":
				reste=value_update+self.stats[stats_name][0]
				self.stats[stats_name][0]=self.stats[stats_name][1]				
				self.player_level_up(-1)
				self.stats_updates("xp",(reste))
		else:
			self.stats[stats_name][0]+=value_update
		return True

	def player_death(self):
		print("mort")
	
	def player_level_up(self, value=1):
		print("level up")
		self.player_xp_level+=value
		print(self.player_xp_level)

	def update(self):
		self.input()
		self.jumping()
		self.move(self.speed)

class player_inventory:
	def __init__(self,Player,items_sprites):
		self.item_dic={}
	
	def get_inventory(self):
		return(self.item_dic)
	
class collectable_items(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups) #Initialisation de la classe parent

        self.image = pygame.image.load('graphics/test/rock.png')
        self.rect = self.image.get_rect(topleft = pos)