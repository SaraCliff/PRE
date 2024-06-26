import pygame

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color,image_path):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.image_path = image_path
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





class Personaje(pygame.sprite.Sprite):
	def __init__(self, database, player1=None, player2=None):
		super().__init__()
		self.database = database
		self.player1 = player1
		self.player2 = player2
		self.selected_image = None
		self.selected_character = None

	def select_character(self, button):
		self.selected_image = button.image
		self.selected_character = button.image_path

	def update_player1(self):
		self.player1 = self.selected_image

	def update_player2(self):
		self.player2 = self.selected_image
	def save_selected_character(self):
		try:
			with open("Logged_in_username.txt", "r") as archivo:
				username = archivo.read().strip()
			if username:
				self.database.select_character1(username, self.selected_character)
		except Exception as e:
			print("Error saving selected character:", e)


	def save_selected_character2(self):
		with open("Logged_in_username.txt", "r") as archivo:
			username = archivo.read().strip()
		if username:
			self.database.select_character2(username, self.selected_character)


