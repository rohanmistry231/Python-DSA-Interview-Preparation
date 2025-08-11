# %% Trie Node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

# %% Trie Class
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True
    
    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end
    
    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# %% Project 1: Word Break
def word_break(s, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and trie.search(s[j:i]):
                dp[i] = True
                break
    return dp[-1]

# Example: print(word_break('applepenapple', ['apple','pen']))  # True

# %% Project 2: Longest Common Prefix
def longest_common_prefix(words):
    if not words:
        return ''
    trie = Trie()
    for word in words:
        trie.insert(word)
    prefix = ''
    current = trie.root
    while len(current.children) == 1 and not current.is_end:
        char = next(iter(current.children))
        prefix += char
        current = current.children[char]
    return prefix

# Example: print(longest_common_prefix(['flower','flow','flight']))  # 'fl'

# %% Project 3: Autocomplete Suggestions
def autocomplete(trie, prefix):
    current = trie.root
    for char in prefix:
        if char not in current.children:
            return []
        current = current.children[char]
    return find_words(current, prefix)

def find_words(node, word):
    result = []
    if node.is_end:
        result.append(word)
    for char, child in node.children.items():
        result.extend(find_words(child, word + char))
    return result

# Example: t = Trie(); t.insert('hello'); print(autocomplete(t, 'he'))  # ['hello']

# %% Project 4: Count Unique Words
def count_unique(words):
    trie = Trie()
    count = 0
    for word in words:
        if not trie.search(word):
            trie.insert(word)
            count += 1
    return count

# Example: print(count_unique(['apple', 'apple', 'banana']))  # 2

# %% Project 5: Replace Words with Prefix
def replace_words(dictionary, sentence):
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    words = sentence.split()
    for i, word in enumerate(words):
        current = trie.root
        prefix = ''
        for char in word:
            if char not in current.children:
                break
            prefix += char
            current = current.children[char]
            if current.is_end:
                words[i] = prefix
                break
    return ' '.join(words)

# Example: print(replace_words(['cat','bat'], 'caterpillar batman'))  # 'cat bat'