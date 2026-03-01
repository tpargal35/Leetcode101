"""
brute Force
c0=0
c1=0
c2=0
for i in nums:
    if i==0:
        c0+=1
    elif i==1:
        c1+=1
    else:
        c2+=1
i=0        
while (c0>0):
    nums[i]=0
    c0-=1
    i+=1
while (c1>0):
    nums[i]=1
    c1-=1
    i+=1
while (c2>0):
    nums[i]=2
    c2-=1
    i+=1
return nums    
"""

def sortColors(nums: List[int]) -> None:
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

nums = [1,2,0,0,0,0,1,1,2,1,0,1,2,1,1]
sortColors(nums)
print(nums)