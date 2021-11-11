import pygame, sys
from pygame.locals import *
from clases import *

#Variables globales:
ANCHO = 800
ALTO = 600

if __name__ == '__main__':
	pygame.init()
	ventana = pygame.display.set_mode((ANCHO, ALTO))

	#Imagen de fondo:
	fondo = pygame.image.load("imagenes/background.png")
	ventana.blit(fondo,(0,0))

	#Titulo:
	pygame.display.set_caption("Asteroides 1.0")

	#Ciclo del juego:
	while True:
		#Para que cierre al precionar la cruz de la ventana
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			pygame.display.update()