import pygame
import sys
from button import Button, Personaje
from one_player_screen import one_player_screen
from two_player_screen import two_player_screen
from how_to_play_screen import how_to_play_screen
def select_player_mode_screen(screen):
    pygame.init()
    BG = pygame.image.load("assets/FONDOmain.png")
    BG = pygame.transform.scale(BG, (1280, 720))

    def get_font(size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("BEAT BLAST", True, "#BA55D3")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        Fondobut = pygame.image.load("assets/Options Rect.png")

        one_player_BUTTON = Button(image= pygame.transform.scale(Fondobut, (500, 109)), pos=(640, 250),
                             text_input="ONE PLAYER", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        two_player_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="TWO PLAYER", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        how_to_play_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 550),
                             text_input="HOW TO PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        sign_out_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 100),
                                    text_input="SIGN OUT", font=get_font(40), base_color="#d7fcd4",
                                    hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [one_player_BUTTON, two_player_BUTTON, how_to_play_BUTTON, sign_out_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_player_BUTTON.checkForInput(MENU_MOUSE_POS):
                    one_player_screen(SCREEN)
                if two_player_BUTTON.checkForInput(MENU_MOUSE_POS):
                    two_player_screen(SCREEN,personaje)
                if how_to_play_BUTTON.checkForInput(MENU_MOUSE_POS):
                    how_to_play_screen(SCREEN)



        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    personaje = Personaje()
    select_player_mode_screen(SCREEN)