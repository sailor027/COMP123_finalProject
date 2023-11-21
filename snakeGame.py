# =====================================================================
"""
COMP 123-1 Final Project
<Minseo Kim, Ko Horiuchi>
"""

# ---------------------------------------------------------------------
'''
Resources Used
- From class
    - hw5
    - GuiExamples/tkinterCanvas2
    - GuiExamples/tkinterCanvas3
- https://docs.python.org/3/tutorial/datastructures.html#
- https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html
'''

# ---------------------------------------------------------------------
# TODO: @Ko get snake to move
# TODO: @Minseo create widgets: quit, restart, score, (highest score)

# ----------
import tkinter as tk
import random

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

        self.snake = [(240, 240), (240, 250), (240, 260)] # Initial list of snake body
        self.direction = "Up"  # Initial snake direction
        self.food = self.createFood()
        self.count = 0  # Count of food eaten
        self.best = 0  # Best score
        self.speed = 400  # Initial speed
        # TODO: Use self.count to keep track of score


    # ---------------------------------------------------------------------
    # Set up snake

    def run(self):
        x, y = self.snake[0]
        if self.count > self.best:
            self.best = self.count
        if ((x >= 0 and x <= 480 and y >= 0 and y <= 480) and
                (self.snake[0] not in self.snake[1:])):
            self.moveSnake()
            self.drawSnake()
            self.rootWin.after(self.speed, self.run)
        else:
            self.canvas.create_text(250, 250, text="Game Over", fill='white', justify=tk.CENTER)  # Game Over
            print(self.count)  # TODO: Delete later


    def drawSnake(self):
        self.canvas.delete("snakes")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="light green", tags="snakes")


    def changeDirection(self, event):
        # TODO: @Ko if conditions so that the snake can't move in the opposite direction
        arrow = event.keysym
        if ((arrow == "Up" and not self.direction == "Down") or
                (arrow == "Down" and not self.direction == "Up") or
                (arrow == "Right" and not self.direction == "Left") or
                (arrow == "Left" and not self.direction == "Right")):
            self.direction = arrow


    def moveSnake(self):
        x, y = self.snake[0]  # Get coordination of 1st snake
        if self.direction == "Up":
            y += -20
        elif self.direction == "Down":
            y += 20
        elif self.direction == "Right":
            x += 20
        elif self.direction == "Left":
            x += -20
        self.snake.insert(0, (x, y))

        if self.snake[0] == self.food:
            self.canvas.delete("food")
            self.food = self.createFood()
            self.count += 1
            self.speed -= 5
            if self.count > 0 and self.count%2 == 0:
                xi, yi = self.snake[-1]
                self.snake.append((xi, yi+20))
            self.drawSnake()

        self.snake.pop()


    def createFood(self):
        x = random.randint(1, 24) * 20
        y = random.randint(1, 24) * 20
        self.canvas.create_oval(x, y, x+20, y+20, fill='red', tags="food")
        return x, y

    def go(self):
        try:
            while True:
                self.run()
                self.rootWin.mainloop()
        except tk.TclError:
            pass # to avoid errors when the window is closed



# =====================================================================
SnakeGUI().go()