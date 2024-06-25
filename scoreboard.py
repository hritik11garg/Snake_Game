from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",20, "normal")
GAME_OVER_FONT = ("Courier",30, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)    # Position at the top of the screen
        self.hideturtle()
        self.update_scoreboard()    # Display the initial score
        
    def update_scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)  # Write the current score

    
    def increase_score(self):
        self.score += 1
        self.clear()    # Clear the previous score
        self.update_scoreboard()    # Update the display
        
    def game_over(self):
        self.goto(0, 0)     # Position in the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
