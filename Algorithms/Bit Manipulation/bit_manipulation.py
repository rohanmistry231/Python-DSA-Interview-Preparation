# %% Get Bit
def get_bit(num, i):
    return (num & (1 << i)) != 0

# %% Set Bit
def set_bit(num, i):
    return num | (1 << i)

# %% Clear Bit
def clear_bit(num, i):
    return num & ~(1 << i)

# %% Project 1: Single Number (XOR)
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example: print(single_number([2,2,1]))  # 1

# %% Project 2: Count Set Bits
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Example: print(count_set_bits(7))  # 3

# %% Project 3: Power of Two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Example: print(is_power_of_two(8))  # True

# %% Project 4: Bitwise Addition
def bitwise_add(a, b):
    while b:
        carry = a & b
        a ^= b
        b = carry << 1
    return a

# Example: print(bitwise_add(5, 3))  # 8

# %% Project 5: Missing Number (XOR)
def missing_number(nums):
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result

# Example: print(missing_number([3,0,1]))  # 2