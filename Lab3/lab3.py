import random
import math
import timeit
import matplotlib.pyplot as plt

def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

def dual_pivot_quicksort(L):
    n = len(L)
    if n <= 1:
        return L 
    elif n == 2: 
        return sorted(L)
    
    pivot1, pivot2 = sorted([L.pop(0), L.pop(0)])
    a = []
    b = []
    c = []
    for element in L:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element < pivot2:
            b.append(element)
        else:
            c.append(element)
    return dual_pivot_quicksort(a) + [pivot1] + dual_pivot_quicksort(b) + [pivot2] + dual_pivot_quicksort(c)


def tri_pivot_quicksort(L):
    n = len(L)
    if n <= 1:
        return L 
    elif n == 2: 
        return sorted(L)
    
    pivot1, pivot2, pivot3 = sorted([L.pop(0), L.pop(0), L.pop(0)])
    a = []
    b = []
    c = []
    d = []
    for element in L:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element < pivot2:
            b.append(element)
        elif pivot2 <= element < pivot3:
            c.append(element)
        else:
            d.append(element)
    return tri_pivot_quicksort(a) + [pivot1] + tri_pivot_quicksort(b) + [pivot2] + tri_pivot_quicksort(c) + [pivot3] + tri_pivot_quicksort(d)

def quad_pivot_quicksort(l):
    n = len(l)
    if n <= 1:
        return l
    elif n == 2 or n == 3:
        return sorted(l)

    pivot1, pivot2, pivot3, pivot4 = sorted([l.pop(0), l.pop(0), l.pop(0), l.pop(0)])
    a = []
    b = []
    c = []
    d = []
    e = []
    for element in l:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element < pivot2:
            b.append(element)
        elif pivot2 <= element < pivot3:
            c.append(element)
        elif pivot3 <= element < pivot4:
            d.append(element)
        else:
            e.append(element)
    return quad_pivot_quicksort(a) + [pivot1] + quad_pivot_quicksort(b) + [pivot2] + quad_pivot_quicksort(c) + [
        pivot3] + quad_pivot_quicksort(d) + [pivot4] + quad_pivot_quicksort(e)


def create_random_list(n):
    l = []
    for _ in range(n):
        l.append(random.randint(1, n))
    return l


def create_near_sorted_list(n, factor):
    l= create_random_list(n)
    l.sort()
    for _ in range(math.ceil(n * factor)):
        index1 = random.randint(0, n - 1)
        index2 = random.randint(0, n - 1)
        l[index1], l[index2] = l[index2], l[index1]
    return l

def test(function,name):
    ns = [i for i in range(1, 10001)]
    ts = []

    for i in range(10000):
        L = create_random_list(i)
        copy = L.copy()
        start = timeit.default_timer()
        L = function(L)
        end = timeit.default_timer()
        ts.append(end - start)
        copy.sort()
        assert(L == copy)

    plt.plot(ns, ts, '.', label= name)
    ts.clear()

test(quicksort_copy, "Quicksort")   
test(dual_pivot_quicksort, "Dual Pivot Quicksort")   
test(tri_pivot_quicksort, "Tri Pivot Quicksort")
test(quad_pivot_quicksort, "Quad Pivot Quicksort")
plt.xlabel("size of list (n)")
plt.ylabel("time (t)")
plt.title("Performance of functions")
plt.legend(loc="upper left")
plt.show()