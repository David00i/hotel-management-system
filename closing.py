#-------------------------------------------------------------------------------
# Name:        Closing Module
# Purpose:     for python project
#
# Author:      Group 6
#
# Title:       Hotel Management System
#-------------------------------------------------------------------------------


# Turtle drawing during the closing of the program
import turtle

def bye():
    s = turtle.Screen()
    s.bgcolor("black")            # Background Colour
    s.title("THANKS FOR YOUR VISITING")

    turtle.TurtleScreen._RUNNING=True
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("yellow")             # Pen Colour
    t.pensize(5)                  # Pen Size
    t.speed(30)                   # Drawing Speed

    t.goto(0,0)                   # Set at origin

    # Tuple
    path1 = (400,400,400,400,400,400,400,400)
    path2 = (300,300,300,300,300,300,300,300)
    path3 = (200,200,200,200,200,200,200,200)
    path4 = (100,100,100,100,100,100,100,100)
    path5 = (50,50,50,50,50,50,50,50,50,50)

    t.penup()
    t.goto(-400,0)

    # Variable Length Arguments (*args)
    def pattern(*path):
        for i in path:
            t.forward(i)
            t.right(45)
            t.penup()
            t.backward(i)
            t.pendown()
            t.write("bye")
            t.stamp()

    pattern(*path1, *path2, *path3,*path4, *path5)
    t.penup()
    t.goto(400,50)
    pattern(*path5, *path4, *path3,*path2, *path1)


    t.color("black")             # make turtle invisible
    t.penup()
    t.goto(500,500)

    turtle.exitonclick()