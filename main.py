from funciones import *
from clases import jugador

#Variables globales:
ANCHO = 1000
ALTO = 750
ARCHIVO = "top10Puntajes.txt"

if __name__ == '__main__':
	pygame.init()
	ventana = pygame.display.set_mode((ANCHO, ALTO))
	
	#Titulo:
	pygame.display.set_caption(NOMBRE_JUEGO)

	#Instanciar jugador:
	nave = jugador.Jugador(ANCHO, ALTO)

	#Sonidos:
	sonido_Colision_Asteroide_Disparo = pygame.mixer.Sound("sonidos/explosion.wav")
	pygame.mixer.music.load("sonidos/music.ogg")
	#con esto la musica quede en loop:
	#pygame.mixer.music.play(loops=-1)

	while True:
		#Menu de opciones inicial del juego:
		menu(ventana, ANCHO, ALTO, ARCHIVO)
		pygame.mouse.set_visible(False)

		nivel = 1
		puntaje = 0
		#Ciclo del juego:
		jugando = True
		while jugando:

			#danio = nivel * 2
			danio = 100
			#Con esto actualiza el nivel cada 90 segundos
			tiempo = pygame.time.get_ticks()
			if tiempo > (90000 * nivel):
				nivel += 1
				if nave.vida < nave.maxHP:
					if danio <= (nave.maxHP - nave.vida):
						nave.vida += danio
					else:
						nave.vida = nave.maxHP
			
			#Indico la imagen del fondo en base al nivel.
			ventana.blit(pygame.image.load("imagenes/espacio" + str(nivel % 6) + ".png"),(0,0))

			#Inserto la nave en la ventana
			nave.dibujar(ventana)

			#Cargar Asteroides:
			cantidad = int(nivel * 0.3 * 16)
			if len(lista_Asteroide) < cantidad:
				for i in range(cantidad):
					#Indico de forma aleatoria la imagen de cual asteroide cargar.
					lista_Asteroide.append(Asteroide(randint(1, 10)))
				del i
			else:
				for x in lista_Asteroide:
					x.dibujar(ventana)
					x.recorrido(ANCHO, ALTO)
				if x.rect.x > ANCHO - 100 or x.rect.y > ALTO - 50:
					lista_Asteroide.remove(x)
				del x
			del cantidad

			#Colision asteroide y nave:
			for asteroide in lista_Asteroide:
				if asteroide.rect.colliderect(nave.rect):
							if nave.vida > danio:
								nave.vida -= danio
							else:
								nave.vida = 0

							lista_Asteroide.remove(asteroide)
			del asteroide
						
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
								puntaje += 10
								lista_Asteroide.remove(meteroritos)
								try:
									nave.listaDisparo.remove(x)
								except ValueError:
									pass
								sonido_Colision_Asteroide_Disparo.play()
						del meteroritos
				del x
	 
			#Movimiento de la nave, debe estar fuera del for de los eventos o la nave no se movera al mantener la tecla presionada
			nave.mover()

			#Barra de HP de la nave:
			barraDeHP(ventana, 5,5, nave.vida, nave.maxHP)
			#Actualizar ventana mostrando el texto (la función internamente lo hace)
			mostrarTextoEnPantalla(ventana, "Puntos: " + str(puntaje) + " --- Nivel: " + str(nivel), FUENTE, 25, BLANCO, ANCHO//2.5, 10) 

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
			if nave.vida == 0:
				jugando = False

		#Indico el fin del juego.
		#Esto decide si se ve o no el mouse, False no se ve y con True si se ve:
		pygame.mouse.set_visible(True)
		finDeLaPartida(ventana, puntaje, nivel, ANCHO, ALTO, ARCHIVO)