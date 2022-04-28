from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def reset_screen():
    tim.reset()


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.lt(10)


def turn_right():
    tim.rt(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset_screen)

screen.exitonclick()
