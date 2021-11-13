import pygame, sys

def pause():
    pausado = True

    while pausado:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False

def mostrarTextoEnPantalla(ventana, texto, tipo_De_Letra, tamanio_De_Letra, color, x, y):
    font = pygame.font.SysFont(tipo_De_Letra, tamanio_De_Letra)
    texto_Ventana = font.render(texto, True, color)
    texto_Recta = texto_Ventana.get_rect()
    texto_Recta.midtop = (x, y)
    ventana.blit(texto_Ventana, texto_Recta)