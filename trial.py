import os
import random
import pygame as pg

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
            self.print_numbers()
            # updating the new board FPS times in a second
            Board.clock.tick(Board.FPS)
            pg.display.update()

    # printing the numbers on the sudoku board
    def print_stuff(self, font_size, text, color, x, y):
        # getting font, fontsize and text to be printed
        self.font = pg.font.Font(None, font_size)
        self.text = text
        self.text_render = self.font.render(self.text, True, color)
        Board.display.blit(self.text_render, (x, y))

    def print_numbers(self):
        self.print_stuff(40, 'Hey', Board.black, 50, 50)

thing = Board()
thing()