from graphics import Window
from cell import Cell

class Sudoku:
    def __init__(self, x1, y1, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        self._create_cells()

    def _create_cells(self):
        for col in range(9):
            cell_cols = []
            for row in range(9):
                cell_cols.append(Cell(self.__win))
            self.__cells.append(cell_cols)

        for col in range(9):
            for row in range(9):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self.__win is None:
            return
        
        x1 = self.__x1 + col * self.__cell_size_x
        y1 = self.__y1 + row * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        if col == 2 or col == 5:
            self.__cells[col][row].draw(x1, y1, x2, y2, "right")

        if row == 2 or row == 5:
            self.__cells[col][row].draw(x1, y1, x2, y2, "bottom")
            
        self.__cells[col][row].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()