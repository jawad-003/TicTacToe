import pygame
import MainGrid
import config

class AiPlayer:
    def __init__(self,grid:MainGrid) -> None:
        self.score=0
        self.board_status=grid.board_status
        pass