from functools import cmp_to_key
def nextPermutation(A):
    if len(A) is 1:
        return A
    n=len(A)
    for i in range(len(A)-1,0,-1):
        if A[i]>A[i-1]:
            break
    if i is 1:
        A.sort()
        return A
    else:
        x=A[i-1]#319
        smallest=i#6
        for j in range(i+1,n):
            if A[j]>x and A[i]<A[smallest]:#52 when j is n-1 i.e 8
                smallest=j
        #swapping the smalles and i-1'th number i.e 52 <--->319
        A[smallest],A[i-1]=A[i-1],A[smallest]
        res=sorted(A[i:])
    return A[:i]+res
print(nextPermutation([507,669,153,856,701,319,652,52]))
