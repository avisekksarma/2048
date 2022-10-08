import pygame
from sys import exit
pygame.init()
win = pygame.display.set_mode((600,600))
running = True

# one way (rect way)
x = pygame.Surface((50,50))
y = x.get_rect(center = (100,100))  # you can put left-top, right,etc also there.
z = pygame.Surface((100,100))
a = z.get_rect(center = (100,100))
# other way( Surface way)
b = pygame.Surface((200,200))
b.fill((200,200,0))
c = pygame.Surface((30,30))
c.fill((0,0,0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255,120,100))
    # one way (rect way)
    pygame.draw.rect(win, (100, 200, 120), a)   # or 'a' can be Rect(1,2,3,4) also there 
						# i.e rectangle object.
    pygame.draw.rect(win, (100, 200, 255), y)

    # other way( Surface way)
    win.blit(b,(300,300))
    win.blit(c,(300,100))
    pygame.display.flip()