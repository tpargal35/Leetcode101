def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    #convert 2-d into low and high, find a relations between rowsize and colsize, find middle of 2-d matrix, can we use modulus ?
    #find candidate row using bs is tough and then element in candidate row 
    m = len(matrix)
    n = len(matrix[0])
    top_row = 0
    bottom_row = m-1
    left = 0
    right = n-1
    while top_row<=bottom_row:
        mid_row = (top_row + bottom_row)//2
        if target > matrix[mid_row][-1]:
            top_row = mid_row + 1
        elif target < matrix[mid_row][0]:
            bottom_row = mid_row - 1
        else:
            break
    while(left<=right):
        mid = (left+right)//2
        if matrix[mid_row][mid] == target:
            return True
        elif matrix[mid_row][mid] > target:
            right = mid-1
        else:
            left = mid+1   

    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))   