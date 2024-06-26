import pygame
from Menu_screen import main_menu


class Juego:
    def __init__(self):
        # Inicialización de Pygame
        pygame.init()

        # Tamaño de la ventana
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720

        # Crear la ventana
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.database = "userdata.db"
        pygame.display.set_caption("Menu")

    def iniciar(self):
        # Llamar al menú principal
        main_menu(self.SCREEN, self.database)


if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()

