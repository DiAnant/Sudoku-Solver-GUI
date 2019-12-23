import os
import time
import random
import pygame as pg

# initializing the pygame module
pg.init()

class Board:
    # defining colors  hex values
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    # setting frame rate
    FPS = 30
    # making a clock variable
    clock = pg.time.Clock()
    # board size
    display_width = 500
    display_height = 500
    display = pg.display.set_mode((display_width, display_height))

    # the sudoku puzzle matrix
    matrix =    [[1,0,0,0,4,0,0,0,0],
                [0,9,2,6,0,0,3,0,0],
                [3,0,0,0,0,5,1,0,0],
                [0,7,0,1,0,0,0,0,4],
                [0,0,4,0,5,0,6,0,0],
                [2,0,0,0,0,4,0,8,0],
                [0,0,9,4,0,0,0,0,1],
                [0,0,8,0,0,6,5,2,0],
                [0,0,0,0,1,0,0,0,6]]

    # the constructor function
    def __init__(self):
        # setting caption
        pg.display.set_caption('Sudoku')
        # displaying the board
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            # filling the board FPS times in a second
            # using desired color
            Board.display.fill(Board.white)
            self.lines()
            self.print_numbers()
            # updating the new board FPS times in a second
            Board.clock.tick(Board.FPS)
            pg.display.update()

    # function for making a line
    def draw_lines(self, surface, color, x, y, width, height):
        # arguements = surface, color, (x,y,width,height)
        self.line_x = x
        self.line_y = y
        self.line_width = width
        self.line_height = height
        line = pg.draw.rect(surface, color, 
        (self.line_x, self.line_y, self.line_width, self.line_height))

    # function for making all the required lines
    def lines(self):
        gap_horizontal = Board.display_height/9
        gap_vertical = Board.display_width/9
        for i in range(1,9):
            if i == 3 or i == 6:
                thickness = 5
            else:
                thickness = 2
            # drawing horizontal lines
            self.draw_lines(Board.display, Board.black,
            0, gap_horizontal*i, self.display_width, thickness)
            # drawing vertical lines
            self.draw_lines(Board.display, Board.black,
            gap_vertical*i, 0, thickness, self.display_height)

    # printing the numbers on the sudoku board
    def print_stuff(self, font_size, text, color, x, y):
        # getting font, fontsize and text to be printed
        self.font = pg.font.Font(None, font_size)
        self.text = text
        self.text_render = self.font.render(self.text, True, color)
        Board.display.blit(self.text_render, (x, y))

    # function for systematically calling the print_stuff() function
    def print_numbers(self):
        gap_horizontal = Board.display_height/9
        gap_vertical = Board.display_width/9
        for i in range(9):
            for j in range(9):
                number = Board.matrix[i][j]
                xx = gap_horizontal*i + 2*gap_horizontal/7
                yy = gap_vertical*j + 2*gap_vertical/7
                if number != 0:
                    self.print_stuff(50, str(number), Board.black, xx, yy)


# making an object of this class
thing = Board()
thing()