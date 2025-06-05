"""
Snake Class
ICS4U
Emily Zhang, Olivia Chen and Su Huang
Act as snake
History:
June 30, 2025: Program creation
June 2, 2025: Functionality completion
June 4: Documentation completion
"""

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Act as snake

    Attributes
        segments: [Turtle]
            List of segments producing snake body
        head: Turtle
            Snake's head

    Methods
        create_snake(self): create snake
        move(self): move snake
        add_segment(self): add snake segment
        extend(self): add snake segment after creating snake
        up(self): turn snake up
        down(self): turn snake down
        left(self): turn snake left
        right(self): turn snake right
    """
    def __init__(self):
        """
        Initialises Snake instance
        """
        self.segments = []

        # Create snake
        self.create_snake()

        # Assign head attribute the first segment
        self.head = self.segments[0]

    def create_snake(self):
        """
        Create snake
        """
        # Add a segment at each starting position
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        """
        Move snake
        """
        # Loop through segments, moving each segment to the preceding segment's position
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        # Move head forward
        self.head.forward(20)


    def add_segment(self, position):
        """
        Add snake segment

        Args
            position: (Int, Int)
                Position of segment
        """
        # Configure new segment
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)

        # Add segment to segments attribute
        self.segments.append(new_segment)

    def extend(self):
        """
        Extend snake
        """
        # Add new segment to last segment's position
        self.add_segment(self.segments[-1].position())

    def up(self):
        """
        Turn snake up
        """
        # If the snake head is not oriented downwards
        if self.head.heading() != DOWN:

            # Set heading up
            self.head.setheading(UP)

    def down(self):
        """
        Turn snake down
        """
        # If the snake head is not oriented upwards
        if self.head.heading() != UP:

            # Set heading down
            self.head.setheading(DOWN)

    def left(self):
        """
        Turn snake left
        """
        # If the snake head is not oriented right
        if self.head.heading() != RIGHT:

            # Set heading left
            self.head.setheading(LEFT)

    def right(self):
        """
        Turn snake right
        """
        # If the snake head is not oriented left
        if self.head.heading() != LEFT:

            # Set heading right
            self.head.setheading(RIGHT)
