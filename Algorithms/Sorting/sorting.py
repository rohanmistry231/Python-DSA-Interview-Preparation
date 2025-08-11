# %% Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# %% Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# %% Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# %% Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# %% Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# %% Heap Sort
import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# %% Project 1: Sort and Find Median (Using Merge Sort)
def find_median(arr):
    sorted_arr = merge_sort(arr[:])
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    return sorted_arr[n//2]

# Example: print(find_median([3, 1, 4, 1, 5]))  # 3

# %% Project 2: Count Inversions (Using Merge Sort Modification)
def count_inversions(arr):
    def merge_and_count(left, right):
        result = []
        inv = i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inv += len(left) - i
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv
    
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    merged, inv_merge = merge_and_count(left, right)
    return merged, inv_left + inv_right + inv_merge

# Example: _, inv = count_inversions([3,1,2]); print(inv)  # 2

# %% Project 3: Sort Nearly Sorted Array (Using Insertion Sort)
def sort_nearly_sorted(arr, k):
    for i in range(1, len(arr)):
        key = arr[i]
        j = max(0, i - k - 1)
        while j < i and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example: print(insertion_sort([2,1,4,3]))  # [1,2,3,4] (adapted)

# %% Project 4: Kth Largest Element (Using Quick Sort)
def kth_largest(arr, k):
    sorted_arr = quick_sort(arr[:])[::-1]
    return sorted_arr[k-1] if k <= len(arr) else None

# Example: print(kth_largest([3,2,1,5,6,4], 2))  # 5

# %% Project 5: Sort Colors (Dutch National Flag - Variant of Quick Sort)
def sort_colors(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example: print(sort_colors([2,0,2,1,1,0]))  # [0,0,1,1,2,2]