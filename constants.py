import pygame

SCREEN= {
    'height': 600,
    'width': 600
}
FRAMERATE = 30

def initFonts():
    AssetManager.loadFont(
            'assets/OpenType/Kaph-Italic.otf', 32, 'heading')
    AssetManager.loadFont(
            'assets/OpenType/Kaph-Regular.otf', 20, 'text')

class AssetManager(object):
    fonts = {}
    images = {}
    sounds = {}
    music = {}

    @classmethod
    def loadFont(cls, file, size, key):
        new_font = pygame.font.Font(file, size)
        cls.fonts[key] = new_font

    @classmethod
    def loadImage(cls, file,key):
        if ".png" in file:
            new_image = pygame.image.load(file).convert_alpha()
        else:
            new_image = pygame.image.load(file).convert()
        cls.images[key] = new_image

    @classmethod
    def isFontLoaded(cls,key):
        try:
            cls.fonts[key]
            return True
        except KeyError:
            return False


    @classmethod
    def renderImage(cls,key,surface,pos):
        surface.blit(cls.images[key],pos)
    
    @classmethod
    def renderFont(cls, key, text, color, surface, pos):
        try:
            surf = cls.fonts[key].render(text, True, color)
            surface.blit(surf, (pos[0]-surf.get_width()//2,pos[1]-surf.get_height()//2))
        except KeyError:
            raise KeyError("Error as unknown key is passed")

