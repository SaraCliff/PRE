import pygame
import sys


def how_to_play_screen(screen):
    pygame.init()
    BG = pygame.image.load("Assets/FONDOmain.png")
    BG = pygame.transform.scale(BG, (1280, 720))



    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    how_to_play_screen(SCREEN)