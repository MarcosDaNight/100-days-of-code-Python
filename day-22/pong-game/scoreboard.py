from turtle import Turtle

ALIGN = "center"
FONT = ('Times New Roman', 15, 'normal')
FONT_OVER = ('Times New Roman', 15, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.goto(-100, 200)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))



    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGN, font=FONT_OVER)
