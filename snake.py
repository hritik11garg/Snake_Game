from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]       # Initial positions of the snake segments
MOVE_DISTANCE = 20      # Distance each segment moves
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]    # The first segment is the head
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Add segments to the snake
 

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)   # Add the segment to the list
            
    def extend(self):
        self.add_segment(self.segments[-1].position())  # Add a new segment at the end
    

    def move(self):
            for seg_num in range(len(self.segments) -1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
            self.head.forward(MOVE_DISTANCE)    # Move each segment to the position of the previous one

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)    # Change direction to up
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # Change direction to down
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  # Change direction to left
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) # Change direction to right
        
    