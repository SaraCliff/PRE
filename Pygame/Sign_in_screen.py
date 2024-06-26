import pygame
import sys
from button import Button, InputText, User, TextDrawer2, TextDrawer

def sign_in_screen(screen):
    from Juego import main_menu
    pygame.init()
    BG = pygame.image.load("Imagenes/Fondos/nubes.png")
    BG = pygame.transform.scale(BG, (1280, 720))

    WIDTH, HEIGHT = 1280, 720

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    PINK = (186, 85, 211)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sign in")

    def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)

    username_input = InputText(pos=(WIDTH // 4 + 275, HEIGHT // 3), size=(WIDTH // 4, 40))
    password_input = InputText(pos=(WIDTH // 4 + 275, HEIGHT // 3 + 80), size=(WIDTH // 4, 40), is_password=True)
    repeat_password_input = InputText(pos=(WIDTH // 4 + 275, HEIGHT // 3 + 160), size=(WIDTH // 4, 40), is_password=True)

    last_verification_state = None

    but = pygame.image.load("assets/Options Rect.png")
    quit_button = Button(image=pygame.transform.scale(but,(200,60)), pos=(WIDTH // 8, HEIGHT // 2 + 300),
                         text_input="BACK", font=get_font(35), base_color="#d7fcd4", hovering_color="White", image_path="assets/Options Rect.png")

    check_button = Button(image=pygame.transform.scale(but, (300, 80)), pos=(WIDTH // 2, HEIGHT // 2 + 300),
                          text_input="CHECK", font=get_font(50), base_color="#d7fcd4", hovering_color="White", image_path="assets/Options Rect.png")

    verification_bg = pygame.image.load("assets/Quit Rect.png")
    verification_bg = pygame.transform.scale(verification_bg, (WIDTH // 2 + 200, 100))

    show_verification_text = False

    while True:
        screen.blit(BG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            username_input.handle_event(event)
            password_input.handle_event(event)
            repeat_password_input.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:

                if quit_button.checkForInput(event.pos):
                    main_menu(screen, database="userdata.db")

                if check_button.checkForInput(event.pos):
                    user = User(username_input.text, password_input.text, repeat_password_input.text)
                    verification_result, verification_color = user.verify()

                    if verification_result != last_verification_state:
                        last_verification_state = verification_result
                    show_verification_text = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    if username_input.active:
                        username_input.active = False
                        password_input.active = True
                    elif password_input.active:
                        password_input.active = False
                        repeat_password_input.active = True
                    else:
                        repeat_password_input.active = False
                        username_input.active = True

        username_input.draw(screen)
        password_input.draw(screen)
        repeat_password_input.draw(screen)
        text_drawer = TextDrawer(screen)
        text_drawer.draw_text("Username:", get_font(32), WHITE,
                              pygame.Rect(WIDTH // 4 - 200, HEIGHT // 3, WIDTH // 2, 40))
        text_drawer.draw_text("Password:", get_font(32), WHITE,
                              pygame.Rect(WIDTH // 4 - 200, HEIGHT // 3 + 80, WIDTH // 2, 40))
        text_drawer.draw_text("Repeat password:", get_font(32), WHITE,
                              pygame.Rect(WIDTH // 4 - 310, HEIGHT // 3 + 160, WIDTH // 2, 40))
        text_drawer.draw_text("BEAT BLAST", get_font(100), PINK,
                              pygame.Rect(WIDTH // 4, HEIGHT // 3 - 150, WIDTH // 2, 40))
        quit_button.changeColor(pygame.mouse.get_pos())
        quit_button.update(screen)
        check_button.changeColor(pygame.mouse.get_pos())
        check_button.update(screen)

        if show_verification_text:
            screen.blit(verification_bg, (WIDTH // 4-100, HEIGHT // 3 + 250))
            TextDrawer2.draw_text(screen, last_verification_state, get_font(16), verification_color,
                                  pygame.Rect(WIDTH // 4, HEIGHT // 3 + 200, WIDTH // 2, 200))

        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    sign_in_screen(SCREEN)








