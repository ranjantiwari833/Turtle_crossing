from turtle import Turtle,colormode
from random import randint,choice

xrange = [x for x in range(-360,381,20)]
yrange = [y for y in range(-240,241,20)]

colormode(255)
class Cars():
    def __init__(self):
        self.total = []
        self.initialize()
        
    def new_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(1,2)
        car.setheading(180)
        car.penup()
        car.color((randint(0,255),randint(0,255),randint(0,255)))
        car.goto(380,choice(yrange))
        self.total.append(car)
    
    def initialize(self):
        for i in range(11):
            car = Turtle()
            car.shape("square")
            car.shapesize(1,2)
            car.setheading(180)
            car.penup()
            car.color((randint(0,255),randint(0,255),randint(0,255)))
            car.goto(choice(xrange),choice(yrange))
            self.total.append(car)
    
    def move(self):
        to_del = []
        for i in range(len(self.total)):
            self.total[i].forward(10)
            if self.total[i].xcor() <= -380:
                to_del.append(i)
        
        for i,val in enumerate(to_del):
            self.total[val].hideturtle()
            self.total.pop(val)


                
        
        

