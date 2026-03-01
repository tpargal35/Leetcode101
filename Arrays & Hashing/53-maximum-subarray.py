# Brute force involves calculating all different sub arrays 
# and sum and keeping track of max, but complexity becomes n^2 
'''
def maxSubArray(nums: List[int]) -> int:
    siz = len(nums)
    maxsumm=nums[0]
    for i in range(0,siz):
        summ=0
        for j in range(i,siz):
            summ+=nums[j]
            maxsumm = max(maxsumm,summ)
    return maxsumm
'''
# Think of optimizing
def maxSubArray(nums: List[int]) -> int:
    summ = nums[0]
    maxsumm = nums[0]
    for i in range(1,len(nums)):
        if summ<0:
            summ=0
        summ+=nums[i]
        maxsumm = max(maxsumm, summ)
    return maxsumm        
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))    
        