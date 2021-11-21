from funciones import *
from clases import jugador

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
	#menu(ventana, ANCHO, ALTO, ARCHIVO)


	#cargarAsteroides(8)

	#Ciclo del juego:
	jugando = True
	while jugando:

		puntaje = 0
		nivel = 5

		#Indico la imagen del fondo en base al nivel.
		ventana.blit(pygame.image.load("imagenes/espacio" + str(nivel % 6) + ".png"),(0,0))
		#Inserto la nave en la ventana
		nave.dibujar(ventana)

		cargarAsteroides(8,ventana, ANCHO, ALTO)


		#Tiempo:
		#tiempo_Asteroides = pygame.time.get_ticks()
		#mostrarTextoEnPantalla(ventana, str(tiempo_Asteroides), FUENTE, 25, BLANCO, 25, 100)

		"""
		#Crear asteroides:
		if tiempo_Asteroides - contador_Asteroides > 1 and cantidad_Asteroides < 8:
			contador_Asteroides = tiempo_Asteroides
			cantidad_Asteroides += 1
			posX = randint(2, 998)
			cargarAsteroides(posX, 0)

		#Comprobar lista asteroides:
		if len(listaAsteroide) > 0:
			for x in listaAsteroide:
				x.dibujar(ventana)
				x.recorrido(ANCHO, ALTO)
				if x.rect.top > 700:
					lista_Asteroide_En_Ventana.append(x)
					listaAsteroide.remove(x)
					

		#Comprobar que existan asteroides en ventana:
		if len(lista_Asteroide_En_Ventana) == 0:
			for x in lista_Asteroide_En_Ventana:
				if x.rect.top > ANCHO + 10 or x.rect.left < -25 or x.rect.right > ALTO + 25:
					lista_Asteroide_En_Ventana.remove(x)
		"""

		#Disparar proyectil:
		if len(nave.listaDisparo) > 0:
			for x in nave.listaDisparo:
				x.dibujar(ventana)
				x.recorrido()
				if x.rect.top < -10:
					nave.listaDisparo.remove(x)
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
					x, y = nave.rect.center
					nave.disparar(x, y)

			#Pausa del juego.
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_p:
					pause(ventana, 75, ALTO/2 - 50)

		
		#Fin del juego:
		if nave.getVida() == 0:
			jugando = False

		#Vuelvan a aparecer asteroides:


		#Actualizar ventana
		pygame.display.update()
		#Esto controla los FP por segundo
		clock.tick(FPS)