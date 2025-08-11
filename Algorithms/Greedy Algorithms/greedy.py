# %% Activity Selection
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    result = [activities[0]]
    last_end = activities[0][1]
    for start, end in activities[1:]:
        if start >= last_end:
            result.append((start, end))
            last_end = end
    return result

# %% Project 1: Fractional Knapsack
def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    total = 0
    for weight, value in items:
        if capacity >= weight:
            total += value
            capacity -= weight
        else:
            total += value * (capacity / weight)
            break
    return total

# Example: print(fractional_knapsack([(10,60),(20,100),(30,120)], 50))  # 240

# %% Project 2: Huffman Coding (Simplified)
# Note: Full impl requires priority queue; basic example
import heapq
def huffman_codes(freq):
    heap = [[f, [char, '']] for char, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        right = heapq.heappop(heap)
        left = heapq.heappop(heap)
        for pair in right[1:]:
            pair[1] = '0' + pair[1]
        for pair in left[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Example: freq = {'a':5,'b':9}; print(huffman_codes(freq))

# %% Project 3: Job Sequencing with Deadlines
def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(j[1] for j in jobs)
    slots = [False] * (max_deadline + 1)
    result = []
    for job, deadline, profit in jobs:
        for d in range(min(max_deadline, deadline), 0, -1):
            if not slots[d]:
                slots[d] = True
                result.append((job, d))
                break
    return result

# Example: jobs = [('a',2,100),('b',1,19)]; print(job_sequencing(jobs))

# %% Project 4: Minimum Platforms for Trains
def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    platforms = max_platforms = 0
    i = j = 0
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platforms += 1
            i += 1
            max_platforms = max(max_platforms, platforms)
        else:
            platforms -= 1
            j += 1
    return max_platforms

# Example: print(min_platforms([900,940],[910,1200]))  # 1

# %% Project 5: Greedy Coin Change
def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count if amount == 0 else -1

# Example: print(greedy_coin_change([25,10,5,1], 30))  # 3