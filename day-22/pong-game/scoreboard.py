from turtle import Turtle

ALIGN = "center"
FONT = ('Times New Roman', 15, 'normal')
FONT_OVER = ('Times New Roman', 15, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.update_score()
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGN, font=FONT_OVER)
