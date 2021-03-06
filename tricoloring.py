colors = ['R', 'G', 'B']


def isStableColor(A, colPlacements):
    color_r = 0
    color_g = 0
    color_b = 0
    for i in range(len(colPlacements)):
        if colPlacements[i] == 'R':
            color_r += A[i]
        if colPlacements[i] == 'G':
            color_g += A[i]
        if colPlacements[i] == 'B':
            color_b += A[i]

    if color_r == color_g and color_g == color_b and color_r == color_b:
        # found the solution
        return ''.join(colPlacements)
    else:
        return "impossible"


def solveColor(A, row, colPlacements, result):
    if row == len(A):
        s = isStableColor(A, colPlacements)
        if s != "impossible":
            result.append(s)

    else:

        for col in range(len(A)):

            for color in colors:
                colPlacements.append(color)

                solveColor(A, row + 1, colPlacements, result)

                colPlacements.pop()  # backtracking

    return result

def solution(A):
    # write your code in Python 3.6
    # lets take one element which can be either R G B ( 3 possibilities)

    colPlacements = []
    result = []

    solveColor(A, 0, colPlacements, result)

    return result


if __name__ == "__main__":

    s = solution( [3, 7, 2, 5, 4 ] )
    print s[0]
