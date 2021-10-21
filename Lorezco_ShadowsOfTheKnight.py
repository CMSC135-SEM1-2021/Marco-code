#Lorezco, John Marco
#CMSC 142

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
w0, h0 = 0, 0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
     
    # We use math.floor to round numbers down to the nearest integer
    # For direction going up
    if "U" in bomb_dir:
        h = y0
        y0 = math.floor((y0 + h0) / 2)

    # For direction going right
    if "R" in bomb_dir:
        w0 = x0
        x0 = math.floor((x0 + w) / 2)
    
    # For direction going down
    if "D" in bomb_dir:
        h0 = y0
        y0 = math.floor((y0 + h) / 2)

    # For direction going left
    if "L" in bomb_dir:
        w = x0
        x0 = math.floor((x0 + w0) / 2)


    # the location of the next window Batman should jump to.
    print(str(int(x0)) + " " + str(int(y0)))
