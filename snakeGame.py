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



    # ---------------------------------------------------------------------
    # Set up snake
    def moveSnake(self):
        pass


    def run(self):
        try:
            self.moveSnake()
        except tk.TclError:
            pass

# =====================================================================
snakeGUI = CanvasGUI
snakeGUI.run()