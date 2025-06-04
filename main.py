from turtle import Screen
import time
from snake import Snake
from number import Number
from scoreboard import Scoreboard

# Instantiate Screen object
screen = Screen()

# Instantiate Snake object
snake = Snake()

# Instantiate Scoreboard object
scoreboard = Scoreboard()

# Define screen attributes
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("telesnake")
screen.tracer(0)

# Different numbers for Number objects to write
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "←"]

# List to store Number objects
number_turtles = []

# Instantiate a Number object for each number
for number in numbers:
    number_turtle = Number(number)
    number_turtles.append(number_turtle)

screen.listen()

# Add key controls for snake movement
screen.onkey(snake.down, "Up")
screen.onkey(snake.up, "Down")
screen.onkey(snake.right, "Left")
screen.onkey(snake.left, "Right")
screen.onkey(snake.left, "d")
screen.onkey(snake.right, "a")
screen.onkey(snake.up, "s")
screen.onkey(snake.down, "w")

game_is_on = True

# While the game is not done
while game_is_on:

    # Move snake
    snake.move()

    # Update screen every 0.1 seconds (to connect snake)
    time.sleep(0.1)
    screen.update()

    # Loop through Number objects and their indices
    for index, number in enumerate(number_turtles):

        # If the snake head collides with a number
        if snake.head.distance(number) < 15:

            # Extend the snake body
            snake.extend()

            # Update phone number with the hit number.
            scoreboard.update_phone_number(str(numbers[index]))

            # Update phone number UI
            scoreboard.update_UI()

            # If the user has finished their phone number, end game and break out of for loop
            if len(scoreboard.phone_number) == 10:
                game_is_on = False
                break

            # Change the position of all the numbers
            for turtle in number_turtles:
                turtle.refresh()

    # If snake head hits screen edge
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:

        # End game
        game_is_on = False

        # Show losing UI
        scoreboard.phone_number_incomplete()

    # If snake head hit snake's other segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:

            # End game
            game_is_on = False

            # Show losing UI
            scoreboard.phone_number_incomplete()

screen.exitonclick()
