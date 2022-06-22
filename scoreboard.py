from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.hideturtle()
        self.penup()

    def r_scoreboard(self):
        self.goto(50, 270)
        self.score += 1
        self.clear()
        self.write(f'{self.score}', align='center', font=('Aerial', 20, 'normal'))

    def l_scoreboard(self):
        self.goto(-50, 270)
        self.score += 1
        self.clear()
        self.write(f'{self.score}', align='center', font=('Aerial', 20, 'normal'))
