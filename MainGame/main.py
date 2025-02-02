import pygame, sys  # Bibliothèque pygame pour gérer le jeu, et sys pour gérer la fermeture de la fenêtre
from settings import *  # Importation des paramètres prédéfinis
from level import *  # Importation du module Level, qui gère la carte et les entités

# Définition de la classe Game, qui gère l'ensemble du jeu
class Game:
	def __init__(self):
		# Initialisation générale
		pygame.init()  # Initialise tous les modules pygame
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))  # Crée une fenêtre de jeu avec les dimensions définies
		pygame.display.set_caption('Zelda NSI')  # Définit le titre de la fenêtre
		self.clock = pygame.time.Clock()  # Création d'un objet pour gérer le temps et le taux de rafraîchissement
		self.level_world = Level("world",self)  # Création d'une instance de la classe Level, qui gère la carte et les entités
		self.level_main_menu = Level("main_menu",self)

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
			self.selected_level.run()   # Met à jour et affiche le niveau de jeu
			pygame.display.update()  # Met à jour l'affichage
			self.clock.tick(FPS)  # Régule la vitesse d'exécution du jeu pour ne pas dépasser le nombre de FPS défini

# Vérifie si ce fichier est exécuté en tant que programme principal
if __name__ == '__main__':
	game = Game()  # Crée une instance du jeu
	game.run()  # Lance la boucle du jeu
