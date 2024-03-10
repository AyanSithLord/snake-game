from turtle import Turtle




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        self.highscore=0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

    def game_over(self):
            self.turtlesize(8,9,10)
            self.goto(0, 0)
            self.write("Game Over",align="center", font=("Ariel",20,"normal"))










