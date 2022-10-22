from lab8 import *
from min_heap import *

def prim1(self):
    if self.number_of_nodes() == 0:
        return self
        
    mst = WeightedGraph(self.number_of_nodes())
    marked = [False for _ in range(self.number_of_nodes())]
    marked[0] = True

    for _ in range(self.number_of_nodes() - 1):
        minWeight = 922337203685477580 

        for node in self.adj:
            if not marked[node]:

                for node1 in self.adj[node]:
                    u = node1[0]
                    w = node1[1]
                    if w < minWeight and marked[u]:
                        minWeight = w
                        newNode1 = node
                        newNode2 = u

        mst.add_edge(newNode1, newNode2, minWeight)
        marked[newNode1] = True

    return mst

def prim2(self):
    if self.number_of_nodes() == 0:
        return self
        
    val = 1001
    marked = [False for _ in range(self.number_of_nodes())]
    mst = WeightedGraph(self.number_of_nodes())
    edges = MinHeap([Element(node, val) for node in range(self.number_of_nodes())])
    
    while edges.is_empty() == False:
        edgesMin = edges.extract_min()
        marked[edgesMin.value] = True
        flag = False
        for node in self.adjacent_nodes(edgesMin.value):
            if marked[node[0]] == False:
                edges.decrease_key(node[0], node[1])
            elif flag == False and edgesMin.key == node[1]:
                mst.add_edge(node[0], edgesMin.value, edgesMin.key)
                flag = True

    return mst
    