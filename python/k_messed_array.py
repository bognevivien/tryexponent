"""
PROBLEM STATEMENT: K-Messed Array Sort
-------------------

Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer k

0 ≤ k ≤ 20
[output] array.integer
"""
from typing import List
import heapq
def k_messed_array(arr: List[int], k : int)-> List[int]:
    """
    1, 4, 5, 2, 3, 7, 8, 6, 10, 9
    r
    w
    k = 2
    """

def k_messed_array(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    if k == 0:
        return arr
        
    heap = []
    write_idx = 0
    
    # Single loop through the array
    for read_idx in range(n):
        # Build initial heap or add new element
        heapq.heappush(heap, arr[read_idx])
        
        # Once we have k+1 elements, start writing
        # This ensures we have enough elements to determine the minimum
        if read_idx >= k:
            arr[write_idx] = heapq.heappop(heap)
            write_idx += 1
    
    # Empty remaining heap
    while heap:
        arr[write_idx] = heapq.heappop(heap)
        write_idx += 1
        
    return arr


arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2

print(k_messed_array(arr, k))