import pygame
import sys
from Model import Model, Flecha
from View import View, Paula
from Top_puntuacion import top_puntuacion
from button import Database

class Presenter:
    def __init__(self, model, view, mp3_file, txt_file):
        self.model = model
        self.view = view
        self.mp3_file = mp3_file
        self.txt_file = txt_file

        self.clock = pygame.time.Clock()
        self.bpm = 82
        self.beat_interval_ms = (60 * 1000) / self.bpm
        self.corchea_interval_ms = self.beat_interval_ms / 2
        self.velocidad_px_ms = 10

        self.flecha_width = 500
        self.flecha_height = 500
        self.collision_rect_margin = 60

        self.referencia_images = {
            "left": pygame.transform.scale(pygame.image.load("arrow_left.png").convert_alpha(), (self.flecha_width, self.flecha_height)),
            "up": pygame.transform.scale(pygame.image.load("arrow_up.png").convert_alpha(), (self.flecha_width, self.flecha_height)),
            "down": pygame.transform.scale(pygame.image.load("arrow_down.png").convert_alpha(), (self.flecha_width, self.flecha_height)),
            "right": pygame.transform.scale(pygame.image.load("arrow_right.png").convert_alpha(), (self.flecha_width, self.flecha_height))
        }

        self.referencia_positions = {
            "left": (50, 50),
            "up": (150, 50),
            "down": (250, 50),
            "right": (350, 50)
        }

        self.paula_images = {
            "arriba": pygame.transform.scale(pygame.image.load("paula_arriba.png").convert_alpha(), (250, 500)),
            "abajo": pygame.transform.scale(pygame.image.load("paula_abajo.png").convert_alpha(), (250, 500)),
            "izquierda": pygame.transform.scale(pygame.image.load("paula_izquierda.png").convert_alpha(), (250, 500)),
            "derecha": pygame.transform.scale(pygame.image.load("paula_derecha.png").convert_alpha(), (250, 500))
        }

        self.paula = Paula(list(self.paula_images.values()), 900, 50)

        self.font = pygame.font.Font("assets/font.ttf", 32)
        self.tiempo_ultimo_beat = pygame.time.get_ticks()
        self.tiempo_ultima_corchea = pygame.time.get_ticks()
        self.beat_count = 0

        # Cargar y reproducir la canción
        pygame.mixer.music.load(self.mp3_file)
        pygame.mixer.music.play(0)  # Reproducir una vez

        # Inicializar la base de datos
        self.db = Database('userdata.db')

    def generar_flechas(self, file_path, beat_count, corchea):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if beat_count < len(lines):
                config = lines[beat_count].strip()
                for i, char in enumerate(config):
                    if corchea and char in '5678':
                        columna = "left" if char == '5' else "up" if char == '6' else "down" if char == '7' else "right"
                        x = self.referencia_positions[columna][0]
                        y = self.view.screen_height - 10
                        flecha = Flecha(self.referencia_images[columna], x, y, self.velocidad_px_ms)
                        self.model.agregar_flecha(flecha)
                    elif not corchea and char in '1234':
                        columna = "left" if char == '1' else "up" if char == '2' else "down" if char == '3' else "right"
                        x = self.referencia_positions[columna][0]
                        y = self.view.screen_height - 10
                        flecha = Flecha(self.referencia_images[columna], x, y, self.velocidad_px_ms)
                        self.model.agregar_flecha(flecha)

    def chequear_colision(self, flecha, posicion_referencia):
        return flecha.collision_rect.colliderect(pygame.Rect(
            posicion_referencia[0] + self.flecha_width // 2 - self.collision_rect_margin,
            posicion_referencia[1] + self.flecha_height // 2 - self.collision_rect_margin,
            self.collision_rect_margin * 2, self.collision_rect_margin * 2))

    def manejar_colision(self, tecla):
        teclas_posiciones = {
            pygame.K_LEFT: self.referencia_positions["left"],
            pygame.K_UP: self.referencia_positions["up"],
            pygame.K_DOWN: self.referencia_positions["down"],
            pygame.K_RIGHT: self.referencia_positions["right"]
        }

        teclas_imagenes = {
            pygame.K_LEFT: self.paula_images["izquierda"],
            pygame.K_UP: self.paula_images["arriba"],
            pygame.K_DOWN: self.paula_images["abajo"],
            pygame.K_RIGHT: self.paula_images["derecha"]
        }

        if tecla in teclas_imagenes:
            self.paula.image = teclas_imagenes[tecla]

        if tecla in teclas_posiciones:
            for flecha in self.model.flechas:
                if self.chequear_colision(flecha, teclas_posiciones[tecla]):
                    self.model.eliminar_flecha(flecha)
                    self.model.incrementar_puntos()
                    break

        if tecla == pygame.K_p:
            self.paula.update()

    def ejecutar(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.manejar_colision(event.key)

            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_beat >= self.beat_interval_ms:
                self.generar_flechas(self.txt_file, self.beat_count, corchea=False)
                self.tiempo_ultimo_beat = tiempo_actual
                self.beat_count += 1

            if tiempo_actual - self.tiempo_ultima_corchea >= self.corchea_interval_ms:
                self.generar_flechas(self.txt_file, self.beat_count, corchea=True)
                self.tiempo_ultima_corchea = tiempo_actual

            self.model.actualizar_flechas()
            self.view.mostrar_fondo()
            self.view.mostrar_flechas(self.model.flechas, self.referencia_images, self.referencia_positions)
            self.view.screen.blit(self.paula.image, self.paula.rect)
            self.view.mostrar_puntaje(self.model.puntos, self.font)
            self.view.actualizar_pantalla()
            self.clock.tick(60)

            # Verificar si la música ha terminado
            if not pygame.mixer.music.get_busy():
                running = False

        # Guardar la puntuación al terminar la partida
        self.db.save_score(self.model.puntos, column=self.db.get_cancion_jugada())
        top_puntuacion(self.view.screen, 'userdata.db')

if __name__ == "__main__":
    pygame.init()
    screen_width = 1280
    screen_height = 720

    model = Model()
    view = View(screen_width, screen_height)

    # Aquí debes obtener los archivos seleccionados (mp3 y txt) de alguna manera, por ejemplo:
    mp3_file = "3 de febrero.mp3"  # Reemplaza esto con la ruta al archivo seleccionado
    txt_file = "chiara.txt"  # Reemplaza esto con la ruta al archivo seleccionado

    presenter = Presenter(model, view, mp3_file, txt_file)

    presenter.ejecutar()

    pygame.quit()
    sys.exit()
