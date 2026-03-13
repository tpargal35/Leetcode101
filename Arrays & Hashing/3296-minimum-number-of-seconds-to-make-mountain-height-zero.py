# Input: mountainHeight = 10, workerTimes = [3,2,2,4]
# Output: 12

# Input: mountainHeight = 5, workerTimes = [1,5]
# Output: 10

# Approach: Binary Search on Answer
# Binary search on time T. For a given T, check if all workers together
# can reduce mountainHeight to 0.
# For each worker, max reductions in time T:
#   worker_time * x*(x+1)/2 <= T  =>  x = floor((-1 + sqrt(1 + 8T/w)) / 2)

import math
from typing import List

def minNumberOfSeconds(mountainHeight: int, workerTimes: List[int]) -> int:

    def max_reductions(worker_time, time_budget):
        # Largest height_reducible such that worker_time * height_reducible*(height_reducible+1)/2 <= time_budget
        height_reducible = int((-1 + math.sqrt(1 + 8 * time_budget / worker_time)) / 2)
        return height_reducible

    def can_finish(time_budget):
        total_reductions = sum(max_reductions(worker_time, time_budget) for worker_time in workerTimes)
        return total_reductions >= mountainHeight

    # Upper bound: slowest possible = single fastest worker does everything
    min_time = 0
    max_time = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

    while min_time < max_time:
        candidate_time = (min_time + max_time) // 2
        if can_finish(candidate_time):
            max_time = candidate_time
        else:
            min_time = candidate_time + 1

    return min_time

# Test 1
print(minNumberOfSeconds(10, [3, 2, 2, 4]))  # Expected: 12
# Test 2
print(minNumberOfSeconds(5, [1, 5]))          # Expected: 10