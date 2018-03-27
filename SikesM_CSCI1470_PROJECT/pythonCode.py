#*****************************************************************************
#
# Name: Margo Sikes
#
# Course: CSCI 1470
#
# Assingment: Project
#
#    Algorithms:
#        Import serial, turtle, io, and time modules
#
#	 Define function that buffers potentiometer input using range of numbers to generalize the input
#	     Returns generalized value
#	 Define fixed update function that reads Arduino serial and saves the most recent line
#            Defines variables globally so that they can be accessed outside of the function
#            Checks to see if the most recent line contains all info needed
#                Adds new and subtracts from old accelerometer values together to determine whether it is being shaken
#                    If the Arduino is being shaken, it calls the reset turtle function
#                Updates the velocity and angle values for movement
#	 Define function resets the turtle + the drawing
#        Define function that makes turtle draw
#            If turtle is outside of bounds of window, doesn't let turtle move forward until its angle faces back inside box
#        Defines time elapsed function that checks to see how much time has passed
#
#        Initialize turtle window at 500,500
#
#        Asks user to give the turtle a color and a size, rejects invalid input
#  	 Set turtle and turtle speed
#        Sets user-given turtle color and size
#
#	 Define values to begin at zero, and creates a starting time for timeElapsed function
#
#	 Set up serial port at COM3 with 57600 baud rate and a timeout of 0
#	 Buffer the serial information using io to make it more readable
#
#	 While drawing program is active
#		Adds the time elapsed to the lag
#		Checks to see if lag is above 0.3
#                   If lag is above 0.3, run the update function that reads the Arduino values
#                    Subtracts 0.3 to reset the lag
#               Updates the turtle movement
#                
#        Terminates turtle when window is closed
#
#       Sources:
#           Fixed update & time elapsed concepts inspired by code from "Game Programming Patterns" by Robert Nystrom, pg. 131
#           Serial and TextIOWrapper code from PySerial's documentation: http://pyserial.readthedocs.io/en/latest/shortintro.html#opening-serial-ports
#
#********************************************************************************

import serial
import io
import turtle
import time

def inputBuffer(inputNum):
    bufferedInput = 0
    if inputNum > 800:
        bufferedInput = 3
    elif inputNum > 600 and inputNum <= 800:
        bufferedInput = 1
    elif inputNum > 400 and inputNum <= 600:
        bufferedInput = 0
    elif inputNum > 200 and inputNum <= 400:
        bufferedInput = -1
    elif inputNum >= 0 and inputNum <= 200:
        bufferedInput = -3
    else:
        bufferedInput = 0
    return bufferedInput

def update():
    global velocity
    global angle
    global prevXyz
    arduinoInput = sio.readlines()
    if len(arduinoInput) > 1:
        inputList = arduinoInput.pop()
        inputList = inputList.split()
        if len(inputList) >= 5:
            xyz = (int(inputList[0])+int(inputList[1])+int(inputList[2]))
            diffXyz = xyz-prevXyz
            prevXyz = xyz
            if diffXyz < -200:
                turtleReset()
            velocity = inputBuffer(int(inputList[3]))+3
            angle = inputBuffer(int(inputList[4]))

def turtleReset():
    draw.clear()
    draw.penup()
    draw.home()
    draw.pendown()

def drawing():
    ##north boundary
    if draw.ycor() >= 400 and draw.heading() >= 0 and draw.heading() <= 180:
        draw.forward(0)
    ##south boundary    
    elif draw.ycor() <= -400 and draw.heading() <= 360 and draw.heading() >= 180:
        draw.forward(0)
    ##east boundary
    elif draw.xcor() >= 700:
        if draw.heading() <= 90 and draw.heading() >= 0:
            draw.forward(0)
        elif draw.heading() >= 270 and draw.heading() <= 360:
            draw.forward(0)
        else:
            draw.forward(velocity)
    ##west boundary
    elif draw.xcor() <= -700 and draw.heading() >= 90 and draw.heading() <= 270:
        draw.forward(0)
    else:
        draw.forward(velocity)
    draw.left(angle)

def timeElapsed():
    global previous
    current = time.time()
    elapsed = current - previous
    previous = current
    return elapsed

window = turtle.Screen()
window.screensize()
window.bgcolor("light blue")
window.setup(width = 1.0, height = 1.0, startx=0, starty=0)
#window.screensize(500,500,"white")
#window.setup(width=510, height=510, startx=0,starty=0)

##turtleColor = input("Choose a pen color: red, orange, yellow, green, blue, or purple: ")
##while turtleColor != "red" and turtleColor != "orange" and turtleColor != "yellow" and turtleColor != "green" and turtleColor != "blue" and turtleColor != "purple":
##    print("Invalid input, please try again.")
##    turtleColor = input("Choose a pen color: red, orange, yellow, green, blue, or purple: ")
##turtleSize = int(input("What size should the pen be from 1-10?: "))
##while turtleSize > 10 or turtleSize < 1:
##    print("Invalid input, please try again.")
##    turtleSize = int(input("What size should the pen be from 1-10?: "))

draw = turtle.Turtle()
##draw.color(turtleColor)
##draw.pensize(turtleSize)
draw.color("green")
draw.pensize(3)
draw.speed(0)

velocity = 0
angle = 0
previous = time.time()
lag = 0.0
prevXyz = 0

ser = serial.Serial('COM3', 57600, timeout=0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))

while True:
    lag += timeElapsed()
    while lag >= .3:
        update()
        lag-= .3
    drawing()
    
window.mainloop()
