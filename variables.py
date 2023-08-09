import pygame

WIDTH = HEIGHT = 560
ROWS = COLS = 8

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

grid = [[0 for i in range(8)] for j in range(8)]