import sys
import pygame
from GameTemplate import GameTemplate
from constants import FRAMERATE, SCREEN, AssetManager
from shapes import Button


class StartMenu(GameTemplate):
    def __init__(self, title, window, width=SCREEN['width'], height=SCREEN['height']) -> None:
        super().__init__(title, window, width, height)
        self.btns = {}
        self.__initialize()

    def __initialize(self):
        AssetManager.loadFont(
            'assets/OpenType/Kaph-Italic.otf', 32, 'heading')
        # Magic number below
        pos = (SCREEN['width']//2-100, SCREEN['height']//2-150)
        playBtn = Button(self.window, 'PLAY', 'heading',
                         Button.sizes['standard'], pos, (140, 140, 140), (190, 190, 190), True,True)
        self.btns['playBtn'] = playBtn

    def render(self):
        self.window.fill((120, 80, 100))
        # magic number below
        pos = (SCREEN['width']/2.0, 100)
        AssetManager.renderFont('heading', 'Main Menu',
                                (100, 200, 120), self.window, pos)
        # pygame.draw.circle(self.window, (0, 255, 150), (150, 250), 50)
        for btn in self.btns:
            self.btns[btn].render()
        pygame.display.update()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(FRAMERATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEMOTION:
                    # print(event.pos)
                    for btn in self.btns:
                        self.btns[btn].checkHovered(event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.btns['playBtn'].checkClick(event.pos):
                        running = False
                        GameTemplate.changeActiveKey('game')
                        
            self.render()
