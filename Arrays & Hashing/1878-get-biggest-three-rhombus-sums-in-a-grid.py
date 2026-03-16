def getBiggestThree(grid):
    m = len(grid)
    n = len(grid[0])
    top = [0, 0, 0]
    def add_val(val):
        if val in top:
            return
        if val > top[0]:
            top[2] = top[1]
            top[1] = top[0]
            top[0] = val
        elif val > top[1]:
            top[2] = top[1]
            top[1] = val
        elif val > top[2]:
            top[2] = val    
    for i in range(m):
        for j in range(n):
            add_val(grid[i][j])
            max_k = min(i, m - 1 - i, j, n - 1 - j)
            for k in range(1, max_k + 1):
                current_sum = 0
                for step in range(k):
                    current_sum += grid[i - k + step][j + step]
                    current_sum += grid[i + step][j + k - step]
                    current_sum += grid[i + k - step][j - step]
                    current_sum += grid[i - step][j - k + step]
                add_val(current_sum)
    return [x for x in top if x > 0]



grid = [[3,4,5,1,3],
        [3,3,4,2,3],
        [20,30,200,40,10],
        [1,5,5,4,1],
        [4,3,2,2,5]]
print(getBiggestThree(grid))