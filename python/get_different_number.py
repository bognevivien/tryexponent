from typing import List
def get_different_number(arr:List[int])-> int:
    arr.sort()
    max_int = 2**31 -1
    for i in range(len(arr)):
        goodIndex = arr[i]
        if goodIndex == 0 or goodIndex == -max_int:
            arr[goodIndex] = -max_int
        else:
            arr[goodIndex] = -arr[goodIndex]

    for elt in arr:
        if abs(elt) != max_int and elt > 0:
            return elt
    return arr

arr = [2,1,0,5,4]
print(get_different_number(arr))