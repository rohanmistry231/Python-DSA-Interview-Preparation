# %% Stack Implementation Using List
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0

# %% Project 1: Balanced Parentheses Check
def is_balanced(parens):
    stack = Stack()
    for char in parens:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.pop() is None:
                return False
    return stack.is_empty()

# Example: print(is_balanced('()'))  # True

# %% Project 2: Reverse a String
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    reversed_s = ''
    while not stack.is_empty():
        reversed_s += stack.pop()
    return reversed_s

# Example: print(reverse_string('hello'))  # 'olleh'

# %% Project 3: Next Greater Element
def next_greater(nums):
    stack = Stack()
    result = [-1] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        while not stack.is_empty() and stack.peek() <= nums[i]:
            stack.pop()
        if not stack.is_empty():
            result[i] = stack.peek()
        stack.push(nums[i])
    return result

# Example: print(next_greater([4, 5, 2, 25]))  # [5, 25, 25, -1]

# %% Project 4: Convert Infix to Postfix
def infix_to_postfix(infix):
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = Stack()
    postfix = ''
    for char in infix:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while not stack.is_empty() and precedence.get(stack.peek(), 0) >= precedence[char]:
                postfix += stack.pop()
            stack.push(char)
    while not stack.is_empty():
        postfix += stack.pop()
    return postfix

# Example: print(infix_to_postfix('A+B*C'))  # 'ABC*+'

# %% Project 5: Evaluate Postfix Expression
def evaluate_postfix(postfix):
    stack = Stack()
    for char in postfix:
        if char.isdigit():
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+': stack.push(a + b)
            elif char == '-': stack.push(a - b)
            elif char == '*': stack.push(a * b)
            elif char == '/': stack.push(a / b)
    return stack.pop()

# Example: print(evaluate_postfix('231*+9-'))  # -4