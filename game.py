import pygame
from GameTemplate import GameTemplate
from constants import FRAMERATE, SCREEN, AssetManager
from shapes import Button


class GameScreen(GameTemplate):
    def __init__(self, title, window, width=SCREEN['width'], height=SCREEN['height']) -> None:
        super().__init__(title, window, width, height)
        self.btns = {}
