# GOAL: robot touch every available tile in the smallest number of moves

# create array grid; mark some tiles as unavailable (make sure all available tiles are connected to one another - i.e. no islands)
# put robot on any available tile
# robot has four functions: turn left; turn right; check tile infront; move forward
# robot cannot move to an unnavailable tile

from enum import Enum

class Tile(Enum):
    SOLID = 0
    EMPTY = 1
    
grid = [
    [1,0,0,0,0,0,0],
    [1,0,1,1,1,0,0],
    [1,1,1,0,1,1,0],
    [1,1,0,0,0,1,1],
    [1,1,0,1,0,0,1],
    [1,1,1,1,0,0,1],
    [1,1,1,1,1,1,1]
]
up = 0
right = 1
down = 2
left = 3
robotPosition = [0,0]   
robotDirection = up

# function for turning the robot's face (robotDirection) once to the left
def turnLeft():
    global robotDirection 
    robotDirection -= 1
    if robotDirection == -1:
        robotDirection = 3
    return

# function for turning robot's face (robotDirection) once to the right
def turnRight():
    global robotDirection 
    robotDirection += 1
    if robotDirection == 4:
        robotDirection = 0
    return

# function for moving the robot forward one tile in the direction it's facing
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

# function for checking if the tile which the robot is facing is EMPTY (available) or SOLID (unavaiable), returns true or false
def checkForwardAndGo():
    global robotDirection
    global robotPosition
    global grid

    # need to get the position I'm trying to move to
    tempPosition = goForward(robotPosition,robotDirection)
    
    # need to check if the X element of the position is in the array's range and not less than zero
    if tempPosition[0] >= len(grid[0]) or tempPosition[0] < 0:
        return False
    # need to check if the Y element of the position is in the array's range and not less than zero
    elif tempPosition[1] >= len(grid) or tempPosition[1] < 0:
        return False
     # if it's valid, move the robot to the tempPosition
    elif grid[tempPosition[0]][tempPosition[1]] == Tile.SOLID:
        return False
    # return True if all False conditions 
    else:
        robotPosition = tempPosition
        return True

# main function 
def navigateGrid(): 
    global robotPosition
    global robotDirection
    global grid

    # Function that repeatedly turns left or right, and checks to move forward
    while True:
        # Start by seeing if it can turn left and move forward
        print("Currently at: " + str(robotPosition))
        printGrid()

        turnLeft()
        if not checkForwardAndGo():
            # Left didn't work, so try right
            turnRight() # back to original direction
            turnRight() # turning to the right, relative to original direction
            if not checkForwardAndGo():
                # Right didn't work either
                print("Stopped at" + str(robotPosition))
                return

def printGrid():
    global robotPosition
    global robotDirection
    global grid

    for rowNum, row in enumerate(grid):
        line = ''
        for colNum, col in enumerate(row):
            if rowNum == robotPosition[1] and colNum == robotPosition[0]:
                line += 'R'
            else:
                line += str(grid[rowNum][colNum])
            if colNum < len(row):
                line += ' '

        print(line)


# Python best practices to call the main function from a __main__ check
if __name__ == "__main__":
    navigateGrid()
