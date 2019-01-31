def prettyPrint(A):
    n=A+(A-1)
    a=[[0]*n for xyz in range(n)]
    value=A
    dir=0
    T=0
    B=len(a)-1
    L=0
    R=len(a)-1
    while T<=B and L<=R:
        if dir is 0:
            for j in range(L,R+1):
                a[T][j]=value
            T+=1
            dir =1
            continue
        if dir is 1:
            for j in range(T,B+1):
                a[j][R]=value
            R-=1
            dir=2
            continue
        if dir is 2:
            for j in range(R,L-1,-1):
                a[B][j]=value
            dir=3
            B-=1
        if dir is 3:
            for j in range(B,T-1,-1):
                a[j][L]=value
            dir=0
            L+=1
        value-=1
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j],end=" ")
        print()
prettyPrint(10)
