matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n=len(matrix)
res=[[0]*n for i in range(n)]
c=0
for i in range(n):
    c=n
    for j in range(n):
        res[i][j]=matrix[c-1][i]
        c-=1
for i in range(n):
    for j in range(n):
        print(res[i][j],end=' ')
    print()
