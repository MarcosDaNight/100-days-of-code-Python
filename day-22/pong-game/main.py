import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game.py")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()
