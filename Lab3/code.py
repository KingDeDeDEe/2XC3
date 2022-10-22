from cgitb import small
import random
import math
from re import L
import timeit
from typing import final
import matplotlib.pyplot as plt
import statistics

#function from lab3.py
def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]
    return L

#function from lab3.py
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

#function from week 3 sorts.py
def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

#function from week 3 sorts.py
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

#function from week 3 sorts.py
def bubble_sort_opt1(L):
    for i in range(len(L)):
        for j in range(len(L) - 1 - i):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

#function from week 3 sorts.py
def bubble_sort_opt2(L):
    for i in range(len(L)):
        swaps = 0
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                swaps += 1
        if swaps == 0:
            return

#function from week 3 sorts.py
def bubble_sort_opt3(L):
    for i in range(len(L)):
        swaps = 0
        for j in range(len(L) - 1 - i):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                swaps += 1
        if swaps == 0:
            return

#function from week 3 sorts.py
def insertion_sort(L):
    for i in range(1, len(L)):
        insert_into(L, i)

#function from week 3 sorts.py
def insert_into(L, n):
    i = n
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i, i-1)
        else:
            return
        i -= 1

#function from week 3 sorts.py
def selection_sort(L):
    for i in range(len(L)):
        mindex = find_min_index(L, i)
        swap(L, i, mindex)

#function from week 3 sorts.py
def find_min_index(L, n):
    mindex = n
    for i in range(n+1, len(L)):
        if L[i] < L[mindex]:
            mindex = i
    return mindex


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

def quad_pivot_quicksort(L):
    n = len(L)
    if n <= 1:
        return L
    elif n == 2 or n == 3:
        return sorted(L)

    pivot1, pivot2, pivot3, pivot4 = sorted([L.pop(0), L.pop(0), L.pop(0), L.pop(0)])
    a = []
    b = []
    c = []
    d = []
    e = []
    for element in L:
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
    return quad_pivot_quicksort(a) + [pivot1] + quad_pivot_quicksort(b) + [pivot2] + quad_pivot_quicksort(c) + [pivot3] + quad_pivot_quicksort(d) + [pivot4] + quad_pivot_quicksort(e)



#function from lab3.py
def create_random_list(length, upper):
    return [random.randint(0,upper) for _ in range(length)]

def create_near_sorted_list(n, factor):
    L = create_random_list(n, n)
    L.sort()
    for _ in range(math.ceil(n * factor)):
        r1 = random.randint(0, n - 1)
        r2 = random.randint(0, n - 1)
        swap(L, r1, r2)
    return L

def quicksort_inplace(L):
    if len(L) < 2:
        return L
    pivot = L[0]

    left = []
    right = []
    for n in L[1:]:
        if n < pivot:
            left.append(n)
        else:
            right.append(n)
    
    return quicksort_inplace(left) + [pivot] + quicksort_inplace(right)
    

def test_in_place(function):
    total = 0
    for i in range(100):
        L = create_random_list(i, 1000)
        copy = L.copy()
        start = timeit.default_timer()
        L = function(L)
        end = timeit.default_timer()
        total += end - start
        copy.sort()

    return total / 100

def test(function,name, factor):
    ns = [i for i in range(1, 1001)]
    ts = []

    for i in range(1000):
        L = create_near_sorted_list(i,factor)
        start = timeit.default_timer()
        function(L)
        end = timeit.default_timer()
        ts.append(end - start)
    plt.plot(ns, ts, '.', label=name)
    ts.clear()

def test1(function,name):
    ns = [i for i in range(1, 1001)]
    ts = []

    for i in range(1000):
        L = create_random_list(i,1000000)
        start = timeit.default_timer()
        function(L)
        end = timeit.default_timer()
        ts.append(end - start)
    plt.plot(ns, ts, '.', label=name)
    ts.clear() 

def test3(function, name):
    ns = [i/1000 for i in range(1, 1001)]
    ts = []

    for i in range(1000):
        L = create_near_sorted_list(1000,i/1000)
        start = timeit.default_timer()
        function(L)
        end = timeit.default_timer()
        ts.append(end - start)
    plt.plot(ns, ts, '.', label=name)
    ts.clear()


def small_lists_test(function, name):
    ns = [i for i in range(1, 51)]
    ts = []

    for i in range(50):
        L = create_random_list(i, 50)
        start = timeit.default_timer()
        function(L)
        end = timeit.default_timer()
        ts.append(end - start)
    plt.plot(ns, ts, '.', label=name)
    ts.clear()

print("In place quicksort is faster by: " + str(test_in_place(my_quicksort) - test_in_place(quicksort_inplace)) + " seconds")

# # Testing fastest quicksort
# test1(quicksort_copy, "Quicksort")   
# test1(dual_pivot_quicksort, "Dual Pivot Quicksort")   
# test1(tri_pivot_quicksort, "Tri Pivot Quicksort")
# test1(quad_pivot_quicksort, "Quad Pivot Quicksort")
# plt.xlabel("size of list (n)")
# plt.ylabel("time (t)")
# plt.title("Performance of functions")
# plt.legend(loc="upper left")
# plt.show()

# #testing qucicksort worstcase vs avg case
# test(quad_pivot_quicksort, "Worstcase", 0)
# test1(quad_pivot_quicksort, "Averagecase")
# plt.xlabel("size of list (n)")
# plt.ylabel("time (t)")
# plt.title("Performance of Quicksort")
# plt.legend(loc="upper left")
# plt.show()

# # Testing sorts with factor 0
# test(quad_pivot_quicksort, "Quad Pivot Quicksort", 0)
# test(insertion_sort, "Insertion sort", 0)
# test(bubble_sort_opt3, "Bubble sort", 0)
# test(selection_sort, "Selection sort", 0)
# plt.xlabel("size of list (n)")
# plt.ylabel("time (t)")
# plt.title("Performance of sorts with almost sorted arrays (factor 0) ")
# plt.legend(loc="upper left")
# plt.show()

# # Testing sorts with factor 0.025
# test(quad_pivot_quicksort, "Quad Pivot Quicksort", 0.025)
# test(insertion_sort, "Insertion sort", 0.025)
# test(bubble_sort_opt3, "Bubble sort", 0.025)
# test(selection_sort, "Selection sort", 0.025)
# plt.xlabel("size of list (n)")
# plt.ylabel("time (t)")
# plt.title("Performance of sorts with almost sorted arrays (factor 0.025) ")
# plt.legend(loc="upper left")
# plt.show()

# # Testing sorts against different factors
# test3(quad_pivot_quicksort, "Quad Pivot Quicksort")
# test3(insertion_sort, "Insertion sort")
# test3(bubble_sort_opt3, "Bubble sort")
# test3(selection_sort, "Selection sort")
# plt.xlabel("factor")
# plt.ylabel("time (t)")
# plt.title("Performance of sorts")
# plt.legend(loc="upper left")
# plt.show()

#Small Lists testing
small_lists_test(bubble_sort, "Bubble Sort")
small_lists_test(insertion_sort, "Insertion Sort")
small_lists_test(selection_sort, "Selection Sort")
small_lists_test(quad_pivot_quicksort, "Quad Pivot Quicksort")
plt.xlabel("size of list (n)")
plt.ylabel("time (t)")
plt.title("Performance of sorts with small list size (10) ")
plt.legend(loc="upper left")
plt.show()

def final_sort(L):

    length = len(L)
    if length < 2:
        return L

    pivot = L[len(L)//2]
    L.remove(pivot)
    left = []
    right = []
    for n in L:
        if n < pivot:
            left.append(n)
        else:
            right.append(n)
    
    return final_sort(left) + [pivot] + final_sort(right)


def test_small_list_worstcase(function, name):
    ns = [i for i in range(1, 51)]
    ts = []

    for i in range(50):
        L = create_near_sorted_list(i,0)
        start = timeit.default_timer()
        function(L)
        end = timeit.default_timer()
        ts.append(end - start)
    plt.plot(ns, ts, '.', label=name)
    ts.clear()

test_small_list_worstcase(final_sort, "Final Sort")
test_small_list_worstcase(quicksort_inplace, "In Place Quicksort")
plt.xlabel("size of list (n)")
plt.ylabel("time (t)")
plt.title("Performance of Final Sort")
plt.legend(loc="upper left")
plt.show()