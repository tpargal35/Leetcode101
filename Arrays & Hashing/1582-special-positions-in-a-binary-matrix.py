def checkrow(mat,i,n):
    c=0
    for a in range(0,n):
        if mat[i][a]==1:
            c+=1
    return c

def checkcol(mat,j,m):
    c=0
    for a in range(0,m):
        if mat[a][j]==1:
            c+=1
    return c   

def numSpecial(mat: List[List[int]]) -> int:
    specs = 0
    m=len(mat)
    n=len(mat[0])
    for i in range(0,m):
        for j in range(0,n):
            if mat[i][j]==1:
                c = 0
                c+=checkrow(mat,i,n)
                c+=checkcol(mat,j,m)
                if c==2:
                    specs+=1
    return specs
mat = [[1,0,0],[0,1,0],[0,0,1]]
print(numSpecial(mat))
    
    