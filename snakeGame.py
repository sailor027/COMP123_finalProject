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

        mainCanvas = tk.Canvas(self.rootWin)


    # ---------------------------------------------------------------------
    # Set up snake
    def moveSnake(self):
        pass


    def run(self):
        pass

# =====================================================================
snakeGUI = CanvasGUI
snakeGUI.run()