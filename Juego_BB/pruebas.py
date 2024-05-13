import pygame
from pygame import mixer

pygame.init()

screen_width = 800  # Ancho de la pantalla
screen_height = 900  # Alto de la pantalla

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Define el BPM (beats por minuto)
bpm = 13
# Calcula el intervalo de tiempo entre cada beat en milisegundos
beat_interval_ms = (60 * 1000) / bpm

# Establece una velocidad en píxeles por milisegundo para el descenso de las flechas
velocidad_px_ms = 0.1

class Arrow():
    def __init__(self, x, y, image_path, key):
        self.x = x
        self.y = y
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (self.original_image.get_width() // 2, self.original_image.get_height() // 2))
        self.key = key
        self.rect = self.image.get_rect(topleft=(x, y))

keys = [
    Arrow(100, 100, "arrow_left.png", pygame.K_a),
    Arrow(200, 100, "arrow_up.png", pygame.K_s),
    Arrow(300, 100, "arrow_right.png", pygame.K_d),
    Arrow(400, 100, "arrow_right.png", pygame.K_w)
]

def load(map):
    rects = []
    with open(map + ".txt", 'r') as f:
        data = f.readlines()
        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == '0':
                    rects.append(pygame.Rect(keys[x].x, y * -110, 50, 20))
    return rects

map_rect = load("smiths")

# Guarda el tiempo en milisegundos desde que se inició el juego
last_update_time = pygame.time.get_ticks()

# Variable para seguir la posición en el mapa
current_position = 0

# Reproduce la música
mixer.music.load("There Is a Light That Never Goes Out.mp3")
mixer.music.play()

while current_position < len(map_rect):
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    k = pygame.key.get_pressed()
    for key in keys:
        if k[key.key]:
            screen.blit(key.image, key.rect)
        else:
            screen.blit(key.image, key.rect)

    # Calcula el tiempo transcurrido desde la última actualización en milisegundos
    current_time = pygame.time.get_ticks()
    elapsed_time_ms = current_time - last_update_time
    last_update_time = current_time

    for i in range(current_position, len(map_rect)):
        rect = map_rect[i]
        pygame.draw.rect(screen, (200, 0, 0), rect)
        # Mueve la flecha a la velocidad establecida y el tiempo transcurrido
        rect.y += velocidad_px_ms * elapsed_time_ms

        # Si la flecha sale de la pantalla, actualiza la posición actual en el mapa
        if rect.y > screen_height:
            current_position = i + 1

    pygame.display.update()

    clock.tick(60)
