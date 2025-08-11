## Queues

### Introduction
Queue is a FIFO (First In, First Out) data structure. Operations: enqueue (add), dequeue (remove), front (peek).

### Types
- **Simple Queue**: Basic FIFO.
- **Priority Queue**: Elements with priorities; highest first.
- **Deque**: Double-ended queue; add/remove from both ends.

### Implementation
- Arrays, linked lists, or Python's collections.deque/heapq.

### Operations
- Enqueue: O(1)
- Dequeue: O(1) for linked/deque, O(n) for array.
- Front: O(1)

### Advantages
- Efficient for FIFO needs.

### Disadvantages
- Fixed size in arrays.

### Applications
- Task scheduling.
- BFS in graphs.
- Buffers.

### Time Complexities
- Basic ops: O(1)