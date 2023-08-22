from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(-20, 280)
        self.pencolor("white")
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", font=("Courier", 14, "normal"))

    def game_over(self):
        self.goto(-60, 0)
        self.write("Game over", font=("Courier", 16, "normal"))

    def update(self):
        self.clear()
        self.score += 1
        self.write_score()
