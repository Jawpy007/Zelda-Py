import pygame, sys #Bibliotheque pygame pour la gestion de TOUT le jeu et sys pour gerer la fenetre
from settings import * #Import des settings predefinis voir le fichier concerné
from level import *

class Game:
	def __init__(self):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
		# general setup
		pygame.init() #Initialisation du jeu
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH)) #Affichage de l'écran
		pygame.display.set_caption('Zelda NSI') #Titre de la fenetre
		self.clock = pygame.time.Clock() #variable qui stocke le Temps du jeu
		self.level = Level()

	def run(self):

		#Boucle pour pouvoir quitter le jeu
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			#Parametre d'affichage assez explicite
			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
=======
		# Initialisation générale
		pygame.init()  # Initialise tous les modules pygame
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))  # Crée une fenêtre de jeu avec les dimensions définies
		pygame.display.set_caption('Zelda NSI')  # Définit le titre de la fenêtre
		self.clock = pygame.time.Clock()  # Création d'un objet pour gérer le temps et le taux de rafraîchissement
		self.level_world = Level("world",self)  # Création d'une instance de la classe Level, qui gère la carte et les entités
		self.level_main_menu = Level("main_menu",self)

=======
		# Initialisation générale
		pygame.init()  # Initialise tous les modules pygame
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))  # Crée une fenêtre de jeu avec les dimensions définies
		pygame.display.set_caption('Zelda NSI')  # Définit le titre de la fenêtre
		self.clock = pygame.time.Clock()  # Création d'un objet pour gérer le temps et le taux de rafraîchissement
		self.level_world = Level("world",self)  # Création d'une instance de la classe Level, qui gère la carte et les entités
		self.level_main_menu = Level("main_menu",self)

>>>>>>> Stashed changes
=======
		# Initialisation générale
		pygame.init()  # Initialise tous les modules pygame
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))  # Crée une fenêtre de jeu avec les dimensions définies
		pygame.display.set_caption('Zelda NSI')  # Définit le titre de la fenêtre
		self.clock = pygame.time.Clock()  # Création d'un objet pour gérer le temps et le taux de rafraîchissement
		self.level_world = Level("world",self)  # Création d'une instance de la classe Level, qui gère la carte et les entités
		self.level_main_menu = Level("main_menu",self)

>>>>>>> Stashed changes
		self.all_level_dic={"world":self.level_world,"main_menu":self.level_main_menu}

		self.selected_level=self.all_level_dic["main_menu"]
	
	def change_level(self,level_name):
		self.selected_level=self.all_level_dic[level_name]


	# Fonction principale du jeu
	def run(self):
		# Boucle principale pour maintenir le jeu en cours d'exécution
		while True:
			for event in pygame.event.get():  # Vérifie tous les événements de pygame
				if event.type == pygame.QUIT:  # Si l'utilisateur ferme la fenêtre
					pygame.quit()  # Quitte pygame
					sys.exit()  # Ferme proprement le programme
			

			# Rafraîchissement de l'affichage
			self.screen.fill('black')  # Remplit l'écran de noir pour éviter les traces des images précédentes
			self.selected_level.run()  # Met à jour et affiche le niveau de jeu
			pygame.display.update()  # Met à jour l'affichage
			self.clock.tick(FPS)  # Régule la vitesse d'exécution du jeu pour ne pas dépasser le nombre de FPS défini
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

if __name__ == '__main__':
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
	game = Game()
	game.run()	
=======
	game = Game()  # Crée une instance du jeu

	game.run()  # Lance la boucle du jeu
>>>>>>> Stashed changes
=======
	game = Game()  # Crée une instance du jeu

	game.run()  # Lance la boucle du jeu
>>>>>>> Stashed changes
=======
	game = Game()  # Crée une instance du jeu

	game.run()  # Lance la boucle du jeu
>>>>>>> Stashed changes
