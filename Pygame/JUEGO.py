import pygame
import sys
from button import Database
from Top_puntuacion import top_puntuacion

pygame.init()

screen_width = 1280
screen_height = 720
ancho = 250
alto = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Ritmo")

fondo_de_pantalla = pygame.image.load("FONDO_CUPIDO.png").convert()
fondo_de_pantalla = pygame.transform.scale(fondo_de_pantalla, (screen_width, screen_height))

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

clock = pygame.time.Clock()

pygame.mixer.music.load("There Is a Light That Never Goes Out.mp3")
pygame.mixer.music.play(0)  # Reproducción en bucle

bpm = 136
beat_interval_ms = (60 * 1000) / bpm
corchea_interval_ms = beat_interval_ms / 2  # Corcheas al doble de velocidad
velocidad_px_ms = 10

flecha_width = 500
flecha_height = 500
collision_rect_margin = 60  # Margen de 60 píxeles

generada_collision_width = 20
generada_collision_height = 20

flechas = []

referencia_images = {
    "left": pygame.transform.scale(pygame.image.load("arrow_left.png").convert_alpha(), (flecha_width, flecha_height)),
    "up": pygame.transform.scale(pygame.image.load("arrow_up.png").convert_alpha(), (flecha_width, flecha_height)),
    "down": pygame.transform.scale(pygame.image.load("arrow_down.png").convert_alpha(), (flecha_width, flecha_height)),
    "right": pygame.transform.scale(pygame.image.load("arrow_right.png").convert_alpha(), (flecha_width, flecha_height))
}

referencia_positions = {
    "left": (50, 50),
    "up": (150, 50),
    "down": (250, 50),
    "right": (350, 50)
}

class Flecha(pygame.sprite.Sprite):
    def __init__(self, image, x, y, velocidad):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocidad = velocidad
        self.collision_rect = pygame.Rect(
            self.rect.centerx - generada_collision_width // 2,
            self.rect.centery - generada_collision_height // 2,
            generada_collision_width,
            generada_collision_height
        )

    def update(self):
        self.rect.y -= self.velocidad
        self.collision_rect.y = self.rect.centery - generada_collision_height // 2

class Paula(pygame.sprite.Sprite):
    def __init__(self, images, x, y):
        super().__init__()
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]

def generar_flechas(file_path, beat_count, corchea):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if beat_count < len(lines):
            config = lines[beat_count].strip()
            for i, char in enumerate(config):
                if corchea and char in '5678':
                    columna = "left" if char == '5' else "up" if char == '6' else "down" if char == '7' else "right"
                    x = referencia_positions[columna][0]
                    y = screen_height - 10
                    flecha = Flecha(referencia_images[columna], x, y, velocidad_px_ms)
                    flechas.append(flecha)
                elif not corchea and char in '1234':
                    columna = "left" if char == '1' else "up" if char == '2' else "down" if char == '3' else "right"
                    x = referencia_positions[columna][0]
                    y = screen_height - 10
                    flecha = Flecha(referencia_images[columna], x, y, velocidad_px_ms)
                    flechas.append(flecha)

def chequear_colision(flecha, posicion_referencia):
    return flecha.collision_rect.colliderect(pygame.Rect(
        posicion_referencia[0] + flecha_width // 2 - collision_rect_margin,
        posicion_referencia[1] + flecha_height // 2 - collision_rect_margin,
        collision_rect_margin * 2, collision_rect_margin * 2))

def manejar_colision(tecla):
    global puntos

    teclas_posiciones = {
        pygame.K_LEFT: referencia_positions["left"],
        pygame.K_UP: referencia_positions["up"],
        pygame.K_DOWN: referencia_positions["down"],
        pygame.K_RIGHT: referencia_positions["right"]
    }

    teclas_imagenes = {
        pygame.K_LEFT: paula_images["izquierda"],
        pygame.K_UP: paula_images["arriba"],
        pygame.K_DOWN: paula_images["abajo"],
        pygame.K_RIGHT: paula_images["derecha"]
    }

    if tecla in teclas_imagenes:
        paula.image = teclas_imagenes[tecla]

    if tecla in teclas_posiciones:
        for flecha in flechas:
            if chequear_colision(flecha, teclas_posiciones[tecla]):
                flechas.remove(flecha)
                puntos += 1
                break

    if tecla == pygame.K_p:
        paula.update()

def get_font(size):

    return pygame.font.Font("assets/font.ttf", size)
font = get_font(32)

paula_images = {
    "arriba": pygame.transform.scale(pygame.image.load("paula_arriba.png").convert_alpha(), (ancho, alto)),
    "abajo": pygame.transform.scale(pygame.image.load("paula_abajo.png").convert_alpha(), (ancho, alto)),
    "izquierda": pygame.transform.scale(pygame.image.load("paula_izquierda.png").convert_alpha(), (ancho, alto)),
    "derecha": pygame.transform.scale(pygame.image.load("paula_derecha.png").convert_alpha(), (ancho, alto))
}

paula = Paula(list(paula_images.values()), 900, 50)  # x, y son las coordenadas donde quieres que aparezca Paula

# Conectar a la base de datos
db = Database('userdata.db')

# Inicialización de variables
tiempo_ultimo_beat = pygame.time.get_ticks()
tiempo_ultima_corchea = pygame.time.get_ticks()
beat_count = 0
puntos = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            manejar_colision(event.key)

    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - tiempo_ultimo_beat >= beat_interval_ms:
        generar_flechas("smiths.txt", beat_count, corchea=False)
        tiempo_ultimo_beat = tiempo_actual
        beat_count += 1

    if tiempo_actual - tiempo_ultima_corchea >= corchea_interval_ms:
        generar_flechas("smiths.txt", beat_count, corchea=True)
        tiempo_ultima_corchea = tiempo_actual

    for flecha in flechas:
        flecha.update()

    flechas = [flecha for flecha in flechas if flecha.rect.bottom > 0]

    screen.blit(fondo_de_pantalla, (0, 0))

    for flecha in flechas:
        screen.blit(flecha.image, flecha.rect)

    for direction, image in referencia_images.items():
        screen.blit(image, referencia_positions[direction])

    screen.blit(paula.image, paula.rect)

    score_text = font.render(f"Puntaje: {puntos}", True, WHITE)
    screen.blit(score_text, (screen_width - score_text.get_width() - 10, 10))

    pygame.display.flip()

    clock.tick(60)

# Guardar la puntuación al terminar la partida
db.save_score(puntos)
top_puntuacion(screen, 'userdata.db')

pygame.quit()
sys.exit()

