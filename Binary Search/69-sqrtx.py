from typing import List, Optional, Dict

def mySqrt(x: int) -> int:
    low = 0
    high = x 
    while (low <= high):
        mid = (low + high) // 2
        if (mid*mid) == x:
            return mid
        elif (mid*mid)>x:
            high = mid -1
        else:
            low = mid + 1   
    return high

# Example 1
x1 = 4
print(mySqrt(x1))  # Expected: 2

# Example 2
x2 = 8
print(mySqrt(x2))  # Expected: 2
