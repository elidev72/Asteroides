import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Asteroides 1.0")
#colores
colorFondo   = (  1, 150,  70)
colorLinea   = (255, 128,   0)
colorCirculo = (255, 255,   0)
colorFiguras = (205,   0, 155)

if __name__ == '__main__':
	while True:
		ventana.fill(colorFondo)
		#lineas
		pygame.draw.line(ventana, colorLinea, (60,90), (200, 100), 20)
		pygame.draw.line(ventana, colorLinea, (80,190), (100, 150), 30)
		pygame.draw.line(ventana, colorLinea, (10,90), (250, 190), 10)

		#circulor
		pygame.draw.circle(ventana, colorCirculo, (400, 450), 100, 30)
		pygame.draw.circle(ventana, colorCirculo, (500, 150), 40, 20)

		#Figuras:
		pygame.draw.rect(ventana, colorFiguras, (100, 250, 120, 250))
		pygame.draw.polygon(ventana, colorFiguras, ((600, 400), (700, 400), (700, 500), (600, 500)))
		
		#Para que cierre al precionar la cruz de la ventana
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			pygame.display.update()