import random
import matplotlib.pyplot as plt
from lab8 import *
from mst import *
import timeit

def create_random_graph(k):
    g  = WeightedGraph(k)
    L = random.sample(range(k), k)
    for i in range(k-1):
        g.add_edge(L[i],L[i+1],random.randint(1,100))
    for _ in range(k):
        g.add_edge(L[random.randint(0,k-1)],L[random.randint(0,k-1)],random.randint(1,100))
    return g

def test(function, name):
    ns = [i for i in range(1, 1001)]
    ts = []

    for i in range(1000):
        g = create_random_graph(i)
        start = timeit.default_timer()
        function(g)
        end = timeit.default_timer()
        ts.append(end - start)
    plt.plot(ns, ts, '.', label=name)
    ts.clear() 

g = create_random_graph(4)
p1 = prim1(g)
p2 = prim2(g)

print(g.adj)
print(p1.adj)
print(p2.adj)

test(prim1, "Prim v1")
test(prim2, "Prim v2")
plt.xlabel("size of graph (n)")
plt.ylabel("time (t)")
plt.title("Performance of Prim methods")
plt.legend(loc="upper left")
plt.show()