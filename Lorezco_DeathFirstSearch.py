# Lorezco, John Marco
# CMSC 142

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Define a function 'block' with the parameter si, the position of
# the Bobnet agent in the List array.
# Use global keyword in calling 'connection' to allow modification
# outside the current scope.
def block(si, List):
    global connection
    for x in List:  # For the position x in the array 'List'
        if x in connection[si]:  # If the link is connected to the Bobnet agent,
            return [si, x]       # return the Bobnet agent's position
    for x in List:  # For the position x in the array 'List'
        if len(connection[x]) > 0:  # If the link's index is greater than 0,
            return [x, connection[x][0]]  # return the link's index
    return [0, 0]   # Else, return [0, 0]

# Define a function link_remover for cutting the link to the path
# where there is a gateway
def link_remover(Link1, Link2):
    global connection
    connection[link1].remove(link2)
    connection[link2].remove(link1)

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
# List: array
# connection: for mapping objects; used to connect of remove links
n, l, e = [int(i) for i in input().split()]
List = []
connection = {}

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    connection.setdefault(n1, []).append(n2)
    connection.setdefault(n2, []).append(n1)

for i in range(e):
    ei = int(input())  # the index of a gateway node
    List.append(ei)    # add/append the index of gateway to the array 'List'

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    link1, link2 = block(si, List) 
    link_remover(link1, link2)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    # .format is used to insert the value from the 'block' function
    print("{0} {1}".format(link1, link2))
