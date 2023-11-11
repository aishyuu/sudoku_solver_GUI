from graphics import Window
from sudoku import Sudoku

def main():
    '''
    Initializing Variables
    margin = The distance we want the board to be away from the corners
    screen_x and screen_y = Dimensions of the window
    cell_size_x and cell_size_y = The length and width of each individual square (to make it all fit nicely)
    '''
    margin = 50
    screen_x = 600
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / 9
    cell_size_y = (screen_y - 2 * margin) / 9
    win = Window(screen_x, screen_y)
    sudoku = Sudoku(margin, margin, cell_size_x, cell_size_y, win)

    win.wait_for_close()

main()