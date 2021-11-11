import pygame, sys
from pygame.locals import *

#nombre color - rgb - codigo hexagono
verde    = (  1, 150,  70) #019646
naranja  = (255, 128,   0) #FF8000
amarillo = (255, 255,   0) #FFFF00
violeta  = (205,   0, 155) #CD009B

if __name__ == '__main__':
	pygame.init()
	ventana = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Practica Inicial")
	
	while True:
		#color de ventana
		ventana.fill(verde)

		#lineas
		pygame.draw.line(ventana, naranja, (60,90), (200, 100), 20)
		pygame.draw.line(ventana, naranja, (80,190), (100, 150), 30)
		pygame.draw.line(ventana, naranja, (10,90), (250, 190), 10)

		#circulor
		pygame.draw.circle(ventana, amarillo, (400, 450), 100, 30)
		pygame.draw.circle(ventana, amarillo, (500, 150), 40, 20)

		#Figuras:
		pygame.draw.rect(ventana, violeta, (100, 250, 120, 250))
		pygame.draw.polygon(ventana, violeta, ((600, 400), (700, 400), (700, 500), (600, 500)))

		#Para que cierre al precionar la cruz de la ventana
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			pygame.display.update()