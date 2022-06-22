from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.shape('square')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def go_up(self):
        change_y = self.ycor() + 20
        self.goto(self.xcor(), change_y)

    def go_down(self):
        change_y = self.ycor() - 20
        self.goto(self.xcor(), change_y)












