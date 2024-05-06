import pygame
import sqlite3
import re

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

class InputText:
	def __init__(self, pos, size, is_password=False):
		self.pos = pos
		self.size = size
		self.text = ""
		self.active = False
		self.is_password = is_password

	def draw(self, screen):
		pygame.draw.rect(screen, (200, 200, 200), (*self.pos, *self.size))
		font = pygame.font.Font("assets/font.ttf", 20)
		masked_text = '*' * len(self.text) if self.is_password else self.text
		text_surface = font.render(masked_text, True, (0, 0, 0))
		screen.blit(text_surface, (self.pos[0] + 5, self.pos[1] + 5))
		if self.active:
			pygame.draw.rect(screen, (0, 255, 0), (*self.pos, *self.size), 2)

	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.is_mouse_on_input(event.pos):
				self.active = True
			else:
				self.active = False
		if event.type == pygame.KEYDOWN and self.active:
			if event.key == pygame.K_BACKSPACE:
				self.text = self.text[:-1]
			else:
				self.text += event.unicode

	def is_mouse_on_input(self, pos):
		x, y = pos
		rect = pygame.Rect(*self.pos, *self.size)
		return rect.collidepoint(x, y)

class Database:
	def __init__(self, filename):
		self.conn = sqlite3.connect(filename)
		self.c = self.conn.cursor()
		self.c.execute('''CREATE TABLE IF NOT EXISTS users
                          (username TEXT PRIMARY KEY, password TEXT)''')
		self.conn.commit()

	def register_user(self, username, password):
		try:
			self.c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
			self.conn.commit()
			return True
		except sqlite3.IntegrityError:
			return False

	def login(self, username, password):
		self.c.execute("SELECT * FROM users WHERE username=?", (username,))
		user = self.c.fetchone()
		if user is not None:
			if user[1] == password:
				return True
			else:
				return "Password is incorrect"
		else:
			return "User doesn't exist"

	def username_exists(self, username):
		self.c.execute("SELECT * FROM users WHERE username=?", (username,))
		return self.c.fetchone() is not None


class User:
	def __init__(self, username, password, repeat_password):
		self.username = username
		self.password = password
		self.repeat_password = repeat_password

	def verify(self):
		db = Database('userdata.db')

		if db.username_exists(self.username):
			return "This username is not available", (255, 0, 0)

		if len(self.password) == 0 or len(self.username) == 0:
			return "Username and password can't be empty", (255, 0, 0)

		if len(self.password) < 9:
			return "The password must be at least 9 characters long", (255, 0, 0)

		if self.password != self.repeat_password:
			return "Passwords don't match", (255, 0, 0)

		if len(self.username) >= 9:
			return "Username must be less than 9 characters", (255, 0, 0)

		if not re.search(r"[A-Z]", self.password) or not re.search(r"[a-z]", self.password) or not re.search(r"\d", self.password) or not re.search(r"[!@#$%^&*()-+]", self.password):
			return ("The password must contain at least one uppercase letter, "
						 "one lowercase letter, one number, and one special character"), (255, 0, 0)

		if db.register_user(self.username, self.password):
			return "You have been registered", (0, 255, 0)

		return "Unknown error", (255, 0, 0)



class TextDrawer:
	def __init__(self, surface):
		self.surface = surface

	def draw_text(self, text, font, color, rect):
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect(center=rect.center)
		self.surface.blit(text_surface, text_rect)


class TextDrawer2:
	@staticmethod
	def draw_text(screen, text, font, color, rect):
		font_surface = font.render(text, True, color)
		font_rect = font_surface.get_rect(center=rect.center)

		words = text.split()
		lines = []
		line = ""
		width, _ = rect.size

		for word in words:
			test_line = line + word + " "
			test_line_width, _ = font.size(test_line)

			if test_line_width <= width:
				line = test_line
			else:
				lines.append(line)
				line = word + " "

		lines.append(line)  # Agregar la última línea

		font_height = font.size("Tg")[1]  # Altura de una línea de texto
		y_offset = font_rect.centery - (len(lines) * font_height) / 2

		for line in lines:
			text_surface = font.render(line, True, color)
			text_rect = text_surface.get_rect(center=(font_rect.centerx, y_offset))
			screen.blit(text_surface, text_rect)
			y_offset += font_height

class Personaje(pygame.sprite.Sprite):
	def __init__(self, player1=None, player2=None):
		super().__init__()
		self.player1 = player1
		self.player2 = player2

	def select_player(self, buttons):
		selected_images = [button.image for button in buttons if button.checkForInput(pygame.mouse.get_pos())]
		if len(selected_images) >= 2:
			self.player1 = selected_images[0]
			self.player2 = selected_images[1]
		return self.player1, self.player2

	def select_character(self, buttons):
		selected_image = None
		while not selected_image:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					for button in buttons:
						if button.checkForInput(pygame.mouse.get_pos()):
							selected_image = button.image
		return selected_image


