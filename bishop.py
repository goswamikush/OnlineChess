import variables
import pygame

WIDTH, HEIGHT = variables.WIDTH, variables.HEIGHT
ROWS, COLS = variables.ROWS, variables.COLS
screen = variables.screen
grid = variables.grid

class Bishop():
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
        pygame.draw.circle(screen, "red", (centerX, centerY), self.radius)
    
    def move(self, newR, newC, currTurn):
        if currTurn != self.player:
            return False
        if newR != self.r and newC != self.c and abs(newR - self.r) == abs(newC - self.c):
            if grid[newR][newC] != 0 and grid[newR][newC].player == self.player:
                return False
            grid[self.r][self.c] = 0
            self.r, self.c = newR, newC
            grid[self.r][self.c] = self
            return True
        return False

    def bannedSpots(self):
        res = set()
        #Top right diagonal
        r, c = self.r - 1, self.c + 1
        while r in range(8) and c in range(8):
            if grid[r][c] != 0:
                break
            res.add((r, c))
            r -= 1
            c += 1
        
        #Top left diagonal
        r, c = self.r - 1, self.c - 1
        while r in range(8) and c in range(8):
            if grid[r][c] != 0:
                break
            res.add((r, c))
            r -= 1
            c -= 1
        
        #Bottom right diagonal
        r, c = self.r + 1, self.c + 1
        while r in range(8) and c in range(8):
            if grid[r][c] != 0:
                break
            res.add((r, c))
            r += 1
            c += 1
        
        #Bottom right diagonal
        r, c = self.r + 1, self.c - 1
        while r in range(8) and c in range(8):
            if grid[r][c] != 0:
                break
            res.add((r, c))
            r += 1
            c -= 1
        
        return res
