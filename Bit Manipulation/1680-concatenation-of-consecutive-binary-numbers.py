'''
Original Approach (Gets TLE):
The previous approach gets Time Limit Exceeded (TLE) because string concatenation 
in Python takes O(N) time for each operation, leading to O(N^2) overall time complexity. 
Additionally, parsing a massive string of length ~10^5 bits and computing its decimal 
value at the very end requires handling extremely large integers, which is computationally expensive.

def decimal_bin(n):
    bin = ""
    while (n>0):
        a = n % 2
        n = n // 2
        bin=str(a)+bin
    return bin    

def bin_decimal(bins):
    pow2 = 1
    dec = 0
    while len(bins) > 0:
        num = int(bins[-1]) * pow2
        bins = bins[:-1]
        pow2 *= 2
        dec = dec + num
    return dec

def concatenatedBinary_old(n: int) -> int:
    MOD = 10**9+7
    finalStr = ""
    for i in range(1,n+1):
        finalStr += decimal_bin(i)
    return (bin_decimal(finalStr)) % MOD
'''

def concatenatedBinary(n: int) -> int:
    """
    Optimized approach using bitwise operations.
    Instead of building a massive string, we build the number mathematically
    and apply the modulo at each step to prevent the number from growing too large.
    """
    MOD = 10**9 + 7
    ans = 0
    
    for i in range(1, n + 1):
        # Step 1: Find the number of bits in the current number 'i'.
        # For example, if i = 2 (binary 10), bit_length is 2.
        # If i = 3 (binary 11), bit_length is 2.
        # If i = 4 (binary 100), bit_length is 3.
        length = i.bit_length()
        
        # Step 2: Left shift the current answer by 'length' bits.
        # This creates room to append the binary representation of 'i'.
        # For example, if ans = 1 (binary 1) and we want to append 2 (binary 10),
        # we shift ans left by 2 bits: 1 << 2 = 4 (binary 100).
        ans = ans << length
        
        # Step 3: Use bitwise OR to combine 'ans' and 'i'.
        # (Using addition `ans + i` would also work here since the shifted bits are all 0s)
        # Continuing the example: 4 (binary 100) | 2 (binary 10) = 6 (binary 110).
        # This effectively concatenates 1 and 10 to get 110.
        ans = ans | i
        
        # Step 4: Take modulo MOD to ensure 'ans' doesn't grow infinitely large.
        # Modular arithmetic allows us to take the modulo at each intermediate step
        # without altering the final remainder. This keeps the numbers small and fast.
        ans = ans % MOD
        
    return ans

print(concatenatedBinary(12))