import pygame
import sys
from button import Button, TextDrawer


def one_player_screen(screen):
    from how_to_play_screen import how_to_play_screen
    from select_player_mode_screen import select_player_mode_screen
    pygame.init()
    WIDTH = 1280
    HEIGHT = 720
    BG = pygame.image.load("assets/fondo2.jpg")
    BG = pygame.transform.scale(BG, (1280, 720))

    def get_font(size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    but = pygame.image.load("assets/Options Rect.png")
    but2= pygame.image.load("assets/fondo2.jpg")
    but3 = pygame.image.load("assets/fondo3.webp")
    but4 = pygame.image.load("assets/fondo4.jpg")
    but5 = pygame.image.load("assets/fondo5.png")
    but6 = pygame.image.load("assets/FONDOmain.png")

    character_one_button = Button(image=pygame.transform.scale(but, (125, 150)), pos=(WIDTH // 4, HEIGHT // 2 + 200 ),
                         text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

    character_two_button = Button(image=pygame.transform.scale(but2, (125, 150)), pos=(WIDTH // 4, HEIGHT // 3 + 100),
                          text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    character_three_button = Button(image=pygame.transform.scale(but3, (125, 150)), pos=(WIDTH // 4 + 200, HEIGHT // 2 + 200),
                                  text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

    character_four_button = Button(image=pygame.transform.scale(but4, (125, 150)), pos=(WIDTH // 4 + 200, HEIGHT // 3 + 100),
                                  text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
    character_five_button = Button(image=pygame.transform.scale(but5, (125, 150)),pos=(WIDTH // 4 + 400, HEIGHT // 2 + 200),
                                    text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

    character_six_button = Button(image=pygame.transform.scale(but6, (125, 150)),pos=(WIDTH // 4 + 400, HEIGHT // 3 + 100),
                                   text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

    ready_button = Button(image=pygame.transform.scale(but, (200, 70)), pos=(WIDTH // 4 + 715, HEIGHT // 2 + 250),
                          text_input="READY", font=get_font(15), base_color="#d7fcd4", hovering_color="White")
    back_button = Button(image=pygame.transform.scale(but, (150, 70)), pos=(WIDTH // 4 - 200, HEIGHT // 2 + 300),
                          text_input="BACK", font=get_font(15), base_color="#d7fcd4", hovering_color="White")
    selected_image = but
    while True:
        SCREEN = screen
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_image_mapping = {character_one_button: but,character_two_button: but2, character_three_button: but3,
                                            character_four_button: but4, character_five_button: but5,character_six_button: but6}

                if ready_button.checkForInput(MENU_MOUSE_POS):
                    how_to_play_screen(SCREEN)

                if back_button.checkForInput(MENU_MOUSE_POS):
                    select_player_mode_screen(SCREEN)

                for button, image in button_image_mapping.items():
                    if button.checkForInput(MENU_MOUSE_POS):
                        selected_image = image
                        break

        text_drawer = TextDrawer(screen)
        text_drawer.draw_text("BEAT BLAST", get_font(100), (186, 85, 211),
                              pygame.Rect(WIDTH // 4, HEIGHT // 3 - 150, WIDTH // 2, 40))
        text_drawer.draw_text("Please select a character:", get_font(15), (0, 0, 0),
                              pygame.Rect(WIDTH // 4 + 400, HEIGHT // 3 + 10, WIDTH // 2, 40))
        screen.blit(pygame.transform.scale(selected_image, (200, 250)), (935, 300))

        character_one_button.update(screen)
        character_two_button.update(screen)
        character_three_button.update(screen)
        character_four_button.update(screen)
        character_five_button.update(screen)
        character_six_button.update(screen)
        ready_button.update(screen)
        back_button.update(screen)

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    one_player_screen(SCREEN)