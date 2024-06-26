import pygame
import sys
from button import Button, Database, Personaje  # Asegúrate de que tu clase Button esté en un archivo llamado button.py
from Menu_screen import main_menu


def top_puntuacion(screen, database):
    pygame.init()
    BG = pygame.image.load("Imagenes/Fondos/pantalla_final.png")
    BG = pygame.transform.scale(BG, (1280, 720))
    from Select_player_mode_screen import select_player_mode_screen

    def get_font(size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    db = Database(database)
    top5_scores = db.get_top5_scores(column = db.get_cancion_jugada())

    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        db.borrar_personaje1()

        MENU_TEXT = get_font(100).render("BEAT BLAST", True,"#d7fcd4" )
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 150))

        Fondobut = pygame.image.load("assets/Options Rect.png")

        NEXT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/Options Rect.png"), (300, 75)), pos=(640, 650),
                             text_input="NEXT", font=get_font(50), base_color="#d7fcd4", hovering_color="White",
                             image_path=Fondobut)

        Quit_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/Options Rect.png"), (125, 70)),
                             pos=(75, 50),
                             text_input="QUIT", font=get_font(20), base_color="#d7fcd4",
                             hovering_color="White", image_path="assets/Options Rect.png")
        log_out_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/Options Rect.png"), (150, 70)),
                                pos=(1150, 50),
                                text_input="LOG OUT", font=get_font(15), base_color="#d7fcd4",
                                hovering_color="White", image_path="assets/Options Rect.png")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Displaying top 5 scores in a video game inspired style
        if top5_scores is not None:
            scores_title = "HIGH SCORES"
            SCORES_TITLE_TEXT = get_font(50).render(scores_title, True, (0,0,0))
            SCORES_TITLE_RECT = SCORES_TITLE_TEXT.get_rect(center=(640, 250))
            SCREEN.blit(SCORES_TITLE_TEXT, SCORES_TITLE_RECT)

            # Headers for Rank and Points
            RANK_HEADER = get_font(35).render("RANK", True, (0,0,0))
            RANK_RECT = RANK_HEADER.get_rect(center=(540, 320))
            SCREEN.blit(RANK_HEADER, RANK_RECT)

            POINTS_HEADER = get_font(35).render("POINTS", True, (0,0,0))
            POINTS_RECT = POINTS_HEADER.get_rect(center=(740, 320))
            SCREEN.blit(POINTS_HEADER, POINTS_RECT)

            for i, score in enumerate(top5_scores):
                rank_text = f"{i + 1}"
                score_text = f"{score}"

                RANK_TEXT = get_font(35).render(rank_text, True, "#FFFFFF")
                RANK_TEXT_RECT = RANK_TEXT.get_rect(center=(540, 370 + (i * 50)))
                SCREEN.blit(RANK_TEXT, RANK_TEXT_RECT)

                SCORE_TEXT = get_font(35).render(score_text, True, "#FFFFFF")
                SCORE_TEXT_RECT = SCORE_TEXT.get_rect(center=(740, 370 + (i * 50)))
                SCREEN.blit(SCORE_TEXT, SCORE_TEXT_RECT)
        else:
            scores_text = "No scores found for the logged-in user."
            SCORES_TEXT = get_font(25).render(scores_text, True, "#FFFFFF")
            SCORES_RECT = SCORES_TEXT.get_rect(center=(640, 350))
            SCREEN.blit(SCORES_TEXT, SCORES_RECT)

        for button in [NEXT_BUTTON, Quit_BUTTON, log_out_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select_player_mode_screen(SCREEN,Personaje, database = "userdata.db")
                if Quit_BUTTON.checkForInput(MENU_MOUSE_POS):
                    db.logout()
                    pygame.quit()
                    sys.exit()
                if log_out_BUTTON.checkForInput(MENU_MOUSE_POS):
                    db.logout()
                    main_menu(SCREEN, database)

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    top_puntuacion(SCREEN, database="userdata.db")




