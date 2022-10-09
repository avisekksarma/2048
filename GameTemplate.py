from constants import SCREEN
import pygame
import sys

class GameTemplate(object):
    # fill this gameobject as you make objects for different screens
    screenObjs = {}
    activeKey = None

    def __init__(self, title, window, width=SCREEN['width'], height=SCREEN['height']) -> None:
        #    assert width == SCREEN['width']
        self.title = title
        self.width = width
        self.height = height
        self.window = window

        pygame.display.set_caption(title)
        pygame.display.set_mode((width, height))

    @classmethod
    def addScreenObj(cls, key, obj):
        # changes the screenObj if same key exists
        cls.screenObjs[key] = obj
        if not cls.activeKey:
            cls.activeKey = key

    @classmethod
    def changeActiveKey(cls, key):
        cls.activeKey = key

    @classmethod
    def run(cls):
        if not cls.activeKey:
            pygame.quit()
            sys.exit()
        try:
            cls.screenObjs[cls.activeKey]
        except KeyError:
            pygame.quit()
            sys.exit()
        pygame.display.set_caption(cls.screenObjs[cls.activeKey].title)
        cls.screenObjs[cls.activeKey].run()
