import sys
coins = [1, 5, 10]
memo = {}

def changeCoin(reminder):

    if reminder < 0:
        return -1
    elif reminder == 0:
        return 0
    elif memo.get(reminder, 0) != 0:
        return memo[reminder]
    else:

        min = sys.maxint

        for coin in coins:
            change_result = changeCoin(reminder - coin)

            if change_result >= 0 and change_result < min:
                min = 1 + change_result

        if min == sys.maxint:
            min = -1

        memo[reminder] = min


        # c1 = changeCoin(reminder - coins[0])
        # if reminder - coins[0] >= 0:
        #     c1 +=1
        #
        # c2 = changeCoin(reminder - coins[1])
        # if reminder - coins[1] >= 0:
        #     c2 +=1
        #
        # c3 = changeCoin(reminder - coins[2])
        # if reminder - coins[2] >= 0:
        #     c3 +=1
        #
        # result = min(c1, c2, c3)
        #
        # print result
        #
        #
        # memo[reminder] = result



    return memo[reminder]


if __name__ == "__main__":

    change = 12
    x = changeCoin(change)
    print x
