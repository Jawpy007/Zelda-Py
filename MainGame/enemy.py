import pygame
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):
	def __init__(self,monster_name,pos,groups,obstacle_sprites):

		# Initialisation générale de l'ennemi
		super().__init__(groups)
		self.sprite_type = 'enemy'  # Définit ce sprite comme un ennemi

		# Chargement des animations
		self.import_graphics(monster_name)
		self.status = 'idle'  # État initial de l'ennemi
		self.image = self.animations[self.status][self.frame_index]  # Définition de l'image initiale

		# Position et collision
		self.rect = self.image.get_rect(topleft = pos)  # Définition de la position initiale
		self.hitbox = self.rect.inflate(0,-10)  # Ajustement de la hitbox
		self.obstacle_sprites = obstacle_sprites  # Liste des obstacles pour la gestion des collisions

		# Chargement des caractéristiques de l'ennemi
		self.monster_name = monster_name  # Nom du monstre
		monster_info = monster_data[self.monster_name]  # Récupération des informations depuis un dictionnaire
		self.health = monster_info['health']  # Points de vie
		self.exp = monster_info['exp']  # Points d'expérience donnés au joueur
		self.speed = monster_info['speed']  # Vitesse de déplacement
		self.attack_damage = monster_info['damage']  # Dégâts d'attaque
		self.resistance = monster_info['resistance']  # Résistance aux attaques
		self.attack_radius = monster_info['attack_radius']  # Portée d'attaque
		self.notice_radius = monster_info['notice_radius']  # Distance à laquelle il détecte le joueur
		self.attack_type = monster_info['attack_type']  # Type d'attaque

		# Interaction avec le joueur
		self.can_attack = True  # Vérifie si l'ennemi peut attaquer
		self.attack_time = None  # Temps de la dernière attaque
		self.attack_cooldown = 400  # Temps d'attente entre deux attaques

	def import_graphics(self,name):
		# Chargement des animations de l'ennemi
		self.animations = {'idle':[],'move':[],'attack':[]}  # Création du dictionnaire des animations
		main_path = f'graphics/monsters/{name}/'  # Chemin du dossier contenant les images
		for animation in self.animations.keys():  # Pour chaque type d'animation
			self.animations[animation] = import_folder(main_path + animation)  # Chargement des images correspondantes

	def get_player_distance_direction(self,player):
		# Calculer la distance et la direction entre l'ennemi et le joueur
		enemy_vec = pygame.math.Vector2(self.rect.center)  # Position de l'ennemi
		player_vec = pygame.math.Vector2(player.rect.center)  # Position du joueur
		distance = (player_vec - enemy_vec).magnitude()  # Calcul de la distance

		if distance > 0:
			direction = (player_vec - enemy_vec).normalize()  # Normalisation pour obtenir un vecteur directionnel
		else:
			direction = pygame.math.Vector2()  # Si la distance est nulle, pas de direction

		return (distance,direction)

	def get_status(self, player):
		# Mise à jour du statut en fonction de la distance du joueur
		distance = self.get_player_distance_direction(player)[0]

		if distance <= self.attack_radius and self.can_attack:
			if self.status != 'attack':
				self.frame_index = 0  # Réinitialisation de l'animation
			self.status = 'attack'  # Passer en mode attaque
		elif distance <= self.notice_radius:
			self.status = 'move'  # Passer en mode déplacement vers le joueur
		else:
			self.status = 'idle'  # Rester immobile

	def actions(self,player):
		# Effectuer des actions en fonction du statut
		if self.status == 'attack':
			self.attack_time = pygame.time.get_ticks()  # Stocker le moment de l'attaque
			print('attack')  # Débogage
		elif self.status == 'move':
			self.direction = self.get_player_distance_direction(player)[1]  # Se diriger vers le joueur
		else:
			self.direction = pygame.math.Vector2()  # Ne pas bouger

	def animate(self):
		# Gestion des animations
		animation = self.animations[self.status]  # Récupérer l'animation correspondant au statut
		
		self.frame_index += self.animation_speed  # Passer au frame suivant
		if self.frame_index >= len(animation):
			if self.status == 'attack':
				self.can_attack = False  # Désactiver temporairement les attaques après une animation
			self.frame_index = 0  # Réinitialiser l'animation

		self.image = animation[int(self.frame_index)]  # Mettre à jour l'image
		self.rect = self.image.get_rect(center = self.hitbox.center)  # Ajuster la hitbox

	def cooldown(self):
		# Gestion du cooldown d'attaque
		if not self.can_attack:
			current_time = pygame.time.get_ticks()  # Récupérer le temps actuel
			if current_time - self.attack_time >= self.attack_cooldown:
				self.can_attack = True  # Réactiver l'attaque après le cooldown

	def update(self):
		# Mettre à jour l'ennemi chaque frame
		self.move(self.speed)  # Déplacement
		self.animate()  # Animation
		self.cooldown()  # Gestion du cooldown

	def enemy_update(self,player):
		# Met à jour les comportements spécifiques de l'ennemi par rapport au joueur
		self.get_status(player)  # Mise à jour du statut
		self.actions(player)  # Effectuer l'action appropriée