from turtle import Turtle

font = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-55, y=260)
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=font)

    def increase_level(self):
        self.level += 1
        self.write_scoreboard()

    def game_over(self):
        self.goto(x=-75, y=0)
        self.write("Game over.", align="left", font=font)
        self.goto(x=-210, y=-30)
        self.write(f"Highest level reached: Level {self.level}", align="left", font=font)
