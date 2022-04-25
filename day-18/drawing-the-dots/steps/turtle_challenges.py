from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("yellow green")


# TODO challenge 1
def make_square():
    '''Function for turtle make a square'''
    for _ in range(4):
        tim.fd(100)
        tim.rt(90)


#make_square()

#TODO make a dashed line
def make_drashed_line():
    for _ in range(15):
        tim.fd(10)
        tim.up()
        tim.fd(10)
        tim.down()


make_drashed_line()

screen = Screen()
screen.exitonclick()
