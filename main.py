import pygame
import variables
import pawn
import rook
import bishop
import knight
import queen
import king
import player
# pygame setup
ROWS, COLS = variables.ROWS, variables.COLS
WIDTH, HEIGHT = variables.WIDTH, variables.HEIGHT

screen = variables.screen
clock = variables.clock
running = variables.running

grid = variables.grid

currTurn = 0

player0 = player.Player(0, set())
player1 = player.Player(1, set())

def draw_board():
    currColor = "black"
    for r in range(8):
        currColor = "black" if currColor != "black" else "white"
        for c in range(8):
            x_start = c * WIDTH // ROWS
            x_end = x_start + WIDTH // ROWS
            
            y_start = r * WIDTH // COLS
            y_end = y_start + WIDTH // COLS

            for x in range(x_start, x_end):
                for y in range(y_start, y_end):
                    screen.set_at((x, y), currColor)
                    
            currColor = "black" if currColor != "black" else "white"

def initialize_grid():
    r = 6
    for c in range(8):
        newPawn = pawn.Pawn(r, c, player0)
        grid[r][c] = newPawn
        newPawn.draw(r, c)
        player0.pieces.add(newPawn)
    
    r = 1
    for c in range(8):
        newPawn = pawn.Pawn(r, c, player1)
        grid[r][c] = newPawn
        newPawn.draw(r, c)
        player1.pieces.add(newPawn)

    r = (0, 7)
    for c in range(8):
        if c == 0 or c == 7:
            newRook = rook.Rook(r[0], c, player1)
            grid[r[0]][c] = newRook
            newRook.draw(r[0], c)
            player1.pieces.add(newRook)

            newRook = rook.Rook(r[1], c, player0)
            grid[r[1]][c] = newRook
            newRook.draw(r[1], c)
            player0.pieces.add(newRook)
        if c == 1 or c == 6:
            newKnight = knight.Knight(r[0], c, player1)
            grid[r[0]][c] = newKnight
            newKnight.draw(r[0], c)
            player1.pieces.add(newKnight)

            newKnight = knight.Knight(r[1], c, player0)
            grid[r[1]][c] = newKnight
            newKnight.draw(r[1], c)
            player0.pieces.add(newKnight)
        if c == 2 or c == 5:
            newBishop = bishop.Bishop(r[0], c, player1)
            grid[r[0]][c] = newBishop
            newBishop.draw(r[0], c)
            player1.pieces.add(newBishop)

            newBishop = bishop.Bishop(r[1], c, player0)
            grid[r[1]][c] = newBishop
            newBishop.draw(r[1], c)
            player0.pieces.add(newBishop)
        if c == 3:
            newQueen = queen.Queen(r[0], c, player1)
            grid[r[0]][c] = newQueen
            newQueen.draw(r[0], c)
            player1.pieces.add(newQueen)
        if c == 4:
            newQueen = queen.Queen(r[1], c, player0)
            grid[r[1]][c] = newQueen
            newQueen.draw(r[1], c)
            player0.pieces.add(newQueen)
    newKing = king.King(7, 3, player0)
    grid[7][3] = newKing
    player0.pieces.add(newKing)
    newKing.draw(7, 3)
    player0.king = newKing

    newKing = king.King(0, 4, player1)
    grid[0][4] = newKing
    newKing.draw(0, 4)
    player1.pieces.add(newKing)
    player1.king = newKing

def update_grid():
    draw_board()
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != 0:
                grid[r][c].draw(r, c)

def calculate_banned_squares():
    playerZeroBannedSpots = set()
    playerOneBannedSpots = set()
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != 0:
                    player = grid[r][c].player
                    bannedSpots = grid[r][c].bannedSpots()
                    for spot in bannedSpots:
                        if player == 0:
                            playerOneBannedSpots.add(spot)
                        else:
                            playerZeroBannedSpots.add(spot)
    # print("0", playerZeroBannedSpots)
    # print("1", playerOneBannedSpots)
                    
# def isCheck(player):
#     pass

# def isCheckMate(player):
#     pass

draw_board()
initialize_grid()

currClicked = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            r = pos[1] // (WIDTH // ROWS)
            c = pos[0] // (HEIGHT // COLS)
            if currClicked != 0 and currClicked.move(r, c, currTurn):
                currClicked = 0
                if currTurn == 0:
                    currTurn = 1
                else:
                    currTurn = 0
            elif grid[r][c] != 0:
                grid[r][c].isClicked = True
                currClicked = grid[r][c]
            player0.isInCheck(grid)
            player1.isInCheck(grid)
    update_grid()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()