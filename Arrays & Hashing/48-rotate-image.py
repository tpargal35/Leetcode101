def rotate(matrix: List[List[int]]) -> None:
    # 1. Transpose: Swap matrix[i][j] with matrix[j][i]
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)): # Use i + 1 to avoid double-swapping
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # 2. Reverse each row to achieve 90-degree clockwise rotation
    for row in matrix:
        row.reverse() 


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print("Original:")
for r in matrix: print(r)

rotate(matrix)

print("\nRotated:")
for r in matrix: print(r)
