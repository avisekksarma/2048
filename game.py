from copy import deepcopy
import sys
import pygame
import random
from GameTemplate import GameTemplate
from constants import FRAMERATE, SCREEN, AssetManager
from shapes import TextRect,Button


#
class Board(object):
    topLeftPos = (SCREEN['width']*0.2, SCREEN['height']*0.2)
    # magic number place
    sqsize = 90
    rectColorDict = {
        '': (205,193,180),
        '2': (238,228,218),
        '4': (237,224,200),
        '8': (242,177,121),
        '16': (245,149,99),
        '32': (246,124,96),
        '64': (246,94,59),
        '128': (237,207,115),
        '256': (237,204,98),
        '512': (237,200,80),
        '1024': (237,197,63),
        '2048': (237,194,45),
    }
    textColorDict = {
        '': (255,255,255),
        '2': (119, 98, 80),
        '4': (119, 98, 80),
        '8': (249, 220, 191),
        '16': (249, 220, 191),
        '32': (249, 220, 191),
        '64': (249, 220, 191),
        '128': (249, 220, 191),
        '256': (249, 220, 191),
        '512': (249, 220, 191),
        '1024': (249, 220, 191),
        '2048': (249, 220, 191),
    }


    def __init__(self, window, size=4):
        # critical ones for a game state = board, prevBoard, unusedPos,score,prevScore
        self.window = window
        self.size = size
        self.board = [['' for j in range(size)]for i in range(size)]
        self.prevBoard  = None # initally set to None
        self.unusedPos = [(i, j) for i in range(4) for j in range(4)]
        self.randomList = [2 for i in range(9)]
        self.randomList.append(4)
        # surface setup of whole board
        self.surface = pygame.Surface((self.sqsize*self.size, self.sqsize*self.size))
        # now surface is rectangle
        self.surf = self.surface.get_rect(top=Board.topLeftPos[0], left=Board.topLeftPos[1])
        self.fillNextNumber()
        self.fillNextNumber()
        self.prevScore = 0
        self.score = 0
        self.continuePlay = False
        self.gameover = False
        # self.__initResources()

    # def __initResources(self):
    #     AssetManager.loadFont()

    def fillNextNumber(self):
        randomNum = random.choice(self.randomList)
        randomIndex = random.randrange(len(self.unusedPos))
        randomPos = self.unusedPos[randomIndex]
        del self.unusedPos[randomIndex]
        self.board[randomPos[0]][randomPos[1]] = randomNum

    def handleMovement(self, keyCode,checkGameOver=False):
        if not checkGameOver:
            self.prevBoard = deepcopy(self.board)
            self.prevScore = self.score
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
                            self.score = self.score + self.board[i][j]
                            
                            self.board[i][j+1]=''
                            # print((i,j))
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
                            self.score = self.score + self.board[i][j]
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
                            self.score = self.score + self.board[j][i]
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
                            self.score = self.score + self.board[j][i]
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

        # print(self.unusedPos)

        if(moved or combined):
            self.fillNextNumber()
        if checkGameOver:
            return combined

    def resetGame(self,window,size=4):
        return Board(window,size)

    def undoMove(self):
        if(self.prevBoard): # i.e do only if prevBoard is not None
            self.board = deepcopy(self.prevBoard)
            self.score = self.prevScore
            self.unusedPos = []
            for i in range(4):
                for j in range(4):
                    if self.board[i][j]=='':
                        self.unusedPos.append((i,j))
        
    def isGameWon(self):
        # print(self.board)
        for i in range(4):
            # print(self.board[i])
            if 2048 in self.board[i]:
               return True 

    def isGameOver(self):
        if len(self.unusedPos) != 0:
            self.gameover = False
            return False
        else:
            lst = []
            board = deepcopy(self.board)
            unusedPos = deepcopy(self.unusedPos)
            score = self.score
            lst.append(self.handleMovement(pygame.K_LEFT,True))
            lst.append(self.handleMovement(pygame.K_RIGHT,True))
            lst.append(self.handleMovement(pygame.K_UP,True))
            lst.append(self.handleMovement(pygame.K_DOWN,True))
            if True not in lst:
                # i.e. not combined, i.e game is over
                self.gameover = True
                return True
            else:
                # restore game state
                self.board = deepcopy(board) 
                self.unusedPos = deepcopy(unusedPos)
                self.score = score
                self.gameover = False
                return False


    def render(self):
        pygame.draw.rect(self.window, (255, 211, 132), self.surf, 0, 10)
        for i in range(self.size):
            for j in range(self.size):
                rectColor = Board.rectColorDict[str(self.board[i][j])]
                textColor = Board.textColorDict[str(self.board[i][j])]
                obj = TextRect(str(self.board[i][j]), (self.topLeftPos[0]+(
                    self.sqsize*j), self.topLeftPos[1]+(self.sqsize*i)), (self.sqsize, self.sqsize),rectColor,textColor)
                obj.draw(self.window)


class GameScreen(GameTemplate):
    def __init__(self, title, window, width=SCREEN['width'], height=SCREEN['height']) -> None:
        super().__init__(title, window, width, height)
        self.btns = {}
        self.gameBoard = Board(window)
        self.__initialize()

    def __initialize(self):
        l= self.gameBoard.surf.left
        b= self.gameBoard.surf.bottom
        pos = (l,b)
        undoBtn = Button(self.window,'UNDO','heading',Button.sizes['medium'],pos,(20,120,200),(200,120,20),True,True)
        self.btns['undoBtn'] = undoBtn
        pos=(pos[0]+undoBtn.size[0]+30,pos[1])
        resetBtn = Button(self.window,'RESET','heading',Button.sizes['medium'],pos,(20,120,200),(200,120,20),True,True)
        self.btns['resetBtn'] = resetBtn
        backBtn = Button(self.window, 'BACK', 'text', Button.sizes['standard'], (
            SCREEN['width']*0.00-20, SCREEN['height']*0.02), (170, 100, 240), (125, 250, 195), True, True)
        self.btns['backBtn'] = backBtn


    def render(self):
        self.window.fill((120, 80, 100))
        # self.window.fill((168, 232, 144))
        pos = (SCREEN['width']//2, 20)
        AssetManager.renderFont(
            'text', 'Score:', (150, 140, 230), self.window, pos)
        pos = (pos[0], pos[1]+50)
        AssetManager.renderFont('heading', str(
            self.gameBoard.score), (150, 140, 230), self.window, pos)
        for btn in self.btns:
            self.btns[btn].render()
        self.gameBoard.render()
        pygame.display.update()

    def manageGameWon(self):
        
        if self.gameBoard.isGameWon():
            surface = pygame.Surface(
                (self.gameBoard.surf.width, self.gameBoard.surf.height))
            surface.set_alpha(12)
            surface.fill((210, 210, 210))
            btns = {}
            pos = (SCREEN['width']//2-158, SCREEN['height']//2-10)
            # btns
            contBtn = Button(self.window, 'CONTINUE', 'text',
                            (150, 60), pos, (20, 120, 200), (200, 120, 20), True, True)
            btns['contBtn'] = contBtn
            pos = (pos[0]+contBtn.size[0]+20, pos[1])
            newGameBtn = Button(self.window, 'NEW GAME', 'text',
                                (150, 60), pos, (20, 120, 200), (200, 120, 20), True, True)
            btns['newGameBtn'] = newGameBtn


            running = True
            clock = pygame.time.Clock()
            
            while running:
                clock.tick(FRAMERATE)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(0)
                    if event.type == pygame.MOUSEMOTION:
                        for btn in btns:
                            btns[btn].checkHovered(event.pos)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if btns['contBtn'].checkClick(event.pos):
                            running = False
                            self.gameBoard.continuePlay = True
                        if btns['newGameBtn'].checkClick(event.pos):
                            running = False
                            self.gameBoard = self.gameBoard.resetGame(self.window)
                            
                # render part
                
                self.window.blit(surface,self.gameBoard.surf)
                pos = (SCREEN['width']//2, SCREEN['height']//2-100)
                AssetManager.renderFont(
                    'heading', 'You Won !!!', (55, 41, 72), self.window, pos)
                for btn in btns:
                    btns[btn].render()
                pygame.display.update()
                # render part ends


    def manageGameOver(self):
        surface = pygame.Surface(
            (self.gameBoard.surf.width, self.gameBoard.surf.height))
        surface.set_alpha(12)
        surface.fill((210, 210, 210))
        btns = {}
        pos = (SCREEN['width']//2-80, SCREEN['height']//2-10)
        # btns
        newGameBtn = Button(self.window, 'NEW GAME', 'text',
                            (150, 60), pos, (20, 120, 200), (200, 120, 20), True, True)
        btns['newGameBtn'] = newGameBtn

        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(FRAMERATE)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(0)
                    if event.type == pygame.MOUSEMOTION:
                        for btn in btns:
                            btns[btn].checkHovered(event.pos)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if btns['newGameBtn'].checkClick(event.pos):
                            running = False
                            self.gameBoard = self.gameBoard.resetGame(
                                self.window)

            # render part

            self.window.blit(surface, self.gameBoard.surf)
            pos = (SCREEN['width']//2, SCREEN['height']//2-100)
            AssetManager.renderFont(
                'heading', f'Game Over !!!', (55, 41, 72), self.window, pos)
            for btn in btns:
                btns[btn].render()
            pygame.display.update()
            # render part ends

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
                    for btn in self.btns:
                        self.btns[btn].checkHovered(event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.btns['undoBtn'].checkClick(event.pos):
                        self.gameBoard.undoMove()
                    if self.btns['resetBtn'].checkClick(event.pos):
                        self.gameBoard = self.gameBoard.resetGame(self.window)
                    if self.btns['backBtn'].checkClick(event.pos):
                        running = False
                        GameTemplate.changeActiveKey('start')
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.gameBoard.handleMovement(event.key)

            self.render()
            if not self.gameBoard.continuePlay:
                self.manageGameWon()
            if self.gameBoard.isGameOver():
                self.manageGameOver()

        
            




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