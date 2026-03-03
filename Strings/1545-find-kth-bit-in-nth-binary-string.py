# Original O(2^n) implementation:
# def findKthBit(n: int, k: int) -> str:
#     if n==1:
#         return 0
#     finalStr = '0'
#     for i in range(2,n+1):
#         invStr = ['1' if i=='0' else '0' for i in finalStr]
#         invStr.reverse()
#         invStr_new = ''.join(invStr)
#         finalStr = finalStr + '1' + invStr_new
#     print(finalStr)    
#     return finalStr[k-1]

def findKthBit(n: int, k: int) -> str:
    # O(n) Time, O(1) Space optimization
    invert_count = 0
    while n > 1:
        length = (1 << n) - 1
        mid = (length // 2) + 1
        
        if k == mid:
            # Middle bit is '1'. Flip if invert_count is odd.
            return '1' if invert_count % 2 == 0 else '0'
        elif k > mid:
            # Right half: flip the problem to left half and track inversion count
            k = length - k + 1
            invert_count += 1
        # Left half: just move to n-1
        n -= 1
        
    # Base case n=1 (S1 = '0')
    return '0' if invert_count % 2 == 0 else '1'

print(findKthBit(4,11))    