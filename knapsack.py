

def ks(n, wt, w, v):
    """n number of items wt is total weight"""

    if n == 0 or wt == 0:
        return 0
    elif w[n-1] > wt:
        return ks(n-1, wt, w, v)
    else:
        item_in = v[n] + ks(n-1, wt-w[n], w, v)
        item_off = ks(n-1, wt, w, v)

        return max(item_in, item_off)




if __name__ == "__main__":

    v = [60, 100, 120]
    w = [10, 20, 30]
    wt = 50

    n = len(w) - 1
    x = ks(n, wt, w, v)
    print x
