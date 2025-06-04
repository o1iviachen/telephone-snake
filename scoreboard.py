from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.phone_number = ""
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.write("your phone number: ", align="center", font=('Arial', 15, 'bold'))

    def update_UI(self):
        self.clear()
        self.write(f"your phone number: {self.phone_number}", align="center", font=('Arial', 15, 'bold'))

    def update_phone_number(self, value):
        if value != "←":
            if len(self.phone_number) != 9:
                self.phone_number += value
            else:
                self.goto(0, 0)
                self.write("thanks for your phone number!", align="center", font=('Arial', 15, 'bold'))
                return True
        else:
            if self.phone_number:
                self.phone_number = self.phone_number[:-1]
        return False

    def phone_number_incomplete(self):
        self.goto(0, 0)
        self.write("incomplete phone number. please try again.", align="center", font=('Arial', 15, 'bold'))

