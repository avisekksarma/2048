import sys
import pygame
from GameTemplate import GameTemplate
from constants import FRAMERATE, SCREEN, AssetManager
from shapes import Button


class InsScreen(GameTemplate):
    def __init__(self, title, window, width=SCREEN['width'], height=SCREEN['height']) -> None:
        super().__init__(title, window, width, height)
        self.btns={}
        self.__initialize()

    def __initialize(self):
        
        AssetManager.loadImage('./assets/images/arrows.png','arrows')
        backBtn = Button(self.window,'BACK','text',Button.sizes['standard'],(SCREEN['width']*0.00-20,SCREEN['height']*0.02),(100,100,170),(125,250,195),True,True)
        self.btns['backBtn'] = backBtn

    def render(self):
        self.window.fill((120, 80, 100))
        # magic number below
        pos = (SCREEN['width']/2.0, 130)
        AssetManager.renderFont('text', 'USE',
                                (100, 200, 120), self.window, pos)
        pos = (pos[0]-80,pos[1]+50)
        AssetManager.renderImage('arrows',self.window,pos)
        pos = (SCREEN['width']/2.0,340)
        AssetManager.renderFont('text', 'for moving the tiles.',(100, 200, 120), self.window, pos)
        pos = (pos[0],400)
        AssetManager.renderFont(
            'text', 'Tiles with same values merge into one!', (100, 200, 120), self.window, pos)
        
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

                    if self.btns['backBtn'].checkClick(event.pos):
                        running = False
                        GameTemplate.changeActiveKey('start')
                    
            self.render()
