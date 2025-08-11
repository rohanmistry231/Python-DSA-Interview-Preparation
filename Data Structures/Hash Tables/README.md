## Hash Tables

### Introduction
Hash table stores key-value pairs using hash function for fast access.

### Implementation
- Array of buckets; hash(key) % size = index.
- Handle collisions: chaining (linked lists) or open addressing.

### Operations
- Insert: O(1) average
- Delete: O(1) average
- Search: O(1) average

### Advantages
- Fast lookups.

### Disadvantages
- Collisions degrade to O(n).
- Memory overhead.

### Applications
- Dictionaries.
- Caches.
- Databases.

### Time Complexities
- Average: O(1), Worst: O(n)