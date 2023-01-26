import pygame

pygame.init()


window_width = 250
window_height = 300


screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Minesweeper")


class Cube():
    width = 35
    height = 35




RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
WHITE = 255,255,255
BLACK = 0,0,0




def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, window_width, blockSize):
        for y in range(0, window_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)
        

def drawGrid2():
    #row 1
    cell1 = pygame.Rect(30,30,Cube.width, Cube.height)
    pygame.draw.rect(screen, BLACK, cell1, 1)

    cell2 = pygame.Rect(70,30,Cube.width, Cube.height)
    pygame.draw.rect(screen, BLACK, cell2, 1)

    cell3 = pygame.Rect(110,30,Cube.width, Cube.height)
    pygame.draw.rect(screen, BLACK, cell3, 1)


    #row 2
    cell4 = pygame.Rect(110,70,Cube.width, Cube.height)
    pygame.draw.rect(screen, BLACK, cell4, 1)

    cell5 = pygame.Rect(70,70,Cube.width, Cube.height)
    pygame.draw.rect(screen, BLACK, cell5, 1)

    cell6 = pygame.Rect(30,70,Cube.width, Cube.height)
    pygame.draw.rect(screen, BLACK, cell6, 1)


    #row 3
    cell7 = pygame.Rect(30,110,Cube.width, Cube.height)
    pygame.draw.rect(screen, BLACK, cell7, 1)

    cell8 = pygame.Rect(70,110,Cube.width, Cube.height)
    pygame.draw.rect(screen, BLACK, cell8, 1)

    cell9 = pygame.Rect(110,110,Cube.width, Cube.height)
    pygame.draw.rect(screen, BLACK, cell9, 1)
        
    mouse = pygame.mouse.get_pos()
    print(mouse)
    if mouse == (30,30):
        print("hovering")
    



running = True
while running:
    pygame.display.update()
    screen.fill(WHITE)
    drawGrid2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_a]:
        print("screee")


 