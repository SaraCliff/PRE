import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movimiento vertical de imagen")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Cargar la imagen
image = pygame.image.load("Assets/FONDOmain.png")
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 0.1))

# Posiciones inicial y final
y_initial = HEIGHT
y_final = 0
y_punto= HEIGHT // 2

def move_vertical():
    clock = pygame.time.Clock()
    contador = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Verificar si es un evento de tecla presionada
                if event.key == pygame.K_UP:  # Verificar si la tecla presionada es la flecha hacia arriba
                    # Verificar si la imagen está dentro del rango con un error de +/- 10
                    if y_punto - 10 <= image_rect.y <= y_punto + 10:
                        contador += 1
                        print("Contador:", contador)

        # Movimiento vertical de la imagen
        start_time = pygame.time.get_ticks()
        while True:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - start_time
            if elapsed_time > 1000:  # Duración de 1 segundo
                break
            y = y_initial + (y_punto - y_initial) * (elapsed_time / 1000)
            image_rect.y = y

            # Limpiar la pantalla
            screen.fill(WHITE)

            # Dibujar imagen en la nueva posición
            screen.blit(image, image_rect)

            # Dibujar punto rojo en la posición final
            pygame.draw.circle(screen, RED, (WIDTH // 2, y_punto), 5)

            # Mostrar contador en la pantalla
            font = pygame.font.Font(None, 36)
            text = font.render("Contador: " + str(contador), True, BLACK)
            screen.blit(text, (10, 10))

            # Actualizar pantalla
            pygame.display.flip()

            # Controlar la frecuencia de actualización
            clock.tick(60)  # 60 fotogramas por segundo

        # Reiniciar la posición inicial de la imagen
        image_rect.y = y_initial

move_vertical()




