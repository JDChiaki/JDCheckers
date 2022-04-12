from checkers import *


def main():
    running = True
    _game = Game()

    while running:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = _game.get_row_col_mouse(pygame.mouse.get_pos())
                _game.select(row, col)
            if event.type == pygame.QUIT:
                running = False
                break

        _game.update()
    pygame.quit()
    exit()


if __name__ == '__main__':
    main()
