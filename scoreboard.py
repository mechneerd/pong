from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()

    def update_score(self):
        self.clear()
        self.goto(50, 270)
        self.write(f'{self.r_score}', align='center', font=('Aerial', 20, 'normal'))
        self.goto(-50, 270)
        self.write(f'{self.l_score}', align='center', font=('Aerial', 20, 'normal'))

    def r_point(self):
        self.l_score += 1
        self.update_score()

    def l_point(self):
        self.r_score += 1
        self.update_score()



