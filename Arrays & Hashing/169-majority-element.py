from typing import List, Optional, Dict

def majorityElement(nums: List[int]) -> int:
    c = 1
    m = nums[0]
    for i in range(1,len(nums)): 
        if nums[i] == m:
            c = c + 1
        else:
            c = c - 1
        if c == 0:
            m = nums[i]
            c=1
    return m

# Example 1
nums1 = [3, 2, 3]
print(majorityElement(nums1))  # Expected: 3

# Example 2
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums2))  # Expected: 2
