## Disjoint Set Union (DSU)

### Introduction
DSU (Union-Find) manages disjoint sets with union and find ops.

### Implementation
- Array for parents/ranks.
- Path compression, union by rank.

### Operations
- Find: O(α(n)) ~ O(1)
- Union: O(α(n))

### Advantages
- Fast set operations.

### Disadvantages
- Only for disjoint sets.

### Applications
- Kruskal's MST.
- Connected components.

### Time Complexities
- Amortized O(1)