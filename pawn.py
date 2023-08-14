import variables
import pygame

WIDTH, HEIGHT = variables.WIDTH, variables.HEIGHT
ROWS, COLS = variables.ROWS, variables.COLS
screen = variables.screen
grid = variables.grid

class Pawn():
    def __init__(self, r, c, player):
        self.isClicked = False
        self.isFirstMove = True
        self.r = r
        self.c = c
        self.player = player.number
        self.playerObj = player
        self.radius = 20
        self.type = "pawn"
    
    def draw(self, r, c):
        centerX = c * WIDTH // 8 + .5 * WIDTH // 8
        centerY = r * WIDTH // 8 + .5 * WIDTH // 8
        if self.player == 0:
            color = "green"
        else:
            color = "brown"
        pygame.draw.circle(screen, color, (centerX, centerY), self.radius)
    
    def move(self, newR, newC, currTurn):
        if currTurn != self.player:
            return False
        possibleSpots = set()
        if self.player == 0:
            if self.isFirstMove:
                if (self.r - 2) in range(8) and grid[self.r - 2][self.c] == 0:
                    possibleSpots.add((self.r - 2, self.c))
            if (self.r - 1) in range(8) and grid[self.r - 1][self.c] == 0:
                possibleSpots.add((self.r - 1, self.c))
            if (self.r - 1) in range(8) and (self.c + 1) in range(8) and grid[self.r - 1][self.c + 1] != 0 and grid[self.r - 1][self.c + 1].player == 1:
                possibleSpots.add((self.r - 1, self.c + 1))
            if (self.r - 1) in range(8) and (self.c - 1) in range(8) and grid[self.r - 1][self.c - 1] != 0 and grid[self.r - 1][self.c - 1].player == 1:
                possibleSpots.add((self.r - 1, self.c - 1))
            
        elif self.player == 1:
            if self.isFirstMove:
                if (self.r + 2) in range(8) and grid[self.r + 2][self.c] == 0:
                    possibleSpots.add((self.r + 2, self.c))
            if (self.r + 1) in range(8) and grid[self.r + 1][self.c] == 0:
                possibleSpots.add((self.r + 1, self.c))
            if (self.r + 1) in range(8) and (self.c + 1) in range(8) and grid[self.r + 1][self.c + 1] != 0:
                possibleSpots.add((self.r + 1, self.c + 1))
            if (self.r + 1) in range(8) and (self.c - 1) in range(8) and grid[self.r + 1][self.c - 1] != 0:
                possibleSpots.add((self.r + 1, self.c - 1))

        if (newR, newC) in possibleSpots:
            if self.playerObj.inCheck:
                grid[self.r][self.c] = 0
                prev = grid[newR][newC]
                grid[newR][newC] = self
                if self.playerObj.isInCheck(grid):
                    grid[self.r][self.c] = self
                    grid[newR][newC] = prev
                    return False
                else:
                    grid[self.r][self.c] = 0
                    self.r, self.c = newR, newC
                    grid[self.r][self.c] = self
                    self.isFirstMove = False
                    return True
            else:
                grid[self.r][self.c] = 0
                self.r, self.c = newR, newC
                grid[self.r][self.c] = self
                self.isFirstMove = False
                return True
        
        return False
    
    def bannedSpots(self):
        res = set()
        
        if self.player == 0:
            dirs = [
                [self.r - 1, self.c + 1],
                [self.r - 1, self.c - 1]
            ]
        else:
            dirs = [
                [self.r + 1, self.c + 1],
                [self.r + 1, self.c - 1],
            ]

        for r, c in dirs:
            if (r not in range(8) or
                c not in range(8) or
                grid[r][c] != 0):
                continue
            res.add((r, c))
        
        return res
