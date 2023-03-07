from turtle import Turtle
starting_position = (0, -270)
move_distance = 15
finish_line_y = 290


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(move_distance)

    def go_down(self):
        self.backward(move_distance)

    def go_to_start(self):
        self.goto(starting_position)

    def is_at_finish_line(self):
        if self.ycor() > finish_line_y:
            return True
        else:
            return False
