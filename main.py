from turtle import Turtle, Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')
game_on = True

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
screen.tracer(0)

screen.listen()
screen.onkey(key='w', fun=l_paddle.go_up)
screen.onkey(key='s', fun=l_paddle.go_down)
screen.onkey(key='i', fun=r_paddle.go_up)
screen.onkey(key='j', fun=r_paddle.go_down)

while game_on:
    screen.update()

screen.exitonclick()
