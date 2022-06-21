#-------------------------------------------------------------------------------
# Name:        Opening Module
# Purpose:     for python project
#
# Author:      Group 6
#
# Title:       Hotel Management System
#-------------------------------------------------------------------------------


# Turtle drawing during the opening of the program
import turtle

def hi():
    s = turtle.Screen()
    s.bgcolor("black")                   # Background Colour
    s.title("WELCOME TO GSIX HOTEL")

    t = turtle.Turtle()
    t.shape("turtle")
    t.color("yellow")                    # Pen Colour
    t.pensize(5)                         # Pen Size
    t.speed(10)                          # Drawing Speed

    t.goto(0,0)                          # Set at origin

    # Tuple for different size pattern
    path1 = (400,400,400,400,400,400,400,400)
    path2 = (300,300,300,300,300,300,300,300)
    path3 = (200,200,200,200,200,200,200,200)
    path4 = (100,100,100,100,100,100,100,100)
    path5 = (50,50,50,50,50,50,50,50,50,50)

    t.penup()
    t.goto(-550,0)
    def pattern(*path):                  # Variable Length Arguments (*args)
        for i in path:
            t.forward(i)
            t.right(45)
            t.penup()
            t.backward(i)
            t.pendown()
            t.write("HI")
            t.stamp()

    pattern(*path1, *path2, *path3,*path4, *path5)
    t.penup()
    t.goto(550,50)
    pattern(*path5, *path4, *path3,*path2, *path1)

    t.color("blue")
    t.penup()
    t.goto(50,90)
    t.pendown()                 # Pattern G
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10)
    t.left(180)
    t.forward(20)

    t.penup()
    t.goto(50,-20)
    t.pendown()                 # Pattern 6
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)

    t.color("black")            # make turtle invisible
    t.penup()
    t.goto(500,500)

    turtle.bye()        # exit with mouse click