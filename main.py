import pygame
from pygame.locals import *
import numpy as np

WINDOW_HEIGHT = 420
WINDOW_WIDTH = 420
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GRID_SIZE = 4
FPS = 12


# Initial state
def setup(g):
    # Glider gun
    g[10][100] = 1
    g[10][99] = 1
    g[9][100] = 1

    g[10][92] = 1
    g[10][91] = 1
    g[9][93] = 1
    g[9][92] = 1
    g[9][91] = 1
    g[8][92] = 1
    g[8][91] = 1

    g[11][89] = 1
    g[12][89] = 1
    g[11][88] = 1

    g[7][89] = 1
    g[7][88] = 1
    g[6][89] = 1

    g[10][78] = 1
    g[10][77] = 1
    g[9][76] = 1
    g[8][75] = 1
    g[7][75] = 1
    g[6][75] = 1
    g[5][76] = 1
    g[4][77] = 1
    g[4][78] = 1

    g[8][66] = 1
    g[7][66] = 1
    g[8][65] = 1

    return g


def main():
    sizeX = WINDOW_WIDTH // GRID_SIZE
    sizeY = WINDOW_HEIGHT // GRID_SIZE

    grid = np.zeros(shape=(sizeY + 2, sizeX + 2))
    grid = setup(grid)

    square = pygame.Surface((GRID_SIZE, GRID_SIZE))

    running = True
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Game of Life')
    clock = pygame.time.Clock()
    pygame.init()

    while running:
        new_grid = np.zeros(shape=(sizeY + 2, sizeX + 2))

        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

        screen.fill(BLACK)

        for y in range(1, sizeY + 1):
            for x in range(1, sizeX + 1):

                # Count neighbours
                n = grid[y - 1][x - 1] + grid[y - 1][x] + grid[y - 1][x + 1] + grid[y][x - 1] + grid[y][x + 1] + \
                    grid[y + 1][x - 1] + grid[y + 1][x] + grid[y + 1][x + 1]
                if (n == 2 or n == 3) and grid[y][x] == 1:
                    new_grid[y][x] = 1
                elif grid[y][x] == 0 and n == 3:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0

                # Draw pixel
                if new_grid[y][x] == 1:
                    square.fill(WHITE)
                else:
                    square.fill(BLACK)

                draw_square = pygame.Rect((x - 1) * GRID_SIZE, (y - 1) * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                screen.blit(square, draw_square)

        grid = np.copy(new_grid)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
