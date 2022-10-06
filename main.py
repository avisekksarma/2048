from startMenu import StartMenu
from constants import SCREEN
import pygame

def runGame():
    pygame.init()
    window = pygame.display.set_mode((SCREEN['width'], SCREEN['height']))
    game = StartMenu('Welcome to 2048 game',window)
    game.run()


if __name__ == "__main__":
    runGame()
