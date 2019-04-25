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


def primeNumber(n):
    """check prime number"""

    if n < 2:
        return False

    if n == 2:
        return True

    for i in range(2, int(math.sqrt(n)) + 1 ):
        if n % i == 0:
            return False
    return True

def denominator(x, y):
    """get the greatest denominator"""
    if x >= y:
        r = x - y
        if r == 0:
            return y
        elif r > y:
            return y
        else:
            return denominator(y, r)


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    memo = []

    if type(l1) == 'int' and type(l2) == 'int':
        memo.append(l1 + l2)
    elif type(l1) == 'int':
        memo.append(l1 + 0)
    elif type(l2) == 'int':
        memo.append(0 + l2)
    elif l1.val and l2.val:
        memo.append(l1.val + l2.val)
    elif l1.val:
        memo.append(l1.val + 0)
    elif l2.val:
        memo.append(0 + l2.val)

    if l1.next and l2.next:
        r = addTwoNumbers(l1.next, l2.next)
        if r:
            memo = memo + r
    elif l1.next and l2.next is None:
        r = addTwoNumbers(l1.next, 0)
        if r:
            memo = memo + r

    if l2.next and l1.next is None:
        r = addTwoNumbers(0, l2.next)
        if r:
            memo = memo + r

    k = 0
    for i in range(len(memo) - 1, -1, -1):

        if memo[i] >= 10:
            k = int(memo[i] / 10)
            memo[i] = (memo[i] % 10)
            if i - 1 > -1:
                memo[i - 1] = memo[i - 1] + k

    print memo

def checkPalingdom(s):
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return checkPalingdom(s[1:-1])
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

    # avl = AVLTree()
    # root = None
    # root = avl.insert(root, 10)
    # root = avl.insert(root, 20)
    # root = avl.insert(root, 30)
    # root = avl.insert(root, 40)
    # root = avl.insert(root, 50)
    # root = avl.insert(root, 25)
    # avl.preOrder(root)

    #print primeNumber(20)

    #print denominator(20, 16)

    # nums = [3, 2, 4]
    # target = 6
    #
    # memo = {}
    # for i in range(len(nums)):
    #     memo[nums[i]] = i
    #
    # print memo
    #
    # for i in range(len(nums)):
    #     x = target - nums[i]
    #     print x
    #     if x in memo and memo.get(x) != i:
    #         print [i, memo.get(x)]
    #         break

    # l1 = [2,4,3]
    # l2 = [5,6,4]
    # root2 = ListNode(2)

    # memo = [7,10,7]
    # for i in range(len(memo) - 1, -1, -1):
    #
    #     if memo[i] >= 10:
    #         k = int(memo[i] / 10)
    #         memo[i] = (memo[i] % 10)
    #         if i - 1 > -1:
    #             memo[i - 1] = memo[i - 1] + k
    #
    # print memo.reverse()
    # print memo
    #
    # v = 1
    # if type(v) == int:
    #     print "int"
    # else:
    #     print type(v)
    #
    #
    #
    # s = "sarangan"
    #
    # for i in range(len(s)):
    #     print s[i]
    # s = "au"
    # temp = ""
    # max_len = 0
    # if len(s) < 2:
    #     max_len = len(s)
    #
    #
    # for i in range(len(s)):
    #     memo = []
    #     print "------"
    #     for j in range(i, len(s)):
    #         if s[j] not in memo:
    #             memo.append(s[j])
    #         else:
    #             break
    #     if max_len < len(memo):
    #         temp = ''.join(memo)
    #         max_len = len(memo)
    #
    # print temp
    # print max_len

    # nums1 = [1,2]
    # nums2 = [3,4]
    #
    # i, j = 0, 0
    # temp = []
    # while i < len(nums1) and j < len(nums2):
    #     if nums1[i] < nums2[j]:
    #         temp.append(nums1[i])
    #         i += 1
    #     else:
    #         temp.append(nums2[j])
    #         j += 1
    # #print temp
    #
    # while i < len(nums1):
    #     temp.append(nums1[i])
    #     i += 1
    #
    # while j < len(nums2):
    #     temp.append(nums2[j])
    #     j += 1
    #
    #
    # #print (temp)
    # if len(temp) > 1:
    #
    #     if len(temp) % 2 == 0:
    #         #x_max = int(math.ceil(len(temp) / 2))
    #         x_min = int(math.floor(len(temp) / 2))
    #         #print x_min
    #
    #         print (temp[x_min] + temp[x_min - 1]) / 2.0
    #     else:
    #         middle = int(math.ceil(len(temp) / 2))
    #         print temp[middle]
    #
    # else:
    #     print temp[0]

    # s = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    # max_len = 0
    # palin = ""
    #
    # memo = set()
    #
    # if len(s) < 3:
    #     if len(s) < 3:
    #         if len(s) == 0:
    #             print ""
    #         elif len(s) == 1:
    #             print s
    #         elif len(s) == 2:
    #             if s[0] == s[-1]:
    #                 print s
    #             else:
    #                 print s[0:1]
    # else:
    #
    #     for i in range(len(s)):
    #
    #         for j in range(i, len(s)):
    #
    #             #print s[i:j+1]
    #
    #             if s[i:j + 1] in memo:
    #                 k = True
    #
    #             else:
    #                 k = checkPalingdom(s[i:j + 1])
    #
    #             if k == True:
    #                 memo.add(s[i:j + 1])
    #             if k == True and len(s[i:j + 1]) > max_len:
    #                 max_len = len(s[i:j + 1])
    #                 palin = s[i:j + 1]
    #
    #     print palin

    s = "ABC"
    words = []
    temp = []
    numRows = 2
    middle_max = numRows - 2
    middle_pointer = 0
    switch_column = False

    for i in range(len(s)):


        if len(temp) < numRows and not switch_column:
            temp.append(s[i])

        if len(temp) == numRows and not switch_column:
            words.append(temp)
            temp = []
            switch_column = True
            continue

        if len(temp) < middle_max and switch_column:
            temp.append(s[i])

        if len(temp) == middle_max and switch_column:
            words.append(temp)
            temp = []
            switch_column = False
            continue

    if len(temp) > 0:
        words.append(temp)

    # print len(s)
    print words
    print "--------"
    # x =[('').join(word) for word in words]
    # print ('').join(x)
    co_str = ''

    for i in range(len(words)):
        for j in range(len(words)):
            if i == 0 or i == len(words):
                if i < len(words[j]) and j % 2 == 0:
                    co_str += words[j][i]
            elif i > 0:
                if j % 2 == 1 and len(words[j]) > 0:
                    co_str += words[j].pop()
                elif i < len(words[j]):
                    co_str += words[j][i]

    print co_str

    print "ACB"