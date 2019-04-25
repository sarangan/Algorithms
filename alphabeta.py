import math

# max
# min
# max

#alpha beta puring

MAX = 10000
MIN = -10000

def minmax(currentDepth, nodeIdx, isMaxMove, scores, actualTreeDepth, alpha, beta ):

    if currentDepth == actualTreeDepth:
        #we have reached the end
        return scores[nodeIdx]

    if isMaxMove:
        #take max value and set next move will be min move

        best = MIN

        for i in range(2):
            value = minmax(currentDepth + 1, nodeIdx * 2 + i, False, scores, actualTreeDepth, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            #alpha beta puring
            if beta <= alpha:
                break

        return best

    else:

        best = MAX

        for i in range(2):

            value = minmax(currentDepth + 1, nodeIdx * 2 + i, True, scores, actualTreeDepth, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


if __name__ == "__main__":

    scores = [3, 5, 6, 9, 1, 2, 0, -1]

    treeDepth = math.log(len(scores), 2)


    print minmax(0, 0, True, scores, treeDepth, MIN, MAX )