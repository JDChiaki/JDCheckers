from .constants import *
from .board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = RED
        self.selected = None
        self.valid_moves = {}
        self.winner = None

    def reset(self):
        self.__init__()

    def update(self):
        self.board.draw_board()
        self.draw_valid_moves()
        self.check_winner()
        pygame.display.update()

    @staticmethod
    def get_row_col_mouse(pos):
        x, y = pos
        r = y//SQ_SIZE
        c = x//SQ_SIZE
        return r, c

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and self.turn == piece.color:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]

            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            return True
        return False

    def draw_valid_moves(self):
        if self.turn == RED:
            color = RED
        else:
            color = BLUE
        for move in self.valid_moves:
            row, col = move
            pygame.draw.circle(WIN, color, (col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2),
                               SQ_SIZE // 2 - 20)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED

    def check_winner(self):
        self.winner = self.board.winner()
        if not self.winner:
            red_txt = GAME_FONT.render(f'RED: {self.board.red_left}/12', True, BLACK)
            WIN.blit(red_txt, (10, HEIGHT + 15))
            blue_txt = GAME_FONT.render(f'BLUE: {self.board.blue_left}/12', True, BLACK)
            WIN.blit(blue_txt, (WIDTH - blue_txt.get_width() - 10, HEIGHT + 15))
            if self.turn == RED:
                turn_txt = GAME_FONT.render('RED\'s TURN', True, RED)
            else:
                turn_txt = GAME_FONT.render('BLUE\'s TURN', True, BLUE)
            WIN.blit(turn_txt, (WIDTH // 2 - turn_txt.get_width() // 2, HEIGHT + 15))
        else:
            pause = True
            while pause:
                CLOCK.tick(FPS)
                winner_txt = GAME_FONT.render(f'{self.winner} WINS!', True, BLACK)
                WIN.blit(winner_txt, (WIDTH // 2 - winner_txt.get_width() // 2, HEIGHT + 15))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pause = False
                            self.reset()
                            break
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                pygame.display.update()
