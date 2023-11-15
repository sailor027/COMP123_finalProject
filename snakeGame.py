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



    # ---------------------------------------------------------------------
    # Set up snake
    def moveSnake(self):
        pass


    def run(self):
        while True:
            # self.moveSnake()
            self.rootWin.update()

# =====================================================================
snakeGUI = CanvasGUI()
snakeGUI.run()