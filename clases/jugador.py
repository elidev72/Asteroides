import pygame
from clases import disparo

class Jugador(pygame.sprite.Sprite):
	"""
	    PRE: El Player no debe haber sido creado, ancho e alto deben ser las dimenciones de alto y
	    ancho de la ventana siendo estos valores de tipo numericos.
	    POST: El Player queda creado.
	"""
	def __init__(self, ancho, alto):
		pygame.sprite.Sprite.__init__(self)
		self.imagenNave = pygame.image.load("imagenes/nave.png").convert()
		self.imagenNave.set_colorkey((   0,   0,   0))
		#Rectangulo imagen:
		self.rect = self.imagenNave.get_rect()

		#Posicion inicial nave:
		self.tamanio_Ancho = ancho
		self.tamanio_Alto = alto
		self.rect.centerx = ancho/2
		self.rect.centery = alto - 50
		self.velocidad = 10
		self.maxHP = 100
		self.vida = self.maxHP
		self.listaDisparo = []

#---------------------------------------------------Metodos-------------------------------------------------
#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Player debe haber sido creado.
	    POST: Indico el nuevo valor que le asigno a la vida del Player.
	"""
	def setVida(self, hp):
		self.vida = hp
#-------------------------------------------------Fin metodo------------------------------------------------

#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Player debe haber sido creado.
	    POST: Devuelvo el valor almacenado en la vida del Player.
	"""
	def getVida(self):
		return self.vida
#-------------------------------------------------Fin metodo------------------------------------------------

#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Player debe haber sido creado.
	    POST: Devuelvo el valor maximo de vida que puede poseer el jugador.
	"""
	def getMaxHP(self):
		return self.maxHP
#

#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Player debe haber sido creado.
	    POST: El Player se mueve por la ventana.
	"""
	def mover(self):
		if self.vida > 0:

			keystate = pygame.key.get_pressed()

			if keystate[pygame.K_LEFT]:
				self.rect.left -= self.velocidad
			if keystate[pygame.K_RIGHT]:
				self.rect.right += self.velocidad
			if keystate[pygame.K_UP]:
				self.rect.centery -= self.velocidad
			if keystate[pygame.K_DOWN]:
				self.rect.centery += self.velocidad

			#Para que no se salga del recuadro:
			if self.rect.left <= 0:
				self.rect.left = 0
			if self.rect.right > self.tamanio_Ancho - 10:
				self.rect.right = self.tamanio_Ancho - 10
			if self.rect.centery > self.tamanio_Alto - 50:
				self.rect.centery = self.tamanio_Alto - 50
			if self.rect.centery < 50:
				self.rect.centery = 50
#-------------------------------------------------Fin metodo------------------------------------------------

#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Player debe haber sido creado, y debo pasarle las coordenadas x e y de la nave.
	    POST: El Player dispara.
	"""
	def disparar(self, x, y):
		#el -21 es para que el disparo salga desde el centro de la nave
		self.listaDisparo.append(disparo.Disparo(x - 21, y - 60))
#-------------------------------------------------Fin metodo------------------------------------------------

#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Player debe haber sido creado.
	    POST: El Player es colocado en la ventana del juego.
	"""
	def dibujar(self, superficie):
		superficie.blit(self.imagenNave, self.rect)
#-------------------------------------------------Fin metodo------------------------------------------------