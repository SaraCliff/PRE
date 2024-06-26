import re
from Database import Database

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
