# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Ali <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(10)

# Draw the Level 4 version of the room
window = room.draw_room(level = 4, n_alcoves = 1, radius = 5)

###
# Start your code here
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
for i in range (2) :
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
    backward(40)
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