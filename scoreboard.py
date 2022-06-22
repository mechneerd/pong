from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()

    def r_scoreboard(self):
        self.goto(50, 270)
        self.clear()
        self.write(f'{self.r_score}', align='center', font=('Aerial', 20, 'normal'))
        if self.xcor() < 380:
            self.r_score += 1

    def l_scoreboard(self):
        self.goto(-50, 270)
        self.clear()
        self.write(f'{self.l_score}', align='center', font=('Aerial', 20, 'normal'))
        if self.xcor() > -380:
            self.l_score += 1
