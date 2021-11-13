from funciones import *
from clases import *

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
		#Movimiento de la nave, debe estar fuera del for de los eventos o la nave no se movera al mantener la tecla presionada
		nave.mover()

		#Para capturar los eventos que van sucediendo
		for evento in pygame.event.get():
			#Para que cierre al precionar la cruz de la ventana
			if evento.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_SPACE:
					nave.disparar()

			#Pausa del juego
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_p:
					pause(ventana, ANCHO/2, ALTO/2 - 50)

		

		#Actualizar ventana
		pygame.display.update()