from funciones import *
from clases import *

#Variables globales:
ANCHO = 1000
ALTO = 750
ARCHIVO = "top10Puntajes.txt"

if __name__ == '__main__':
	pygame.init()
	ventana = pygame.display.set_mode((ANCHO, ALTO))

	#Esto decide si se ve o no el mouse, False no se ve y con True si se ve
	#pygame.mouse.set_visible(False)
	
	#Titulo:
	pygame.display.set_caption(NOMBRE_JUEGO)

	#Instanciar jugador:
	nave = jugador.Jugador(ANCHO, ALTO)

	#Menu de opciones inicial del juego:
	menu(ventana, ANCHO, ALTO, ARCHIVO)

	#Ciclo del juego:
	jugando = True
	while jugando:
		puntaje = 0
		nivel = 1

		#Indico la imagen del fondo en base al nivel.
		ventana.blit(pygame.image.load("imagenes/espacio" + str(nivel % 6) + ".png"),(0,0))

		#Inserto la nave en la ventana
		nave.dibujar(ventana)
		#Movimiento de la nave, debe estar fuera del for de los eventos o la nave no se movera al mantener la tecla presionada
		nave.mover()

		#Para capturar los eventos que van sucediendo
		for evento in pygame.event.get():
			#Para que cierre al precionar la cruz de la ventana.
			if evento.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			#Para que cierre al precionar la tecla escape.
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

			#Para que la nave dispare.
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_SPACE:
					nave.disparar()

			#Pausa del juego.
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_p:
					pause(ventana, 75, ALTO/2 - 50)

		
		#Fin del juego:
		if nave.getVida() == 0:
			jugando = False

		#Actualizar ventana
		pygame.display.update()
		#Esto controla los FP por segundo
		clock.tick(FPS)