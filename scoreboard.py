from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        