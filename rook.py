import variables
import pygame

WIDTH, HEIGHT = variables.WIDTH, variables.HEIGHT
ROWS, COLS = variables.ROWS, variables.COLS
screen = variables.screen
grid = variables.grid

class Rook():
    def __init__(self, r, c, player):
        self.isClicked = False
        self.movedYet = False
        self.r = r
        self.c = c
        self.player = player
        self.radius = 20
    
    def draw(self, r, c):
        centerX = c * WIDTH // 8 + .5 * WIDTH // 8
        centerY = r * WIDTH // 8 + .5 * WIDTH // 8
        pygame.draw.circle(screen, "blue", (centerX, centerY), self.radius)
    
    def move(self, newR, newC, currTurn):
        if currTurn != self.player:
            return False
        if (newC == self.c and newR != self.r) or (newR == self.r and newC != self.c):
            if grid[newR][newC] != 0 and grid[newR][newC].player == self.player:
                return False
            grid[self.r][self.c] = 0
            self.r, self.c = newR, newC
            grid[self.r][self.c] = self
            return True
        return False

    def bannedSpots(self):
        res = set()

        #Spaces in front
        tempR = self.r - 1
        while tempR >= 0:
            if grid[tempR][self.c] != 0:
                break
            res.add((tempR, self.c))
            tempR -= 1
        
        #Spaces below
        tempR = self.r + 1
        while tempR < 8:
            if grid[tempR][self.c] != 0:
                break
            res.add((tempR, self.c))
            tempR += 1

        #Spaces to the left
        tempC = self.c - 1
        while tempC >= 0:
            if grid[self.r][tempC] != 0:
                break
            res.add((self.r, tempC))
            tempC -= 1
        
        #Spaces to the right
        tempC = self.c + 1
        while tempC < 8:
            if grid[self.r][tempC] != 0:
                break
            res.add((self.r, tempC))
            tempC += 1
        
        return res



