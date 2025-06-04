from turtle import Turtle
from random import randint


class Number(Turtle):

    def __init__(self, value):
        super().__init__()
        self.value = value
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        self.write(value, font=('Arial', 14, 'bold'))


    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 260)
        self.clear()
        self.goto(random_x, random_y)
        self.write(self.value, font=('Arial', 14, 'bold'))



