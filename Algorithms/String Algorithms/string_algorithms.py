# %% KMP
def kmp(text, pattern):
    def compute_lps(pat):
        lps = [0] * len(pat)
        length = 0
        i = 1
        while i < len(pat):
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# %% Rabin-Karp
def rabin_karp(text, pattern, prime=101):
    n, m = len(text), len(pattern)
    if m > n:
        return -1
    p_hash = t_hash = 0
    h = 1
    for i in range(m - 1):
        h = (h * 256) % prime
    for i in range(m):
        p_hash = (256 * p_hash + ord(pattern[i])) % prime
        t_hash = (256 * t_hash + ord(text[i])) % prime
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            t_hash = (256 * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime
    return -1

# %% Project 1: Longest Palindromic Substring
def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = max_len = 0
    for i in range(n):
        dp[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2 and s[i] == s[j]:
                dp[i][j] = True
            elif s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
            if dp[i][j] and length > max_len:
                start = i
                max_len = length
    return s[start:start + max_len]

# Example: print(longest_palindrome('babad'))  # 'bab'

# %% Project 2: String Matching with Wildcards
def wildcard_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif p[j-1] == '?' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[m][n]

# Example: print(wildcard_match('aa', 'a*'))  # True

# %% Project 3: Longest Repeating Subsequence
def longest_repeating(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]

# Example: print(longest_repeating('AABB'))  # 2

# %% Project 4: Implement strStr (Using KMP)
def str_str(haystack, needle):
    return kmp(haystack, needle)

# Example: print(str_str('hello', 'll'))  # 2

# %% Project 5: Group Anagrams (Hashing like Rabin-Karp)
def group_anagrams(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# Example: print(group_anagrams(['eat','tea','tan']))  # [['eat','tea'],['tan']]