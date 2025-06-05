"""
Number Class
ICS4U
Emily Zhang, Olivia Chen and Su Huang
Act as numbers and the delete character required to enter phone number
History:
June 30, 2025: Program creation
June 2, 2025: Functionality completion
June 4: Documentation completion
"""

from turtle import Turtle
from random import randint


class Number(Turtle):
    """
    Represents a number or delete character, inherits from Turtle class

    Attributes
        value: str | int
            Text of number or delete character

    Methods
        refresh(self): randomly reposition number
    """

    def __init__(self, value):
        """
        Initialises Number instance

        Args
            value: str | int
                Text of number or delete character
        """
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
        """
        Randomly reposition Number instance
        """
        # Generate random position for Number object
        random_x = randint(-280, 280)
        random_y = randint(-280, 260)

        # Clear previous text
        self.clear()

        # Go to random position
        self.goto(random_x, random_y)

        # Write new text with same value
        self.write(self.value, font=('Arial', 14, 'bold'))



