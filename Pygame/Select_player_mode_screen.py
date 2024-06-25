import pygame
import sys
from button import Button, Personaje, Database
from one_player_screen import one_player_screen
from Two_player_screen import two_player_screen
from How_to_play_screen import how_to_play_screen
from Menu_screen import main_menu
def select_player_mode_screen(screen, personaje,database):
    pygame.init()

    BG = pygame.image.load("Imagenes/Fondos/pantalla_principal.png")
    BG = pygame.transform.scale(BG, (1280, 720))

    def get_font(size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("BEAT BLAST", True, "#BA55D3")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 150))

        Fondobut = pygame.image.load("assets/Options Rect.png")

        one_player_BUTTON = Button(image= pygame.transform.scale(Fondobut, (500, 109)), pos=(640, 300),
                             text_input="ONE PLAYER", font=get_font(40), base_color="#d7fcd4", hovering_color="White", image_path = "assets/Options Rect.png")

        two_player_BUTTON = Button(image=Fondobut, pos=(640, 450),
                                text_input="TWO PLAYER", font=get_font(40), base_color="#d7fcd4", hovering_color="White", image_path = "assets/Options Rect.png")
        how_to_play_BUTTON = Button(image=Fondobut, pos=(640, 600),
                             text_input="HOW TO PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="White",image_path = "assets/Options Rect.png")
        log_out_BUTTON = Button(image=pygame.transform.scale(Fondobut, (175, 70)), pos=(1175, 50),
                                    text_input="LOG OUT", font=get_font(20), base_color="#d7fcd4",
                                    hovering_color="White", image_path = "assets/Options Rect.png")

        Quit_BUTTON = Button(image=pygame.transform.scale(Fondobut, (125, 70)), pos=(75, 50),
                                text_input="Quit", font=get_font(20), base_color="#d7fcd4",
                                hovering_color="White", image_path="assets/Options Rect.png")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        database = Database('userdata.db')
        for button in [one_player_BUTTON, two_player_BUTTON, how_to_play_BUTTON, log_out_BUTTON,Quit_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.logout()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_player_BUTTON.checkForInput(MENU_MOUSE_POS):
                    one_player_screen(SCREEN)
                if two_player_BUTTON.checkForInput(MENU_MOUSE_POS):
                    two_player_screen(SCREEN,personaje,database)
                if how_to_play_BUTTON.checkForInput(MENU_MOUSE_POS):
                    how_to_play_screen(SCREEN)
                if log_out_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    main_menu(SCREEN,database = "userdata.db")
                if Quit_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    personaje = Personaje(database = "userdata.db")
    select_player_mode_screen(SCREEN, personaje,database = "userdata.db")