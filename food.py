from turtle import Turtle, Screen
from random import randint



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color("red")
        self.speed(0)
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.new_location()


    def new_location(self):
        rand_x= randint(-280,280)
        rand_y= randint(-280,280)
        self.goto(x=rand_x, y=rand_y)

    






