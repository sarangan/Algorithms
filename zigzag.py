"""
*  *   *
 *   *   *
"""

def zigZag(str, rows):

    row = 0

    arr = ["" for i in range(len(str))]


    for i in range(len(str)):

        arr[row] += str[i]

        if row == rows-1:
            down = False
        elif row == 0:
            down = True

        if down:
            row += 1
        else:
            row -= 1

    print arr




if __name__ == "__main__":
    zigZag("GEEKSFORGEEKS", 3)