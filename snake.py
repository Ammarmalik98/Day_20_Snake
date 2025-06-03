STARTING_POINT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

from turtle import Turtle, Screen

class Snake:

    def __init__(self):
        """ Creates a new snake """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for square in range(0, 3):
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(STARTING_POINT[square])
            self.segments.append(new_square)

    def move(self):
        """ moves the snake object """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """ moves the snake object up """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ moves the snake object down """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ moves the snake object left """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ moves the snake object right """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)