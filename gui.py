import tkinter as tk
from chessboard import Chessboard

class Gui:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chess Game")
        self.buttons = [[None for _ in range(8)] for _ in range(8)]

        self.create_board()

    def create_board(self):
        for row in range(8):
            for col in range(8):
                button = tk.Button(self.window, text="", width = 8, height = 4)
                button.grid(row=row, column = col)
                self.buttons[row][col] = button


    def run(self):
        self.window.mainloop()

    
b1 = Gui()
b1.run()