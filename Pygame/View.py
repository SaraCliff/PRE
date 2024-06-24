import pygame

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

class View:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Juego de Ritmo")

        self.fondo_de_pantalla = pygame.image.load("FONDO_CUPIDO.png").convert()
        self.fondo_de_pantalla = pygame.transform.scale(self.fondo_de_pantalla, (screen_width, screen_height))

        self.WHITE = (255, 255, 255)

    def mostrar_fondo(self):
        self.screen.blit(self.fondo_de_pantalla, (0, 0))

    def mostrar_flechas(self, flechas, referencia_images, referencia_positions):
        for flecha in flechas:
            self.screen.blit(flecha.image, flecha.rect)
        for direction, image in referencia_images.items():
            self.screen.blit(image, referencia_positions[direction])

    def mostrar_puntaje(self, puntos, font):
        score_text = font.render(f"Puntaje: {puntos}", True, self.WHITE)
        self.screen.blit(score_text, (self.screen_width - score_text.get_width() - 10, 10))

    def actualizar_pantalla(self):
        pygame.display.flip()
