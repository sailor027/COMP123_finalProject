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

        self.quitButton=tk.Button(self.rootWin, text="Quit", font="Menlo 20", command=self.quit)
        self.quitButton.grid(row=2, column=3)

        self.replay_button = tk.Button(self.rootWin, text="Replay", font="Menlo 20", command=self.restart)
        self.replay_button.grid(row=1, column=3)


        self.count = 0  # Count of food eaten
        self.count_label = tk.Label(self.rootWin, text="Score: 0", font=("Menlo", 20), fg="black", bg="white")
        self.count_label.grid(row=1, column=1, rowspan=2)

        self.best = self.getBestScore()  # Best score
        self.best_label = tk.Label(self.rootWin, font="Menlo 20", fg='white', bg='black')
        self.best_label['text'] = 'Best: ' + str(self.best)
        self.best_label.grid(row=1, column=2, rowspan=2)


        self.canvas = tk.Canvas(self.rootWin, bg = 'black', width=500, height=500, bd=0)
        self.canvas.grid(row=3, column=0, columnspan=4)
        # Show all of the canvas
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

        self.rootWin.bind("<Key>", self.keys)

        self.pause = False
        self.gameOver = False
        self.snake = [(240, 240), (240, 250), (240, 260)]  # Initial list of snake body
        self.direction = "Up"  # Initial snake direction
        self.food = self.createFood()
        self.speed = 400  # Initial speed

        self.run()


    # ---------------------------------------------------------------------
    # Set up snake

    def run(self):
        """If current score is higher than best score, update best score.
        If game is not paused, while snake head is within the canvas and has not run into itself, continue to move
        snake and wait self.speed seconds until it runs again so that the game speeds up. If snake runs into itself
        or the walls of the canvas save current best score and shows message. If the game is paused, show message
        until further input by user."""
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
                self.saveBestScore()
                self.gameOver = True
                self.gameOverText = self.canvas.create_text(250, 230, text="Game Over \n \n [r]estart / [q]uit",
                                        font=('Menlo', 15), fill='white', justify=tk.CENTER)
        elif self.pause:
            self.pauseText = self.canvas.create_text(250, 250, text="Game Paused \n \n [c]ontinue / [r]estart / [q]uit",
                                    font=('Menlo', 15), fill='white', justify=tk.CENTER)


    def drawSnake(self):
        """Deletes snake body before drawing a new one. For every coordination in the list self.snake, draw a green
        square and tag it as 'snake'."""
        self.canvas.delete("snakes")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="light green", tags="snakes")


    def keys(self, event):
        """Assigns keys to commands.
        For arrow keys, prevent snake from going to the opposite direction.
        Esc => quit game
        Space => pause game"""
        key = event.keysym
        if ((key == "Up" and not self.direction == "Down") or
                (key == "Down" and not self.direction == "Up") or
                (key == "Right" and not self.direction == "Left") or
                (key == "Left" and not self.direction == "Right")):
            self.direction = key
        elif key == "Escape":
            self.quit()
        elif key == "space":
            self.pause = True
        if self.pause:
            if key == "c":
                self.pause = False
                self.canvas.delete(self.pauseText)
                self.run()
            if key == "r":
                self.pause = False
                self.canvas.delete(self.pauseText)
                self.restart()
            if key == "q":
                self.quit()
        if self.gameOver:
            if key == "r":
                self.gameOver = False
                self.canvas.delete(self.gameOverText)
                self.restart()
            if key == "q":
                self.quit()



    def moveSnake(self):
        """Get coordination of the 1st snake body and adds 20 to the direction of the key that was pressed. Insert
        new coordination at [0] of snake list and deletes [-1], so that it looks like the snake is moving."""
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
        """Gets a random coordinate within the canvas size. Draws a red circle and tag it as 'food'."""
        x = random.randint(1, 24) * 20
        y = random.randint(1, 24) * 20
        self.canvas.create_oval(x, y, x+20, y+20, fill='red', tags="food")
        return x, y

    # ---------------------------------------------------------------------
    def go(self):
        self.rootWin.mainloop()

    def restart(self):
        """Initialises all settings so that the game can restart."""
        self.canvas.delete(tk.ALL)
        self.snake = [(240, 240), (240, 250), (240, 260)]  # Initial list of snake body
        self.drawSnake()
        self.direction = "Up"  # Initial snake direction
        self.food = self.createFood()
        self.count = 0  # Count of food eaten
        self.count_label['text'] = "Score: " + str(self.count)
        self.speed = 400  # Initial speed
        self.pause = False
        self.run()

    def quit(self, event=None):  # TODO: fix, delete comments
        self.saveBestScore()
        self.rootWin.destroy()

    def saveBestScore(self):
        """Saves best score in 'bestScore.txt' file, so that it can be retrieved even when a new game is started"""
        fileOut = open('bestScore.txt', 'w')
        fileOut.write(str(self.best))
        fileOut.close()

    def getBestScore(self):
        """Retrieves best score from file"""
        fileIn = open('bestScore.txt', 'r')
        bestScore = fileIn.read()
        fileIn.close()
        if bestScore == '':
            bestScore = 0
        else:
            bestScore = int(bestScore)
        return bestScore







# =====================================================================
SnakeGUI().go()