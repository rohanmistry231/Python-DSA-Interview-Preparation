# %% Simple Queue Using List
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0

# %% Priority Queue Using Heapq
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))
    
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

# %% Deque Using Collections
from collections import deque

dq = deque()

# %% Project 1: Implement Circular Queue
class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = self.rear = -1
        self.size = size
    
    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            return  # Full
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.front == -1:
            return None  # Empty
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

# Example: cq = CircularQueue(3); cq.enqueue(1); print(cq.dequeue())  # 1

# %% Project 2: Generate Binary Numbers Using Queue
def generate_binary(n):
    q = Queue()
    q.enqueue('1')
    result = []
    for _ in range(n):
        binary = q.dequeue()
        result.append(binary)
        q.enqueue(binary + '0')
        q.enqueue(binary + '1')
    return result

# Example: print(generate_binary(3))  # ['1', '10', '11']

# %% Project 3: Sliding Window Maximum Using Deque
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []
    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

# Example: print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]

# %% Project 4: Job Scheduling with Priority Queue
def schedule_jobs(jobs):
    pq = PriorityQueue()
    for job, pri in jobs:
        pq.push(job, pri)
    schedule = []
    while pq.heap:
        schedule.append(pq.pop())
    return schedule

# Example: jobs = [('Job1', 2), ('Job2', 1)]; print(schedule_jobs(jobs))  # ['Job2', 'Job1']

# %% Project 5: Reverse First K Elements of Queue
def reverse_k(q, k):
    stack = Stack()
    for _ in range(k):
        stack.push(q.dequeue())
    while not stack.is_empty():
        q.enqueue(stack.pop())
    for _ in range(len(q.items) - k):
        q.enqueue(q.dequeue())

# Example: q = Queue(); [q.enqueue(i) for i in [1,2,3,4]]; reverse_k(q, 3); print(q.items)  # [3,2,1,4]