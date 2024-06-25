import pygame
import sys
from button import Button, TextDrawer, Personaje, Database

def one_player_screen(screen):
    from Select_player_mode_screen import select_player_mode_screen
    from Menu_screen import main_menu
    from Select_level_screen import select_level_screen
    pygame.init()
    WIDTH = 1280
    HEIGHT = 720
    BG = pygame.image.load("Imagenes/Fondos/nubes.png")
    BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

    def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)

    # Cargar imágenes y sus rutas
    image_paths = [
        "assets/Options Rect.png",
        "Imagenes/Personajes/mariapaula.png",
        "Imagenes/Personajes/sara_soto.png",
        "Imagenes/Personajes/ramona.png",
        "Imagenes/Personajes/robert_smith.png"
    ]

    images = [pygame.image.load(path) for path in image_paths]

    buttons = [
        Button(image=pygame.transform.scale(images[1], (300, 300)), pos=(WIDTH // 4, HEIGHT // 2 + 200),
               text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White", image_path=image_paths[1]),

        Button(image=pygame.transform.scale(images[2], (300, 300)), pos=(WIDTH // 4, HEIGHT // 3 + 100),
               text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White", image_path=image_paths[2]),

        Button(image=pygame.transform.scale(images[3], (300, 300)), pos=(WIDTH // 4 + 300, HEIGHT // 2 + 200),
               text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White", image_path=image_paths[3]),

        Button(image=pygame.transform.scale(images[4], (300, 300)), pos=(WIDTH // 4 + 300, HEIGHT // 3 + 100),
               text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White", image_path=image_paths[4]),
    ]

    ready_button = Button(image=pygame.transform.scale(images[0], (200, 70)), pos=(WIDTH // 4 + 715, HEIGHT // 2 + 250),
                          text_input="READY", font=get_font(15), base_color="#d7fcd4", hovering_color="White", image_path=image_paths[0])
    back_button = Button(image=pygame.transform.scale(images[0], (150, 70)), pos=(WIDTH // 4 - 200, HEIGHT // 2 + 300),
                         text_input="BACK", font=get_font(15), base_color="#d7fcd4", hovering_color="White", image_path=image_paths[0])
    log_out_BUTTON = Button(image=pygame.transform.scale(images[0], (150, 70)), pos=(1150, 50),
                            text_input="LOG OUT", font=get_font(15), base_color="#d7fcd4",
                            hovering_color="White", image_path=image_paths[0])
    Quit_BUTTON = Button(image=pygame.transform.scale(images[0], (125, 70)), pos=(75, 50),
                         text_input="Quit", font=get_font(20), base_color="#d7fcd4",
                         hovering_color="White", image_path="assets/Options Rect.png")

    database = Database('userdata.db')
    personaje = Personaje(database)

    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.logout()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ready_button.checkForInput(MENU_MOUSE_POS):
                    personaje.save_selected_character()
                    select_level_screen(SCREEN, database = "userdata.db")
                if back_button.checkForInput(MENU_MOUSE_POS):
                    select_player_mode_screen(SCREEN, personaje, database = "userdata.db")
                if log_out_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    main_menu(SCREEN, database = "userdata.db")
                if Quit_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    pygame.quit()
                    sys.exit()
                for button in buttons:
                    if button.checkForInput(MENU_MOUSE_POS):
                        personaje.select_character(button)

        text_drawer = TextDrawer(screen)
        text_drawer.draw_text("BEAT BLAST", get_font(100), (186, 85, 211),
                              pygame.Rect(WIDTH // 4, HEIGHT // 3 - 100, WIDTH // 2, 40))
        text_drawer.draw_text("Please select a character:", get_font(15), (255, 255, 255),
                              pygame.Rect(WIDTH // 4 + 400, HEIGHT // 3 + 10, WIDTH // 2, 40))
        pygame.draw.rect(SCREEN, (255, 255, 255), (935, 300, 200, 200), 0)

        if personaje.selected_image is not None:
            screen.blit(pygame.transform.scale(personaje.selected_image, (300, 300)), (887.5, 260))

        for button in buttons + [ready_button, back_button, log_out_BUTTON, Quit_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)



        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    one_player_screen(SCREEN)
