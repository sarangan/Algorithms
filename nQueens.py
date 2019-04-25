
def isValidPlacement(colPlacements):

    last_queen = colPlacements[-1]

    #no need to check the last queen is because its already our new placement queen
    for i in range(len(colPlacements) - 1 ):


        getAbsDistance = abs(colPlacements[i] - last_queen)


        if getAbsDistance == 0 or getAbsDistance == ( (len(colPlacements) - 1)  - i ):
            return False

    return True




def solveNQueens(n, row, colPlacements, result):


    if row == n:

        #result.append(colPlacements)
        print printBoard(n,colPlacements)

    else:

        for col in range(n):

            colPlacements.append(col)

            if isValidPlacement(colPlacements):
                solveNQueens(n, row+1, colPlacements, result)

            colPlacements.pop()


def printBoard(n, colPlacements):

    for i in range(len(colPlacements)):

        temp = ''
        for j in range(n):

            if j == colPlacements[i]:
                temp += ' Q '
            else:
                temp += ' - '
        print temp

    print "--------------------------------------------"

# def printBoard(n, colPlacements):
#         temp = []
#         for i in range(len(colPlacements)):
#             q = ["." for i in range(n)]
#             q[i] = "Q"
#             temp.append(''.join(q))
#         print temp


if __name__ == "__main__":
    no_of_queens = 4
    colPlacements = [] #[0 for i in range(no_of_queens)]
    result = []
    solveNQueens(no_of_queens, 0, colPlacements, result)

    #print result
