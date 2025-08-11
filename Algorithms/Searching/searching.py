# %% Linear Search
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# %% Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# %% DFS (Graph)
def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == target:
        return True
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False

# %% BFS (Graph)
from collections import deque
def bfs(graph, start, target):
    visited = set()
    q = deque([start])
    visited.add(start)
    while q:
        current = q.popleft()
        if current == target:
            return True
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return False

# %% Project 1: Find All Occurrences (Linear Search)
def find_all_occurrences(arr, target):
    return [i for i, val in enumerate(arr) if val == target]

# Example: print(find_all_occurrences([1,2,2,3], 2))  # [1,2]

# %% Project 2: Search in Rotated Sorted Array (Binary Search Variant)
def search_rotated(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# Example: print(search_rotated([4,5,6,7,0,1,2], 0))  # 4

# %% Project 3: Word Search in Grid (DFS)
def word_search(grid, word):
    def dfs(i, j, index):
        if index == len(word):
            return True
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[index]:
            return False
        temp = grid[i][j]
        grid[i][j] = '#'
        found = (dfs(i+1, j, index+1) or dfs(i-1, j, index+1) or
                 dfs(i, j+1, index+1) or dfs(i, j-1, index+1))
        grid[i][j] = temp
        return found
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dfs(i, j, 0):
                return True
    return False

# Example: grid = [['A','B','C'],['D','E','F']]; print(word_search(grid, 'ABE'))  # True

# %% Project 4: Shortest Path in Maze (BFS)
def shortest_path_maze(maze, start, end):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    rows, cols = len(maze), len(maze[0])
    visited = set()
    q = deque([(start, 0)])
    visited.add(start)
    while q:
        (x, y), dist = q.popleft()
        if (x, y) == end:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(((nx, ny), dist + 1))
    return -1

# Example: maze = [[0,1],[0,0]]; print(shortest_path_maze(maze, (0,0), (1,1)))  # 2

# %% Project 5: Find Peak Element (Binary Search)
def find_peak(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return arr[low]

# Example: print(find_peak([1,2,1,3,5,6,4]))  # 2 or 6