import imp
from constants import SCREEN
import pygame


class GameTemplate(object):
    def __init__(self,title,window, width=SCREEN['width'],height=SCREEN['height']) -> None:
    #    assert width == SCREEN['width']
       self.title = title 
       self.width = width 
       self.height = height
       self.window = window

       pygame.display.set_caption(title)
       pygame.display.set_mode((width,height))
    
