import pygame

pygame.init()


window_width = 800
window_height = 500


screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Minesweeper")


class Cube():
    width = 15
    height = 15


#def makeGrid():
#def makeGrid():
 #   for x in range(0,10):
  #      pygame.draw.rect(screen, (225,0,0), pygame.Rect(25, 25, Cube.height, Cube.width))

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, window_width, blockSize):
        for y in range(0, window_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (0,0,0), rect, 1)
        





running = True
while running:
    pygame.display.update()
    screen.fill((255,255,255))
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False