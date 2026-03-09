import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Configuración de pantalla
ANCHO = 600
ALTO = 400
TAM_CELDA = 20

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Vibora")

reloj = pygame.time.Clock()

# Función para dibujar la serpiente
def dibujar_serpiente(serpiente):
    for bloque in serpiente:
        pygame.draw.rect(pantalla, VERDE, [bloque[0], bloque[1], TAM_CELDA, TAM_CELDA])

# Función principal del juego
def juego():
    x = ANCHO // 2
    y = ALTO // 2

    dx = 0
    dy = 0

    serpiente = []
    longitud = 1

    comida_x = random.randrange(0, ANCHO, TAM_CELDA)
    comida_y = random.randrange(0, ALTO, TAM_CELDA)

    puntaje = 0
    fuente = pygame.font.SysFont(None, 35)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    dx = -TAM_CELDA
                    dy = 0
                elif evento.key == pygame.K_RIGHT:
                    dx = TAM_CELDA
                    dy = 0
                elif evento.key == pygame.K_UP:
                    dy = -TAM_CELDA
                    dx = 0
                elif evento.key == pygame.K_DOWN:
                    dy = TAM_CELDA
                    dx = 0

        x += dx
        y += dy

        # Verificar colisión con bordes
        if x < 0 or x >= ANCHO or y < 0 or y >= ALTO:
            break

        pantalla.fill(NEGRO)

        # Dibujar comida
        pygame.draw.rect(pantalla, ROJO, [comida_x, comida_y, TAM_CELDA, TAM_CELDA])

        cabeza = [x, y]
        serpiente.append(cabeza)

        if len(serpiente) > longitud:
            del serpiente[0]

        # Verificar colisión consigo misma
        for bloque in serpiente[:-1]:
            if bloque == cabeza:
                return

        dibujar_serpiente(serpiente)

        # Verificar si come la manzana
        if x == comida_x and y == comida_y:
            comida_x = random.randrange(0, ANCHO, TAM_CELDA)
            comida_y = random.randrange(0, ALTO, TAM_CELDA)
            longitud += 1
            puntaje += 1

        texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
        pantalla.blit(texto, [10, 10])

        pygame.display.update()
        reloj.tick(10)

    pygame.quit()
    sys.exit()

juego()