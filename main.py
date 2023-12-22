from turtle import Screen
from winner import Winner
import player
import time

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Turtle Racing Game")
screen.tracer(0)

# Defining classes
turtle = player.Player()
winner = Winner()

# Making a prompt to ask the user
title ="Make a bet"
prompt = "Who will win the race (Violet, Indigo, Blue, Green, Yellow, Orange, Red)?"

is_valid_color = False
while not is_valid_color:
    user_input = screen.textinput(title, prompt).lower()
    for color in player.COLORS:
        if user_input == color:
            is_valid_color = True
            break

# Create turtles
for _ in range(0, 7):
    turtle.create_turtle()

is_race_started = False
if user_input:
    is_race_started = True

while is_race_started:
    time.sleep(0.1)
    screen.update()
        
    # Make the turtle move
    turtle.move_turtle()

    # Detect when the turtle reaches the finish line
    for tur in turtle.all_turtles:
        if tur.xcor() > 280:
            is_race_started = False
            if user_input == tur.fillcolor():
                winner.turtle.write(f"{tur.fillcolor().capitalize()} Won! You Won", align="center", font=("Courier", 16, "normal"))
            else:
                winner.turtle.write(f"{tur.fillcolor().capitalize()} Won! You Lost", align="center", font=("Courier", 16, "normal"))

            print(tur.fillcolor())
            break

screen.exitonclick()
