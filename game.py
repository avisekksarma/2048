from copy import deepcopy
import sys
import pygame
import random
from GameTemplate import GameTemplate
from constants import FRAMERATE, SCREEN
from shapes import TextRect,Button


#
class Board(object):
    topLeftPos = (SCREEN['width']*0.2, SCREEN['height']*0.2)
    # magic number place
    sqsize = 90

    def __init__(self, window, size=4):
        self.window = window
        self.size = size
        self.board = [['' for j in range(size)]for i in range(size)]
        self.prevBoard  = None # initally set to None
        self.unusedPos = [(i, j) for i in range(4) for j in range(4)]
        self.randomList = [2 for i in range(9)]
        self.randomList.append(4)
        # surface setup of whole board
        self.surf = pygame.Surface((self.sqsize*self.size, self.sqsize*self.size))
        # now surface is rectangle
        self.surf = self.surf.get_rect(top=Board.topLeftPos[0], left=Board.topLeftPos[1])
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
        self.prevBoard = deepcopy(self.board)
        self.unusedPos = []
        moved = False
        combined = False
        # many things are made for 4*4 matrix 2048 for now
        if (keyCode == pygame.K_LEFT):
            for i in range(4):
                # ====================
                # for storing value part
                lst = []
                flag = -1
                for j in range(4):
                    if self.board[i][j]:
                        lst.append(self.board[i][j])
                        if flag == 0:
                            flag = 1 # 1 indicates -> now move is necessary
                    else:
                        # setting flag = true for when at least one empty square i.e movement to be done for sure
                        if flag == -1: # -1 indicates no '' till now
                            flag = 0 # 0 indicates first time '' occured
                # for moving part
                if flag==1:
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
                        if(self.board[i][j] and self.board[i][j]==self.board[i][j+1]):
                            self.board[i][j]*=2
                            self.board[i][j+1]=''
                            print((i,j))
                            j=j+2
                            
                            combined = True
                        else:
                            j=j+1
                # ====================
                # repeated part
                lst = []
                flag = -1
                for j in range(4):
                    if self.board[i][j]:
                        lst.append(self.board[i][j])
                        if flag == 0:
                            flag = 1 
                    else:
                        if flag == -1 :
                            flag = 0 
                # for moving part
                if flag==1:
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
                flag = -1
                for j in range(3,-1,-1):
                    if self.board[i][j]:
                        lst.append(self.board[i][j])
                        if flag == 0:
                            flag = 1 
                    else:
                        if flag == -1 :
                            flag = 0
                if flag==1:
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
                        if(self.board[i][j] and self.board[i][j]==self.board[i][j-1]):
                            self.board[i][j]*=2
                            self.board[i][j-1]=''
                            j=j-2
                            combined = True
                        else:
                            j=j-1

                # repeated part
                lst = []
                flag = -1
                for j in range(3,-1,-1):
                    if self.board[i][j]:
                        lst.append(self.board[i][j])
                        if flag == 0:
                            flag = 1
                    else:
                        if flag == -1:
                            flag = 0
                if flag==1:
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
                flag = -1
                for j in range(4):
                    if self.board[j][i]:
                        lst.append(self.board[j][i])
                        if flag == 0:
                            flag = 1
                    else:
                        if flag == -1:
                            flag = 0
                # for moving part
                if flag==1:
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
                        if(self.board[j][i] and self.board[j][i]==self.board[j+1][i]):
                            self.board[j][i]*=2
                            self.board[j+1][i]=''
                            j=j+2
                            combined = True
                        else:
                            j=j+1
                # ====================
                # repeated part
                lst = []
                flag = -1
                for j in range(4):
                    if self.board[j][i]:
                        lst.append(self.board[j][i])
                        if flag == 0:
                            flag = 1
                    else:
                        if flag == -1:
                            flag = 0
                # for moving part
                if flag==1:
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
                flag = -1
                for j in range(3,-1,-1):
                    if self.board[j][i]:
                        lst.append(self.board[j][i])
                        if flag == 0:
                            flag = 1
                    else:
                        if flag == -1:
                            flag = 0

                if flag==1:
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
                        if(self.board[j][i] and self.board[j][i]==self.board[j-1][i]):
                            self.board[j][i]*=2
                            self.board[j-1][i]=''
                            j=j-2
                            combined = True
                        else:
                            j=j-1

                # ============================
                lst = []
                flag = -1
                for j in range(3,-1,-1):
                    if self.board[j][i]:
                        lst.append(self.board[j][i])
                        if flag == 0:
                            flag = 1
                    else:
                        if flag == -1:
                            flag = 0
                if flag==1:
                    moved = True
                for j in range(3,-1,-1):
                    if 4-j-1<len(lst):
                        self.board[j][i] = lst[4-(j+1)]
                    else:
                        self.unusedPos.append((j,i))
                        self.board[j][i] = ''
                # ==========================

        print('moved = ',moved)
        print('combined = ',combined)
        if(moved or combined):
            self.fillNextNumber()

    def undoMove(self):
        self.board = deepcopy(self.prevBoard)
        

    def render(self):
        pygame.draw.rect(self.window, (255, 211, 132), self.surf, 0, 10)
        for i in range(self.size):
            for j in range(self.size):
                obj = TextRect(str(self.board[i][j]), (self.topLeftPos[0]+(
                    self.sqsize*j), self.topLeftPos[1]+(self.sqsize*i)), (self.sqsize, self.sqsize))
                obj.draw(self.window)


class GameScreen(GameTemplate):
    def __init__(self, title, window, width=SCREEN['width'], height=SCREEN['height']) -> None:
        super().__init__(title, window, width, height)
        self.btns = {}
        self.gameBoard = Board(window)
        self.__initialize()

    def __initialize(self):
        l= self.gameBoard.surf.left
        t= self.gameBoard.surf.top
        pos = (l,t)
        undoBtn = Button(self.window,'Undo','heading',Button.sizes['medium'],pos,(160,120,200),(200,120,200),True)
        self.btns['undoBtn'] = undoBtn


    def render(self):
        self.window.fill((120, 80, 100))
        for btn in self.btns:
            self.btns[btn].render()
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