import pygame
import sys
from button import TextDrawer2, Button, Database, Personaje
from Menu_screen import main_menu


# Función para obtener la fuente "Press-Start-2P" en el tamaño deseado
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

# Función principal de la pantalla de instrucciones
def how_to_play_screen(screen):
    from Select_player_mode_screen import select_player_mode_screen
    pygame.init()

    # Cargar imagen de fondo
    BG = pygame.image.load("Imagenes/Fondos/nubes.png")
    BG = pygame.transform.scale(BG, (1280, 720))

    # Colores
    white = (255, 255, 255)

    # Fuente para el título y subtítulos
    title_font = get_font(60)
    subtitle_font = get_font(36)
    additional_font = get_font(24)

    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        database = Database('userdata.db')

        MENU_TEXT = get_font(100).render("BEAT BLAST", True, "#BA55D3")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Título
        title_text = "HOW TO PLAY"
        title_surface = title_font.render(title_text, True, "#FFD700")
        title_rect = title_surface.get_rect(center=(640, 250))
        screen.blit(title_surface, title_rect)

        # Instrucciones para un jugador
        single_player_text = "Single Player Mode: Use arrow keys to match the rhythm of the song."
        single_player_rect = pygame.Rect(100, 350, 1080, 50)
        TextDrawer2.draw_text(screen, single_player_text, subtitle_font, white, single_player_rect)

        # Instrucciones para dos jugadores
        multi_player_text = "Two Player Mode: Player 1 uses arrow keys. Player 2 uses WASD keys."
        multi_player_rect = pygame.Rect(100, 480, 1080, 50)
        TextDrawer2.draw_text(screen, multi_player_text, subtitle_font, white, multi_player_rect)

        Fondobut = pygame.image.load("assets/Options Rect.png")

        log_out_BUTTON = Button(image=pygame.transform.scale(Fondobut, (175, 70)), pos=(1175, 50),
                                text_input="LOG OUT", font=get_font(20), base_color="#d7fcd4",
                                hovering_color="White", image_path="assets/Options Rect.png")

        Quit_BUTTON = Button(image=pygame.transform.scale(Fondobut, (125, 70)), pos=(75, 50),
                             text_input="Quit", font=get_font(20), base_color="#d7fcd4",
                             hovering_color="White", image_path="assets/Options Rect.png")

        BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/Options Rect.png"), (300, 75)),
                             pos=(640, 650),
                             text_input="BACK", font=get_font(50), base_color="#d7fcd4", hovering_color="White",
                             image_path=Fondobut)

        personaje = Personaje(database="userdata.db")

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.logout()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if log_out_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    main_menu(SCREEN, database="userdata.db")
                if Quit_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    pygame.quit()
                    sys.exit()
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select_player_mode_screen(SCREEN, personaje, database)

        for button in [log_out_BUTTON,Quit_BUTTON,BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    how_to_play_screen(SCREEN)
