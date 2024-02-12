from turtle import Turtle, Screen
"""
Swati Poojary did the circle and the main function
Mohammed Abujbara did the pattern function
Samira Alsaqqa did the hexagon function
Maryam Sabt did square and SetPos function
Everyone in this group made sure to work together and help each other in the divided work
"""
def SetPos(turta,x,y):
    """
    Sets the position of the turtle to the specified coordinates (x, y).
    - turta: Turtle object
    - x: x-coordinate
    - y: y-coordinate
    """
    turta.penup()
    turta.goto(x,y)
    turta.pendown()
    
def circle(turta, circle_color, border_color):
    """
    Draws a circle filled with a color and outlined with another color.
    - turta: Turtle object
    - circle_color: Color to fill the circle
    - border_color: Color for the circle's outline
    """
    turta.pencolor(border_color)
    turta.pensize(3)
    turta.begin_fill()
    turta.fillcolor(circle_color)
    turta.circle(50)
    turta.end_fill()

def square(turta, square_color, border_color):
    """
    Draws a square filled with a color and outlined with another color.
    - turta: Turtle object
    - square_color: Color to fill the square
    - border_color: Color for the square's outline
    """
    turta.pencolor(border_color) 
    turta.pensize(3) 
    turta.up()
    turta.down()
    turta.begin_fill() 
    turta.fillcolor(square_color)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()
    
def hexagon(turta, hexa_color, border_color):
    """
    Draws a hexagon filled with a color and outlined with another color.
    - turta: Turtle object
    - hexa_color: Color to fill the hexagon
    - border_color: Color for the hexagon's outline
    """
    turta.pencolor(border_color)
    turta.pensize(3)    # Set the pen size to 3
    turta.up()       # make the pen up
    turta.down()        # Put the pen down to start drawing
    turta.begin_fill()  # Begin filling the shape
    turta.fillcolor(hexa_color) # Set the fill color to the hexagon color
    turta.left(60)       # Rotate the turtle left by 60 degrees 
    turta.forward(50)   # move forward by 50 units to draw the first side
    turta.left(60)      # Repeat the previous step five more times to draw the remaining sides of the hexagon
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.end_fill()
    
def pattern(turta, hexa_color, circle_color, square_color, border_color):
    """
    Draws a pattern with hexagon, circle, and square filled with colors.
    - turta: Turtle object
    - hexa_color: Color for hexagon
    - circle_color: Color for circle
    - square_color: Color for square
    - border_color: Color for borders
    """
    #set position for circle, square and hexagon 1
    
    SetPos(turta,0,0)  
    circle(turta, circle_color, border_color)
    SetPos(turta,90,0)   
    square(turta, square_color, border_color)
    SetPos(turta,-110,0)
    hexagon(turta, hexa_color, border_color)
   
    #set position for circle, square and hexagon 2

    SetPos(turta,90,-120)  
    circle(turta, circle_color, border_color)
    SetPos(turta,180,-120)  
    square(turta, square_color, border_color)
    SetPos(turta,-15,-120)
    hexagon(turta, hexa_color, border_color)

    #set position for circle, square and hexagon 3

    SetPos(turta,-90, 120)  
    circle(turta, circle_color, border_color)
    SetPos(turta,0,120)   
    square(turta, square_color, border_color)
    SetPos(turta,-200, 120)
    hexagon(turta, hexa_color, border_color)
   
def main():
    """
    Main function for drawing the pattern based on user input.
    """
    wind=Screen()   # Create a screen object
    wind.bgcolor("light blue")    # Set the background color of the screen
    turtle =Turtle()   # Create a turtle object
    turtle.speed(0)   # Set the speed of the turtle
    
    # Ask the user to input colors for the shapes
    
    hexa_color = input("Enter color for hexagon: ")
    circle_color = input("Enter color for circle: ")
    square_color = input("Enter color for square: ")
    border_color = input("Enter color for borders: ")
   
    pattern(turtle, hexa_color, circle_color, square_color, border_color)   # Draw the pattern
    wind.exitonclick()   # Close the screen when clicked


main()