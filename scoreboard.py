from snake import Snake
from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        self.points=0
        super().__init__()
        self.color("yellow")
        self.speed(0)
        self.hideturtle()
        self.pu()
        self.goto(0,250)
        self.show_score()
        
    def show_score(self):
        self.write(f"Score= {self.points}", False, "center", ("Comic Sans MS",16,"bold"))


    def update_score(self):
        self.clear()
        global points
        self.points+=1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!.", False, "center", ("Comic Sans MS",24,"bold"))
        self.hideturtle()


               