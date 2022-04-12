from .constants import *


class Piece:
    RED_PIECE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'red_piece.png')).convert_alpha(),
                                       (SQ_SIZE - 20, SQ_SIZE - 20))
    BLUE_PIECE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'blue_piece.png')).convert_alpha(),
                                        (SQ_SIZE - 20, SQ_SIZE - 20))

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.crown = pygame.transform.scale(CROWN_SURFACE, (SQ_SIZE - 40, SQ_SIZE - 40))
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col * SQ_SIZE + SQ_SIZE // 2
        self.y = self.row * SQ_SIZE + SQ_SIZE // 2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self):
        if self.color == RED:
            WIN.blit(self.RED_PIECE,
                     (self.x - self.RED_PIECE.get_width() // 2, self.y - self.RED_PIECE.get_height() // 2))
        elif self.color == BLUE:
            WIN.blit(self.BLUE_PIECE,
                     (self.x - self.BLUE_PIECE.get_width() // 2, self.y - self.BLUE_PIECE.get_height() // 2))
        if self.king:
            WIN.blit(self.crown, (self.x - self.crown.get_width() // 2, self.y - self.crown.get_height() // 2))

    def __repr__(self):
        if self.color == BLUE:
            return 'BLUE'
        return 'RED'
