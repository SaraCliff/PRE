import pygame

class Model:
    def __init__(self):
        self.puntos = 0
        self.flechas = []

    def incrementar_puntos(self):
        self.puntos += 1

    def reset_puntos(self):
        self.puntos = 0

    def agregar_flecha(self, image, x, y, velocidad):
        flecha = {
            'image': image,
            'rect': image.get_rect(topleft=(x, y)),
            'velocidad': velocidad,
            'collision_rect': pygame.Rect(
                x + image.get_width() // 2 - 10,
                y + image.get_height() // 2 - 10,
                20,
                20
            )
        }
        self.flechas.append(flecha)

    def eliminar_flecha(self, flecha):
        self.flechas.remove(flecha)

    def actualizar_flechas(self):
        for flecha in self.flechas:
            flecha['rect'].y -= flecha['velocidad']
            flecha['collision_rect'].y = flecha['rect'].centery - 10
        self.flechas = [flecha for flecha in self.flechas if flecha['rect'].bottom > 0]

