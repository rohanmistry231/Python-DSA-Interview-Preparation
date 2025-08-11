# %% Graph Using Adjacency List (Undirected)
class Graph:
    def __init__(self):
        self.adj = {}
    
    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []
    
    def add_edge(self, u, v, weight=None):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))  # Undirected

# For Directed: Remove self.adj[v].append

# For Weighted: Use weight

# %% BFS Traversal
from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for neighbor, _ in graph.adj[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

# %% Project 1: Find Path Exists
def path_exists(graph, start, end):
    visited = set()
    stack = [start]
    while stack:
        v = stack.pop()
        if v == end:
            return True
        if v not in visited:
            visited.add(v)
            stack.extend([n for n, _ in graph.adj[v] if n not in visited])
    return False

# Example: g = Graph(); g.add_edge(1,2); print(path_exists(g,1,2))  # True

# %% Project 2: Count Connected Components (Undirected)
def count_components(graph):
    visited = set()
    count = 0
    for v in graph.adj:
        if v not in visited:
            dfs(graph, v, visited)
            count += 1
    return count

def dfs(graph, v, visited):
    visited.add(v)
    for neighbor, _ in graph.adj[v]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example: g.add_edge(3,4); print(count_components(g))  # 2

# %% Project 3: Shortest Path BFS (Unweighted)
def shortest_path(graph, start, end):
    q = deque([(start, 0)])
    visited = set([start])
    while q:
        v, dist = q.popleft()
        if v == end:
            return dist
        for neighbor, _ in graph.adj[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, dist + 1))
    return -1

# Example: print(shortest_path(g,1,2))  # 1

# %% Project 4: Detect Cycle in Directed Graph
def has_cycle(graph):
    visited = set()
    rec_stack = set()
    for v in graph.adj:
        if v not in visited:
            if dfs_cycle(graph, v, visited, rec_stack):
                return True
    return False

def dfs_cycle(graph, v, visited, rec_stack):
    visited.add(v)
    rec_stack.add(v)
    for neighbor, _ in graph.adj[v]:
        if neighbor not in visited:
            if dfs_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True
    rec_stack.remove(v)
    return False

# Example: dg = Graph(); dg.add_edge(1,2); dg.add_edge(2,1, directed=True); print(has_cycle(dg))  # True (modify add_edge for directed)

# Note: Adjust add_edge for directed by removing bidirectional.

# %% Project 5: Topological Sort (Directed Acyclic)
def topological_sort(graph):
    visited = set()
    stack = []
    for v in graph.adj:
        if v not in visited:
            dfs_topo(graph, v, visited, stack)
    return stack[::-1]

def dfs_topo(graph, v, visited, stack):
    visited.add(v)
    for neighbor, _ in graph.adj[v]:
        if neighbor not in visited:
            dfs_topo(graph, neighbor, visited, stack)
    stack.append(v)

# Example: dag = Graph(); dag.add_edge(1,2); dag.add_edge(2,3); print(topological_sort(dag))  # [1,2,3]