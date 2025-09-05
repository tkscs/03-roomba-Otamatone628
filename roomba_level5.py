# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Ali <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 3

# Draw the Level 5 version of the room
window = room.draw_room(level = 5, n_alcoves = n_alcoves)

###
# Start your code here
forward(560)
left(180)
for i in range(3) :
    forward(40)
    left(90)
    forward(120)
    right(90)
    forward(40)
    left(90)
    forward(40)
    right(90)
    forward(120)
    right(90)
    backward(200)
    for i in range (4) :
        forward(40)
        right(90)
        forward(40)
        left (90)
        forward(40)
        left(90)
        backward(40)
    forward(160)
forward(40)
left(90)
forward(120)
right(90)
forward(40)
left(90)
forward(40)
right(90)
forward(80)
backward(80)
right(90)
forward(40)
for i in range(3) :
    forward(240)
    left(90)
    forward(40)
    left(90)
    forward(240)
    right(90)
    forward(40)
    right(90) 
forward(200)
# End your code here
###
 
window.exitonclick()