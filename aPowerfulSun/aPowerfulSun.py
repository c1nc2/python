
# first import the turtle
import turtle

# creating the function
def aPowerfulSun():
    window = turtle.Screen()
    
    # making the bcakground black
    window.bgcolor("black")

    # naming the variables and creating the color of the lines
    lines = turtle.Turtle()
    lines.speed(10)
    lines.color("yellow")

    # making the loop and making it 36 turns 
    for _ in range(36):
        lines.forward(100)
        lines.right(45)
        lines.forward(100)
        lines.right(135)
        lines.forward(100)
        lines.right(45)
        lines.forward(100)
        lines.right(135)
        lines.right(10)
        
    turtle.done()

# this will make function start
aPowerfulSun()


