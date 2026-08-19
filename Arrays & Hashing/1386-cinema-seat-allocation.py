from collections import defaultdict
from typing import List

# Approach 1: Hash Map with Sets
# def maxNumberOfFamilies(n: int, reservedSeats: List[List[int]]) -> int:
#     reserved = defaultdict(set)
#     for row, seat in reservedSeats:
#         reserved[row].add(seat)
# 
#     res = 0
#     for row in reserved:
#         taken = reserved[row]
#         left = not any(s in taken for s in (2, 3, 4, 5))
#         right = not any(s in taken for s in (6, 7, 8, 9))
#         middle = not any(s in taken for s in (4, 5, 6, 7))
# 
#         if left:
#             res += 1
#             if right:
#                 res += 1
#         elif right:
#             res += 1
#         elif middle:
#             res += 1
# 
#     res += (n - len(reserved)) * 2
#     return res

# Approach 2: Bitmask (Optimal Space & Constant Time)
def maxNumberOfFamilies(n: int, reservedSeats: List[List[int]]) -> int:
    reserved = defaultdict(int)
    for row, seat in reservedSeats:
        if 2 <= seat <= 9:
            reserved[row] |= (1 << seat)

    LEFT = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)      # 60
    RIGHT = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)     # 960
    MIDDLE = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)    # 240

    res = 0
    for mask in reserved.values():
        left = (mask & LEFT) == 0
        right = (mask & RIGHT) == 0
        middle = (mask & MIDDLE) == 0

        if left:
            res += 1
            if right:
                res += 1
        elif right:
            res += 1
        elif middle:
            res += 1

    res += (n - len(reserved)) * 2
    return res

n = 3
reservedSeats = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
print(maxNumberOfFamilies(n, reservedSeats))
