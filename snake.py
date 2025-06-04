from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.segments = []

        # Create snake
        self.create_snake()

        # Assign head attribute the first segment
        self.head = self.segments[0]

    def create_snake(self):

        # Add a segment at each starting position
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):

        # Loop through segments, moving each segment to the preceding segment's position
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        # Move head forward
        self.head.forward(20)


    def add_segment(self, position):

        # Configure new segment
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)

        # Add segment to segments attribute
        self.segments.append(new_segment)

    def extend(self):

        # Add new segment to last segment's position
        self.add_segment(self.segments[-1].position())

    def up(self):

        # If the snake head is not oriented downwards
        if self.head.heading() != DOWN:

            # Set heading up
            self.head.setheading(UP)

    def down(self):

        # If the snake head is not oriented upwards
        if self.head.heading() != UP:

            # Set heading down
            self.head.setheading(DOWN)

    def left(self):

        # If the snake head is not oriented right
        if self.head.heading() != RIGHT:

            # Set heading left
            self.head.setheading(LEFT)

    def right(self):

        # If the snake head is not oriented left
        if self.head.heading() != LEFT:

            # Set heading right
            self.head.setheading(RIGHT)
