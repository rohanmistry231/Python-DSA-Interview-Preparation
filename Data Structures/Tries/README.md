## Tries

### Introduction
Trie (prefix tree) stores strings for efficient prefix-based operations.

### Structure
- Nodes with children dict.
- End flag for word end.

### Operations
- Insert: O(len(word))
- Search: O(len(word))
- Prefix search: O(len(prefix))

### Advantages
- Fast string ops.

### Disadvantages
- High memory.

### Applications
- Autocomplete.
- Spell check.

### Time Complexities
- O(m) where m is key length.