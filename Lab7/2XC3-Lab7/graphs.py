from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)

#Breadth First Search
def BFS2(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    nodes = {node1 : [node1]}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return nodes[current_node] + [node]
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                nodes[node] = nodes[current_node] + [node]
    return []

#Depth First Search
def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    nodes = {node1 : [node1]}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if not marked[node]:
                    nodes[node] = nodes[current_node] + [node]
                if node == node2:
                    return nodes[current_node] + [node]
                S.append(node)
    return []

#Breadth First Search
def BFS3(G, node1):
    Q = deque([node1])
    marked = {node1 : True}
    predecessor = {}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                if node not in predecessor:
                    predecessor[node] = current_node
    return predecessor

#Depth First Search
def DFS3(G, node1):
    S = [node1]
    marked = {}
    predecessor = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                S.append(node)
                if node not in predecessor and node != node1:
                    predecessor[node] = current_node
    return predecessor

def has_cycle(G):
    nodes =  list(G.adj.keys())
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(nodes) != 0:
        node1 = nodes.pop()
        while marked[node1]: # if its alr been visted go to the next one
            if len(nodes) == 0:
                break
            node1 = nodes.pop()
        S = [(node1,-1)]
        while len(S) != 0:
            current_node = S.pop()
            if not marked[current_node[0]]:
                marked[current_node[0]] = True
                for node in G.adj[current_node[0]]:
                    if current_node[1] != node:
                        S.append((node,current_node[0]))
            else:
                return True
    return False

def is_connected(G):
    if G.number_of_nodes() == 0 or len(DFS3(G, next(iter(G.adj.keys())))) + 1 < G.number_of_nodes():
        return False
    else:
        return True
