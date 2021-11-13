import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, ANCHO, ALTO):
		pygame.sprite.Sprite.__init__(self)
		self.imagenNave = pygame.image.load("Imagenes/player.png").convert()
		self.imagenNave.set_colorkey((   0,   0,   0))
		#Rectangulo imagen:
		self.rect = self.imagenNave.get_rect()

		#Posicion inicial nave:
		self.tamanio_Ancho = ANCHO
		self.tamanio_Alto = ALTO
		self.rect.centerx = ANCHO/2
		self.rect.centery = ALTO - 50
		self.velocidad = 10
		self. vida = 100
		self.listaDisparo = []

#---------------------------------------------------Metodos-------------------------------------------------
#-----------------------------------------------Inicio metodo-----------------------------------------------
	def mover(self, keystate):
		if self.vida > 0:

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
	def disparar(self):
		pass
#-------------------------------------------------Fin metodo------------------------------------------------

#-----------------------------------------------Inicio metodo-----------------------------------------------
	def dibujar(self, superficie):
		superficie.blit(self.imagenNave, self.rect)
#-------------------------------------------------Fin metodo------------------------------------------------