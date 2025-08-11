## Linked Lists

### Introduction
Linked lists are linear data structures where elements (nodes) are linked via pointers. Unlike arrays, they allow dynamic size and efficient insertions/deletions.

### Types
- **Singly Linked List**: Each node points to the next. Traversal is one-way.
- **Doubly Linked List**: Each node points to next and previous. Two-way traversal.
- **Circular Linked List**: Last node points back to first, forming a circle.

### Node Structure
- Data: Value stored.
- Pointer(s): To next (singly/circular), or next/previous (doubly).

### Operations
- Insertion: At beginning (O(1)), end (O(n) for singly, O(1) for doubly with tail), position (O(n)).
- Deletion: Similar complexities.
- Traversal: O(n).
- Search: O(n).

### Advantages
- Dynamic size.
- Efficient insertions/deletions.

### Disadvantages
- No random access.
- Extra memory for pointers.

### Applications
- Implementing stacks/queues.
- Music playlists (circular).
- Browser history (doubly).

### Time Complexities
- Access: O(n)
- Insert/Delete: O(1) at known position.