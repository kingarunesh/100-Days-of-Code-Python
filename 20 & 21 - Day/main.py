from turtle import Screen
import snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = snake.Snake()
food = Food()
scoreboard = ScoreBoard()

# key listen
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend_segment()
        food.refresh()

    # detect collision with wall (game over)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


























screen.exitonclick()
