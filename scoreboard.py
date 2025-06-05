"""
Scoreboard Class
ICS4U
Emily Zhang, Olivia Chen and Su Huang
Show phone number and result user interface
History:
June 30, 2025: Program creation
June 2, 2025: Functionality completion
June 4: Documentation completion
"""

from turtle import Turtle


class Scoreboard(Turtle):
    """
    Shows user's phone number as it is entered alongside "losing" and "winning" user interfaces, inherited from Turtle class

    Attributes
        phone_number: str
            User's phone number

    Methods
        update_UI(self): update user interface after "winning" or editing phone number
        update_phone_number(self, value): update phone number attribute
        phone_number_incomplete(self): show "losing" user interface
    """
    def __init__(self):
        """
        Initialises Scoreboard instance
        """
        # Call Turtle constructor
        super().__init__()

        self.phone_number = ""

        # Configure Scoreboard object
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.write("your phone number: ", align="center", font=('Arial', 15, 'bold'))

    def update_UI(self):
        """
        Update user interface after "winning" or editing phone number
        """
        # Clear previous text
        self.clear()

        # Update phone number UI
        self.write(f"your phone number: {self.phone_number}", align="center", font=('Arial', 15, 'bold'))

    def update_phone_number(self, value):
        """
        Update phone number attribute

        Args
            value: str
                Text of number or delete character
        """
        # If the snake head hit a number
        if value != "←":

            # Add number to phone number
            self.phone_number += value

            # If the phone number is 10 characters long, move scoreboard to centre
            if len(self.phone_number) == 10:
                self.goto(0, 0)

        # If not, the user is deleting the latest number
        else:
            if self.phone_number:
                self.phone_number = self.phone_number[:-1]

    def phone_number_incomplete(self):
        """
        Show "losing" user interface
        """
        self.goto(0, 0)
        self.write("incomplete phone number. please try again.", align="center", font=('Arial', 15, 'bold'))

