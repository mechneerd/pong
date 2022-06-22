from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

degree_top = random.randint(90, 130)
degree_bottom = random.randint(0, 45)

#TODO screen setup
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')
game_on = True

#TODO create object
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ping = Ball()
screen.tracer(0)
score = Scoreboard()
score1 = Scoreboard()

# TODO paddle movement
screen.listen()
screen.onkey(key='w', fun=l_paddle.go_up)
screen.onkey(key='s', fun=l_paddle.go_down)
screen.onkey(key='i', fun=r_paddle.go_up)
screen.onkey(key='j', fun=r_paddle.go_down)

#TODO game start
while game_on:
    time.sleep(0.1)
    screen.update()
    ping.random_move()

    #TODO Wall reflect
    if ping.ycor() > 280 or ping.ycor() < -280:
        ping.wall_reflect()

    #TODO paddle reflect
    if ping.distance(r_paddle) < 50 and ping.xcor() > 330 or ping.distance(l_paddle) < 50 and ping.xcor() > -330:
        ping.paddle_reflect()
    if ping.xcor() > 350 or ping.xcor() < -350:
        screen.update()
        ping.goto(0, 0)
        ping.second_move()
        score.l_scoreboard()
        score1.r_scoreboard()











screen.exitonclick()
