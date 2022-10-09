from GameTemplate import GameTemplate
from startMenu import StartMenu
from game import GameScreen
from insScreen import InsScreen
from constants import SCREEN,initFonts
import pygame

def runGame():
    pygame.init()
    window = pygame.display.set_mode((SCREEN['width'], SCREEN['height']))
    initFonts()
    start = StartMenu('Welcome to 2048 game',window)
    game = GameScreen('2048 Game',window)
    ins =  InsScreen('Instructions',window)
    GameTemplate.addScreenObj('start',start)
    GameTemplate.addScreenObj('game',game)
    GameTemplate.addScreenObj('ins',ins)
    GameTemplate.changeActiveKey('start')
    while True:
        GameTemplate.run()


if __name__ == "__main__":
    runGame()
