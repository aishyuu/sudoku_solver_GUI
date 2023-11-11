class Cell:
    def __init__(self, win, value=0):
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.value = value
        self.__win = win

    def draw(self, x1, y1, x2, y2, special = "none"):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        half_x = (x1 + x2) / 2
        half_y = (y1 + y2) / 2

        if special == "none":
            self.__win.draw_square(x1, y1, x2, y2, half_x, half_y, self.value)
        if special == "right":
            self.__win.draw_square_right_bold(x1, y1, x2, y2, half_x, half_y, self.value)
        if special == "bottom":
            self.__win.draw_square_bottom_bold(x1, y1, x2, y2, half_x, half_y, self.value)