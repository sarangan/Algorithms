import random
import math
from BT import Node
from AVLTree import AVLTree

def biSearch(li, x, low, high):
    """this is binary search tree"""
    # if high - low < 2:
    #     return li[low] == x or li[high] == x
    mid = int((low + high) / 2)  #low + int((high - low)/2)

    if low == mid or low == high:
        return li[low] == x or li[high] == x

    if li[mid] == x:
        return True
    elif li[mid] > x:
        return biSearch(li, x, low, mid)
    elif li[mid] < x:
        return biSearch(li, x, mid, high)

def selectionSort(li):
    """selection sort"""
    for i in range(0,len(li)):
        for j in range(0,len(li)):
            if li[i] < li[j]:
                li[i], li[j] = li[j], li[i]
    print li


def bubbleSort(li):
    """bubble sort"""
    for i in range(0, len(li)):
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    print li


def insertionSort(li):
    """insertion sort"""
    for i in range(1, len(li)):
        temp = li[i]
        for j in range(i-1, -1, -1):
            if temp < li[j]:
                li[j+1], li[j] = li[j], li[j+1]

    print li


def shellSort(li):
    """shell sort"""
    gap = int(len(li) / 2)

    while gap > 0:

        for i in range(gap):

            for j in range(i + gap, len(li), gap):

                for k in range(j, -1, -gap):

                    if li[k] > li[j]:
                        li[k], li[j] = li[j], li[k]

        gap = int(gap / 2)


    print li


def merge(left, right):
    i,j =0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

    if i < len(left):
        for k in range(i, len(left)):
            result.append(left[k])

    if j < len(right):
        for k in range(j, len(right)):
            result.append(right[k])

    return result

def mergeSort(li):
    """merge sort"""

    #print li

    if len(li) < 2:
        return li[:]
    else:
        mid = int(len(li) / 2)
        left = mergeSort(li[:mid])
        right = mergeSort(li[mid:])
        return merge(left, right)


def quickSort(li):
    """quick sort"""

    if len(li) < 2:
        return li

    median = int(len(li)/2)

    left, right, eq = [], [], []
    for i in range(len(li)):
        if li[i] == li[median]:
            eq.append(li[i])
        elif li[i] < li[median]:
            left.append(li[i])
        else:
            right.append(li[i])

    return quickSort(left) + eq + quickSort(right)


def partition(li, low, high):
    """partitioning"""

    pivot = li[high]
    i = low - 1

    for j in range(low, high):

        if li[j] < pivot:
            i = i + 1
            li[j], li[i] = li[i], li[j]
    i = i + 1
    li[i], li[high] = li[high], li[i]

    return i




def quickSort2(li, low, high):
    """quick sort 2"""

    if low < high:
        p = partition(li, low, high)

        quickSort2(li, low, p-1)
        quickSort2(li, p+1, high)


def redixSort(li, bucket):
    """redix sort"""

    d = {}
    done = True

    for i in range(0, len(li)):
        bk = 1 * int(math.pow(10, bucket))
        pointer = int((li[i] / bk ) % 10)
        #print pointer

        if pointer != 0:
            done = False

        if d.get(pointer):
            temp = d[pointer]
            temp.append(li[i])
            d[pointer] = temp
        else:
            d[pointer] = [li[i]]

    k = 0
    for i in d.values():
        if i is not None:
            arr = i
            for l in arr:
                li[k] = l
                k += 1

    if done == True:
        return li

    m = redixSort(li, bucket + 1 )
    return m


def countSort(li):
    """count sort"""

    cs = [None] * 100

    for i in range(len(li)):

        if li[i] >= len(cs):
            cs = cs + ([None] * (li[i] - len(cs) / 2 ) )

        if li[i] < len(cs):
            pointer = li[i]
            get_arr = cs[pointer]
            if get_arr is not None:
                get_arr.append(pointer)
                cs[pointer] = get_arr
            else:
                cs[pointer] = [pointer]
    li = []
    for j in range(len(cs)):
        if cs[j] is not None:
            for k in cs[j]:
                li.append(k)

    return li


def heapify(li, i):
    """min heapify"""

    parent = (i - 1) / 2

    if parent >= 0:
        if li[i] < li[parent]:
            li[parent], li[i] = li[i], li[parent]
            heapify(li, parent)

    # else:
    #     return li



def heapSort(li):
    """heap sort"""

    for i in range(len(li)-1, -1, -1):
        heapify(li, i)

    print li

    arr = []
    while len(li) > 0:


        li[0], li[len(li) - 1] = li[len(li) - 1], li[0]
        arr.append(li[-1])

        lk = li[0:len(li) - 1]

        for i in range(len(lk) - 1, -1, -1):
            heapify(lk, i)

        li = lk


        # print li
        #
        # for i in range( (len(li) - (j+1) - 1 ), -1, -1):
        #     #print str(li[i]) + "---" + str(i)
        #     heapify(li, i)
        # print li
        #break

    print arr
import random
import math
from BT import Node

def biSearch(li, x, low, high):
    """this is binary search tree"""
    # if high - low < 2:
    #     return li[low] == x or li[high] == x
    mid = int((low + high) / 2)  #low + int((high - low)/2)

    if low == mid or low == high:
        return li[low] == x or li[high] == x

    if li[mid] == x:
        return True
    elif li[mid] > x:
        return biSearch(li, x, low, mid)
    elif li[mid] < x:
        return biSearch(li, x, mid, high)

def selectionSort(li):
    """selection sort"""
    for i in range(0,len(li)):
        for j in range(0,len(li)):
            if li[i] < li[j]:
                li[i], li[j] = li[j], li[i]
    print li


def bubbleSort(li):
    """bubble sort"""
    for i in range(0, len(li)):
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    print li


def insertionSort(li):
    """insertion sort"""
    for i in range(1, len(li)):
        temp = li[i]
        for j in range(i-1, -1, -1):
            if temp < li[j]:
                li[j+1], li[j] = li[j], li[j+1]

    print li


def shellSort(li):
    """shell sort"""
    gap = int(len(li) / 2)

    while gap > 0:

        for i in range(gap):

            for j in range(i + gap, len(li), gap):

                for k in range(j, -1, -gap):

                    if li[k] > li[j]:
                        li[k], li[j] = li[j], li[k]

        gap = int(gap / 2)


    print li


def merge(left, right):
    i,j =0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

    if i < len(left):
        for k in range(i, len(left)):
            result.append(left[k])

    if j < len(right):
        for k in range(j, len(right)):
            result.append(right[k])

    return result

def mergeSort(li):
    """merge sort"""

    #print li

    if len(li) < 2:
        return li[:]
    else:
        mid = int(len(li) / 2)
        left = mergeSort(li[:mid])
        right = mergeSort(li[mid:])
        return merge(left, right)


def quickSort(li):
    """quick sort"""

    if len(li) < 2:
        return li

    median = int(len(li)/2)

    left, right, eq = [], [], []
    for i in range(len(li)):
        if li[i] == li[median]:
            eq.append(li[i])
        elif li[i] < li[median]:
            left.append(li[i])
        else:
            right.append(li[i])

    return quickSort(left) + eq + quickSort(right)


def partition(li, low, high):
    """partitioning"""

    pivot = li[high]
    i = low - 1

    for j in range(low, high):

        if li[j] < pivot:
            i = i + 1
            li[j], li[i] = li[i], li[j]
    i = i + 1
    li[i], li[high] = li[high], li[i]

    return i




def quickSort2(li, low, high):
    """quick sort 2"""

    if low < high:
        p = partition(li, low, high)

        quickSort2(li, low, p-1)
        quickSort2(li, p+1, high)


def redixSort(li, bucket):
    """redix sort"""

    d = {}
    done = True

    for i in range(0, len(li)):
        bk = 1 * int(math.pow(10, bucket))
        pointer = int((li[i] / bk ) % 10)
        #print pointer

        if pointer != 0:
            done = False

        if d.get(pointer):
            temp = d[pointer]
            temp.append(li[i])
            d[pointer] = temp
        else:
            d[pointer] = [li[i]]

    k = 0
    for i in d.values():
        if i is not None:
            arr = i
            for l in arr:
                li[k] = l
                k += 1

    if done == True:
        return li

    m = redixSort(li, bucket + 1 )
    return m


def countSort(li):
    """count sort"""

    cs = [None] * 100

    for i in range(len(li)):

        if li[i] >= len(cs):
            cs = cs + ([None] * (li[i] - len(cs) / 2 ) )

        if li[i] < len(cs):
            pointer = li[i]
            get_arr = cs[pointer]
            if get_arr is not None:
                get_arr.append(pointer)
                cs[pointer] = get_arr
            else:
                cs[pointer] = [pointer]
    li = []
    for j in range(len(cs)):
        if cs[j] is not None:
            for k in cs[j]:
                li.append(k)

    return li


def heapify(li, i):
    """min heapify"""

    parent = (i - 1) / 2

    if parent >= 0:
        if li[i] < li[parent]:
            li[parent], li[i] = li[i], li[parent]
            heapify(li, parent)

    # else:
    #     return li



def heapSort(li):
    """heap sort"""

    for i in range(len(li)-1, -1, -1):
        heapify(li, i)

    heap = []
    j = 0
    while len(li) > 0:

        li[0], li[len(li) - 1] = li[len(li) - 1], li[0]
        heap.append(li[-1])
        li = li[0: (len(li) - 1)]
        for i in range(len(li) - 1, -1, -1):
            heapify(li, i)
    print heap


def hanoi(n, f, t, s):
    """
    tower of hanoi
    n number of stacks
    f from stack
    s spare stack
    t target stack
    """

    if n == 1:
        print "move " + " from " + f + " to " + t
    else:
        hanoi(n-1, f, s, t)
        hanoi(1, f, t, s)
        hanoi(n-1, s, t, f)


def fib(n):
    """fib expontional way"""
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

m = {1: 1, 2: 1}
def fibdp(n):
    """fib dp way"""

    if m.get(n):
        return m[n]
    else:
        mo = fib(n-1) + fib(n-2)
        m[n] = mo
        return mo

def fibdpBT(n):
    """fib dp bottom to top way start from minimal to solve larger"""
    mo = {1: 1, 2: 1}

    for i in range(3, n+1):
        k = mo[i-1] + mo[i-2]
        mo[i] = k

    return mo[n]

def palindom(s):
    """check if its palingdom or not"""
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindom(s[1:-1])
        else:
            return False



if __name__ == "__main__":

    li = [45, 56, 12, 5, 78, 123, 647, 1, 45, 3, 21]

    # li.sort()
    # fi = biSearch(li, 67, 0, len(li))
    # print fi

    #selectionSort(li)

    #bubbleSort(li)

    #insertionSort(li)

    #shellSort(li)

    # lk = mergeSort(li)
    # print lk

    # quickSort2(li, 0, len(li)-1)
    # print li

    # lk = redixSort(li, 0)
    # print lk

    # lk = countSort(li)
    # print lk

    #heapSort(li)

    #hanoi(3, 'f', 't', 's')

    # f = fib(40)
    # print f

    # f = fibdp(10)
    # print f
    #
    # f = fibdpBT(10)
    # print f

    # s = palindom("anafna")
    # print s

    #Binary search tree
    # n = Node(5)
    # n.insert(12)
    # n.insert(7)
    # n.insert(27)
    # n.insert(3)
    # n.insert(15)
    # n.printTree()
    # print n.search(2)

    avl = AVLTree()
    root = None
    root = avl.insert(root, 10)

    root = avl.insert(root, 20)
    root = avl.insert(root, 30)
    root = avl.insert(root, 40)
    root = avl.insert(root, 50)
    root = avl.insert(root, 25)

    avl.preOrder(root)






