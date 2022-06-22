import random
from turtle import Turtle
from random import Random

degree_top = random.randint(90, 130)
degree_bottom = random.randint(0, 45)


class Ball(Turtle, Random):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.turtlesize(stretch_wid=1)
        self.penup()
        self.move_x = 10
        self.move_y = 10

    def random_move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def wall_reflect(self):
        self.move_y *= -1

    def paddle_reflect(self):
        self.move_x *= -1


