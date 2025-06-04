from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):

        # Call Turtle constructor
        super().__init__()

        # Configure Scoreboard object
        self.hideturtle()
        self.phone_number = ""
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.write("your phone number: ", align="center", font=('Arial', 15, 'bold'))

    def update_UI(self):

        # Clear previous text
        self.clear()

        # Update phone number UI
        self.write(f"your phone number: {self.phone_number}", align="center", font=('Arial', 15, 'bold'))

    def update_phone_number(self, value):

        # If the snake head hit a number
        if value != "←":

            # Add number to phone number
            self.phone_number += value

            # If the phone number is 10 characters long, it is complete
            if len(self.phone_number) == 10:
                self.goto(0, 0)
                self.write("thanks for your phone number!", align="center", font=('Arial', 15, 'bold'))

        # If not, the user is deleting the latest number
        else:
            if self.phone_number:
                self.phone_number = self.phone_number[:-1]

    def phone_number_incomplete(self):
        self.goto(0, 0)
        self.write("incomplete phone number. please try again.", align="center", font=('Arial', 15, 'bold'))

