import variables
import pygame

WIDTH, HEIGHT = variables.WIDTH, variables.HEIGHT
ROWS, COLS = variables.ROWS, variables.COLS
screen = variables.screen
grid = variables.grid

class Knight():
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
        pygame.draw.circle(screen, "purple", (centerX, centerY), self.radius)
    
    def move(self, newR, newC, currTurn):
        print(self.r, self.c)
        print(newR, newC)
        if currTurn != self.player:
            return False
        possibleMovesList = [(self.r - 1, self.c + 2), 
                            (self.r - 1, self.c - 2), 
                            (self.r + 1, self.c + 2),
                            (self.r + 1, self.c - 2),
                            (self.r - 2, self.c + 1),
                            (self.r - 2, self.c - 1),
                            (self.r + 2, self.c + 1),
                            (self.r + 2, self.c - 1)]
        
        possibleMoves = set()
        for move in possibleMovesList:
            if move[0] in range(8) and move[1] in range(8):
                possibleMoves.add(move)

        if (newR, newC) in possibleMoves:
            if grid[newR][newC] != 0 and grid[newR][newC].player == self.player:
                return False
            grid[self.r][self.c] = 0
            self.r, self.c = newR, newC
            grid[self.r][self.c] = self
            return True
        return False
        
