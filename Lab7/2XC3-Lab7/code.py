from graphs import *
import random
import matplotlib.pyplot as plt


def create_random_graph(k,c):
    g  = Graph(k)
    for _ in range(c):
        r = random.sample(range(k), 2)
        g.add_edge(r[0], r[1])
    return g

def test(function, name):
    ns = [i for i in range(420)]
    ts = []

    for i in range (420):
        total = 0
        for _ in range(100):
            g = create_random_graph(100,i)
            total += function(g)
        ts.append(total/100)

    plt.plot(ns, ts, '.', label=name)
    ts.clear() 

g = Graph(7)

g.add_edge(6,4)
g.add_edge(4,3)
g.add_edge(4,5)
g.add_edge(4,2)
g.add_edge(5,3)
g.add_edge(2,1)
g.add_edge(3,1)

print(BFS2(g, 1, 4))
print(BFS2(g, 4, 1))

print(DFS2(g, 1, 4))
print(BFS3(g, 1))
print(DFS3(g, 1))
print(DFS2(g, 3, 3))

print(has_cycle(g))

test(has_cycle, "has_cycle")
plt.ylabel("Percentage of graphs with cycle (k=100)")
plt.xlabel("c (num of edges)")
plt.title("has_cycle")
plt.show()

test(is_connected, "is_connected")
plt.ylabel("Percentage of graphs that are connected (k=100)")
plt.xlabel("c (num of edges)")
plt.title("is_connected")
plt.show()