from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("yellow green")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


# TODO challenge 1
def make_square():
    """Function for turtle make a square"""
    for _ in range(4):
        tim.fd(100)
        tim.rt(90)


# make_square()

# TODO make a dashed line
def make_drashed_line():
    """Function for turtle make a dashed line"""
    for _ in range(15):
        tim.fd(10)
        tim.up()
        tim.fd(10)
        tim.down()


# make_drashed_line()

# TODO make a any gemoetric figure with turtle
def drawn_shape(sides):
    """Fucntion to make a any gemoetric figure"""
    angle = 360 / sides

    for _ in range(sides):
        tim.fd(100)
        tim.rt(angle)


screen = Screen()
screen.delay(40)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    drawn_shape(shape_side_n)

screen.exitonclick()
