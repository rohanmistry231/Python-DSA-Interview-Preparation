# %% Fibonacci Memoization
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# %% Fibonacci Tabulation
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# %% Project 1: 0/1 Knapsack (Tabulation)
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

# Example: print(knapsack([1,3,4],[1,4,5],7))  # 9

# %% Project 2: Longest Common Subsequence (Memoization)
def lcs(s1, s2, i=0, j=0, memo={}):
    key = (i, j)
    if key in memo:
        return memo[key]
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        memo[key] = 1 + lcs(s1, s2, i+1, j+1, memo)
    else:
        memo[key] = max(lcs(s1, s2, i+1, j, memo), lcs(s1, s2, i, j+1, memo))
    return memo[key]

# Example: print(lcs('abcde', 'ace'))  # 3

# %% Project 3: Coin Change (Tabulation)
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Example: print(coin_change([1,2,5], 11))  # 3

# %% Project 4: Edit Distance (Tabulation)
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

# Example: print(edit_distance('kitten', 'sitting'))  # 3

# %% Project 5: Longest Increasing Subsequence (Tabulation)
def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Example: print(lis([10,9,2,5,3,7,101,18]))  # 4