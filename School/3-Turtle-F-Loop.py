import turtle # Allows us to use turtles
turtle.clear()
wn = turtle.Screen() # Creates a playground for turtles
alex = turtle.Turtle() # Create a turtle, assign to alex

for c in ["yellow", "red", "purple", "blue"]:
    alex.color(c)   
    alex.forward (50)
    alex.left (90)

wn.mainloop() # Wait for user to close window
turtle.bye()