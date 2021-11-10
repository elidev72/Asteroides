import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Asteroides 1.0")
colorFondo = (1, 150, 70)

while True:
	ventana.fill(colorFondo)
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		pygame.display.update()