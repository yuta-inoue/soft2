import random
class Sort:
    def __init__(self):
        pass
    def bubble_sort(self, x):
        for i in xrange(len(x)):
            j = len(x) - 1
            while j > i:
                if x[j - 1] > x[j]:
                    x[j - 1], x[j] = x[j], x[j -1]
                j -= 1
    def selection_sort(self, x):
        for i in xrange(len(x)):
            mini = i
            for j in xrange(i + 1, len(x)):
                if x[j] < x[mini]:
                    mini = j
            if i != mini:
                x[i], x[mini] = x[mini], x[i]

    def quick_sort(self, x):
        self.__quicksort(x, 0, len(x) - 1)

    def __quicksort(self, x, left, right):
        pl = left
        pr = right
        y = x[(pl + pr) / 2]

        while True:
            while x[pl] < y: pl += 1
            while x[pr] > y: pr -= 1
            if pl <= pr:
                x[pl], x[pr] = x[pr], x[pl]
                pl += 1
                pr -= 1
            if pl > pr:
                break

        if left < pr: self.__quicksort(x, left, pr)
        if pl < right: self.__quicksort(x, pl, right)

    def heap_sort(self, x):
        for i in xrange((len(x) - 1) / 2, -1, -1):
            self.__downheap(x, i, len(x) - 1)

        for i in xrange(len(x) - 1, 0, -1):
            x[0], x[i] = x[i], x[0]
            self.__downheap(x, 0, i - 1)

    def __downheap(self, x, left, right):
        tmp = x[left]
        child = None
        parent = None

        parent = left
        while parent < (right + 1) / 2:
            cl = parent * 2 + 1
            cr = cl + 1
            if cr <= right and x[cr] > x[cl]:
                child = cr
            else:
                child = cl
            if tmp >= x[child]:
                break
            x[parent] = x[child]
            parent = child

        x[parent] = tmp

    def merge_sort(self, x):
        self.buff = [0 for i in xrange(len(x))]
        self.__mergesort(x, 0, len(x) - 1)

    def __mergesort(self, x, left, right):
        if left >= right: return

        center = (left + right) / 2
        self.__mergesort(x, left, center)
        self.__mergesort(x, center + 1, right)

        p = 0
        for i in xrange(left, center + 1):
            self.buff[p] = x[i]; p += 1

        i = center + 1
        j = 0
        k = left
        while i <= right and j < p:
            if self.buff[j] <= x[i]:
                x[k] = self.buff[j]; k += 1; j += 1
            else:
                x[k] = x[i]; k += 1; i += 1

        while j < p:
            x[k] = self.buff[j]; k += 1; j += 1
    def random_array(self):
        list = range(100)
        random.shuffle(list)
        return list

def print_list(list):
    for x in list:
        print(x)
