def convert(mat: list[list[int]]):
    arr=[]
    for row in mat:
        arr=arr+row
        
    return arr


def diagonalSum(mat: list[list[int]]) -> int:
    step=len(mat[0])-1
    sum=0
    print(f"step:{step}")
    if step%2==0:
        for x in range(0,step+1):
            sum=sum+mat[x][x]
        for x in range(0,step+1):
            if x==step/2:
                continue
            else:
                sum=sum+mat[step-x][x]
    else:
        for x in range(0,step+1):
            sum=sum+mat[x][x]
        for x in range(0,step+1):
            sum=sum+mat[step-x][x]
    return sum

print(diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))