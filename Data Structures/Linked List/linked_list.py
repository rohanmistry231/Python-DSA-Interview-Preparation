# %% Singly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# %% Singly Linked List Class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

# %% Doubly Linked List Node
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# %% Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')

# %% Circular Linked List Class (Singly Based)
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head
    
    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=' -> ')
            current = current.next
            if current == self.head:
                break
        print('(back to head)')

# %% Project 1: Reverse a Singly Linked List
def reverse_sll(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example: sll = SinglyLinkedList(); sll.append(1); sll.append(2); new_head = reverse_sll(sll.head)

# %% Project 2: Detect Cycle in Circular Linked List
def has_cycle(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

# Example: cll = CircularLinkedList(); cll.append(1); cll.append(2); print(has_cycle(cll.head))

# %% Project 3: Merge Two Sorted Doubly Linked Lists
def merge_dll(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.data < head2.data:
        head1.next = merge_dll(head1.next, head2)
        head1.next.prev = head1
        head1.prev = None
        return head1
    else:
        head2.next = merge_dll(head1, head2.next)
        head2.next.prev = head2
        head2.prev = None
        return head2

# Example: dll1 = DoublyLinkedList(); dll1.append(1); dll2 = DoublyLinkedList(); dll2.append(2); merged = merge_dll(dll1.head, dll2.head)

# %% Project 4: Find Middle of Singly Linked List
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None

# Example: sll = SinglyLinkedList(); sll.append(1); sll.append(2); sll.append(3); print(find_middle(sll.head))

# %% Project 5: Remove Duplicates from Singly Linked List
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Example: sll = SinglyLinkedList(); sll.append(1); sll.append(1); sll.append(2); remove_duplicates(sll.head)