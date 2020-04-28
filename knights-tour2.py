import pygame
import sys

# fucntions


def colour_board(x, y, color):
    pygame.draw.rect(screen, color, [
                     (MARGIN + WIDTH) * x + MARGIN, (MARGIN + HEIGHT) * y + MARGIN, WIDTH, HEIGHT],3)


def text_objects(text, font):
    textSurface = font.render(str(text), True, WHITE)
    return textSurface, textSurface.get_rect()


def display_text(x, y, text):
    font = pygame.font.Font('freesansbold.ttf', WIDTH*3//5)
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = ((MARGIN + WIDTH) * x + MARGIN +
                       WIDTH/2, (MARGIN + HEIGHT) * y + MARGIN+HEIGHT/2)
    screen.blit(TextSurf, TextRect)


def isSafe(new_x, new_y, board):
    if (0 <= new_x < 8 and 0 <= new_y < 8 and board[new_x][new_y] == -1):
        return True
    return False


def tour(curr_x, curr_y, move_x, move_y, board, pos):
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT: sys.exit()  # If user clicked close

    screen.fill(BLACK)

    for row in range(8):
        for column in range(8):
            colour_board(column, row, RED)
            if board[row][column] >= 0:
                display_text(row, column, board[row][column])


    pygame.display.update()
    if pos == 65:
        return True

    for i in range(8):
        new_x = curr_x+move_x[i]
        new_y = curr_y+move_y[i]
        if isSafe(new_x,new_y,board):
            board[new_x][new_y] = pos
            if tour(new_x, new_y, move_x,move_y, board, pos+1):
                return True

            board[new_x][new_y]=-1

    return False


# colors
WHITE = (225, 225, 225)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# the main window
WINDOW_SIZE = (490, 490)
WIDTH = 50
HEIGHT = 50
MARGIN = 10

# initial setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Knights Tour")

move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
board = [[-1 for i in range(8)]for i in range(8)]
board[0][0] = 0

tour(0, 0, move_x, move_y, board, 1)
