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
# TODO: @Minseo create widgets: quit, replay, score, (highest score)

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
        self.lblTitle.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.quitButton=tk.Button(self.rootWin, text="Quit", font="Menlo 20", command= self.quit)
        self.quitButton.grid(row=2, column=3)

        self.replay_button = tk.Button(self.rootWin, text="Replay", font="Menlo 20",command=self.restart)
        self.replay_button.grid(row=1, column=3)


        self.count = 0  # Count of food eaten
        self.count_label = tk.Label(self.rootWin, text="Score: 0", font=("Menlo", 20), fg="black", bg="white")
        self.count_label.grid(row=1,column=1, rowspan=2)

        self.best = 0  # Best score
        self.best_label = tk.Label(self.rootWin, text="Best: 0", font="Menlo 20", fg='white', bg='black')
        self.best_label.grid(row=1, column=2, rowspan=2)


        # ---------------------------------------------------------------------

        self.canvas = tk.Canvas(self.rootWin, bg = 'black', width=500, height=500, bd=0)
        self.canvas.grid(row=3, column=0, columnspan=4)
        # Show all of the canvas
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

        self.rootWin.bind("<Key>", self.keys)

        self.pause = False
        self.snake = [(240, 240), (240, 250), (240, 260)]  # Initial list of snake body
        self.direction = "Up"  # Initial snake direction
        self.food = self.createFood()
        self.speed = 400  # Initial speed


    # ---------------------------------------------------------------------
    # Set up snake

    def run(self):
        x, y = self.snake[0]
        if self.count > self.best:
            self.best = self.count
            self.best_label['text'] = "Best: " + str(self.best)
        if not self.pause:
            if ((x >= 0 and x <= 480 and y >= 0 and y <= 480) and
                    (self.snake[0] not in self.snake[1:])):
                self.moveSnake()
                self.drawSnake()
                self.rootWin.after(self.speed, self.run)
            else:
                self.canvas.create_text(250, 230, text="Game Over", fill='white', justify=tk.CENTER)  # Game Over
                self.canvas.create_text(250,270, text="[c]ontinue / [r]estart / [q]uit")
                print(self.count)  # TODO: Delete later
        elif self.pause:
            self.canvas.create_text(250, 250, text="Game Paused", fill='white', justify=tk.CENTER)



    def drawSnake(self):
        self.canvas.delete("snakes")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="light green", tags="snakes")


    def keys(self, event):
        """Assigns keys to commands.
        For arrow keys, prevent snake from going to the opposite direction.
        Ecs => quit game"""
        key = event.keysym
        if ((key == "Up" and not self.direction == "Down") or
                (key == "Down" and not self.direction == "Up") or
                (key == "Right" and not self.direction == "Left") or
                (key == "Left" and not self.direction == "Right")):
            self.direction = key
        elif key == "Escape":
            self.quit()
        elif key == "space":
            self.restart()


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
            """If snake eats food, increase speed by 5ms and make body longer by 1 square"""
            self.canvas.delete("food")
            self.food = self.createFood()
            self.count += 1
            self.count_label['text'] = "Score: " + str(self.count)
            self.speed -= 5
            xi, yi = self.snake[-1]
            self.snake.append((xi, yi+20))
            self.drawSnake()

        self.snake.pop()



    def createFood(self):
        x = random.randint(1, 24) * 20
        y = random.randint(1, 24) * 20
        self.canvas.create_oval(x, y, x+20, y+20, fill='red', tags="food")
        return x, y

    # ---------------------------------------------------------------------
    def go(self):
        try:
            while True:
                self.run()
                self.rootWin.mainloop()
        except tk.TclError:
            pass  # to avoid errors when the window is closed

    def restart(self):
        self.pause = False
        self.canvas.delete(tk.ALL)
        self.snake = [(240, 240), (240, 250), (240, 260)]  # Initial list of snake body
        self.direction = "Up"  # Initial snake direction
        self.food = self.createFood()
        self.count = 0  # Count of food eaten
        self.count_label['text'] = "Score: " + str(self.count)
        self.speed = 400  # Initial speed

    def quit(self):
        self.rootWin.destroy()



# =====================================================================
SnakeGUI().go()