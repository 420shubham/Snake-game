from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_LIMIT=285

screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake= Snake()
food=Food()
score= Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food)<15:
        print("snake ear food")
        score.update_score()
        food.new_location()
        snake.extend()

    if snake.head.xcor()>SCREEN_LIMIT or snake.head.xcor()<-SCREEN_LIMIT or snake.head.ycor()>SCREEN_LIMIT or snake.head.ycor()<-SCREEN_LIMIT:
        game_is_on=False
        score.game_over()

    for seg in snake.seg_list[1:]:
        if snake.head.distance(seg)<10:
            game_is_on=False
            score.game_over()


screen.exitonclick()