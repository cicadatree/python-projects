# GOAL: robot touch every available tile in the smallest number of moves

# create array grid; mark some tiles as unavailable (make sure all available tiles are connected to one another - i.e. no islands)
# put robot on any available tile
# robot has four functions: turn left; turn right; check tile infront; move forward
# robot cannot move to an unnavailable tile

from enum import Enum

class Tile(Enum):
    SOLID = 0
    EMPTY = 1
    ROBOT = 2
    
grid = [
    [1,0,0,0,0,0,0],
    [1,0,1,1,1,0,0],
    [1,1,1,0,1,1,0],
    [1,1,0,0,0,1,1],
    [1,1,0,1,0,0,1],
    [1,1,1,1,0,0,1],
    [1,1,1,1,1,1,1]
]

robotPosition = [0,0] 
up = 0
right = 1
down = 2
left = 3
robotDirection = up

def turnLeft():
    global robotDirection 
    robotDirection -= 1
    if robotDirection == -1:
        robotDirection = 3
    return

def turnRight():
    global robotDirection 
    robotDirection += 1
    if robotDirection == 4:
        robotDirection = 0
    return

def goForward(position,direction):
    if direction == 0: #up
        position[1] -= 1
    elif direction == 1: #right
        position[0] += 1
    elif direction == 2: #down
        position[1] += 1
    elif direction == 3: #left
        position[0] -= 1
    return position


def checkForwardAndGo():
    global robotDirection
    global robotPosition
    global grid
    # need to get the position I'm going to
    tempPosition = goForward(robotPosition,robotDirection)
    # need to check if the position I'm going to is empty
    if tempPosition 
    # if it's valid, move the robot to the tempPosition

    return # return success or fail (true or false)

turnLeft() 

