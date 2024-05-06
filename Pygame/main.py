import pygame
from menu_screen import main_menu

# Inicialización de Pygame
pygame.init()

# Tamaño de la ventana
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Crear la ventana
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

if __name__ == "__main__":
    main_menu(SCREEN)
