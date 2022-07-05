import time
import pygame 
import numpy

# Define colors
color_background = (0, 0, 0)
color_grid = (0, 45, 24)
color_die_next = (150, 150, 150)
color_alive_next = (255, 0, 98)

# Define update screen function
def update(screen, cells, size, with_progress=False):
    updated_cells = numpy.zeros((cells.shape[0], cells.shape[1]))

    for row, col in numpy.ndindex(cells.shape):

        alive = numpy.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = color_background if cells[row, col] == 0 else color_alive_next

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = color_die_next

            elif 2<= alive <=3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = color_alive_next
        else:
            if alive == 3:
               updated_cells[row, col] = 1
               if with_progress:
                    color = color_alive_next
        
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))
    
    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 700))

    cells = numpy.zeros((70, 90))
    screen.fill(color_grid)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()
            
        screen.fill(color_grid)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.0010)

if __name__ == '__main__':
    main()





