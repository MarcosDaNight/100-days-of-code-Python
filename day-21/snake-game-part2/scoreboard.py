from turtle import Turtle, Screen

ALIGN = "center"
FONT = ('Times New Roman', 15, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.show_score()
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write("Score: " + str(self.score), False, align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.show_score()
