import pygame
import sys
from button import Button, Database
from menu_screen import main_menu
from Nivel import Nivel

def select_level_screen(screen, database):
    pygame.init()

    BG = pygame.image.load("assets/FONDOmain.png")
    BG = pygame.transform.scale(BG, (1280, 720))

    def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)

    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("BEAT BLAST", True, "#BA55D3")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 150))

        Fondobut = pygame.image.load("assets/Options Rect.png")

        level1_BUTTON = Button(image=pygame.transform.scale(Fondobut, (500, 109)), pos=(640, 300),
                               text_input="LEVEL 1", font=get_font(40), base_color="#d7fcd4", hovering_color="White", image_path="assets/Options Rect.png")

        level2_BUTTON = Button(image=Fondobut, pos=(640, 450),
                               text_input="LEVEL 2", font=get_font(40), base_color="#d7fcd4", hovering_color="White", image_path="assets/Options Rect.png")

        level3_BUTTON = Button(image=Fondobut, pos=(640, 600),
                               text_input="LEVEL 3", font=get_font(40), base_color="#d7fcd4", hovering_color="White", image_path="assets/Options Rect.png")

        log_out_BUTTON = Button(image=pygame.transform.scale(Fondobut, (175, 70)), pos=(1175, 50),
                                text_input="LOG OUT", font=get_font(20), base_color="#d7fcd4",
                                hovering_color="White", image_path="assets/Options Rect.png")

        Quit_BUTTON = Button(image=pygame.transform.scale(Fondobut, (125, 70)), pos=(75, 50),
                             text_input="Quit", font=get_font(20), base_color="#d7fcd4",
                             hovering_color="White", image_path="assets/Options Rect.png")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        database = Database('userdata.db')
        for button in [level1_BUTTON, level2_BUTTON, level3_BUTTON, log_out_BUTTON, Quit_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.logout()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    nivel = Nivel("3 de febrero.mp3", "chiara.txt")
                    nivel.ejecutar()
                if level2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    nivel = Nivel("Jeff Hardy.mp3", "Blnko.txt")
                    nivel.ejecutar()
                if level3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    nivel = Nivel("3 de febrero.mp3", "chiara.txt")
                    nivel.ejecutar()
                if log_out_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    main_menu(SCREEN, database="userdata.db")
                if Quit_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    select_level_screen(SCREEN, database="userdata.db")

