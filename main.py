from turtle import Screen
import time
from snake import Snake
from number import Number
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("telesnake")
screen.tracer(0)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "←"]
number_turtles = []
segments = []
snake = Snake()
scoreboard = Scoreboard()
for number in numbers:
    number_turtle = Number(number)
    number_turtles.append(number_turtle)

screen.listen()

# change
screen.onkey(snake.down, "Up")
screen.onkey(snake.up, "Down")
screen.onkey(snake.right, "Left")
screen.onkey(snake.left, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    for index, number in enumerate(number_turtles):
        if snake.head.distance(number) < 15:
            snake.extend()
            if scoreboard.update_phone_number(str(numbers[index])):
                game_is_on = False
            scoreboard.update_UI()
            for turtle in number_turtles:
                turtle.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.phone_number_incomplete()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.phone_number_incomplete()

screen.exitonclick()
