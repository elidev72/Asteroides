import pygame

class Disparo(pygame.sprite.Sprite):
	"""
	    PRE: El Disparo no debe haber sido creado, indicar las posiciones del disparo.
	    POST: El Disparo queda creado.
	"""
	def __init__(self, posX, posY):
		pygame.sprite.Sprite.__init__(self)
		self.imagenDisparo = pygame.image.load("imagenes/laser1.png")
		self.rect = self.imagenDisparo.get_rect()
		self.velocidad_Disparo = 10
		self.rect.top = posY
		self.rect.left = posX

#---------------------------------------------------Metodos-------------------------------------------------

#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Disparo debe haber sido creado.
	    POST: El Disparo se mueve por la ventana.
	"""
	def recorrido(self):
		self.rect.top -= self.velocidad_Disparo
#-------------------------------------------------Fin metodo------------------------------------------------

#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Disparo debe haber sido creado.
	    POST: El Disparo es colocado en la ventana del juego.
	"""
	def dibujar(self, superficie):
		superficie.blit(self.imagenDisparo, self.rect)
#-------------------------------------------------Fin metodo------------------------------------------------