# Equal Sides of an Array
# Find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.

def find_even_index(arr):
    for i in range(0, len(arr)):
        if sum(arr[:i + 1]) == sum(arr[i:]):
            return i
    return -1
