import pygame
import sys
from button import InputText, Database, Button, TextDrawer


def log_in_screen(screen):
    from menu_screen import main_menu
    from select_player_mode_screen import select_player_mode_screen
    pygame.init()
    WIDTH, HEIGHT = 1280, 720
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    PINK = (186, 85, 211)
    BG = pygame.image.load("assets/FONDOmain.png")
    BG = pygame.transform.scale(BG, (1280, 720))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Inicio de sesión")

    username_input = InputText(pos=(WIDTH // 4 + 275, HEIGHT // 3), size=(WIDTH // 4, 40))
    password_input = InputText(pos=(WIDTH // 4 + 275, HEIGHT // 3 + 80), size=(WIDTH // 4, 40), is_password=True)

    database = Database('userdata.db')

    def get_font(size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    log_in_button = Button(image=pygame.transform.scale(pygame.image.load("assets/Options Rect.png"), (300, 80)),
                           pos=(WIDTH // 2, HEIGHT // 2 + 300), text_input="LOG IN", font=get_font(35),
                           base_color="#d7fcd4", hovering_color="White")
    back_button = Button(image=pygame.transform.scale(pygame.image.load("assets/Options Rect.png"), (200, 40)),
                         pos=(WIDTH // 7, HEIGHT // 2 + 300), text_input="BACK", font=get_font(35),
                         base_color="#d7fcd4", hovering_color="White")

    last_verification_state = None
    message_bg = pygame.transform.scale(pygame.image.load("assets/Quit Rect.png"), (500, 100))

    while True:
        screen.blit(BG, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            username_input.handle_event(event)
            password_input.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                    # Verificar si se hace clic en un campo de texto para activarlo
                if username_input.is_mouse_on_input(event.pos):
                    username_input.active = True
                    password_input.active = False
                elif password_input.is_mouse_on_input(event.pos):
                    password_input.active = True
                    username_input.active = False
                else:
                    username_input.active = False
                    password_input.active = False
                if log_in_button.checkForInput(event.pos):
                    result = database.login(username_input.text, password_input.text)
                    if result == True:
                        select_player_mode_screen(screen)
                    else:
                        last_verification_state = result
                if back_button.checkForInput(event.pos):
                    main_menu(screen)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                main_menu(screen)

        pygame.draw.rect(screen, GRAY, (WIDTH // 4 + 275, HEIGHT // 3, WIDTH // 4, 40))
        pygame.draw.rect(screen, GRAY, (WIDTH // 4 + 275, HEIGHT // 3 + 80, WIDTH // 4, 40))
        text_drawer = TextDrawer(screen)
        text_drawer.draw_text("Username:", get_font(32), WHITE, pygame.Rect(WIDTH // 4 - 200, HEIGHT // 3, WIDTH // 2, 40))
        text_drawer.draw_text("Password:",get_font(32), WHITE, pygame.Rect(WIDTH // 4 - 200, HEIGHT // 3 + 80, WIDTH // 2, 40))
        text_drawer.draw_text("BEAT BLAST", get_font(100), PINK, pygame.Rect(WIDTH // 4, HEIGHT // 3 - 150, WIDTH // 2, 40))
        username_input.draw(screen)
        password_input.draw(screen)
        log_in_button.changeColor(pygame.mouse.get_pos())
        log_in_button.update(screen)
        back_button.changeColor(pygame.mouse.get_pos())
        back_button.update(screen)

        if last_verification_state is not None:
            message_rect = message_bg.get_rect(center=(WIDTH // 2, HEIGHT // 2+150))
            screen.blit(message_bg, message_rect)
            text_drawer.draw_text(last_verification_state, get_font(20), RED, message_rect)

        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    log_in_screen(SCREEN)


