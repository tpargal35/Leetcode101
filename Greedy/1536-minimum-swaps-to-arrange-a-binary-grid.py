def minSwaps(grid: List[List[int]]) -> int:
    n = len(grid)

    # Step 1: For each row, count trailing zeros from the right
    trailing_zeros = []
    for i in range(n):
        count = 0
        for j in range(n - 1, -1, -1):
            if grid[i][j] == 0:
                count += 1
            else:
                break
        trailing_zeros.append(count)

    # Step 2: Greedy — for row i, we need at least (n - 1 - i) trailing zeros
    swaps = 0
    for i in range(n):
        required = n - 1 - i

        # Find the first row at position >= i that has enough trailing zeros
        target = -1
        for j in range(i, n):
            if trailing_zeros[j] >= required:
                target = j
                break

        # If no valid row found, arrangement is impossible
        if target == -1:
            return -1

        # Bubble the target row up to position i via adjacent swaps
        while target > i:
            trailing_zeros[target], trailing_zeros[target - 1] = trailing_zeros[target - 1], trailing_zeros[target]
            target -= 1
            swaps += 1

    return swaps


grid = [[0,0,1],[1,1,0],[1,0,0]]
print(minSwaps(grid))