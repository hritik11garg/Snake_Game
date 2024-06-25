from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create the snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()     # Update the screen
    time.sleep(0.1)     # Pause for a short period
    
    snake.move()        # Move the snake
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move food to a new random location
        snake.extend()  # Add a new segment to the snake
        scoreboard.increase_score()     # Increase the score
        
    
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False      # End the game
        scoreboard.game_over()  # Display "Game Over"
    
    
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()    # Keep the window open until clicked