# %% Factorial (Recursion)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# %% Generate Subsets (Backtracking)
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result

# %% Project 1: Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example: print(fibonacci(5))  # 5

# %% Project 2: N-Queens (Backtracking)
def n_queens(n):
    board = [['.'] * n for _ in range(n)]
    result = []
    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                return False
        return True
    
    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    backtrack(0)
    return result

# Example: print(n_queens(4))  # Solutions

# %% Project 3: Generate Parentheses
def generate_parentheses(n):
    result = []
    def backtrack(open_count, close_count, path):
        if open_count == close_count == n:
            result.append(path)
            return
        if open_count < n:
            backtrack(open_count + 1, close_count, path + '(')
        if close_count < open_count:
            backtrack(open_count, close_count + 1, path + ')')
    backtrack(0, 0, '')
    return result

# Example: print(generate_parentheses(2))  # ['(())', '()()']

# %% Project 4: Sudoku Solver
def solve_sudoku(board):
    def is_valid(row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == num:
                return False
        return True
    
    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in '123456789':
                        if is_valid(row, col, num):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = '.'
                    return False
        return True
    
    backtrack()
    return board

# Example: board = [['5','3','.'],['6','.','.'],['.','9','8']]; print(solve_sudoku(board))

# %% Project 5: Permutations
def permutations(nums):
    result = []
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(path)
                path.pop()
    backtrack([])
    return result

# Example: print(permutations([1,2]))  # [[1,2],[2,1]]