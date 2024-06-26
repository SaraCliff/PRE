import pygame

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