import pygame
#initalize the PYGAME
pygame.init()
#Setting screen size & NAME
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("CHESS")
#Making Board
rows = cols=int(8)
square_size=100
white_colour=(250,250,250)
black_colour=(0,0,0)
#main
def draw_squares(screen):
    screen.fill(white_colour)
    for row in range(rows):
        for colm in range(row % 2, rows, 2):
            pygame.draw.rect(screen, black_colour, (colm * square_size, row*square_size, square_size, square_size))       
draw_squares(screen)
#loop
i=True
while i:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            i=False
    pygame.display.update()
pygame.quit()