import variables
import pygame

WIDTH, HEIGHT = variables.WIDTH, variables.HEIGHT
ROWS, COLS = variables.ROWS, variables.COLS
screen = variables.screen
grid = variables.grid

class Queen():
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
        pygame.draw.circle(screen, "yellow", (centerX, centerY), self.radius)
    
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
        elif newR != self.r and newC != self.c and abs(newR - self.r) == abs(newC - self.c):
            if grid[newR][newC] != 0 and grid[newR][newC].player == self.player:
                return False
            grid[self.r][self.c] = 0
            self.r, self.c = newR, newC
            grid[self.r][self.c] = self
            return True
        return False

