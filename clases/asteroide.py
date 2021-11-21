import pygame, random

class Asteroide(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagenAsteroide = pygame.image.load("imagenes/meteorGrey_med1.png").convert()
		self.imagenAsteroide.set_colorkey((0,0,0))
		self.rect = self.imagenAsteroide.get_rect()
		self.velocidad_y = random.randrange(1, 10) #Velocidad aleatoria
		self.velocidad_x = random.randrange(1, 10) #Velocidad aleatoria
		self.rect.x = random.randrange(1000 - 200)
		self.rect.y = random.randrange(-100, -40)

	def recorrido(self, Ancho, Alto):
		self.rect.y += self.velocidad_y
		self.rect.x += self.velocidad_x
		
	def dibujar(self, superficie):
		superficie.blit(self.imagenAsteroide, self.rect)
