import pygame
import os

pygame.init()

WIDTH = HEIGHT = 720
SCORE_BOARD = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT+SCORE_BOARD))
pygame.display.set_caption('JDCheckers')
CROWN_SURFACE = pygame.image.load(os.path.join('assets', 'crown.png')).convert_alpha()
pygame.display.set_icon(CROWN_SURFACE)

GAME_FONT = pygame.font.Font(os.path.join('assets', 'LHANDW.TTF'), 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

FPS = 60
CLOCK = pygame.time.Clock()

ROWS = COLS = 8
SQ_SIZE = WIDTH // ROWS
