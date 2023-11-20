# =====================================================================
"""
COMP 123-1 Final Project
Minseo Kim, Ko Horiuchi
"""
# ----------
import tkinter as tk
import random

# ---------------------------------------------------------------------
# TODO: @Ko get snake to move
# TODO: @Minseo create widgets: quit, restart, score, (highest score)

# =====================================================================
class SnakeGUI:

    # ---------------------------------------------------------------------
    # Set up window
    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Snake Game")

        # ---------------------------------------------------------------------
        # Widgets

        self.lblTitle = tk.Label(self.rootWin, text="Snake Game", font=('Menlo bold', 20), justify=tk.CENTER)
        self.lblTitle.grid(row=0, column=0, padx=10, pady=10)

        # ---------------------------------------------------------------------

        self.canvas = tk.Canvas(self.rootWin, bg = 'black', width=500, height=500, bd=0)
        self.canvas.grid(row=3, column=0)
        # Show all of the canvas
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))


        self.rootWin.bind("<Key>", self.changeDirection)

        # Initial list of snake body
        self.snake = [(250, 250), (250, 270), (250, 290)]
        # Initial snake direction
        self.direction = "Up"
        self.food = self.createFood()

        self.run()

    # ---------------------------------------------------------------------
    # Set up snake


    def run(self):
        # FIXME: How do I get the snake to slow down?
        self.moveSnake()
        self.drawSnake()
        self.rootWin.after(500, self.run)


    def drawSnake(self):
        self.canvas.delete("snakes")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+10, y+10, fill="light green", tags="snakes")


    def changeDirection(self, event):
        # TODO: @Ko if conditions so that the snake can't move in the opposite direction
        arrow = event.keysym
        self.direction = arrow


    # FIXME: Testing snake move
    def moveSnake(self):
        x, y = self.snake[0]  # Get coordination of 1st snake
        if self.direction == "Up":
            y += -10
        elif self.direction == "Down":
            y += 10
        elif self.direction == "Right":
            x += 10
        elif self.direction == "Left":
            x += -10

        self.snake.insert(0, (x, y))


        # TODO: If snake eats food, delete food, make longer
        if self.snake[0] == self.food:
            self.canvas.delete("food")
            self.food = self.createFood()
            self.snake.insert(-1, (x, y+20*(len(self.snake)-1)))
            self.drawSnake()

        self.snake.pop()

    def createFood(self):
        x = random.randint(1, 49) * 10
        y = random.randint(1, 49) * 10
        self.canvas.create_oval(x, y, x+10, y+10, fill='red', tags="food")
        return x, y

    def go(self):
        try:
            while True:
                # self.run() # FIXME: Why does the snake slow down when this is removed?
                self.rootWin.update() # process events
        except tk.TclError:
            pass # to avoid errors when the window is closed



# =====================================================================
SnakeGUI().go()