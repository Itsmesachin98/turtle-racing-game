from turtle import Turtle
import random

COLORS = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

class Player:
    def __init__(self):
        self.all_turtles = []
        self.index = 0
        self.x_cor = -280
        self.y_cor = -120


    def create_turtle(self):
        self.new_turtle = Turtle("turtle")
        self.new_turtle.penup()
        self.new_turtle.color(COLORS[self.index])
        self.new_turtle.goto(self.x_cor, self.y_cor)
        self.all_turtles.append(self.new_turtle)
        self.index += 1
        self.y_cor += 40

    def move_turtle(self):
        for turtle in self.all_turtles:
            turtle.forward(random.randint(1, 20))
