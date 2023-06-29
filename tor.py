import pygame
import numpy as np
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 10
CELLS_X = WIDTH // CELL_SIZE
CELLS_Y = HEIGHT // CELL_SIZE
field = np.zeros((CELLS_X, CELLS_Y), dtype=bool)
def get_neighbors(x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx = (x + dx) % CELLS_X
            ny = (y + dy) % CELLS_Y
            neighbors.append((nx, ny))
    return neighbors
def update_cells():
    new_field = np.copy(field)
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            neighbors = get_neighbors(x, y)
            alive_neighbors = sum([field[nx, ny] for nx, ny in neighbors])
            if field[x, y] and alive_neighbors not in [2, 3]:
                new_field[x, y] = False
            elif not field[x, y] and alive_neighbors == 3:
                new_field[x, y] = True
    field[:] = new_field[:]
def draw_cells(screen):
    for x in range(CELLS_X):
        for y in range(CELLS_Y):
            if field[x, y]:
                pygame.draw.rect(screen, (255, 255, 255), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    paused = False
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
        if not paused:
            update_cells()
        screen.fill((0, 0, 0))
        draw_cells(screen)
        pygame.display.flip()
    pygame.quit()
if __name__ == '__main__':
    main()
