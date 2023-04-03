from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 5)
        self.goto(position)
        self.color("white")
        self.speed("fastest")
        self.ht()

    def paddle_movement(self):

        self.setheading(90)
        self.st()

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 35
        self.moving_speed = 0.1

    def ball_movement(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move

        self.goto(x_cor, y_cor)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.moving_speed *= 0.9

    def new_ball(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.moving_speed = 0.1


class ScoreBoard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.l_score}", False, "center", ("courier", 40, "normal"))
        self.goto(100, 240)
        self.write(f"{self.r_score}", False, "center", ("courier", 40, "normal"))

    def update_r_score(self):
        self.r_score += 1
        print(self.r_score)
        self.update_score()

    def update_l_score(self):
        self.l_score += 1
        print(self.l_score)
        self.update_score()
