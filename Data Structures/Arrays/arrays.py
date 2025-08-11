# %% Array Implementation (Using Python List)
class Array:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
    
    def insert(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
    
    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        return None
    
    def delete(self, index):
        if 0 <= index < self.size:
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None

# %% Project 1: Rotate Array
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return arr

# Example: arr = [1, 2, 3, 4, 5]; print(rotate_array(arr, 2))  # [4, 5, 1, 2, 3]

# %% Project 2: Find Missing Number
def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example: arr = [1, 2, 4, 5]; print(find_missing_number(arr, 5))  # 3

# %% Project 3: Merge Sorted Arrays
def merge_sorted_arrays(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

# Example: print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]

# %% Project 4: Maximum Subarray Sum
def max_subarray_sum(arr):
    max_so_far = max_ending_here = arr[0]
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Example: print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1]))  # 6

# %% Project 5: Remove Duplicates from Sorted Array
def remove_duplicates(arr):
    if not arr:
        return 0
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[write_index - 1]:
            arr[write_index] = arr[i]
            write_index += 1
    return arr[:write_index]

# Example: arr = [1, 1, 2, 2, 3]; print(remove_duplicates(arr))  # [1, 2, 3]