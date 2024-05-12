import pygame
import sys
from button import Button, TextDrawer, Personaje

def two_player_screen(screen, personaje):
    from how_to_play_screen import how_to_play_screen
    from select_player_mode_screen import select_player_mode_screen
    pygame.init()
    WIDTH = 1280
    HEIGHT = 720
    BG = pygame.image.load("assets/fondo2.jpg")
    BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

    def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)

    but = pygame.image.load("assets/Options Rect.png")
    but2 = pygame.image.load("assets/fondo2.jpg")
    but3 = pygame.image.load("assets/fondo3.webp")
    but4 = pygame.image.load("assets/fondo4.jpg")
    but5 = pygame.image.load("assets/fondo5.png")
    but6 = pygame.image.load("assets/FONDOmain.png")

    buttons = [
        Button(image=pygame.transform.scale(but, (125, 150)),
               pos=(WIDTH // 4 - 100, HEIGHT // 3 + 100),
               text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White"),
        Button(image=pygame.transform.scale(but2, (125, 150)),
               pos=(WIDTH // 4 - 100, HEIGHT // 2 + 200),
               text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White"),
        Button(image=pygame.transform.scale(but3, (125, 150)),
               pos=(WIDTH // 4 + 100, HEIGHT // 3 + 100),
               text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White"),
        Button(image=pygame.transform.scale(but4, (125, 150)),
               pos=(WIDTH // 4 + 100, HEIGHT // 2 + 200),
               text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White"),
        Button(image=pygame.transform.scale(but5, (125, 150)),
               pos=(WIDTH // 4 + 300, HEIGHT // 3 + 100),
               text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White"),
        Button(image=pygame.transform.scale(but6, (125, 150)),
               pos=(WIDTH // 4 + 300, HEIGHT // 2 + 200),
               text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
    ]

    ready_button = Button(image=pygame.transform.scale(but, (200, 50)),
                          pos=(WIDTH // 4 + 800, HEIGHT // 2 + 310),
                          text_input="READY", font=get_font(15),
                          base_color="#d7fcd4", hovering_color="White")

    player_buttons = [
        Button(image=pygame.transform.scale(but, (200, 60)),
               pos=(WIDTH // 4 + 515, HEIGHT // 2 + 250),
               text_input="PLAYER 1", font=get_font(15),
               base_color="#d7fcd4", hovering_color="White"),
        Button(image=pygame.transform.scale(but, (200, 60)),
               pos=(WIDTH // 4 + 815, HEIGHT // 2 + 250),
               text_input="PLAYER 2", font=get_font(15),
               base_color="#d7fcd4", hovering_color="White")
    ]

    back_button = Button(image=pygame.transform.scale(but, (150, 50)),
                         pos=(WIDTH // 4 - 200, HEIGHT // 2 + 310),
                         text_input="BACK", font=get_font(15),
                         base_color="#d7fcd4", hovering_color="White")

    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        selected_images = [personaje.player1, personaje.player2]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ready_button.checkForInput(MENU_MOUSE_POS):
                    how_to_play_screen(SCREEN)
                if back_button.checkForInput(MENU_MOUSE_POS):
                    select_player_mode_screen(SCREEN)
                for i, button in enumerate(player_buttons):
                    if button.checkForInput(MENU_MOUSE_POS):
                        if i == 0:  # Si se presiona el botón PLAYER 1
                            personaje.player1 = personaje.select_character(buttons)
                        elif i == 1:  # Si se presiona el botón PLAYER 2
                            personaje.player2 = personaje.select_character(buttons)

        text_drawer = TextDrawer(screen)
        text_drawer.draw_text("BEAT BLAST", get_font(100), (186, 85, 211),
                              pygame.Rect(WIDTH // 4, HEIGHT // 3 - 150, WIDTH // 2, 40))
        text_drawer.draw_text("Please select a character:", get_font(15), (0, 0, 0),
                              pygame.Rect(WIDTH // 4 + 400, HEIGHT // 3 + 10, WIDTH // 2, 40))

        # Dibujar las imágenes seleccionadas con las posiciones adecuadas
        if selected_images[0] is not None:
            SCREEN.blit(pygame.transform.scale(selected_images[0], (200, 250)), (735, 300))
        if selected_images[1] is not None:
            SCREEN.blit(pygame.transform.scale(selected_images[1], (200, 250)), (1035, 300))

        for button in buttons + player_buttons + [ready_button, back_button]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, (255, 255, 255), (735, 300, 200, 250), 2)
        pygame.draw.rect(SCREEN, (255, 255, 255), (1035, 300, 200, 250), 2)

        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    personaje = Personaje()  # Crear una instancia de la clase Personaje sin valores iniciales
    two_player_screen(SCREEN, personaje)





