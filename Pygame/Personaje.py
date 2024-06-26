import pygame
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


