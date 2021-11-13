from funciones import *
from clases import *

from pygame.locals import *

#Variables globales:
ANCHO = 800
ALTO = 600

#Boleano juego:
jugando = True

if __name__ == '__main__':
	pygame.init()
	ventana = pygame.display.set_mode((ANCHO, ALTO))

	#Esto decide si se ve o no el mouse, False no se ve y con True si se ve
	pygame.mouse.set_visible(False)
	
	#Titulo:
	pygame.display.set_caption("Asteroides 1.0")

	#Instanciar jugador:
	nave = jugador.Player(ANCHO, ALTO)

	#Ciclo del juego:
	while True:
		#Imagen de fondo:
		ventana.blit(pygame.image.load("imagenes/background.png"),(0,0))

		#Inserto la nave en la ventana
		nave.dibujar(ventana)

		#Para que cierre al precionar la cruz de la ventana
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			#Pausa del juego
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_p:
					#Mostrar que el juego esta en pausa
					mostrarTextoEnPantalla(ventana, "Juego en pausa, presione C para seguir jugando", "Arial", 40, ( 255, 255, 255), ANCHO/2, ALTO/2 - 50)
					pygame.display.update() #esto es necesario o de lo contrario el cartel anterior no aparecera
					pause()

		#Movimiento de la nave, debe estar fuera del for de los eventos o la nave no se movera al mantener la tecla presionada
		nave.mover(pygame.key.get_pressed())

		pygame.display.update()