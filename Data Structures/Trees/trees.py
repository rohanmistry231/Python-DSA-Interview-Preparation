# %% Binary Tree Node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# %% Binary Search Tree Insert
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(data)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(data)
                    break

# %% AVL Tree (Simplified Insert without Balance)
# Note: Full AVL needs rotation; this is basic

# %% Heap Using Heapq (Min Heap)
import heapq

heap = []

# %% Project 1: Inorder Traversal Binary Tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# Example: bst = BST(); bst.insert(2); bst.insert(1); inorder(bst.root)  # 1 2

# %% Project 2: Find Height of Binary Tree
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# Example: print(height(bst.root))  # 2

# %% Project 3: Check if BST
def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not min_val < root.data < max_val:
        return False
    return is_bst(root.left, min_val, root.data) and is_bst(root.right, root.data, max_val)

# Example: print(is_bst(bst.root))  # True

# %% Project 4: Kth Smallest in BST
def kth_smallest(root, k):
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.data
        root = root.right

# Example: bst.insert(3); print(kth_smallest(bst.root, 2))  # 2

# %% Project 5: Heap Sort Using Min Heap
def heap_sort(nums):
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]

# Example: print(heap_sort([3,1,4,1,5]))  # [1,1,3,4,5]