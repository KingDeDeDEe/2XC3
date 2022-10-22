import random
import timeit
import matplotlib.pyplot as plt

#Copy
def create_random_list(n, upper):
    return [random.randint(0, upper) for _ in range(n)]

ns = [10 * i for i in range(1000)]
ts = []
runs = 1000

for n in ns:
    arr1 = create_random_list(n, 1000)
    total = 0

    for _ in range(runs):
        start = timeit.default_timer()
        arr2 = arr1.copy()
        end = timeit.default_timer()

        total += (end - start)
    ts.append(total / runs)

plt.plot(ns, ts, '.', label='copy() runtime')
plt.xlabel("input length (n)")
plt.ylabel("time (t)")
plt.title("Performance of copy() over input size")
plt.legend(loc="upper left")
plt.show()

#Lookups
l = create_random_list(1000000, 1000)
lookups = []

for i in range(len(l)):
    start = timeit.default_timer()
    if l[i] in l:
        pass
    end = timeit.default_timer()
    lookups += [end - start]

plt.plot([i for i in range(1000000)], lookups, '.', label='lookups performance')
plt.xlabel('lookup index (n)')
plt.ylabel('time (t)')
plt.title("Performance of lookups on each index")
plt.legend(loc="upper left")
plt.show()

l = create_random_list(1000000, 1000)
lookups = []

for i in range(len(l)):
    start = timeit.default_timer()
    if l[i] == l[i]:
        pass
    end = timeit.default_timer()
    lookups += [end - start]

plt.plot([i for i in range(1000000)], lookups, '.', label='lookups performance')
plt.xlabel('lookup index (n)')
plt.ylabel('time (t)')
plt.title("Performance of lookups on each index")
plt.legend(loc="upper left")
plt.show()

#Append

ns = [i for i in range(1, 1000001)]
ts = []
runs = 100
ls = []

for i in range(1000000):
    total = 0
    start = timeit.default_timer()
    ls.append(i)
    end = timeit.default_timer()
    total += end - start
    ts.append(total)

plt.plot(ns, ts, '.', label='append() running time')
plt.xlabel("n")
plt.ylabel("time (t)")
plt.title("Performance of append()")
plt.legend(loc="upper left")
plt.show()
ts.clear()

# Experiment 1
for i in range(1000000):
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        ls.append(i)
        end = timeit.default_timer()
        total += end - start
        ls.pop()
    ls.append(i)
    ts.append(total / runs)

plt.plot(ns, ts, '.', label='append() running time')
plt.xlabel("n")
plt.ylabel("time (t)")
plt.title("Performance of append() (avg)")
plt.legend(loc="upper left")
plt.show()
ts.clear()

# Experiment 2
for _ in range(1000000):
    total = 0
    start = timeit.default_timer()
    ls.append(random.random())
    end = timeit.default_timer()
    total += end - start
    ts.append(total)

plt.plot(ns, ts, '.', label='append() running time')
plt.xlabel("n")
plt.ylabel("time (t)")
plt.title("Performance of append() with random elements")
plt.legend(loc="upper left")
plt.show()
ts.clear()

for _ in range(1000000):
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        ls.append(random.random())
        end = timeit.default_timer()
        total += end - start
        ls.pop()
    ls.append(random.random())
    ts.append(total / runs)

plt.plot(ns, ts, '.', label='append() running time')
plt.xlabel("n")
plt.ylabel("time (t)")
plt.title("Performance of append() with random elements (avg)")
plt.legend(loc="upper left")
plt.show()
ts.clear()

# Experiment 3
for _ in range(1000000):
    total = 0
    x = random.randint(0, len(ls) - 1)
    ls[x] = random.choice(ls)
    start = timeit.default_timer()
    ls.append(random.random())
    end = timeit.default_timer()
    total += end - start
    ts.append(total)

plt.plot(ns, ts, '.', label='append() running time')
plt.xlabel("n")
plt.ylabel("time (t)")
plt.title("Performance of append() using the elements")
plt.legend(loc="upper left")
plt.show()
