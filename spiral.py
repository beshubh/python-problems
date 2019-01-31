matrix= [
  [ 0, 0, 0 ],
  [ 200, 0, 90 ],
  [ 2000, 2002, 2000 ]
]
mat=[[2002]*4]*4
c=1
T,B,R,L=0,3,3,0
d=0
while T<=B and L<=R:
  if d is 0:
    for i in range(L,R+1):
      mat[T][i]=c
      c=c+1
    T+=1
  if d is 1:
    for i in range(T,B+1):
      mat[i][R]=c
      c=c+1
    R-=1
  if d is 2 :
    for i in range(R,L+1):
      mat[B][i]=c
      c=c+1
    B-=1
  if d is 3:
    for i in range(B,T+1):
      mat[L][i]=c
      c=c+1
    L+=1
  d=(d+1)%4
for i in range(len(mat)):
  for j in range(len(mat[i])):
    print(mat[i][j],end=' ')
  print()
