import pygame

pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Configuración de la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Ritmo")

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Carga y reproducción de música
pygame.mixer.music.load("There Is a Light That Never Goes Out.mp3")
pygame.mixer.music.play(-1)  # Reproducción en bucle

bpm = 136
beat_interval_ms = (60 * 1000) / bpm
velocidad_px_ms = 3

flecha_width = 100
flecha_height = 100

flechas = []

referencia_images = {
    "left": pygame.transform.scale(pygame.image.load("arrow_left.png").convert_alpha(), (flecha_width, flecha_height)),
    "up": pygame.transform.scale(pygame.image.load("arrow_up.png").convert_alpha(), (flecha_width, flecha_height)),
    "down": pygame.transform.scale(pygame.image.load("arrow_down.png").convert_alpha(), (flecha_width, flecha_height)),
    "right": pygame.transform.scale(pygame.image.load("arrow_right.png").convert_alpha(), (flecha_width, flecha_height))
}

referencia_positions = {
    "left": (300, 500),
    "up": (400, 500),
    "down": (500, 500),
    "right": (600, 500)
}

# Función para generar flechas según las configuraciones del archivo
def generar_flechas(file_path, beat_count):
    with open('smiths.txt', 'r') as file:
        lines = file.readlines()
        if beat_count < len(lines):
            config = lines[beat_count].strip()
            for i, char in enumerate(config):
                if char != '0':
                    columna = "left" if i == 0 else "up" if i == 1 else "down" if i == 2 else "right"
                    if columna == "left":
                        x = 300
                    elif columna == "up":
                        x = 400
                    elif columna == "down":
                        x = 500
                    elif columna == "right":
                        x = 600
                    y = 50
                    flecha = Flecha(referencia_images[columna], x, y, velocidad_px_ms)
                    flechas.append(flecha)

class Flecha(pygame.sprite.Sprite):
    def __init__(self, image, x, y, velocidad):
        super().__init__()
        self.image = image
        # Modificar las dimensiones del rectángulo de colisión
        nuevo_ancho = 10  # Ancho deseado
        nuevo_alto = 10   # Alto deseado
        self.rect = pygame.Rect(x, y, nuevo_ancho, nuevo_alto)
        self.velocidad = velocidad

    def update(self):
        self.rect.y += self.velocidad

# Inicialización de variables
tiempo_ultimo_beat = pygame.time.get_ticks()
beat_count = 0
puntos = 0

# Fuente para el texto del puntaje
font = pygame.font.SysFont(None, 36)

# Bucle principal del juego
running = True
while running:
    # Control de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if any(flecha.rect.colliderect(referencia_images["left"].get_rect(topleft=referencia_positions["left"])) for flecha in flechas):
                    puntos += 1
            elif event.key == pygame.K_UP:
                if any(flecha.rect.colliderect(referencia_images["up"].get_rect(topleft=referencia_positions["up"])) for flecha in flechas):
                    puntos += 1
            elif event.key == pygame.K_DOWN:
                if any(flecha.rect.colliderect(referencia_images["down"].get_rect(topleft=referencia_positions["down"])) for flecha in flechas):
                    puntos += 1
            elif event.key == pygame.K_RIGHT:
                if any(flecha.rect.colliderect(referencia_images["right"].get_rect(topleft=referencia_positions["right"])) for flecha in flechas):
                    puntos += 1

    # Generar flechas en cada beat
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - tiempo_ultimo_beat >= beat_interval_ms:
        generar_flechas("file.txt", beat_count)
        tiempo_ultimo_beat = tiempo_actual
        beat_count += 1

    # Actualizar la posición de las flechas
    for flecha in flechas:
        flecha.update()

    # Eliminar las flechas que salen de la pantalla
    flechas = [flecha for flecha in flechas if flecha.rect.top < screen_height]

    # Dibujar todo en la pantalla
    screen.fill(WHITE)
    for flecha in flechas:
        screen.blit(flecha.image, flecha.rect)

    # Dibujar imágenes de referencia
    for direction, image in referencia_images.items():
        screen.blit(image, referencia_positions[direction])

    # Mostrar puntaje en la pantalla
    score_text = font.render(f"Puntaje: {puntos}", True, GREEN)
    screen.blit(score_text, (screen_width - score_text.get_width() - 10, 10))

    pygame.display.flip()

    # Control de la velocidad del juego
    clock.tick(60)

pygame.quit()

