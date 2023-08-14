import variables
import pygame

WIDTH, HEIGHT = variables.WIDTH, variables.HEIGHT
ROWS, COLS = variables.ROWS, variables.COLS
screen = variables.screen
grid = variables.grid

class Player():
    def __init__(self, number, pieces):
        self.number = number
        self.inCheck = False
        self.pieces = pieces
        self.king = None

    def isInCheck(self, grid):
        self.inCheck = self.king.isInCheck(grid)
        return self.inCheck