from turtle import Turtle, Screen
from dots import Dots
screen = Screen()
screen.screensize(canvwidth=400, canvheight=600)
screen.colormode(255)
screen.bgcolor(170,223,241)
screen.title("Kat's Dot House as Inspired by Chihuly Glass House")

dots = Dots()
is_running = True
dots.start_dots()
while is_running:
    dots.new_dots_pair()

screen.exitonclick()
