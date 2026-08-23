from typing import List, Optional, Dict

def sumGame(num: str) -> bool:
    num = list(num)
    sizen = len(num)
    mid = sizen // 2
    sum1, sum2 = 0, 0
    q = 0

    for i in range(sizen):
        if i < mid:
            if num[i] == '?':
                q += 1
            else:
                sum1 += int(num[i])
        else:
            if num[i] == '?':
                q -= 1
            else:
                sum2 += int(num[i])

    suma = sum1 - sum2
    return (suma * 2 + q * 9) != 0


# Example 1
num1 = "5023"
print(sumGame(num1))  # Expected: False

# Example 2
num2 = "25??"
print(sumGame(num2))  # Expected: True

# Example 3
num3 = "?3295???"
print(sumGame(num3))  # Expected: False
