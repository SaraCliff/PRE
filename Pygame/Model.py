import pygame

class Flecha(pygame.sprite.Sprite):
    def __init__(self, image, x, y, velocidad):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocidad = velocidad
        self.collision_rect = pygame.Rect(
            self.rect.centerx - 10,
            self.rect.centery - 10,
            20,
            20
        )

    def update(self):
        self.rect.y -= self.velocidad
        self.collision_rect.y = self.rect.centery - 10

class Model:
    def __init__(self):
        self.puntos = 0
        self.flechas = []

    def incrementar_puntos(self):
        self.puntos += 1

    def reset_puntos(self):
        self.puntos = 0

    def agregar_flecha(self, flecha):
        self.flechas.append(flecha)

    def eliminar_flecha(self, flecha):
        self.flechas.remove(flecha)

    def actualizar_flechas(self):
        for flecha in self.flechas:
            flecha.update()
        self.flechas = [flecha for flecha in self.flechas if flecha.rect.bottom > 0]
