import pygame
import sys
from button import Button, TextDrawer, Personaje, Database

def two_player_screen(screen, personaje,database):
    from How_to_play_screen import how_to_play_screen
    from Select_player_mode_screen import select_player_mode_screen
    from Menu_screen import main_menu
    pygame.init()
    WIDTH = 1280
    HEIGHT = 720
    BG = pygame.image.load("Imagenes/Fondos/nubes.png")
    BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

    SCREEN = pygame.display.set_mode((1280, 720))
    database = Database('userdata.db')
    personaje = Personaje(database)  # Crear una instancia de la clase Personaje sin valores iniciales


    def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)

    image_paths = [
        "assets/Options Rect.png",
        "Imagenes/Personajes/mariapaula.png",
        "Imagenes/Personajes/sara_soto.png",
        "Imagenes/Personajes/ramona.png",
        "Imagenes/Personajes/robert_smith.png"
    ]

    images = [pygame.image.load(path) for path in image_paths]
    database = Database('userdata.db')

    buttons = [
        Button(image=pygame.transform.scale(images[1], (300, 300)), pos=(WIDTH // 4, HEIGHT // 2 + 200),
               text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White",
               image_path=image_paths[1]),

        Button(image=pygame.transform.scale(images[2], (300, 300)), pos=(WIDTH // 4, HEIGHT // 3 + 100),
               text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White",
               image_path=image_paths[2]),

        Button(image=pygame.transform.scale(images[3], (300, 300)), pos=(WIDTH // 4 + 250, HEIGHT // 2 + 200),
               text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White",
               image_path=image_paths[3]),

        Button(image=pygame.transform.scale(images[4], (300, 300)), pos=(WIDTH // 4 + 250, HEIGHT // 3 + 100),
               text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White",
               image_path=image_paths[4]),
    ]

    ready_button = Button(image=pygame.transform.scale(images[0], (200, 50)),
                          pos=(WIDTH // 4 + 815, HEIGHT // 2 + 310),
                          text_input="READY", font=get_font(15),
                          base_color="#d7fcd4", hovering_color="White", image_path=image_paths[0])

    player_buttons = [
        Button(image=pygame.transform.scale(images[0], (200, 60)),
               pos=(WIDTH // 4 + 515, HEIGHT // 2 + 200),
               text_input="PLAYER 1", font=get_font(15),
               base_color="#d7fcd4", hovering_color="White", image_path=image_paths[0]),
        Button(image=pygame.transform.scale(images[0], (200, 60)),
               pos=(WIDTH // 4 + 815, HEIGHT // 2 + 200),
               text_input="PLAYER 2", font=get_font(15),
               base_color="#d7fcd4", hovering_color="White", image_path=image_paths[0])
    ]

    back_button = Button(image=pygame.transform.scale(images[0], (150, 50)),
                         pos=(WIDTH // 4 - 200, HEIGHT // 2 + 310),
                         text_input="BACK", font=get_font(15),
                         base_color="#d7fcd4", hovering_color="White", image_path=image_paths[0])

    log_out_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/Options Rect.png"), (150, 70)),
                            pos=(1150, 50),
                            text_input="LOG OUT", font=get_font(15), base_color="#d7fcd4",
                            hovering_color="White", image_path="assets/Options Rect.png")
    Quit_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/Options Rect.png"), (125, 70)), pos=(75, 50),
                        text_input="QUIT", font=get_font(20), base_color="#d7fcd4",
                        hovering_color="White", image_path="assets/Options Rect.png")

    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        selected_images = [personaje.player1, personaje.player2]


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.logout()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ready_button.checkForInput(MENU_MOUSE_POS):
                    if personaje.player1 is not None and personaje.player2 is not None:
                        personaje.save_selected_character()
                        personaje.save_selected_character2()
                        how_to_play_screen(SCREEN)
                if back_button.checkForInput(MENU_MOUSE_POS):
                    select_player_mode_screen(SCREEN, personaje,database)
                if log_out_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    main_menu(SCREEN,database)
                if Quit_BUTTON.checkForInput(MENU_MOUSE_POS):
                    database.logout()
                    pygame.quit()
                    sys.exit()
                for button in buttons:
                    if button.checkForInput(MENU_MOUSE_POS):
                        personaje.select_character(button)
                for i, button in enumerate(player_buttons):
                    if button.checkForInput(MENU_MOUSE_POS):
                        if i == 0:  # Si se presiona el botón PLAYER 1
                            personaje.update_player1()
                        elif i == 1:  # Si se presiona el botón PLAYER 2
                            personaje.update_player2()

        text_drawer = TextDrawer(screen)
        text_drawer.draw_text("BEAT BLAST", get_font(100), (186, 85, 211),
                              pygame.Rect(WIDTH // 4, HEIGHT // 3 - 100, WIDTH // 2, 40))
        text_drawer.draw_text("Please select a character:", get_font(15), (255, 255, 255),
                              pygame.Rect(WIDTH // 4 + 290, HEIGHT // 3 + 10, WIDTH // 2, 40))

        pygame.draw.rect(SCREEN, (255, 255, 255), (735, 300, 200, 200), 0)
        pygame.draw.rect(SCREEN, (255, 255, 255), (1035, 300, 200, 200), 0)
        # Dibujar las imágenes seleccionadas con las posiciones adecuadas
        if selected_images[0] is not None:
            SCREEN.blit(pygame.transform.scale(selected_images[0], (300, 300)), (687.5, 260))
        if selected_images[1] is not None:
            SCREEN.blit(pygame.transform.scale(selected_images[1], (300, 300)), (987.5, 260))

        for button in buttons + player_buttons + [ready_button, back_button, log_out_BUTTON,Quit_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)



        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    database = Database('userdata.db')
    personaje = Personaje(database)  # Crear una instancia de la clase Personaje sin valores iniciales
    two_player_screen(SCREEN, personaje,database)
