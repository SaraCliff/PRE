import sqlite3
import ast


class Database:

	def __init__(self, filename):
		self.conn = sqlite3.connect(filename)
		self.c = self.conn.cursor()
		self.c.execute('''CREATE TABLE IF NOT EXISTS users
                          (username TEXT PRIMARY KEY, password TEXT, SignIn INTEGER DEFAULT 0, Personaje1 TEXT, Personaje1 TEXT, Top5_chiara TEXT,Top5_smiths TEXT, Top5_cure TEXT, Top5_blnko TEXT, Cancion_jugada TEXT)''')
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
			if user[2] == 1:  # Verificar si el usuario ya está logueado
				return "User is already logged in"
			if user[1] == password:
				self.c.execute("UPDATE users SET SignIn=? WHERE username=?", (1, username))
				self.conn.commit()  # Guardar los cambios en la base de datos
				with open("Logged_in_username.txt", "w") as archivo:
					archivo.write(username)
				return True
			else:
				return "Password is incorrect"
		else:
			return "User doesn't exist"



	def logout(self):
		try:
			with open("Logged_in_username.txt", "r") as archivo:
				username = archivo.read().strip()
			if username:  # Si hay un usuario conectado
				self.c.execute("UPDATE users SET SignIn=? WHERE username=?", (0, username))
				self.conn.commit()
				with open("Logged_in_username.txt", "w") as archivo:
					archivo.write("")  # Borra el nombre de usuario del archivo
			return True
		except Exception as e:
			print("Error during logout:", e)
			return False

	def actualizar_cancion_jugada(self, cancion):
		try:
			with open("Logged_in_username.txt", "r") as archivo:
				username = archivo.read().strip()
			if username:  # Si hay un usuario conectado
				self.c.execute("UPDATE users SET cancion_jugada=? WHERE username=?", (cancion, username))
				self.conn.commit()
				return True
		except Exception as e:
			print("Error durante la actualización de la canción jugada:", e)
		return False



	def select_character1(self, username, selected_image_path):
		try:
			self.c.execute("UPDATE users SET Personaje1=? WHERE username=?", (selected_image_path, username))
			self.conn.commit()
			return True
		except Exception as e:
			print("Error during character selection:", e)
			return False

	def select_character2(self, username, selected_image_path):
		try:
			self.c.execute("UPDATE users SET Personaje2=? WHERE username=?", (selected_image_path, username))
			self.conn.commit()
			return True
		except Exception as e:
			print("Error during character selection:", e)
			return False

	def get_top5_scores(self, column):
		with open("Logged_in_username.txt", "r") as archivo:
			username = archivo.read().strip()
		if username:
			self.c.execute(f"SELECT {column} FROM users WHERE username=?", (username,))
			result = self.c.fetchone()
			if result and result[0]:
				try:
					scores = ast.literal_eval(result[0])
					top5_scores = sorted(set(scores), reverse=True)[:5]  # Usa un set para eliminar duplicados
					return top5_scores
				except (ValueError, SyntaxError) as e:
					print(f"Error parsing top5 scores: {e}")
					return None
			else:
				return None
		else:
			return None

	def username_exists(self, username):
		self.c.execute("SELECT * FROM users WHERE username=?", (username,))
		return self.c.fetchone() is not None

	def save_score(self, score, column):
		with open("Logged_in_username.txt", "r") as archivo:
			username = archivo.read().strip()
		if username:
			self.c.execute(f"SELECT {column} FROM users WHERE username=?", (username,))
			result = self.c.fetchone()
			if result and result[0]:
				try:
					scores = ast.literal_eval(result[0])
					scores.append(score)
					self.c.execute(f"UPDATE users SET {column}=? WHERE username=?", (str(scores), username))
					self.conn.commit()
				except (ValueError, SyntaxError) as e:
					print(f"Error updating scores: {e}")
			else:
				scores = [score]
				self.c.execute(f"UPDATE users SET {column}=? WHERE username=?", (str(scores), username))
				self.conn.commit()

	def borrar_personaje1(self):
		try:
			with open("Logged_in_username.txt", "r") as archivo:
				username = archivo.read().strip()
			if username:
				self.c.execute("UPDATE users SET Personaje1=? WHERE username=?", (None, username))
				self.conn.commit()
				return True
			else:
				return False
		except Exception as e:
			print("Error during deleting Personaje1:", e)
			return False

	def borrar_personaje2(self):
		try:
			with open("Logged_in_username.txt", "r") as archivo:
				username = archivo.read().strip()
			if username:
				self.c.execute("UPDATE users SET Personaje2=? WHERE username=?", (None, username))
				self.conn.commit()
				return True
			else:
				return False
		except Exception as e:
			print("Error during deleting Personaje2:", e)
			return False

	def get_cancion_jugada(self):
		with open("Logged_in_username.txt", "r") as archivo:
			username = archivo.read().strip()
		if username:
			self.c.execute("SELECT Cancion_jugada FROM users WHERE username=?", (username,))
			result = self.c.fetchone()
			if result and result[0]:
				return result[0]  # Devuelve directamente el valor de la columna Cancion_jugada
			else:
				return None
		else:
			return None

	def get_personaje1(self):
		with open("Logged_in_username.txt", "r") as archivo:
			username = archivo.read().strip()
		if username:
			self.c.execute("SELECT Personaje1 FROM users WHERE username=?", (username,))
			result = self.c.fetchone()
			if result and result[0]:
				return result[0]  # Devuelve directamente el valor de la columna Cancion_jugada
			else:
				return None
		else:
			return None

	def get_highest_score(self, column):
		try:
			with open("Logged_in_username.txt", "r") as archivo:
				username = archivo.read().strip()
		except FileNotFoundError:
			print("Error: Logged_in_username.txt not found.")
			return None

		if username:
			self.c.execute(f"SELECT {column} FROM users WHERE username=?", (username,))
			result = self.c.fetchone()
			if result and result[0]:
				try:
					scores = ast.literal_eval(result[0])
					if scores:
						highest_score = max(scores)
						return highest_score
					else:
						return None
				except (ValueError, SyntaxError) as e:
					print(f"Error parsing scores: {e}")
					return None
			else:
				return None
		else:
			return None
