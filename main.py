from GameTemplate import GameTemplate
from startMenu import StartMenu
from GameTemplate import GameTemplate
from game import GameScreen
from constants import SCREEN
import pygame

def runGame():
    pygame.init()
    window = pygame.display.set_mode((SCREEN['width'], SCREEN['height']))
    start = StartMenu('Welcome to 2048 game',window)
    game = GameScreen('2048 Game',window)
    GameTemplate.addScreenObj('start',start)
    GameTemplate.addScreenObj('game',game)
    GameTemplate.changeActiveKey('start')
    GameTemplate.run()


if __name__ == "__main__":
    runGame()
