# ---------------------- ORIGINAL SOLUTION ----------------------
# Time: O(m * n * (m + n))  |  Space: O(1)

# def checkrow(mat,i,n):
#     c=0
#     for a in range(0,n):
#         if mat[i][a]==1:
#             c+=1
#     return c

# def checkcol(mat,j,m):
#     c=0
#     for a in range(0,m):
#         if mat[a][j]==1:
#             c+=1
#     return c   

# def numSpecial(mat: List[List[int]]) -> int:
#     specs = 0
#     m=len(mat)
#     n=len(mat[0])
#     for i in range(0,m):
#         for j in range(0,n):
#             if mat[i][j]==1:
#                 c = 0
#                 c+=checkrow(mat,i,n)
#                 c+=checkcol(mat,j,m)
#                 if c==2:
#                     specs+=1
#     return specs

# ---------------------- OPTIMIZED SOLUTION ----------------------
# Precompute row and column counts in one pass, then check in a second pass.
# Time: O(m * n)  |  Space: O(m + n)

def numSpecial(mat):
    m = len(mat)
    n = len(mat[0])

    # Precompute number of 1s in each row and each column
    row_count = [0] * m
    col_count = [0] * n

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1

    # A cell is special if it's a 1 AND its row and column each have exactly one 1
    specs = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                specs += 1

    return specs

mat = [[1,0,0],[0,1,0],[0,0,1]]
print(numSpecial(mat))