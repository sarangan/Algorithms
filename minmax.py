import math

# max
# min
# max

def minmax(currentDepth, nodeIdx, isMaxMove, scores, actualTreeDepth ):

    if currentDepth == actualTreeDepth:
        #we have reached the end
        return scores[nodeIdx]

    if isMaxMove:
        #print nodeIdx * 2
        #take max value and set next move will be min move
        return max(
            minmax(currentDepth + 1, nodeIdx * 2, False, scores, actualTreeDepth),
            minmax(currentDepth + 1, nodeIdx * 2 + 1, False, scores, actualTreeDepth)
        )
    else:
        #print nodeIdx * 2

        return min(
            minmax(currentDepth + 1, nodeIdx * 2, True, scores, actualTreeDepth),
            minmax(currentDepth + 1, nodeIdx * 2 + 1, True, scores, actualTreeDepth)
        )


if __name__ == "__main__":

    scores = [3, 5, 2, 9]

    treeDepth = math.log(len(scores), 2)

    print minmax(0, 0, True, scores, treeDepth)