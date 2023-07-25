import pygame
import config

class MainGrid:
    def __init__(self) -> None:
        self.size=int(input("Enter the N of the NxN grid:")) #the N of the N x N grid
        self.grid_elements=[] #empty list to hold the coordinates and colored flag of each rectangle
        self.grid_color=(255,255,255)
        self.CheckSize()
        pass

    def CheckSize(self):
        areaOfBlocks=config.BLOCKWIDTH*config.BLOCKHEIGHT*self.size*self.size
        if areaOfBlocks > config.WIDTH * config.HEIGHT:
            # check if the no of nxn squares will fit in the window
            print("Sorry grid is too big for window size please try again...........")
            quit()
        pass

    def CheckInputs(self, screen , events,Player)-> bool:
        for event in events:
            #check in events
            if event.type == pygame.MOUSEBUTTONDOWN: #checks if the mouse is pressed on a grid element
                for (index,[posx, posy, is_pressed]) in enumerate(self.grid_elements):
                    # self.grid contain all the coordinates of the grid elements 
                    grid_element = pygame.Rect(posx, posy, config.BLOCKWIDTH, config.BLOCKHEIGHT)
                    if grid_element.collidepoint(pygame.mouse.get_pos()): 
                        if is_pressed is None:
                        #check if not already pressed and see if rect coordinates overlap current mouse coordinates
                            self.grid_elements[index][2]=Player.drawSymbol(posx,posy,screen)
                            #sets the is_pressed to either True or False depending on which player presses the element
                        return True
        return False
                    
    def checkForWin(self):
        self.board_status = [sublist[2] for sublist in self.grid_elements]
        #the grid elements list contains all the rectangles [posx,posy and if marked or not] in sublists
        #Seperate the if_marked from grid elements and tranfer it to board_status to check for wins and draw
        for index in range(self.size):
            row_start = index * self.size
            row_end = (index + 1) * self.size

            col_start=index
            col_end=((self.size)*(self.size-1))+index+2

            left_dia_start=0
            left_dia_stop=self.size*self.size

            right_dia_start=self.size-1
            right_dia_stop=(self.size*self.size)-self.size+1

            row_check=(self.board_status[row_start:row_end])
            col_check=(self.board_status[col_start:col_end:self.size])
            left_dia_check=(self.board_status[left_dia_start:left_dia_stop:self.size+index])
            right_dia_check=(self.board_status[right_dia_start:right_dia_stop:self.size-index])


            if row_check==['X']*self.size or col_check==['X']*self.size or left_dia_check==['X']*self.size or right_dia_check==['X']*self.size:
                #if any row or col or diagonal contains only x then player 1 wins
                print("Player 1 wins!")
                return True
            elif row_check==['O']*self.size or col_check==['O']*self.size or left_dia_check==['O']*self.size or right_dia_check==['O']*self.size:
                #if any row or col or diagonal contains only O then player 2
                print("Player 2 wins!")    
                return False
            elif not None in self.board_status:
                #if all the rows and cols are filled and no winner found the game is draw
                print("The game is a draw.")
                self.RestartGrid()
                return None
        return None 
                
    def generateGrid(self,screen)->None:
        self.grid_elements=[]
        posy=posx=(config.WIDTH-config.BLOCKWIDTH*self.size)//2 
        #initial position of the first block depending on the no of blocks - width of screen divide by 2 
        #sets grid to the middle with equal spacing from the border
        for rows in range(self.size):
            for cols in range(self.size):
                grid_element = pygame.Rect(posx, posy, config.BLOCKWIDTH, config.BLOCKHEIGHT)
                self.grid_elements.append([posx,posy,None])
                #each element in  grid_elements holds the x pos, y pos and boolean value to check if element clicked
                pygame.draw.rect(screen,self.grid_color, grid_element,  3) 
                #draws squares at posx,posy of size config.BLOCKWIDTH*config.BLOCKHEIGHT
                posx+=config.BLOCKWIDTH
                #add to x position for next rectangle
            posx=(config.WIDTH-config.BLOCKWIDTH*self.size)//2#reset the x position to initial position of x
            posy+=config.BLOCKHEIGHT#add to the y postion
            #when row is complete reset the x position and add block height to y position
        pass
    
    def RestartGrid(self)->None:
        screen=pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        backgroundcolor=(0,0,0)
        screen.fill(backgroundcolor)
        self.generateGrid(screen)
        pass


