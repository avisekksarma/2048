from curses import KEY_LEFT, KEY_RIGHT
import sys
from termios import INPCK
import pygame
import random
from GameTemplate import GameTemplate
from constants import FRAMERATE, SCREEN, AssetManager
from shapes import TextRect


#
class Board(object):
    topLeftPos = (SCREEN['width']*0.2, SCREEN['height']*0.2)

    def __init__(self, window, size=4):
        self.window = window
        self.size = size
        self.board = [['' for j in range(size)]for i in range(size)]
        self.prevBoard  = self.board
        self.unusedPos = [(i, j) for i in range(4) for j in range(4)]
        self.randomList = [2 for i in range(9)]
        self.randomList.append(4)
        # self.__initResources()

    # def __initResources(self):
    #     AssetManager.loadFont()

    def fillNextNumber(self):
        randomNum = random.choice(self.randomList)
        randomIndex = random.randrange(len(self.unusedPos))
        randomPos = self.unusedPos[randomIndex]
        del self.unusedPos[randomIndex]
        self.board[randomPos[0]][randomPos[1]] = randomNum

    def handleMovement(self, keyCode):
        self.prevBoard = self.board
        self.unusedPos = []
        moved = False
        combined = False
        # many things are made for 4*4 matrix 2048 for now
        if (keyCode == pygame.K_LEFT):
            for i in range(4):
                # ====================
                # for storing value part
                lst = []
                flag = False
                for j in range(4):
                    if self.board[i][j]:
                        lst.append(self.board[i][j])
                    else:
                        # setting flag = true for when at least one empty square i.e movement to be done for sure
                        flag = True
                # for moving part
                if flag:
                    moved = True
                    for j in range(4):
                        if j < len(lst):
                            self.board[i][j] = lst[j]
                        else:
                            self.board[i][j] = ''
                # ====================
                if(self.board[i][0]):
                    j=0
                    while j < 3:
                        if(self.board[i][j]==self.board[i][j+1]):
                            self.board[i][j]*=2
                            self.board[i][j+1]=''
                            j=j+2
                            combined = True
                        else:
                            j=j+1
                # ====================
                # repeated part
                lst = []
                flag = False
                for j in range(4):
                    if self.board[i][j]:
                        lst.append(self.board[i][j])
                    else:
                        flag = True
                # for moving part
                if flag:
                    moved = True
                    for j in range(4):
                        if j < len(lst):
                            self.board[i][j] = lst[j]
                        else:
                            self.unusedPos.append((i,j))
                            self.board[i][j] = ''
                # ====================

        elif (keyCode == pygame.K_RIGHT):
            for i in range(4):
                # ============================
                lst = []
                flag = False
                for j in range(3,-1,-1):
                    if self.board[i][j]:
                        lst.append(self.board[i][j])
                    else:
                        flag = True
                if flag:
                    moved = True
                    for j in range(3,-1,-1):
                        if 4-j-1<len(lst):
                            self.board[i][j] = lst[4-(j+1)]
                        else:
                            self.board[i][j] = ''
                # ==========================
                if(self.board[i][3]):
                    j=3
                    while j > 0:
                        if(self.board[i][j]==self.board[i][j-1]):
                            self.board[i][j]*=2
                            self.board[i][j-1]=''
                            j=j-2
                            combined = True
                        else:
                            j=j-1

                # repeated part
                lst = []
                flag = False
                for j in range(3,-1,-1):
                    if self.board[i][j]:
                        lst.append(self.board[i][j])
                    else:
                        flag = True
                if flag:
                    moved = True
                    for j in range(3,-1,-1):
                        if 4-j-1<len(lst):
                            self.board[i][j] = lst[4-(j+1)]
                        else:
                            self.unusedPos.append((i,j))
                            self.board[i][j] = ''

        elif (keyCode == pygame.K_UP):
            for i in range(4):
                # ====================
                # for storing value part
                lst = []
                flag = False
                for j in range(4):
                    if self.board[j][i]:
                        lst.append(self.board[j][i])
                    else:
                        flag = True
                # for moving part
                if flag:
                    moved = True
                    for j in range(4):
                        if j < len(lst):
                            self.board[j][i] = lst[j]
                        else:
                            self.board[j][i] = ''
                # ====================
                if(self.board[0][i]):
                    j=0
                    while j < 3:
                        if(self.board[j][i]==self.board[j+1][i]):
                            self.board[j][i]*=2
                            self.board[j+1][i]=''
                            j=j+2
                            combined = True
                        else:
                            j=j+1
                # ====================
                # repeated part
                lst = []
                flag = False
                for j in range(4):
                    if self.board[j][i]:
                        lst.append(self.board[j][i])
                    else:
                        flag = True
                # for moving part
                if flag:
                    moved = True
                    for j in range(4):
                        if j < len(lst):
                            self.board[j][i] = lst[j]
                        else:
                            self.unusedPos.append((j,i))
                            self.board[j][i] = ''
                # ====================

        elif (keyCode == pygame.K_DOWN):
            for i in range(4):
                # ============================
                lst = []
                flag = False
                for j in range(3,-1,-1):
                    if self.board[j][i]:
                        lst.append(self.board[j][i])
                    else:
                        flag = True
                if flag:
                    moved = True
                    for j in range(3,-1,-1):
                        if 4-j-1<len(lst):
                            self.board[j][i] = lst[4-(j+1)]
                        else:
                            self.board[j][i] = ''
                # ==========================
                if(self.board[3][i]):
                    j=3
                    while j > 0:
                        if(self.board[j][i]==self.board[j-1][i]):
                            self.board[j][i]*=2
                            self.board[j-1][i]=''
                            j=j-2
                            combined = True
                        else:
                            j=j-1

                # ============================
                lst = []
                flag = False
                for j in range(3,-1,-1):
                    if self.board[j][i]:
                        lst.append(self.board[j][i])
                    else:
                        flag = True
                if flag:
                    moved = True
                    for j in range(3,-1,-1):
                        if 4-j-1<len(lst):
                            self.board[j][i] = lst[4-(j+1)]
                        else:
                            self.unusedPos.append((j,i))
                            self.board[j][i] = ''
                # ==========================

        if(moved or combined):
            self.fillNextNumber()

    def render(self):

        # magic number place
        sqsize = 90

        surf = pygame.Surface((sqsize*self.size, sqsize*self.size))
        surf = surf.get_rect(top=Board.topLeftPos[0], left=Board.topLeftPos[1])
        pygame.draw.rect(self.window, (255, 211, 132), surf, 0, 10)
        for i in range(self.size):
            for j in range(self.size):
                obj = TextRect(str(self.board[i][j]), (self.topLeftPos[0]+(
                    sqsize*j), self.topLeftPos[1]+(sqsize*i)), (sqsize, sqsize))
                obj.draw(self.window)


class GameScreen(GameTemplate):
    def __init__(self, title, window, width=SCREEN['width'], height=SCREEN['height']) -> None:
        super().__init__(title, window, width, height)
        self.btns = {}
        self.gameBoard = Board(window)

    def render(self):
        self.window.fill((120, 80, 100))
        self.gameBoard.render()
        pygame.display.update()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        self.gameBoard.fillNextNumber()
        while running:
            clock.tick(FRAMERATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.gameBoard.handleMovement(event.key)

            self.render()


# for i in range(4):
                
            #     # for joining part
            #     for j in range(3):
            #         if (j+1 > 3):
            #             break
            #         if (self.board[i][j] == self.board[i][j+1]):
            #             self.board[i][j] *= 2
            #             self.board[i][j+1] = ''
            #             j = j+1
            #     # for storing value part
            #     lst = []
            #     for j in range(4):
            #         if self.board[i][j]:
            #             lst.append(self.board[i][j])
            #     # for moving part
            #     for j in range(4):
            #         if j < len(lst):
            #             self.board[i][j] = lst[j]
            #         else:
            #             self.unusedPos.append((i,j))
            #             self.board[i][j] = ''