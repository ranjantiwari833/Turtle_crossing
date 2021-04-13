from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto((0,-280))
        self.score = 1
        self.setheading(90)

        
    def go_forward(self):
        self.forward(10)
        
        