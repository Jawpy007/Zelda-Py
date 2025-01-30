import pygame, sys #Bibliotheque pygame pour la gestion de TOUT le jeu et sys pour gerer la fenetre
from settings import * #Import des settings predefinis voir le fichier concerné
from level import *

class Game:
	def __init__(self):
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

if __name__ == '__main__':
	game = Game()
	game.run()	