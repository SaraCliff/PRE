import pygame
import sys
from Button import Button
from Database import Database
from Personaje import Personaje
from Menu_screen import main_menu
from Nivel import Nivel
from Select_player_mode_screen import select_player_mode_screen

def select_level_screen(screen, database):
    pygame.init()

    BG = pygame.image.load("Imagenes/Fondos/mapa_niveles.png")
    BG = pygame.transform.scale(BG, (1280, 720))

    def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)

    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(60).render("BEAT BLAST", True, (255, 255, 255))
        MENU_RECT = MENU_TEXT.get_rect(center=(450, 150))

        Fondobut = pygame.image.load("assets/Options Rect.png")

        database = Database('userdata.db')

        # Obtenemos las puntuaciones más altas
        high_score_chiara = database.get_highest_score("top5_chiara") or 0
        high_score_blnko = database.get_highest_score("top5_blnko") or 0
        high_score_smiths = database.get_highest_score("top5_smiths") or 0
        high_score_cure = database.get_highest_score("top5_cure") or 0

        # Definimos el umbral de puntuación
        score_threshold_chiara = 178
        score_threshold_smiths = 330
        score_threshold_cure = 350
        score_threshold_blnko = 268


        # Determinamos el color del texto basado en la puntuación
        color_chiara = (0, 255, 0) if high_score_chiara >= score_threshold_chiara else (255, 0, 0)
        color_smiths = (0, 255, 0) if high_score_smiths >= score_threshold_smiths else (255, 0, 0)
        color_cure = (0, 255, 0) if high_score_cure >= score_threshold_cure else (255, 0, 0)
        color_blnko = (0, 255, 0) if high_score_blnko >= score_threshold_blnko else (255, 0, 0)

        # Muestra la puntuación y el umbral para cada canción
        SCORE_HEADER = get_font(10).render(f"{high_score_chiara}/{score_threshold_chiara}", True, color_chiara)
        SCORE_RECT = SCORE_HEADER.get_rect(center=(300, 320))
        SCREEN.blit(SCORE_HEADER, SCORE_RECT)

        RANK_HEADER = get_font(10).render("3 de febrero - Chiara Oliver", True, color_chiara)
        RANK_RECT = RANK_HEADER.get_rect(center=(300, 340))
        SCREEN.blit(RANK_HEADER, RANK_RECT)

        SCORE_HEADER = get_font(10).render(f"{high_score_smiths}/{score_threshold_smiths}", True, color_smiths)
        SCORE_RECT = SCORE_HEADER.get_rect(center=(500, 670))
        SCREEN.blit(SCORE_HEADER, SCORE_RECT)

        RANK_HEADER = get_font(10).render("There is a light that never goes out - The Smiths", True, color_smiths)
        RANK_RECT = RANK_HEADER.get_rect(center=(500, 690))
        SCREEN.blit(RANK_HEADER, RANK_RECT)

        SCORE_HEADER = get_font(10).render(f"{high_score_cure}/{score_threshold_cure}", True, color_cure)
        SCORE_RECT = SCORE_HEADER.get_rect(center=(750, 270))
        SCREEN.blit(SCORE_HEADER, SCORE_RECT)

        RANK_HEADER = get_font(10).render("Just like heaven - The Cure", True, color_cure)
        RANK_RECT = RANK_HEADER.get_rect(center=(750, 290))
        SCREEN.blit(RANK_HEADER, RANK_RECT)

        SCORE_HEADER = get_font(10).render(f"{high_score_blnko}/{score_threshold_blnko}", True, color_blnko)
        SCORE_RECT = SCORE_HEADER.get_rect(center=(980, 690))
        SCREEN.blit(SCORE_HEADER, SCORE_RECT)

        RANK_HEADER = get_font(10).render("Jeff Hardy - Blnko", True, color_blnko)
        RANK_RECT = RANK_HEADER.get_rect(center=(980, 710))
        SCREEN.blit(RANK_HEADER, RANK_RECT)

        # Botones de nivel
        level1_BUTTON = Button(image=pygame.transform.scale(Fondobut, (100, 40)), pos=(290, 380),
                               text_input="LEVEL 1", font=get_font(10), base_color="#d7fcd4", hovering_color="White", image_path="assets/Options Rect.png")

        level2_BUTTON = Button(image=pygame.transform.scale(Fondobut, (100, 40)), pos=(490, 640),
                               text_input="LEVEL 2", font=get_font(10), base_color="#d7fcd4" if high_score_chiara >= score_threshold_smiths else "#808080",
                               hovering_color="White", image_path="assets/Options Rect.png")

        level3_BUTTON = Button(image=pygame.transform.scale(Fondobut, (100, 40)), pos=(750, 320),
                               text_input="LEVEL 3", font=get_font(10), base_color="#d7fcd4" if high_score_smiths >= score_threshold_cure else "#808080",
                               hovering_color="White", image_path="assets/Options Rect.png")

        level4_BUTTON = Button(image=pygame.transform.scale(Fondobut, (100, 40)), pos=(980, 660),
                               text_input="LEVEL 4", font=get_font(10), base_color="#d7fcd4" if high_score_cure >= score_threshold_blnko else "#808080",
                               hovering_color="White", image_path="assets/Options Rect.png")

        log_out_BUTTON = Button(image=pygame.transform.scale(Fondobut, (175, 50)), pos=(1175, 27.5),
                                text_input="LOG OUT", font=get_font(20), base_color="#d7fcd4", hovering_color="White", image_path="assets/Options Rect.png")

        Quit_BUTTON = Button(image=pygame.transform.scale(Fondobut, (125, 50)), pos=(75, 27.5),
                             text_input="Quit", font=get_font(20), base_color="#d7fcd4", hovering_color="White", image_path="assets/Options Rect.png")

        BACK_BUTTON = Button(image=pygame.transform.scale(Fondobut, (100, 50)), pos=(60, 690),
                             text_input="BACK", font=get_font(20), base_color="#d7fcd4", hovering_color="White",
                             image_path="assets/Options Rect.png")


        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [level1_BUTTON, level2_BUTTON, level3_BUTTON, level4_BUTTON, log_out_BUTTON, Quit_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.logout()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.actualizar_cancion_jugada(cancion="top5_chiara")
                    nivel = Nivel("MP3_files/3 de febrero.mp3", "Txt_files/chiara.txt", bpm=82,fondo_de_pantalla="Imagenes/Fondos/nivel1.png")
                    nivel.ejecutar()
                if level2_BUTTON.checkForInput(MENU_MOUSE_POS) and high_score_chiara >= score_threshold_chiara:
                    database.actualizar_cancion_jugada(cancion="top5_smiths")
                    nivel = Nivel("MP3_files/There Is a Light That Never Goes Out.mp3", "Txt_files/smiths.txt", bpm=136, fondo_de_pantalla="Imagenes/Fondos/nivel2.png")
                    nivel.ejecutar()
                if level3_BUTTON.checkForInput(MENU_MOUSE_POS) and high_score_smiths >= score_threshold_smiths:
                    database.actualizar_cancion_jugada(cancion="top5_cure")
                    nivel = Nivel("MP3_files/Just like heaven.mp3", "Txt_files/cure.txt", bpm=151, fondo_de_pantalla="Imagenes/Fondos/nivel3.png")
                    nivel.ejecutar()
                if level4_BUTTON.checkForInput(MENU_MOUSE_POS) and high_score_cure >= score_threshold_cure:
                    database.actualizar_cancion_jugada(cancion="top5_blnko")
                    nivel = Nivel("MP3_files/Jeff Hardy.mp3", "Txt_files/Blnko.txt", bpm=122, fondo_de_pantalla="Imagenes/Fondos/nivel4.png")
                    nivel.ejecutar()
                if log_out_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    main_menu(SCREEN, database="userdata.db")
                if Quit_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    pygame.quit()
                    sys.exit()
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.borrar_personaje1()
                    database.borrar_personaje2()
                    select_player_mode_screen(SCREEN,Personaje, database = "userdata.db")

        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    select_level_screen(SCREEN, database="userdata.db")

