from pickle import FALSE
import pygame
from constants import AssetManager


class Button:
    sizes = {'standard': (200, 70), 'medium': (150, 90), 'huge': (200, 150)}
    # size = (width,height), and pos = (left,top)

    def __init__(self, window, text, fontKey, size, pos, textColor, hoverColor=None, isRound=False, hoverOn=False) -> None:
        self.window = window
        self.text = text
        self.fontKey = fontKey
        self.size = size
        self.pos = pos
        self.hoverOn = hoverOn
        self.isRound = isRound
        self.textColor = textColor
        self.hoverColor = hoverColor if hoverColor else textColor
        self.rect = pygame.Rect(
            self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.isHovered = False
        self.__initialize()

    def __initialize(self):
        isLoaded = AssetManager.isFontLoaded(self.fontKey)
        if not isLoaded:
            raise Exception('Unknown font key used')
        self.roundedVal = 5 if self.isRound else 0

    def checkHovered(self, pos):
        if self.rect.collidepoint(pos):
            self.isHovered = True
        else:
            self.isHovered = False

    def checkClick(self, pos) -> bool:
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def render(self):
        pygame.draw.rect(self.window, (120, 80, 100),
                         self.rect, 0, self.roundedVal)
        fontColor = self.hoverColor if self.isHovered else self.textColor
        AssetManager.renderFont(self.fontKey, self.text, fontColor,
                                self.window, (self.rect.centerx, self.rect.centery))
