from typing import List
"""
input: arr = [-8,0,1,3]
left, right = 0, 4
while 0< 3:
    mid = 0+4 // 2 == 2
    arr[2] = 1 < 2
        left = 2
    mid = 
output: 2 # since arr[2] == 2

"""
def index_equals_value_search(arr: List[int]) -> int:
    n = len(arr)
    left, right = 0, n-1
    ans = -1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == mid:
            ans = mid
            right = mid - 1
        elif arr[mid] > mid:
            right = mid -1
        else:
            left = mid + 1
    # for i, elt in enumerate(arr):
    #     if elt == i :
    #         return i 

    return ans

print(index_equals_value_search([0,1,2,3,4]))