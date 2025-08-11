# %% Dijkstra
import heapq
def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        dist, u = heapq.heappop(pq)
        if dist > distances[u]:
            continue
        for v, weight in graph[u]:
            new_dist = dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    return distances

# %% BFS/DFS (From earlier)
# See searching.py

# %% Topological Sort
def topological_sort(graph):
    visited = set()
    stack = []
    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]

# %% Project 1: Shortest Path in Weighted Graph (Dijkstra)
# Example: graph = {'A':[('B',1),('C',4)]}; print(dijkstra(graph, 'A'))

# %% Project 2: Connected Components (DFS)
def connected_components(graph):
    visited = set()
    components = []
    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)
    return components

# Example: graph = {1:[2],3:[]}; print(connected_components(graph))

# %% Project 3: Level Order Traversal (BFS on Tree)
from collections import deque
def level_order(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result

# Example: Assume TreeNode class

# %% Project 4: Course Schedule (Topological Sort)
def can_finish(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for course, pre in prerequisites:
        graph[pre].append(course)
    return len(topological_sort(graph)) == num_courses

# Example: print(can_finish(2, [[1,0]]))  # True

# %% Project 5: Minimum Spanning Tree (Prim's - Similar to Dijkstra)
def mst_prim(graph, start):
    mst = []
    visited = set()
    pq = [(0, start, None)]
    while pq:
        weight, u, parent = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if parent is not None:
            mst.append((parent, u, weight))
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (w, v, u))
    return mst

# Example: graph = {'A':[('B',1),('C',3)]}; print(mst_prim(graph, 'A'))