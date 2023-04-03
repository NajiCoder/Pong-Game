from turtle import Screen
from Pong import *
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

score = ScoreBoard()

ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_on = True


while game_on:

    screen.update()
    time.sleep(ball.moving_speed)

    r_paddle.paddle_movement()
    l_paddle.paddle_movement()

    ball.ball_movement()

    # Detect collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle
    if ball.xcor() > 340 and ball.distance(r_paddle) < 40 or ball.xcor() < -340 and ball.distance(l_paddle) < 40:
        print("made contact")
        ball.paddle_bounce()

    # Detect when r_paddle misses
    if ball.xcor() > 390:
        print("game over")
        ball.new_ball()
        score.update_l_score()

    # Detect when l_paddle misses
    if ball.xcor() < -390:
        ball.new_ball()
        score.update_r_score()


screen.exitonclick()
