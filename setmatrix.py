A=[[1,0,1],
   [1,1,1],
   [1,1,1]
   ]
c=0
row={}
col={}
for i in range(len(A)):
    for j in range(len(A[0])):
        if (A[i][j]==0):
            for x in range(len(A[0])):
                A[i][x] =0
            for y in range(len(A)):
                print(y,j)
                A[y][j]=0
        break
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j],end=' | ')
    print()