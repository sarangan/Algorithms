def printBoard(board):
    """print successfull board"""
    print board

def checkValidMove(board, row, col):


    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, 4, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveQueens(board, queens, row=0):
    """backtracking n queens main recursive func"""

    #print row
    #print "--"

    if row >= queens:
        return True

    for col in range(queens):

        print row, col

        print checkValidMove(board, row, col)

        if checkValidMove(board, row, col):
            board[row][col] = 1

            if solveQueens(board, queens, row+1) == True:
                return True

            board[row][col] = 0

    return False



if __name__ == "__main__":


    queens = 4

    board = [[0 for i in range(queens)] for j in range(queens)]

    print board

    x = solveQueens(board, queens)

    if x:
        printBoard(board)