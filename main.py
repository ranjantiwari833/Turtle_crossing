from turtle import Screen, colormode
import time
from player import Player
from cars import Cars
from scoreboard import Score

colormode(255)

def main():
    #Screen Initialization
    sleep_time = 0.25
    screen = Screen()
    screen.setup(800,600)
    screen.bgcolor("white")
    screen.tracer(0)
    screen.title("Turtle Crossing")
    screen.listen()
    
    #Player Initialization
    player = Player()
    cars = Cars()
    score = Score()
    
    screen.onkeypress(player.go_forward,"Up")
    
    game_on = True
    counter =0
    
    while game_on:
        screen.update()
        cars.move()
        time.sleep(sleep_time)
        
        #detect collision
        for i in range(len(cars.total)):
            if player.distance(cars.total[i]) < 20:
                game_on = False
                score.game_over()
        
        #level up
        if player.ycor() >= 270:
            player.goto(0,-280)
            score.score_update()
            screen.update()
            time.sleep(2)
            sleep_time *= 0.8                   
        
        #new car
        if counter % 3 ==0:
            cars.new_car()
        counter+=1
    
    screen.exitonclick()

if __name__ == "__main__":
    main()