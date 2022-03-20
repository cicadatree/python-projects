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
dirStrings = ['Up', 'Right', 'Down', 'Left']
robotPosition = [0,0]   
robotDirection = right

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
    newPosition = list(position) # Create a copy to modify and return
    if direction == 0: #up
        newPosition[1] -= 1
    elif direction == 1: #right
        newPosition[0] += 1
    elif direction == 2: #down
        newPosition[1] += 1
    elif direction == 3: #left
        newPosition[0] -= 1
    return newPosition

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
    elif grid[tempPosition[1]][tempPosition[0]] == Tile.SOLID.value:
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
    # Limiting it to 5 iterations, for now
    for i in range(5):
        # Start by seeing if it can turn left and move forward
        print()
        print("Robot direction is: " + dirStrings[robotDirection])
        printGrid()
        print()

        turnLeft()
        print("Trying Left turn")
        if not checkForwardAndGo():
            # Left didn't work, so try right
            print("Left turn failed, trying Right turn")
            turnRight() # back to original direction
            turnRight() # turning to the right, relative to original direction
            if not checkForwardAndGo():
                # Right didn't work either
                print("Right turn failed, Stopping")
                return
            else:
                print("Right turn succeeded!" + str(robotPosition))
        else:
            print("Left turn succeeded!" + str(robotPosition))

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
