# %% Simple Hash Table with Chaining
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def remove(self, key):
        index = self.hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

# %% Project 1: Find First Non-Repeating Character
def first_non_repeating(s):
    ht = HashTable()
    for char in s:
        ht.insert(char, ht.get(char) + 1 if ht.get(char) else 1)
    for char in s:
        if ht.get(char) == 1:
            return char
    return None

# Example: print(first_non_repeating('aabbc'))  # 'c'

# %% Project 2: Group Anagrams
def group_anagrams(words):
    ht = HashTable()
    for word in words:
        sorted_word = ''.join(sorted(word))
        if ht.get(sorted_word):
            ht.get(sorted_word).append(word)
        else:
            ht.insert(sorted_word, [word])
    return [item for sublist in self.table for item in sublist if item]  # Simplified return

# Example: print(group_anagrams(['eat', 'tea', 'tan']))  # Groups

# %% Project 3: Check Subarray Sum Zero
def subarray_zero(nums):
    ht = HashTable()
    ht.insert(0, -1)
    cum_sum = 0
    for i, num in enumerate(nums):
        cum_sum += num
        if ht.get(cum_sum) is not None:
            return True
        ht.insert(cum_sum, i)
    return False

# Example: print(subarray_zero([4,2,-3,1,6]))  # True

# %% Project 4: Longest Substring Without Repeating Characters
def longest_substring(s):
    ht = HashTable()
    max_len = start = 0
    for i, char in enumerate(s):
        if ht.get(char) and ht.get(char) >= start:
            start = ht.get(char) + 1
        ht.insert(char, i)
        max_len = max(max_len, i - start + 1)
    return max_len

# Example: print(longest_substring('abcabcbb'))  # 3

# %% Project 5: Two Sum
def two_sum(nums, target):
    ht = HashTable()
    for i, num in enumerate(nums):
        complement = target - num
        if ht.get(complement) is not None:
            return [ht.get(complement), i]
        ht.insert(num, i)
    return []

# Example: print(two_sum([2,7,11,15], 9))  # [0,1]