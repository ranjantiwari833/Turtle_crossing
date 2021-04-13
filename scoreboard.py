from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",20, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-300,260)
        self.write("Score: {}".format(self.score),False,ALIGNMENT,FONT)
        self.goto(0,260)
        self.write("Reach Here",False,ALIGNMENT,FONT)
    
    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0,260)
        self.write("GAME OVER!! Score: {}".format(self.score),False,ALIGNMENT,FONT)
    
    def score_update(self):
        self.score += 1
        self.clear()
        self.goto(-300,260)
        self.write("Score: {}".format(self.score),False,ALIGNMENT,FONT)
        self.goto(0,260)
        self.write("Reach Here",False,ALIGNMENT,FONT)