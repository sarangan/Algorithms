

def printPath(maze, movement):


    for r in maze:
        print r

    print "---------------------------"

    for r in movement:
        print r


def safeMove(maze, x, y):

    if x >= 0 and y >= 0 and x < len(maze) and y < len(maze) and maze[x][y] == 1:
        return True

    return False


def makeMove(maze, movement, row, col ):

    if row == len(maze)-1 and col == len(maze)-1:
        movement[row][col] = 1
        return True

    if safeMove(maze, row, col) == True:

        movement[row][col] = 1

        if makeMove(maze, movement,  row+1, col) == True:
            return True


        if makeMove(maze, movement,  row, col+1) == True:
            return True

        movement[row][col] = 0

        return False



def solveMaze(maze):

    movement = [ [0 for j in range(4)] for i in range(4) ]

    if makeMove(maze, movement, 0, 0 ) == False:
        print "path does not exist"

    printPath(maze, movement)


if __name__ == "__main__":


    maze = [ [1, 0, 0, 0],
             [1, 1, 1, 1],
             [0, 0, 1, 1],
             [1, 1, 1, 1]]

    solveMaze(maze)