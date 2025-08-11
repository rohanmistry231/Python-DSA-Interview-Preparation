# %% DSU Class
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

# %% Project 1: Detect Cycle in Undirected Graph
def detect_cycle(edges, n):
    dsu = DSU(n)
    for u, v in edges:
        if not dsu.union(u, v):
            return True
    return False

# Example: print(detect_cycle([(0,1),(1,2),(2,0)], 3))  # True

# %% Project 2: Number of Provinces (Connected Components)
def num_provinces(connections):
    n = len(connections)
    dsu = DSU(n)
    for i in range(n):
        for j in range(i+1, n):
            if connections[i][j]:
                dsu.union(i, j)
    return len(set(dsu.find(i) for i in range(n)))

# Example: print(num_provinces([[1,1,0],[1,1,0],[0,0,1]]))  # 2

# %% Project 3: Accounts Merge
def accounts_merge(accounts):
    dsu = DSU(len(accounts))
    email_to_id = {}
    for i, acc in enumerate(accounts):
        for email in acc[1:]:
            if email in email_to_id:
                dsu.union(i, email_to_id[email])
            email_to_id[email] = i
    merged = {}
    for email, id in email_to_id.items():
        root = dsu.find(id)
        merged.setdefault(root, set()).add(email)
    return [[accounts[root][0]] + sorted(merged[root]) for root in merged]

# Example: acc = [['John','j1','j2'],['John','j3']]; print(accounts_merge(acc))

# %% Project 4: Redundant Connection
def redundant_connection(edges):
    dsu = DSU(len(edges) + 1)
    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]
    return []

# Example: print(redundant_connection([[1,2],[1,3],[2,3]]))  # [2,3]

# %% Project 5: Satisfiability of Equality Equations
def equations_possible(equations):
    dsu = DSU(26)
    for eq in equations:
        if eq[1] == '=':
            a, b = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
            dsu.union(a, b)
    for eq in equations:
        if eq[1] == '!':
            a, b = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
            if dsu.find(a) == dsu.find(b):
                return False
    return True

# Example: print(equations_possible(['a==b','b!=a']))  # False