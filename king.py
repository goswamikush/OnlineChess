import variables
import pygame

WIDTH, HEIGHT = variables.WIDTH, variables.HEIGHT
ROWS, COLS = variables.ROWS, variables.COLS
screen = variables.screen
grid = variables.grid

class King():
    def __init__(self, r, c, player):
        self.isClicked = False
        self.isFirstMove = True
        self.r = r
        self.c = c
        self.player = player.number
        self.playerObj = player
        self.player = player
        self.radius = 20
    
    def draw(self, r, c):
        centerX = c * WIDTH // 8 + .5 * WIDTH // 8
        centerY = r * WIDTH // 8 + .5 * WIDTH // 8
        if self.player == 0:
            color = "orange"
        else:
            color = "blue"
        pygame.draw.circle(screen, color, (centerX, centerY), self.radius)
    
    def move(self, newR, newC, currTurn):
        if currTurn != self.player:
            return False
        possibleMovesList = [[self.r + 1, self.c],
                            [self.r - 1, self.c],
                            [self.r, self.c + 1],
                            [self.r, self.c - 1],
                            [self.r + 1, self.c - 1],
                            [self.r + 1, self.c + 1],
                            [self.r - 1, self.c - 1],
                            [self.r - 1, self.c + 1]]
        
        possibleMovesSet = set()
        for move in possibleMovesList:
            if (move[0] not in range(8) or 
                move[1] not in range(8) or
                (grid[move[0]][move[1]] != 0 and grid[move[0]][move[1]].player == self.player)):
                continue
            possibleMovesSet.add((move[0], move[1]))
        
        if (newR, newC) in possibleMovesSet:
            grid[self.r][self.c] = 0
            self.r, self.c = newR, newC
            grid[self.r][self.c] = self
            return True

        return False

    def bannedSpots(self):
        res = set()
        
        dirs = [
            [self.r + 1, self.c],
            [self.r - 1, self.c],
            [self.r, self.c - 1],
            [self.r, self.c + 1],
            [self.r + 1, self.c + 1],
            [self.r + 1, self.c - 1],
            [self.r - 1, self.c + 1],
            [self.r - 1, self.c - 1]
        ]

        for r, c in dirs:
            if (r not in range(8) or
                c not in range(8) or
                grid[r][c] != 0):
                continue
            res.add((r, c))
        
        return res