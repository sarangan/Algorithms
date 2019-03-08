
def isValidPlacement(colPlacements):

    last_queen = colPlacements[-1]

    print 'last_queen'
    print last_queen

    for i in range(len(colPlacements)):

        getAbsDistance = abs(colPlacements[i] - last_queen)

        print 'getAbsDistance'
        print getAbsDistance


        if getAbsDistance == 0 or getAbsDistance == (len(colPlacements) - i ):
            return False

    return True




def solveNQueens(n, row, colPlacements, result):


    if row == n:

        result.append(colPlacements)
        print result

    else:

        for col in range(n):

            colPlacements.append(col)
            #colPlacements[col] = col

            print isValidPlacement(colPlacements)

            if isValidPlacement(colPlacements):
                solveNQueens(n, row+1, colPlacements, result)

            colPlacements.pop()



if __name__ == "__main__":
    no_of_queens = 8
    colPlacements = [] #[0 for i in range(no_of_queens)]
    result = []
    solveNQueens(no_of_queens, 0, colPlacements, result)

    print result
