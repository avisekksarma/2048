import pygame

SCREEN= {
    'height': 600,
    'width': 600
}
FRAMERATE = 30

class AssetManager(object):
    fonts = {}
    sounds = {}
    music = {}

    @classmethod
    def loadFont(cls, file, size, key):
        new_font = pygame.font.Font(file, size)
        cls.fonts[key] = new_font
    
    @classmethod
    def isFontLoaded(cls,key):
        try:
            cls.fonts[key]
            return True
        except KeyError:
            return False

    @classmethod
    def renderFont(cls, key, text, color, surface, pos):
        try:
            surf = cls.fonts[key].render(text, True, color)
            surface.blit(surf, (pos[0]-surf.get_width()//2,pos[1]-surf.get_height()//2))
        except KeyError:
            raise KeyError("Error as unknown key is passed")

