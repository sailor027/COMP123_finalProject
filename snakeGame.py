# =====================================================================
"""
COMP 123-1 Final Project
Minseo Kim, Ko Horiuchi
"""
# ----------
import tkinter as tk
import random

# =====================================================================
class CanvasGUI:

    # ---------------------------------------------------------------------
    # Set up window
    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Snake Game")

        self.canvas = tk.Canvas(self.rootWin, bg = 'black', width = 500, height = 500, bd = 0)
        self.canvas.grid(row=1, column=1)
        # Show all of the canvas
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

        body = self.canvas.create_rectangle(250, 250, 270, 270, fill="light green")

        # Bind the main window to respond to mouse button and keyboard entry
        self.rootWin.bind("<Up>", self.snakeUp)
        self.rootWin.bind("<Down>", self.snakeDown)
        self.rootWin.bind("<Right>", self.snakeRight)
        self.rootWin.bind("<Left>", self.snakeLeft)




    # ---------------------------------------------------------------------
    # Set up snake

    def moveSnake(self):
        pass

    def snakeUp(self):
        pass

    def snakeDown(self):
        pass

    def snakeRight(self):
        pass

    def snakeLeft(self):
        pass


    def run(self):
        try:
            while True:
                self.moveSnake()
                self.rootWin.mainloop()
        except tk.TclError:
            pass

# =====================================================================
snakeGUI = CanvasGUI()
snakeGUI.run()