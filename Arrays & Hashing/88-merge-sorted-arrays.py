def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1       # pointer for last valid element in nums1
    p2 = n - 1       # pointer for last element in nums2
    p  = m + n - 1   # pointer for last position in nums1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # if nums2 still has elements left, copy them over
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p  -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)