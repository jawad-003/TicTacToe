import pygame
import Player
import MainGrid
import config

def main():
    pygame.init() #initialize pygame
    grid=MainGrid.MainGrid()
    player1= Player.Player('O',config.PLAYER1COLOR)#set the symbol of the player and 
    player2=Player.Player('X',config.PLAYER2COLOR)
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    backgroundcolor=(0,0,0)
    screen.fill(backgroundcolor)
    grid.generateGrid(screen)
    turn=0 # first turn will be the player 1
    running = True
    winner=None
    while running:
        events = pygame.event.get()
        #event.get() function takes events from the event queue
        #to avoid dataloss by calling twice set it as a variable
        #calling it twice causes loss of events
        if turn%2==0 and grid.CheckInputs(screen,events,player1):
            turn+=1
        elif turn%2!=0 and grid.CheckInputs(screen,events,player2):
            turn+=1
        pygame.display.update()
        winner=grid.checkForWin()
        if winner is not None:
            if winner==True:   
                player1.score+=1
                print("Current Score:",player1.score)
            else:
                player2.score+=1
                print("Current Score:",player2.score)

            print("\nDo you want to play again?:")
            choice=str(input("Enter y or n:")).lower()
            if choice=="y":
                winner=None
                grid.RestartGrid()
            elif choice=="n":
                print(f"Player1 Scored:{player1.score}\nPlayer2 Scored:{player2.score}")
                if(player1.score>player2.score):
                    print("Player1 wins")
                elif(player2.score<player1.score):
                    print("Player2 wins")
                elif(player1.score==player2.score):
                    print("Draw")
                running=False
        pygame.display.update()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    return
  
if __name__=="__main__":
    main()
