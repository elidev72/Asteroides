import pygame, random

class Asteroide(pygame.sprite.Sprite):
	"""
	    PRE: El Asteroide no debe haber sido creado, indicar el numero de imagen que se desea utilizar.
	    POST: El Asteroide queda creado.
	"""
	def __init__(self, numero):
		pygame.sprite.Sprite.__init__(self)
		self.imagenAsteroide = pygame.image.load("imagenes/meteorito" + str(numero) + ".png").convert()
		self.imagenAsteroide.set_colorkey((0,0,0))
		self.rect = self.imagenAsteroide.get_rect()
		self.velocidad_y = random.randrange(1, 5) #Velocidad aleatoria
		self.velocidad_x = random.randrange(1, 5) #Velocidad aleatoria
		self.rect.x = random.randrange(1000 - 200)
		self.rect.y = random.randrange(-100, -40)
#---------------------------------------------------Metodos-------------------------------------------------

#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Asteroide debe haber sido creado.
	    POST: El Asteroide se mueve por la ventana.
	"""
	def recorrido(self, Ancho, Alto):
		self.rect.y += self.velocidad_y
		self.rect.x += self.velocidad_x
#-------------------------------------------------Fin metodo------------------------------------------------

#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Asteroide debe haber sido creado.
	    POST: El Asteroide es colocado en la ventana del juego.
	"""
	def dibujar(self, superficie):
		superficie.blit(self.imagenAsteroide, self.rect)
#-------------------------------------------------Fin metodo------------------------------------------------