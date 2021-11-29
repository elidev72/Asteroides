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

	#Sonidos:
	sonido_Colision_Asteroide_Disparo = pygame.mixer.Sound("sonidos/explosion.wav")
	pygame.mixer.music.load("sonidos/music.ogg")
	pygame.mixer.music.play(3)
	#Ciclo del juego:
	jugando = True
	while jugando:

		puntaje = 0
		nivel = 1

		#Indico la imagen del fondo en base al nivel.
		ventana.blit(pygame.image.load("imagenes/espacio" + str(nivel % 6) + ".png"),(0,0))
		#Inserto la nave en la ventana
		nave.dibujar(ventana)

		#Cargar Asteroides:
		cantidad = 8
		if len(lista_Asteroide) < cantidad:
			for i in range(cantidad):
				lista_Asteroide.append(Asteroide(randint(1, 10)))
		else:
			for x in lista_Asteroide:
				x.dibujar(ventana)
				x.recorrido(ANCHO, ALTO)
			if x.rect.x > ANCHO - 100 or x.rect.y > ALTO - 50:
				lista_Asteroide.remove(x)


		#Colision asteroide y nave:
		for asteroide in lista_Asteroide:
			if asteroide.rect.colliderect(nave.rect):
						nave.setVida(nave.getVida() - 25)
						lista_Asteroide.remove(asteroide)
						print("Colision: Asteroide / Nave")
					

		#Disparar proyectil:
		if len(nave.listaDisparo) > 0:
			for x in nave.listaDisparo:
				x.dibujar(ventana)
				x.recorrido()
				if x.rect.top < -10:
					nave.listaDisparo.remove(x)
				#Colision disparo asteroide:
				else:
					for meteroritos in lista_Asteroide:
						if x.rect.colliderect(meteroritos.rect):
							lista_Asteroide.remove(meteroritos)
							try:
								nave.listaDisparo.remove(x)
							except ValueError:
								print("Elemento x no esta en la lista")
							sonido_Colision_Asteroide_Disparo.play()
							print("Colision: Asteroide / Disparo ")
 
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


		#Actualizar ventana
		pygame.display.update()
		#Esto controla los FP por segundo
		clock.tick(FPS)

	#Indico el fin del juego.
	#ventana.blit(pygame.image.load("imagenes/espacio.png"),(0,0))
	#mostrarTextoEnPantalla(ventana, "FIN DEL JUEGO", FUENTE, 120, (159,249,174), ANCHO/10, ALTO/12)