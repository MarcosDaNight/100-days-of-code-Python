import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game.py")
screen.tracer(0)

paddle = Paddle()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
