
import pygame
import sys
from Model import Model
from View import View
from Presenter import Presenter

class Nivel:
    def __init__(self, mp3_file, txt_file, bpm, fondo_de_pantalla, db_file='userdata.db'):
        self.mp3_file = mp3_file
        self.txt_file = txt_file
        self.bpm = bpm
        self.fondo_de_pantalla = fondo_de_pantalla
        self.db_file = db_file

        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Juego de Ritmo")

        self.model = Model()
        self.view = View(self.screen_width, self.screen_height, self.fondo_de_pantalla)
        self.presenter = Presenter(self.model, self.view, self.mp3_file, self.txt_file, self.bpm)

    def ejecutar(self):
        self.presenter.ejecutar()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen_width = 1280
    screen_height = 720

    mp3_file = "MP3_files/Jeff Hardy.mp3"
    txt_file = "Txt_files/Blnko.txt"
    bpm = 122
    fondo_de_pantalla = "Imagenes/Fondos/FONDO_CUPIDO.png"

    nivel = Nivel(mp3_file, txt_file, bpm, fondo_de_pantalla)
    nivel.ejecutar()




