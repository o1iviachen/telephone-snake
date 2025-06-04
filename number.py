from turtle import Turtle
from random import randint


class Number(Turtle):

    def __init__(self, value):

        # Call Turtle constructor
        super().__init__()

        # Initialise value object attribute as value argument
        self.value = value

        # Configure Number object
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):

        # Generate random position for Number object
        random_x = randint(-280, 280)
        random_y = randint(-280, 260)

        # Clear previous text
        self.clear()

        # Go to random position
        self.goto(random_x, random_y)

        # Write new text with same value
        self.write(self.value, font=('Arial', 14, 'bold'))



