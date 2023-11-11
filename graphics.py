from tkinter import Tk, BOTH, Canvas, Label

class Window:
    #Initializing the window, creating the canvas, and running the protocol
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Sudoku")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    #Update the screen whenever animate or change something and we want it to reflect that on the screen
    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks

    #The app will be constantly updating itself (meant to be used on main)
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()

    #When the user clicks on the x on the top right, the protocol "WM_DELETE_WINDOW" will execute
    #This will cause the self.__running var to become False
    #Will also be useful for when we want to stop the updating and leave it as is
    def close(self):
        self.__running = False

    #Draws a square
    #We're not making a function for individual lines because we're not going to modify them
    def draw_square(self, x1, y1, x2, y2, half_x, half_y, value=0):
        #Top Wall
        self.__canvas.create_line(x1, y1, x2, y1, fill="black", width=2)

        #Right Wall
        self.__canvas.create_line(x2, y1, x2, y2, fill="black", width=2)

        #Bottom Wall
        self.__canvas.create_line(x1, y2, x2, y2, fill="black", width=2)
        
        #Left Wall
        self.__canvas.create_line(x1, y1, x1, y2, fill="black", width=2)

        #Text in the middle
        self.__canvas.create_text(half_x, half_y, text=value)

        #Packing everything
        self.__canvas.pack(fill=BOTH, expand=1)

    #Draw Square with the right side bold
    def draw_square_right_bold(self, x1, y1, x2, y2, half_x, half_y, value=0):
        #Top Wall
        self.__canvas.create_line(x1, y1, x2, y1, fill="black", width=2)

        #Right Wall
        self.__canvas.create_line(x2, y1, x2, y2, fill="black", width=6)

        #Bottom Wall
        self.__canvas.create_line(x1, y2, x2, y2, fill="black", width=2)
        
        #Left Wall
        self.__canvas.create_line(x1, y1, x1, y2, fill="black", width=2)

        #Text in the middle
        self.__canvas.create_text(half_x, half_y, text=value)

        #Packing everything
        self.__canvas.pack(fill=BOTH, expand=1)

    #
    def draw_square_bottom_bold(self, x1, y1, x2, y2, half_x, half_y, value=0):
        #Top Wall
        self.__canvas.create_line(x1, y1, x2, y1, fill="black", width=2)

        #Right Wall
        self.__canvas.create_line(x2, y1, x2, y2, fill="black", width=2)

        #Bottom Wall
        self.__canvas.create_line(x1, y2, x2, y2, fill="black", width=6)
        
        #Left Wall
        self.__canvas.create_line(x1, y1, x1, y2, fill="black", width=2)

        #Text in the middle
        self.__canvas.create_text(half_x, half_y, text=value)

        #Packing everything
        self.__canvas.pack(fill=BOTH, expand=1)