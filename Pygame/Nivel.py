
import pygame
import sys
from Model import Model
from View import View
from Presenter import Presenter

class Nivel:
    def __init__(self, mp3_file, txt_file, db_file='userdata.db'):
        self.mp3_file = mp3_file
        self.txt_file = txt_file
        self.db_file = db_file

        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Juego de Ritmo")

        self.model = Model()
        self.view = View(self.screen_width, self.screen_height)
        self.presenter = Presenter(self.model, self.view, self.mp3_file, self.txt_file)

    def ejecutar(self):
        self.presenter.ejecutar()
        pygame.quit()
        sys.exit()


