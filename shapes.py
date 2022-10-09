import pygame
from constants import AssetManager

# General usable shapes across projects
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
        if self.hoverOn:
            if self.rect.collidepoint(pos):
                self.isHovered = True
            else:
                self.isHovered = False
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


# Rectangle with text
class  TextRect(object):
    # size = (w,h) and pos = (l,t)
    def __init__(self,text,pos,size=(60,60),fillColor=(205,173,142),textColor=(37, 27, 55),fontKey='num1',isRounded=True,roundVal=2) -> None:
        self.size = size
        self.pos = pos
        self.fillColor = fillColor
        self.textColor = textColor
        self.fontKey = fontKey
        self.isRounded = isRounded
        self.roundVal = roundVal
        self.text = text
        self.rect = pygame.Rect(pos[0],pos[1],size[0],size[1])

    def draw(self,window):
        pygame.draw.rect(window,self.fillColor,self.rect,0,self.roundVal)
        pygame.draw.rect(window,(187, 155, 126),self.rect, 2, self.roundVal)
        AssetManager.renderFont(self.fontKey,self.text,self.textColor,window,self.rect.center)
