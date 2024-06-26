import pygame
import sys
from Top_puntuacion import top_puntuacion
from button import Database
from Model import Model
from View import View

class Presenter:
    def __init__(self, model, view, mp3_file, txt_file, bpm):
        self.model = model
        self.view = view
        self.mp3_file = mp3_file
        self.txt_file = txt_file

        # Usar el BPM proporcionado
        self.bpm = bpm

        self.clock = pygame.time.Clock()
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


        self.font = pygame.font.Font("assets/font.ttf", 32)
        self.tiempo_ultimo_beat = pygame.time.get_ticks()
        self.tiempo_ultima_corchea = pygame.time.get_ticks()
        self.beat_count = 0

        # Cargar y reproducir la canción
        pygame.mixer.music.load(self.mp3_file)
        pygame.mixer.music.play(0)  # Reproducir una vez

        # Inicializar la base de datos
        self.db = Database('userdata.db')

    def cargar_imagenes_paula(self):
        personaje_image = self.db.get_personaje1()
        if personaje_image:
            if personaje_image == "Imagenes/Personajes/mariapaula.png":
                paula_arriba = "Imagenes/Paula/paula_arriba.png"
                paula_abajo = "Imagenes/Paula/paula_abajo.png"
                paula_izquierda = "Imagenes/Paula/paula_izquierda.png"
                paula_derecha = "Imagenes/Paula/paula_derecha.png"
            elif personaje_image == "Imagenes/Personajes/sara_soto.png":
                paula_arriba = "Imagenes/sara/sara_arriba.png"
                paula_abajo = "Imagenes/sara/sara_abajo.png"
                paula_izquierda = "Imagenes/sara/sara_izquierda.png"
                paula_derecha = "Imagenes/sara/sara_derecha.png"
            elif personaje_image == "Imagenes/Personajes/ramona.png":
                paula_arriba = "Imagenes/ramona/ramona_arriba.png"
                paula_abajo = "Imagenes/ramona/ramona_abajo.png"
                paula_izquierda = "Imagenes/ramona/ramona_izquierda.png"
                paula_derecha = "Imagenes/ramona/ramona_derecha.png"
            else:
                # Default: imágenes de Paula genéricas si no se reconoce el personaje
                paula_arriba = "Imagenes/robert/robert_arriba.png"
                paula_abajo = "Imagenes/robert/rober_abajo.png"
                paula_izquierda = "Imagenes/robert/robert_izquierda.png"
                paula_derecha = "Imagenes/robert/robert_derecha.png"

            return paula_arriba, paula_abajo, paula_izquierda, paula_derecha

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
                        self.model.agregar_flecha(self.referencia_images[columna], x, y, self.velocidad_px_ms)
                    elif not corchea and char in '1234':
                        columna = "left" if char == '1' else "up" if char == '2' else "down" if char == '3' else "right"
                        x = self.referencia_positions[columna][0]
                        y = self.view.screen_height - 10
                        self.model.agregar_flecha(self.referencia_images[columna], x, y, self.velocidad_px_ms)

    def chequear_colision(self, flecha, posicion_referencia):
        return flecha['collision_rect'].colliderect(pygame.Rect(
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
            pygame.K_LEFT: self.view.paula_images[2],
            pygame.K_UP: self.view.paula_images[0],
            pygame.K_DOWN: self.view.paula_images[1],
            pygame.K_RIGHT: self.view.paula_images[3]
        }

        if tecla in teclas_imagenes:
            self.view.paula_index = self.view.paula_images.index(teclas_imagenes[tecla])

        if tecla in teclas_posiciones:
            for flecha in self.model.flechas:
                if self.chequear_colision(flecha, teclas_posiciones[tecla]):
                    self.model.eliminar_flecha(flecha)
                    self.model.incrementar_puntos()
                    break

        if tecla == pygame.K_p:
            self.view.actualizar_paula()

    def ejecutar(self):
        paula_arriba, paula_abajo, paula_izquierda, paula_derecha = self.cargar_imagenes_paula()
        paula_images = [
            pygame.transform.scale(pygame.image.load(paula_arriba).convert_alpha(), (400, 500)),
            pygame.transform.scale(pygame.image.load(paula_abajo).convert_alpha(), (400, 500)),
            pygame.transform.scale(pygame.image.load(paula_izquierda).convert_alpha(), (400, 500)),
            pygame.transform.scale(pygame.image.load(paula_derecha).convert_alpha(), (400, 500))
        ]

        self.view.cargar_paula_images(paula_images, 900, 50)

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
                self.beat_count += 1
                self.tiempo_ultimo_beat = tiempo_actual

            if tiempo_actual - self.tiempo_ultima_corchea >= self.corchea_interval_ms:
                self.generar_flechas(self.txt_file, self.beat_count, corchea=True)
                self.tiempo_ultima_corchea = tiempo_actual

            self.model.actualizar_flechas()

            self.view.mostrar_fondo()
            self.view.mostrar_flechas(self.model.flechas, self.referencia_images, self.referencia_positions)
            self.view.mostrar_puntaje(self.model.puntos, self.font)
            self.view.mostrar_paula()
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
    view = View(screen_width, screen_height, fondo_de_pantalla="Imagenes/Fondos/nivel4.png")

    # Aquí debes obtener los archivos seleccionados (mp3 y txt) de alguna manera, por ejemplo:
    mp3_file = "MP3_files/Jeff Hardy.mp3"  # Reemplaza esto con la ruta al archivo seleccionado
    txt_file = "Txt_files/Blnko.txt"  # Reemplaza esto con la ruta al archivo seleccionado
    bpm = 122

    presenter = Presenter(model, view, mp3_file, txt_file,bpm)

    presenter.ejecutar()

    pygame.quit()
    sys.exit()
