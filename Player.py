import pygame
import config

class Player:
    def __init__(self,symbol,color) -> None:
        self.score=0
        self.color=color
        self.symbol=symbol

    def drawSymbol(self,posx,posy,screen):
        if(self.symbol=='O'):
            print("Turn for Player-1")
            x=posx+config.BLOCKWIDTH//2
            y=posy+config.BLOCKHEIGHT//2
            radius=config.BLOCKWIDTH//2-10
            pygame.draw.circle(screen,self.color,(x,y),radius)
            #set the position of the circle to the middle of the clicked square 
            # draw circle of radius half of the rectangle width -1
            return self.symbol
        elif(self.symbol=='X'):
            print("Turn for Player-2")
            spacing=10
            pygame.draw.lines(screen, self.color, False, [(posx+spacing,posy+spacing),(posx+config.BLOCKWIDTH-spacing,posy+config.BLOCKHEIGHT-spacing)],10)
            #draw line from the left upper corner to lower right corner 
            pygame.draw.lines(screen, self.color, False, [(posx+config.BLOCKWIDTH-spacing,posy+spacing),(posx+spacing,posy+config.BLOCKHEIGHT-spacing)], 10)
            #draws line form the right upper corner to lower left corner
            return self.symbol
        pass