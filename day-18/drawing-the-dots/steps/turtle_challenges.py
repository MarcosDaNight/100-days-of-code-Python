from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("yellow green")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# TODO challenge 1
def make_square():
    """Function for turtle make a square"""
    for _ in range(4):
        tim.fd(100)
        tim.rt(90)


# make_square()

# TODO make a dashed line
def make_dashed_line():
    """Function for turtle make a dashed line"""
    for _ in range(15):
        tim.fd(10)
        tim.up()
        tim.fd(10)
        tim.down()


# make_dashed_line()

# TODO make a any gemoetric figure with turtle
def drawn_shape(sides):
    """Function to make  any geometric figure"""
    angle = 360 / sides

    for _ in range(sides):
        tim.fd(100)
        tim.rt(angle)


def crescent_drawn():
    """Function to make a crescent geometric figures"""
    for shape_side_n in range(3, 10):
        tim.color(random_color())
        drawn_shape(shape_side_n)


# crescent_drawn()

# TODO challenge 4, generate a random walk
def random_walk(size):
    """Function to make random walk"""
    if size > 0:
        tim.color(random_color())
        tim.fd(30)
        tim.setheading(random.choice(directions))
        return random_walk(size - 1)
    return

tim.pensize(15)
tim.speed(10)


screen = Screen()
screen.colormode(255)
random_walk(200)
screen.exitonclick()
